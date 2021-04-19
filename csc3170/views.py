from pickle import GET

import pymysql
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
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
        return Response("msg:success")

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
        return Response({"msg:success"})

    def post(self,request):
        print(request.method,"r1q")
        if request.method=="POST":
            print(request.POST)

            name=request.POST.getlist("name")[0]
            ug=request.POST.getlist("ug")[0]
            pw=(int)(request.POST.getlist("pwd")[0])
            with connection.cursor() as cursor:
                rst=(cursor.execute(f"select pwd from ug{ug} where username='{name}'"))
                if rst==1:
                    temp=(int) (cursor.fetchone()[0])
                    if temp==pw:
                        print("thisisachived")
                        j=render(request,f"page{ug}.html",{"ug":ug})
                        j.set_cookie("bing","1145141919810")
                        return j
                    else:
                        return render(request,"main.html")
                else:
                    rst=cursor.execute(f"select * from mysql.user where User='{name}'")
                    if rst==1:
                        return render(request,"main.html")
                    else:
                        return render(request,"main.html")

def search(request):
    if request.method==GET:
        result=JSONParser().parse(request)
        ug=result.get("ug")
        uid=result.get("uid")
        appid=result.get("appid")
        with connection.cursor as cursor:
            temp=cursor.execute(f"select * from application where uid={uid}")
            result=temp.fetchall()
            return render(request,"query1.html",{"list":result})


def iambornforthis(request,id=1,paralist=None):
    j=render(request,f"page{id}.html",paralist)

    return HttpResponse({"MSG":"S"})#render(request=request,template_name=f'page{id}.html',context=paralist)
