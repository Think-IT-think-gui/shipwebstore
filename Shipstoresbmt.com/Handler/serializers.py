from rest_framework import serializers
from . models import Login_info,Key_info,Admin_info,Admin_uploads_file,Admin_Serial_number

class ClientInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login_info
        fields = '__all__'
class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key_info
        fields = '__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_info
        fields = '__all__'        

class AdminUploads(serializers.ModelSerializer):
    class Meta:
        model = Admin_uploads_file
        fields = '__all__'                

class Serial_number_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_Serial_number
        fields = '__all__'               