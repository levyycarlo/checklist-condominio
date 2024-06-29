from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CadastroSindicoManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CadastroSindico(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=30, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    inicio_mandato = models.DateField(blank=True, null=True)
    fim_mandato = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=14, unique=True, blank=True, null=True)
    password = models.CharField(max_length=128)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CadastroSindicoManager()

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
