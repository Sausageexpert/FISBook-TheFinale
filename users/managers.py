from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self,reg_no,password,first_name,**other_fields):
        if not reg_no:
            raise ValueError("You must provide registration number")
        if not first_name:
            raise ValueError("You must provide first name")
        user = self.model(reg_no=reg_no,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,reg_no,password,first_name,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be staff")
        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be superuser")
        user = self.create_user(reg_no,password,first_name,**other_fields)
        return user