import json
import datetime
from django.http import  HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from csc3170.serizalizer import CreateUserSerizalizer,LoginSerizalizer
from django.db import connection

# Create your views here
def ug1_new_insert(request):
    return render(request,'ug1_new_application.html')

def ug1_my_pattent(request):
    return render(request,'ug1_my_patent.html')

def ug1_my_application(request):
    return render(request,'ug1_my_application.html')

def ug1_index(request):
    return render(request,'page1.html')

def ug2_index(request):

    return render(request,"page2.html")

class UserAuthorization(ViewSet):
    serializer=CreateUserSerizalizer
    def list(self,request):
        return Response("msg:success")

    def post(self,request):
        if request.method=="POST":

            with connection.cursor()as cursor:
                name=request.POST.getlist("name")[0]
                ug=(int)(request.POST.getlist("ug")[0])
                password = (int)(request.POST.getlist("pwd")[0])
                cursor.execute(f"select count(*) from ug{ug}")
                tot=cursor.fetchone()[0]
                cursor.execute(f"insert into  ug{ug} (username,uid,pwd)values ('{name}',{tot+1},{password})")
            return Response({"msg":"success"})

class login(ViewSet):
    serializer=LoginSerizalizer
    def list(self,request):
        return Response({"msg:success"})

    def post(self,request):
        if request.method=="POST":

            name=request.POST.getlist("name")[0]
            ug=request.POST.getlist("ug")[0]
            pw=(int)(request.POST.getlist("pwd")[0])
            with connection.cursor() as cursor:
                rst=(cursor.execute(f"select pwd,uid from ug{ug} where username='{name}'"))
                if rst==1:
                    q=cursor.fetchone()
                    temp=(int) (q[0])
                    if temp==pw:
                        j=render(request,f"page{ug}.html",{"ug":ug,"uid":(int)(q[1])})
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

def home(request):
    return render(request,template_name="main.html")

class UG1_Search_Pattent(ViewSet): #ug1_main --> ug1_my_pattent
    serializer = CreateUserSerizalizer

    def list(self, request):
        return Response("POST,PUT")

    # 搜索
    def post(self, request):
        if request.method == "POST":
            uid = request.POST.getlist("uid")[0]
            app_type = request.POST.getlist("app_type")[0]
            with connection.cursor()as cursor:
                if int(app_type) == 0:#
                    cursor.execute("select pattent_id from pattent where uid=%s", (uid))
                    ptt = cursor.fetchall()
                    l0 = []
                    for i in ptt:
                        l0.append(i[0])
                    returndata = {"pid": l0, "uid":uid}
                    return render(request,f"ug1_my_patent.html",returndata)

class UG1_Search_Application(ViewSet):      #ug1_main --> ug1_my_application
    serializer = CreateUserSerizalizer

    def list(self, request):
        return Response("POST,PUT")

    # 搜索
    def post(self, request):
        if request.method == "POST":
            uid = request.POST.getlist("uid")[0]

            ug = request.POST.getlist("ug")[0]

            with connection.cursor()as cursor:
                    cursor.execute(f"select app_id,final_status from result where app_type=1&&app_id in (select app_id from application where uid={uid})")
                    app = cursor.fetchall()
                    btr='<tr><th>application id</th><th>result</th></tr>'
                    for j in app:
                        btr+=f'<tr><td>{j[0]}</td><td>{j[1]}</td></tr>'
                    cursor.execute(f"select status_1,status_2,status_3,app_id from result where app_type=0&&app_id in (select app_id from application where uid={uid})")
                    app = cursor.fetchall()
                    str = '<tr><th>application id</th><th>status1</th><th>status2</th><th>status3</th></tr>'
                    for j in app:
                        str += f'<tr><td>{j[3]}</td><td>{j[0]}</td><td>{j[1]}</td><td>{j[2]}</td></tr>'
                    returndata = {"application": str,"bpplication":btr,"uid":uid}
                    return render(request,f"ug{ug}_my_application.html",returndata)

class Pattent_Detail(ViewSet):
    serializer = CreateUserSerizalizer

    def list(self, request):
        return Response("POST,PUT")

    # 搜索
    def post(self, request):
        if request.method == "POST":
            pid = request.POST.getlist("pid")[0]
            uid = (int)(request.POST.getlist("uid")[0])
            with connection.cursor()as cursor:
                cursor.execute("select * from pattent where pattent_id=%s", (pid))
                ptt = cursor.fetchall()
                str = '<tr><th>Patent id</th><th>Patent Name</th><th>Owner</th><th>Start Date</th><th>Expire Date</th></tr>'
                for j in ptt:
                    str += f'<tr><td>{j[0]}</td><td>{j[-1]}</td><td>{j[2]}</td><td>{j[3]}</td><td>{j[4]}</td></tr>'

                return_data = {"pattents": str, "uid":uid,"pid":pid}

        return render(request,f"patent_info.html",return_data)

class UG1_new_application(ViewSet):      #ug1_main --> ug1_new_application
    serializer = CreateUserSerizalizer

    def list(self, request):
        return Response("POST,PUT")

    def post(self, request):
        if request.method == "POST":
            uid = request.POST.getlist("uid")[0]
        return render(request,f"ug1_new_application.html",{"uid":uid})

class UG1_insert(ViewSet):
    serializer = CreateUserSerizalizer

    def list(self, request):
        return Response("POST,PUT")

    # 增加申请
    def post(self, request):
        if request.method == "POST":
            uid = (int)(request.POST.getlist("uid")[0])
            ename = request.POST.getlist("ename")[0]
            pname = request.POST.getlist("pname")[0]
            type_lv1 = (int)(request.POST.getlist("type_lv1")[0])
            type_lv2 = (int)(request.POST.getlist("type_lv2")[0])
            type_lv3 = (int)(request.POST.getlist("type_lv3")[0])
            text = request.POST.getlist("text")[0]
            app_date = datetime.date.today().strftime("%Y-%m-%d")
            with connection.cursor()as cursor:
                sql_get_appid = f"select app_id from application"
                cursor.execute(sql_get_appid)
                exist_appid=cursor.fetchall()
                num=len(exist_appid)
                app_id=uid*10000+num

                sql = f"INSERT INTO application (app_id, app_date, uid, ename, pname, type_lv1, type_lv2, type_lv3, text,app_type)  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                #insert result

                param = (app_id, app_date, uid, ename, pname, type_lv1, type_lv2, type_lv3, text,0)
                cursor.execute(sql, param)
                cursor.execute(f"insert into result(app_id,app_date,finished,uid,ename,pname,app_type)values({app_id},'{app_date}',-1,{uid},'{ename}','{pname}',0)")
        return render(request,f"ug1_success.html",{"uid":uid})

class UG1_app_detail(ViewSet):#修改需要的数据：uid, appid, 返回能给修改人看的数据app_id, app_date, ename, type_lv1~3, pname, text(前6个不能改，只能改后两个),需要修改则进入modify_app页面
    serializer = CreateUserSerizalizer

    def list(self, request):
        return Response("POST,PUT")

    def post(self, request):
        if request.method == "POST":
            uid = request.POST.getlist("uid")[0]
            app_id=request.POST.getlist("app_id")[0]
            with connection.cursor()as cursor:
                cursor.execute("select app_date,ename,type_lv1,type_lv2,type_lv3,pname,text from application where app_id=%s", (app_id))
                app = cursor.fetchall()
                d = {}
                for j in app:
                    d['app_date'] = j[0]
                    d['ename'] = j[1]
                    d['type_lv1'] = j[2]
                    d['type_lv2'] = j[3]
                    d['type_lv3'] = j[4]
                    d['pname'] = j[5]
                    d['text'] = j[6]
                html="<label>"
                for i in d:
                    html+=f"{i}<input value='{d.get(i)}' id='{i}'><br>"
                html+="</label>"
                cursor.execute(f"select status_1,status_2,status_3,finished,final_status from result where app_id={app_id}")
                j=cursor.fetchone()
                if j[3]==-1:
                    html+="<b>Pending</b><button onclick='addinfor()'>Modify</button><br>"
                elif j[3]<2:
                    html+=f"<b>Processing at stage{j[3]+2}</b>"
                else:
                    html+="<b>Finished</b><br>"

                    if j[4]==0:
                        html+=f"<b>Your Application for Patent {j[-1]} have been rejected</b><br>"
                        cursor.execute(f"select * from reject_detail where app_id={app_id}")
                        temp=cursor.fetchall()
                        reason1=0
                        reason2=0
                        reason3=0
                        for i in temp:
                            reason1+=i[6]
                            reason2+=i[7]
                            reason3+=i[8]
                        lst=[reason1,reason2,reason3]
                        for i in range(0,3):
                            if lst[i]!=0:
                                html+=f"<b>Rejection from reason{i} based on{lst[i]} references</b><br>"
                    else:
                        cursor.execute(f"select * from pattent where application_id={app_id}")
                        j=cursor.fetchone()

                        html+=f"<b>Your Application for Patent {j[-1]} have been approved</b><br><b>The Patent Number is {j[0]}</b><br><b>Your Patent will be valid from {j[3]} to {j[4]}"
                returndata = {"app_info": html,"uid":uid,"app_id":app_id}
        return render(request,f"ug1_modify_application.html",returndata)

class UG1_modify_owner(ViewSet):#修改需要的数据：uid, pid, app_type, app_otype, new_owner
    serializer = CreateUserSerizalizer

    def list(self, request):
        return Response("POST,PUT")

    def post(self, request):
        if request.method == "POST":
            uid = (int)(request.POST.getlist("uid")[0])
            pid = request.POST.getlist("pid")[0]
            app_type = 1
            app_new_owner = request.POST.getlist("app_new_owner")[0]
            app_otype=request.POST.getlist("app_otype")[0]
            with connection.cursor()as cursor:
                #生成appid
                sql_get_appid=f"select app_id from application"
                cursor.execute(sql_get_appid)
                exist_appid=cursor.fetchall()
                num=len(exist_appid)
                app_id=num+uid*10000
                app_date = datetime.date.today().strftime("%Y-%m-%d")
                if app_type == 1:
                    # 变更新的所有者
                    sql1=f"insert into application (app_id, app_new_owner, app_otype, pid, uid,app_type,app_date) values (%s,%s,%s,%s,%s,%s,%s)"
                    param1=(app_id,app_new_owner,app_otype,pid,uid,app_type,app_date)
                    cursor.execute(sql1,param1)
                    cursor.execute(f"insert into result (app_id,app_date,app_type,uid,finished)values({app_id},{app_date},1,{uid},-1)")
                    return render(request,f"ug1_success.html",{"uid":uid})

class UG1_modify_application(ViewSet):#修改需要的数据：uid, pid, app_type, app_otype, new_owner
    serializer = CreateUserSerizalizer

    def list(self, request):
        return Response("POST,PUT")

    def post(self, request):
        if request.method == "POST":
            uid = request.POST.getlist("uid")[0]
            app_id=request.POST.getlist("app_id")[0]
            pname=request.POST.getlist("pname")[0]
            text=request.POST.getlist("text")[0]
            with connection.cursor()as cursor:
                # 数据库modify，变更已提交的申请
                cursor.execute("UPDATE application SET pname=%s, text=%s where app_id=%s", (pname,text,app_id))
                return render(request,f"ug1_success.html",{"uid":uid})

class UG1_delete(ViewSet):
    serializer = CreateUserSerizalizer

    def get(self, request):
        return Response("POST,PUT")

    def post(self, request):
        if request.method == "POST":
            app_id = request.POST.getlist("app_id")[0]
            with connection.cursor()as cursor:
                # 数据库delete
                cursor.execute("delete from application where app_id=%s", (app_id))
                cursor.execute("delete from result where app_id=%s", (app_id))
        return render(request,f"ug1_delete.html")

class UG1_success(ViewSet): #ug1_sucess --> ug1_main
    serializer = CreateUserSerizalizer

    def list(self, request):
        return Response("POST,PUT")

    def post(self, request):
        if request.method == "POST":
            uid = request.POST.getlist("uid")[0]
            return render(request,f"page1.html", {"uid":uid})

class  ug2_modify(ViewSet):
    serializer=CreateUserSerizalizer

    def list(self,requset):
        return Response("POST")

    def post(self,request):
        if request.method=="POST":
            appid = (int)(request.POST.getlist("appid")[0])
            type=request.POST.getlist("type")[0]
            id=request.POST.getlist("uid")[0]
            result = request.POST.getlist("result")[0]


            result= True if result=="true" else False

            with connection.cursor() as cursor:

                if type=='0':
                    reasonlist=request.POST.getlist("why[]")

                    cursor.execute(f"select finished from result where app_id={appid}")
                    finished=cursor.fetchone()[0]
                    cursor.execute(f"update result set status_{finished+2}={result},finished={finished+1} where(app_id={appid})")
                    if not result:
                        cursor.execute(f"insert into reject_detail (app_id,status,reason_1,reason_2,reason_3,ref_reason1,ref_reason2,ref_reason3)values({appid},0,0,0,0,0,0,0)")
                        for i in range(0,3):
                            if reasonlist[i]!='0':
                                cursor.execute(f"update reject_detail set reason_{i+1}=1,ref_reason{i+1}={(int)(reasonlist[i])} where(app_id={appid})")
                    if finished>=1:
                        cursor.execute(f"select status_1,status_2,status_3 from result where app_id={appid}")
                        temp=cursor.fetchone()
                        if temp[0]*temp[1]*temp[2]!=0:
                            cursor.execute(f"update result set final_status=1 where app_id={appid}")
                            cursor.execute(f"select * from application where app_id={appid}")
                            j=cursor.fetchone()
                            startdate=datetime.date.today().strftime('%Y-%m-%d')
                            year=datetime.date.today().year+20
                            month=datetime.date.today().month
                            day=datetime.date.today().day
                            enddate=datetime.date(year, month, day).strftime('%Y-%m-%d')
                            cursor.execute(f"insert into pattent(start_date,expire_date,pattent_id,application_id,owner,pname,type_lv1,type_lv2,type_lv3,content,uid,owner_type)values({startdate},{enddate},{j[2]+j[0]},{j[0]},'{j[3]}','{j[4]}',{j[5]},{j[6]},{j[7]},'{j[8]}',{j[2]},0)")
                        else:
                            cursor.execute(f"update result set final_status=0 where app_id={appid}")
                else:
                    if result:

                        cursor.execute(f"select pid,app_new_owner,app_otype from application where app_id={appid}")
                        temp=cursor.fetchone()
                        pid=temp[0]
                        oname=temp[1]
                        otype=temp[2]
                        id=0

                        if int(otype)==1:
                            cursor.execute(f"select cid from company where cname='{oname}'")
                            id = cursor.fetchone()[0]
                            cursor.execute(f"insert into company_own set comp_id={id},pid={pid}")
                        else:
                            cursor.execute(f"select id from personal where name='{oname}'")
                            id = cursor.fetchone()[0]
                            cursor.execute(f"insert into company_own set id={id},pid={pid}")

                        cursor.execute(f"update result set finished=2,status_1=1,status_2=1,status_3=1,final_status=1 where app_id={appid}")
                        cursor.execute(f"update pattent set owner_type={otype},owner='{oname}',owner_id={id} where pattent_id={pid}")
                    else:
                        cursor.execute(f"update result set finished=2,status_1=0,status_2=0,status_3=0,final_status=0 where app_id={appid}")
                return render(request,"page2.html",{"uid":id})

class ug2_fetch(ViewSet):
    serializer = CreateUserSerizalizer

    def list(self, requset):
        return Response("POST")

    def post(self, request):

        if request.method == "POST":
            uid=request.POST.getlist("uid")[0]
            type=request.POST.getlist("type")[0]
            appid = request.POST.getlist("pid")[0]
            with connection.cursor() as cursor:

                if type=='1':
                    if appid!="":
                        cursor.execute(f"select app_id,app_new_owner,app_otype,pid from application where app_id={(int)(appid)}&&app_type=1")
                        k = cursor.fetchone()

                        pid=k[3]
                        no=k[1]
                        new_ot="personal" if k[2]==0 else "company"
                        cursor.execute(f"select owner,owner_type from pattent where pattent_id={pid}")
                        q=cursor.fetchone()
                        co=q[0]
                        cot="personal" if q[1]==0 else "company"
                        return render(request,"app_owner_detail.html",{"appid":k[0],"no":no,"not":new_ot,"uid":uid,"pid":k[3],"co":co,"cot":cot})

                    else:
                        cursor.execute("select app_id from result where app_type=1&&finished<=1")
                        k = cursor.fetchall()
                        return HttpResponse(json.dumps(k))
                else:
                    if appid!="":
                        cursor.execute(f"select app_id,ename,pname,type_lv1,type_lv2,type_lv3,text from application where app_id={(int)(appid)}&&app_type=0")
                        k = cursor.fetchone()
                        appid=k[0]
                        ename=k[1]
                        pname=k[2]
                        lv1=k[3]
                        lv2=k[4]
                        lv3=k[5]
                        text=k[6]
                        dic={"uid":uid,"appid":appid,"ename":ename,"pname":pname,"lv1":lv1,"lv2":lv2,"lv3":lv3,"text":text}
                        cursor.execute(f"select finished from result where app_id={appid}")
                        finish=cursor.fetchone()[0]
                        return render(request,"app_new_detail.html",dic)

                    else:
                        cursor.execute("select app_id from result where app_type=0&&finished<=1")
                        k = cursor.fetchall()
                        return HttpResponse(json.dumps(k))

def ug3_index(request):
    return render(request,'page3.html')

class UG3_Behavior(ViewSet):
    serializer = CreateUserSerizalizer

    def list(self, request):
        return Response("POST,PUT")

    def post(self, request):
        if request.method == "POST":
            comp_id=request.POST.getlist("company_id")[0]
            type_lv1=request.POST.getlist("type_lv1")[0]
            type_lv2=request.POST.getlist("type_lv2")[0]
            with connection.cursor() as cursor:
                cursor.execute(f"select pid from company_own where comp_id={(int)(comp_id)}")
                pnumber=len(cursor.fetchall())
                ptt_1_list=[]
                cursor.execute(f"select type_lv1 from pattent where pattent_id in (select pid from company_own where comp_id={(int)(comp_id)})")
                ptt_type_1=cursor.fetchall()
                for i1 in ptt_type_1:
                    ptt_1_list.append(i1[0])
                ptt_1_list_type=set(ptt_1_list)
                dict_1={}
                dict_2={}
                dict_3={}
                for j1 in ptt_1_list_type:
                   dict_1[j1]=ptt_1_list.count(j1)
                if type_lv1!="":
                    ptt_2_list=[]
                    cursor.execute(f"select type_lv2 from pattent where pattent_id in (select pid from company_own where comp_id={(int)(comp_id)}) and type_lv1={(int)(type_lv1)}")
                    ptt_type_2=cursor.fetchall()
                    for i2 in ptt_type_2:
                        ptt_2_list.append(i2[0])
                    ptt_2_list_type=set(ptt_2_list)
                    for j2 in ptt_2_list_type:
                        dict_2[j2]=ptt_2_list.count(j2)
                    if type_lv2!="":
                        ptt_3_list=[]
                        cursor.execute(f"select type_lv3 from pattent where pattent_id in (select pid from company_own where comp_id={(int)(comp_id)}) and type_lv2={(int)(type_lv2)} and type_lv1={(int)(type_lv1)}")
                        ptt_type_3=cursor.fetchall()
                        for i3 in ptt_type_3:
                            ptt_3_list.append(i3[0])
                        ptt_3_list_type=set(ptt_3_list)
                        for j3 in ptt_3_list_type:
                            dict_3[j3]=ptt_3_list.count(j3)
                html1=""
                for i in dict_1:
                    html1+=f"<tr><td>{i}</td><td>{dict_1.get(i)}</td></tr>"
                html2=""
                for i in dict_2:
                    html2+=f"<tr><td>{i}</td><td>{dict_2.get(i)}</td></tr>"
                html3 = ""
                for i in dict_3:
                    html3 += f"<tr><td>{i}</td><td>{dict_3.get(i)}</td></tr>"
                return render(request,f"answer.html",{"dict_1":html1,"dict_2":html2,"dict_3":html3,"pattent_number":comp_id,"lv1":type_lv1,"lv2":type_lv2})

