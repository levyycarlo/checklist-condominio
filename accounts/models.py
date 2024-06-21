from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class CadastroSindicoManager(BaseUserManager):
    def create_user(self, email, nome, cpf, data_nascimento, inicio_mandato, fim_mandato, password=None):
        if not email:
            raise ValueError('O email deve ser fornecido')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, cpf=cpf, data_nascimento=data_nascimento,
                          inicio_mandato=inicio_mandato, fim_mandato=fim_mandato)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, cpf, data_nascimento, inicio_mandato, fim_mandato, password=None):
        user = self.create_user(email, nome, cpf, data_nascimento, inicio_mandato, fim_mandato, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CadastroSindico(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=30)
    data_nascimento = models.DateField()
    inicio_mandato = models.DateField()
    fim_mandato = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    password = models.CharField(max_length=128)

    last_login = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'cpf', 'data_nascimento', 'inicio_mandato', 'fim_mandato']

    objects = CadastroSindicoManager()

    def __str__(self):
        return self.email

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_superuser
