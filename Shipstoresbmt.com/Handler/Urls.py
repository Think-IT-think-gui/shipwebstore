from django.urls import path
from . views import Login_Api,Key_Values,Admin_Api,HomePage,TokenAuthPage,UploadPage,UploadPageAdmin,UploadPageAdmin_upload,Serial_number,Upload_file,Login_Out

urlpatterns = [
    path('ShipStore/login/', Login_Api.as_view()),
    path('ShipStore/login/Data', Login_Out.as_view()),
    path('ShipStore/Admin_login/pass_key/', Key_Values.as_view()),

    path('ShipStore/Admin_login/Upload', UploadPageAdmin.as_view()),
    path('ShipStore/Admin_login/new_key', Serial_number.as_view()),
    path('ShipStore/Admin_login/Upload/Data', UploadPageAdmin_upload.as_view()),
    path('ShipStore/Admin_login/', Admin_Api.as_view()),
    path('ShipStore/', HomePage.as_view()),
    path('ShipStore/login/ShipStore_Token/', TokenAuthPage.as_view()),
    path('ShipStore/login/ShipStore_Token/UploadPage', UploadPage.as_view()),
    path('ShipStore/login/ShipStore_Token/action/', Upload_file.as_view()),


]