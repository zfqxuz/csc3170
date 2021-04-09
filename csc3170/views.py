from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from csc3170.serizalizer import CreateUserSerizalizer
from django.db import connection
# Create your views here.

class UserAuthorization(ViewSet):
    serializer=CreateUserSerizalizer
    def list(self,request):
        return Response("POST,PUT")

    def post(self,request):
        if request.method=="POST":
            with connection.cursor()as cursor:
                instruct=JSONParser().parse(request)
                ug=instruct["ug"]
                name = instruct["name"]
                password = instruct["pwd"]
                cursor.execute(f"create user '{name}'@'%' identified by '{password}'")
                if ug==1:
                    cursor.execute(f"grant insert, select,delete on csc3170.application to '{name}'@'%' ")
                    cursor.execute(f"grant select on csc3170.result to '{name}'@'%' ")
                elif ug==2:
                    cursor.execute(f"grant all on csc3170.result to '{name}'@'%' ")
                    cursor.execute(f"grant all on csc3170.pattent to '{name}'@'%' ")
                    cursor.execute(f"grant all on csc3170.reject_details to '{name}'@'%' ")
                elif ug==3:
                    cursor.execute(f"grant select on csc3170.ID2COMP to '{name}'@'%'")

            return Response({"msg":"success"})
