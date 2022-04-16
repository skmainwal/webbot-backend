from app.png.encodeb64_png import book_new, cancel_new, query_new, blood_test_new


def welcome_message():

    message = "Hi, my name is <b>Olivia</b>, how can I help you ? Please select one of the options"
    result = {"workflow_type":"GP_APPT","event": "AI_RESPONSE", "type": "PRESET", "message": message, "disable_input": True, "preset_responses": [
        {"image": book_new, "text": "Book an Appointment", "sub_text": "",
         "event": "GP_BOOK"},
        {"image": blood_test_new, "text": "Book Blood or Allergy Test", "sub_text": "",
         "event": "GP_BLOOD"}
        , {"image": cancel_new, "text": "Modify/Cancel appointment",
                                        "sub_text": "",
                                        "event": "GP_MODIFY"},
        {"image": query_new, "text": "You have a query ?", "sub_text": "",
         "event": "GP_QUERY"}]}
    return result
   