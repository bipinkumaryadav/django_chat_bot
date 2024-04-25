from django.shortcuts import render, HttpResponse
from chatbot import chat_dec
import pyrebase

config = {
  "apiKey": "AIzaSyDTOZWIXa9OSjxGOuPPJadkib29Yk1CiWE",
  "authDomain": "mystique-9366b.firebaseapp.com",
  "databaseURL": "https://mystique-9366b-default-rtdb.firebaseio.com",
  "projectId": "mystique-9366b",
  "storageBucket": "mystique-9366b.appspot.com",
  "messagingSenderId": "830212311511",
  "appId": "1:830212311511:web:a17f4175c66e4fb1172392",
}
# Initialising database,auth and firebase for further use
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()


# create a function
def simple_view(request):
    try:
        word = request.GET['user_text']
        resp = chat_dec.check_word(word)
        user = authe.sign_in_with_email_and_password("bipinkumaryadav8416@gmail.com", "bipin8416")
        users_ref = database.child("Demo")
        for x in users_ref.get():
            print(x.val())

        data = {
                  "DesiredDate": "2024-04-15",
                  "DesiredTime": "12:37",
                  "GuestName": "prabhat",
                  "ItemOrdered": "apple",
                  "PaidBy": "uuu",
                  "Priority": "High Priority",
                  "RoomNo": "211",
                  "Stage": "Created",
                  "TaskAdderId": "00000",
                  "TaskAdderName": "Guest",
                  "timestamp": "{.sv=timestamp}"
            }
        cont = {"message": resp[0]}
        database.child("Tasks").push(data)

        return render(request, "index2.html", context=cont)
    except Exception as e:
        print(e)
        return render(request, "index2.html")

