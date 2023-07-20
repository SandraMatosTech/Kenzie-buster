from rest_framework.views import APIView, Request, Response,status
from users.models import User
from users.serializers import UserSerializer
from .utils import check_users

class UserView(APIView):
    def get(self, request= Request) -> Response:
        users= User.objects.all()
        serializer= UserSerializer(users, many=True)
        return Response (serializer.data, status=status.HTTP_200_OK)

    def post(self, request=Request) ->Response:
        if "email" in request.data and "username" in request.data:
            try:
                check_users( request.data['email'],request.data['username'])
            except Exception as error:
                return Response(error.message,400)



       
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
    
        return Response (serializer.data, status=status.HTTP_201_CREATED)

      