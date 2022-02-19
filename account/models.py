from django.contrib.gis.db import models
from django.contrib.gis import forms
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# create a new user
class MyAccountManager(BaseUserManager):
    def create_user(self, email, phone, username, password=None):
        if not email:
            raise ValueError("استفاده از ایمیل به منظور تسهیل ارتباط و اطلاع رسانی ضروریست")
        if not username:
            raise ValueError("لطفا نام کاربری را وارد کنید")
        if not phone:
            raise ValueError("لطفا تلفن همراه را وارد کنید")
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            phone = phone,
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
        
    def create_superuser(self, email, username, phone, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            phone = phone,
            password = password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# def get_profile_image_filepath(self):
#     return f'profile_images/{self.pk}/{"profile_image.png"}' 

# def get_default_profile_image():
#     return "articles/img/asemankesht2forweb.png"

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="رایانامه", max_length=60,unique=True)
    username = models.CharField(max_length=60,verbose_name="نام کاربری", unique=True)
    phone = models.CharField(verbose_name="تلفن همراه",null=False, blank=False, unique=True,max_length=25)
    address = models.TextField(verbose_name="آدرس مزرعه",help_text="لطفا آدرس مزرعه یا باغ را وارد کنید")
    date_joined = models.DateTimeField(blank=True, null=True, verbose_name="تاریخ عضویت", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="آخرین بازدید",auto_now = True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    products = models.TextField(verbose_name="توضیحات",blank=True, null=True,help_text="چه گیاهان و بذر هایی کشت میکنید")
    area = models.PositiveIntegerField(blank=True, null=True,verbose_name="مساحت ",help_text="لطفا مساحت باغ یا سطح زیر کشت را وارد کنید")
    # profile_image = models.ImageField(verbose_name="تصویر پروفایل",upload_to=get_profile_image_filepath, height_field=None, width_field=None, max_length=255,blank=True, null=True,default=get_default_profile_image)
    geom=models.MultiPolygonField(srid=4326,blank=True, null=True,verbose_name='مزرعه من', )
    hide_email = models.BooleanField(default=True)
    hide_phone = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']

    def __str__(self):
        return self.username


    # def get_profile_image_filename(self):
    #     return str(self.profile_image)[str(self.profile_image).index(f'profile_images/{self.pk}/'):]

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True
    


    
    