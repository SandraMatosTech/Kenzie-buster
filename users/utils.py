from users.exceptions import UserException
from .models import User
from rest_framework.views import Response

def check_users(email, username):
    
        error=[]
        if User.objects.filter(email__iexact=email).exists():
            error.append("email")

        if User.objects.filter(username__iexact=username).exists():
            error.append("username")
        if len(error)==2:
            raise UserException({
                "email": [
                    "email already registered."
                ],
                "username": [
                    "username already taken."
                ]
            })
        elif len(error)==1:
            if error[0] =="email":
                raise UserException({ "email": [
            "email already registered."
            ]})
            else:
                raise UserException({"username": [
                  "username already taken."
             ]})
