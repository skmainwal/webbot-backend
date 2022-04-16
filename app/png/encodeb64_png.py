import base64

# doctor_encoded= base64.b64encode(open('app/static/images/png/doctor.png','rb').read()).decode()
# doctor_2_encoded= base64.b64encode(open('app/static/images/png/doctor_2.jpeg','rb').read()).decode()
# book_encoded= base64.b64encode(open('app/static/images/png/book.png','rb').read()).decode()
# cancel_encoded = base64.b64encode(open('app/static/images/png/cancel.png','rb').read()).decode()
# query_encoded = base64.b64encode(open('app/static/images/png/query.png','rb').read()).decode()
# center_image = base64.b64encode(open('app/static/images/png/sydney.png','rb').read()).decode()
# center_image1 = base64.b64encode(open('app/static/images/png/sydney1.png','rb').read()).decode()

book_new = base64.b64encode(open('app/png/book_new.png','rb').read()).decode()
cancel_new = base64.b64encode(open('app/png/cancel_new.png','rb').read()).decode()
blood_test_new = base64.b64encode(open('app/png/blood_test_new.png','rb').read()).decode()
query_new = base64.b64encode(open('app/png/query_new.png','rb').read()).decode()