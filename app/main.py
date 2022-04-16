from fastapi import FastAPI, WebSocket,  WebSocketDisconnect
from fastapi.responses import HTMLResponse
from app.workflow_data.workflow import webbot_workflow
import logging
logging.basicConfig(filename="app.log", filemode='a', format='%(asctime)s %(levelname)s-%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

app = FastAPI()


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()

@app.websocket("/api/v1/chatbot")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            logging.info("Recived data", data)
            print(data)
            to_send_data=webbot_workflow(recivedData=data)
            await manager.send_personal_message(to_send_data, websocket)


            # await manager.send_personal_message(f"You wrote: {data}", websocket)
           
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        # await manager.broadcast(f"Client #{client_id} left the chat")