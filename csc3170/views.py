import os
import pymysql
import django.db
from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from csc3170.serizalizer import CreateUserSerizalizer,LoginSerizalizer
from django.db import connection,connections
import smtplib
# Create your views here

class UserAuthorization(ViewSet):
    serializer=CreateUserSerizalizer
    def list(self,request):
        return Response("POST,PUT")

    def post(self,request):
        if request.method=="POST":

            db = pymysql.connect(host="localhost", user="root",password= "123456", database="csc3170")
            with db.cursor()as cursor:
                instruct=JSONParser().parse(request)
                ug=instruct["ug"]
                name = instruct["name"]
                password = instruct["pwd"]
                print(f"create user '{name}'@'%' identified by '{password}'")
                cursor.execute(f"create user '{name}'@'%' identified by '{password}'")
                if ug==1:
                    tot=cursor.execute("select count(*) from ug1")
                    cursor.execute(f"insert into  ug1 (username,uid,pwd)values ('{name}',{tot},{password})")
                    cursor.execute(f"grant insert, select,delete on csc3170.application to '{name}'@'%' ")
                    cursor.execute(f"grant select on csc3170.result to '{name}'@'%' ")
                elif ug==2:
                    tot=cursor.execute("select count(*) from ug2")
                    cursor.execute(f"insert into  ug2 (username,uid,pwd)values ('{name}',{tot},{password})")
                    cursor.execute(f"grant all on csc3170.result to '{name}'@'%' ")
                    cursor.execute(f"grant all on csc3170.pattent to '{name}'@'%' ")
                    cursor.execute(f"grant all on csc3170.reject_details to '{name}'@'%' ")
                elif ug==3:
                    tot=cursor.execute("select count(*) from ug3")
                    cursor.execute(f"insert into  ug3 (username,uid,pwd)values ('{name}',{tot},{password})")
                    cursor.execute(f"grant select on csc3170.ID2COMP to '{name}'@'%'")
                cursor.close()
            return Response({"msg":"success"})

class login(ViewSet):
    serializer=LoginSerizalizer
    def list(self,request):
        return Response("post")

    def post(self,request):
        if request.method=="POST":
            temp=JSONParser().parse(request)
            name=temp.get("name")
            ug=temp.get("ug")
            pw=temp.get("pwd")
            with connection.cursor() as cursor:
                rst=(cursor.execute(f"select pwd from ug{ug} where username='{name}'"))
                if rst==1:
                    temp=(int) (cursor.fetchone()[0])

                    if temp==pw:
                        return render(request,f"login{ug}.html",{'group':ug})
                    else:
                        return Response("wrong password or username")
                else:
                    rst=cursor.execute(f"select * from mysql.user where User='{name}'")
                    if rst==1:
                        return Response("wrong password or username")
                    else:
                        return Response("Create an account")
        return Response({"MSG":"SUCCESS"})

