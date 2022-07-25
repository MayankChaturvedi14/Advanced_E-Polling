from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import datetime

# Create your models here.
class Registeration(models.Model):
    Name = models.CharField(max_length=69)
    Email = models.EmailField()
    Mobile = models.CharField(max_length=13)
    Address = models.CharField(max_length=100)
    Aadhar = models.CharField(max_length=12,unique=True)
    VoterID = models.CharField(max_length=10,unique=True)
    DOB = models.DateField(default=datetime.datetime.now().strftime("%Y/%m/%d"))
    
class Cn_Registeration(models.Model):
    Candidate_Name = models.CharField(max_length=69,unique=True)
    Party = models.CharField(max_length=60,unique=True)
    Address = models.CharField(max_length=60)
    ElectoralConstituencies = models.CharField(max_length=60,unique=True)
    Mobile = models.CharField(max_length=13,unique=True)
    Gender = models.CharField(max_length=60)
    doc_file = models.FileField(upload_to='documents/%Y/%m/%d',blank=True, null=True)

    
class Party(models.Model):
    BJP = models.IntegerField(default=0)
    INC = models.IntegerField(default=0)
    BSP = models.IntegerField(default=0)
    TMC = models.IntegerField(default=0)
    NCP = models.IntegerField(default=0)
    NPP = models.IntegerField(default=0)
    AAP = models.IntegerField(default=0)
    JDU = models.IntegerField(default=0)
    RJD = models.IntegerField(default=0)
    SP = models.IntegerField(default=0)
    CPI = models.IntegerField(default=0)
    CPIM = models.IntegerField(default=0)
    RLD = models.IntegerField(default=0)
    NOTA = models.IntegerField(default=0)
    

# class CustomUserManager(BaseUserManager):
#     use_in_migrations=True
#     def create_user(self, user_name,VoterID,DOB):
#         if not VoterID:
#             raise ValueError("Voter ID required")
#         user = self.model(user_name=user_name,VoterID=VoterID,DOB=DOB)
#         user.set_password(VoterID)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, user_name, password, **extra_fields): 
#         extra_fields.setdefault('is_staff', True)  
#         extra_fields.setdefault('is_superuser', True)  
#         extra_fields.setdefault('is_active', True)  
#         if extra_fields.get('is_staff') is not True:  
#             raise ValueError(_('Superuser must have is_staff=True.'))  
#         if extra_fields.get('is_superuser') is not True:  
#             raise ValueError(_('Superuser must have is_superuser=True.'))  
#         return self.create_user(user_name, password, **extra_fields)   


# class User(AbstractUser):
#     user_name = models.CharField(max_length=69)
#     password = models.CharField(max_length=100)
#     VoterID = models.CharField(max_length=10,primary_key=True)
#     DOB = models.DateField(default=datetime.datetime.now().strftime("%Y/%m/%d"))
#     objects = CustomUserManager()  
#     USERNAME_FIELD="VoterID"
#     REQUIRED_FIELDS = []
#     is_staff = models.BooleanField(default=False)  
#     is_active = models.BooleanField(default=True)
#     def has_perm(self, perm, obj=None):  
#         "Does the user have a specific permission?"  
#         return True  
  
#     def is_staff(self):  
#         "Is the user a member of staff?"  
#         return self.staff  
    
#     @property  
#     def is_admin(self):  
#         "Is the user a admin member?"  
#         return self.admin  

#     def __str__(self):  
#         return self.VoterID    

class MyUserManager(BaseUserManager):
    def create_user(self, user_name, vid, DOB):
        if not user_name:
            raise ValueError("username required")
        if not vid:
            raise ValueError("VoterID required")
        if not DOB:
            raise ValueError("DOB required")

        user = self.model(
            user_name=user_name,
            VoterID = vid,
            DOB = DOB
        )
        user.set_password(vid)
        user.save(using=self._db)
        return user


    def create_superuser(self,user_name,password=None):
        if not user_name:
            raise ValueError("username required")
        user = self.model(
            user_name=user_name,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save(using=self._db)
        return user
        
class Voter(models.Model):
    VoterID = models.CharField(max_length=20)

class MyUser(AbstractBaseUser,PermissionsMixin):
    user_name = models.CharField(unique=True, max_length=69)
    VoterID = models.CharField(max_length=20,primary_key=True)
    DOB = models.DateField(default=None, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    if is_superuser:
        USERNAME_FIELD = "user_name"
        REQUIRED_FIELDS = ['password']
    else:
        USERNAME_FIELD = "user_name"
        REQUIRED_FIELDS = ['VoterID','DOB']


    objects = MyUserManager()

    def __str__(self) -> str:
        data = self.VoterID + " " +str(self.is_admin)
        return data

    def hasprem(self,prem,obj=None):
        return True

    def has_module_prems(self, app_label):
        return True

    

        


