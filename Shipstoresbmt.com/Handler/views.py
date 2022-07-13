from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import ClientInfoSerializer,KeySerializer,AdminSerializer,AdminUploads,Serial_number_Serializer
from . models import Login_info,Key_info,Admin_info,Admin_uploads_file,Admin_Serial_number
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication,TokenAuthentication, BaseAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
import sqlite3
from pathlib import Path
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from time import *
import uuid

#============================================User name and email===========================================
BASE_DIR = Path(__file__).resolve().parent.parent
class Login_Api(APIView):
    def get(self, request):
        Recieved_data = Login_info.objects.all()
        serializer = ClientInfoSerializer(Recieved_data, many=True)
       # return Response(serializer.data)
        return render(request, 'Error_page/error_page.html') 
    def post(self, request):    
        serializer = ClientInfoSerializer(data=request.data) 
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'Token_page/Token_page.html')
        else:
            return render(request, 'Error_page/error_page.html')

class Login_Out(APIView):
    def get(self, request):
        Recieved_data = Login_info.objects.all()
        serializer = ClientInfoSerializer(Recieved_data, many=True)
        return Response(serializer.data)
#==========================================create Pass-phrase======================================

class Key_Values(APIView):
    def get(self, request):
        Recieved_data = Key_info.objects.all()
        serializer = KeySerializer(Recieved_data, many=True)
        return Response(serializer.data)
    def post(self, request):    
        serializer = KeySerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return render(request, 'Accepted_page/Accepted_page.html')
        else:
            return render(request, 'Error_page/error_page.html')

#===============================================admin login============================================
class Admin_Api(APIView):
    def get(self, request):
        return render(request, 'Admin_login/Admin_login.html',)
        #Recieved_data = Admin_info.objects.all()
        #serializer = AdminSerializer(Recieved_data, many=True)
        #return Response(serializer.data)
    def post(self, request):    
        serializer = AdminSerializer(data=request.data) 
        if serializer.is_valid():
            user_password_check = request.data['Password_value']
            user_name_check = request.data['User_name']
            conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
            c = conn1.cursor()
            c.execute(f"SELECT * FROM  Handler_Admin_info WHERE  User_name='{user_name_check}'")
            Clients_info = c.fetchone()
            conn1.commit()
            conn1.close()  
            print(Clients_info)
            if Clients_info == []:
             return render(request, 'Error_page/error_page.html')
            else:
             try: 
               if user_password_check == Clients_info[2]:
                return render(request, 'Admin_panel/Admin.html')
               else:  
                   return render(request, 'Error_page/error_page.html')
             except:
               return render(request, 'Error_page/error_page.html')
        else:
            return render(request, 'Error_page/error_page.html')

#=============================================home page==============================================
class HomePage(APIView):
   def get(self,request):
    return render(request, 'index.html')

#===========================================pass-phrase aythentication==================================
class TokenAuthPage(APIView):
    def get(self,request):
      return render(request, 'Error_page/error_page.html') 
    def post(self, request):
        print(request) 
        serializer = KeySerializer(data=request.data) 
        if serializer.is_valid(): 
            user_check = request.data['Key_value']          
            conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
            c = conn1.cursor()
            c.execute(f"SELECT * FROM  Handler_Key_info WHERE  Key_value='{user_check}'")
            Clients_info = c.fetchone()
            print(Clients_info)
            conn1.commit()
            conn1.close()  
            if Clients_info == None: 
              return render(request, 'Error_page/error_page.html')
            else:
             conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
             c = conn1.cursor()
             c.execute(f"DELETE from  Handler_Key_info WHERE  Key_value='{user_check}'")
             conn1.commit()
             conn1.close() 
             conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
             c = conn1.cursor()
             c.execute(f"SELECT * FROM  Handler_Admin_uploads_file ")
             Clients_info2 = c.fetchall()
             conn1.commit()
             conn1.close()  
             return render(request, 'Log_forms_page/Log_forms_fill.html', {'data':Clients_info2})
        else:
          return render(request, 'Error_page/error_page.html')  
#============================================================================================

#============================================================================================
class UploadPage(APIView):
    def get(self,request):
      return render(request, 'Upload_document/Upload_D.html') 

class UploadPageAdmin(APIView):
    def get(self,request):
      return render(request, 'Upload_document _admin/Upload_admin.html') 
    def post(self,request):
          pass
#============================================================================================


#============================================================================================
class UploadPageAdmin_upload(APIView):
    def get(self,request):
        conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
        c = conn1.cursor()
        c.execute(f"SELECT * FROM  Handler_Admin_uploads_file ")
        Clients_info9 = c.fetchall()
        conn1.commit()
        conn1.close()          
        print(Clients_info9)
        return Response(Clients_info9) 
#============================================================================================


#============================================================================================
class Serial_number(APIView):
    def get(self,request):
      Recieved_data = Admin_Serial_number.objects.all()
      serializer = Serial_number_Serializer(Recieved_data)
      print(serializer.data)
  #    return Response(serializer.data) 
      return render(request, 'Upload_document _admin/Upload_admin.html') 
    def post(self,request):
       serializer =  Serial_number_Serializer(data=request.data) 
       if serializer.is_valid(): 
        print(serializer.data['Number_code'])   
        print()
        conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
        c = conn1.cursor()
        c.execute(f"""UPDATE Handler_Admin_Serial_number SET Number_code = :Number_code""",{'Number_code':serializer.data['Number_code']})
        conn1.commit()
        conn1.close() 
        return render(request, 'Accepted_page/Accepted_page.html')
       else:
        return render(request, 'Error_page/error_page.html')
#============================================================================================


#============================================================================================
class Upload_file(APIView):
    def get(self,request):
     return render(request, 'Error_page/error_page.html') 
    def post(self,request):
       try: 
        conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
        c = conn1.cursor()
        c.execute(f"SELECT * FROM  Handler_Admin_Serial_number ")
        Clients_info3 = c.fetchall()
        conn1.commit()
        conn1.close()    
        uploading_file = request.FILES['file_up']
        fs = FileSystemStorage()
        old = uploading_file.name
        name_Serial = str(old)[:-4]+"_"+"["+str(Clients_info3[0][1])+"].pdf"
        fs.save(name_Serial,uploading_file)
        current_date = strftime("%d/%b/%Y")
        conn1 = sqlite3.connect(f'{BASE_DIR}\\db.sqlite3')
        c = conn1.cursor()
        new_id = int(str(int(uuid.uuid1()))[4:7])
        print(new_id )
        c.execute("INSERT INTO Handler_Admin_uploads_file VALUES (:id,:File_Name, :date)",
               {   'id':new_id  ,
                   'File_Name': name_Serial,
                   'date': current_date,  
               }) 

       # c.execute(f"DELETE from  Handler_Admin_uploads_file")       
        conn1.commit()
        conn1.close()        
        return render(request, 'Accepted_page2/Accepted_page.html')
       except:
          return render(request, 'Error_page/error_page.html') 
#============================================================================================
