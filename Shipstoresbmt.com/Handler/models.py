from django.db import models

class Login_info(models.Model):
    Full_Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Full_Name

class Key_info(models.Model):
    Key_value = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Key_value

class Admin_info(models.Model):
    User_name = models.CharField(max_length=100)
    Password_value = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.User_name


class Admin_uploads_file(models.Model):
    File_Name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.File_Name


class Admin_Serial_number(models.Model):
    Number_code = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.Number_code
                