import logging

from app.workflow_data.welcomeMessage import welcome_message
def webbot_workflow(recivedData):
    # print("Function run",welcome_message())
    # return "love"
    if(recivedData["event"]=="CONNECTED"):
        return welcome_message()