from django import forms
from django.utils.translation import gettext_lazy as _
from .models import CadastroSindico

class SindicoLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        try:
            sindico = CadastroSindico.objects.get(email=email)
        except CadastroSindico.DoesNotExist:
            sindico = None
            self.add_error('email', _("Email ou senha incorretos. Por favor, tente novamente."))

        if sindico and not sindico.check_password(password):
            self.add_error('password', _("Email ou senha incorretos. Por favor, tente novamente."))

        cleaned_data['sindico'] = sindico
        return cleaned_data

class CadastroSindicoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CadastroSindico
        fields = ['email', 'nome', 'data_nascimento', 'inicio_mandato', 'fim_mandato', 'cpf', 'password']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError(_('As senhas não correspondem.'), code='password_mismatch')

        return password_confirm

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CadastroSindico.objects.filter(email=email).exists():
            raise forms.ValidationError(_('Este e-mail já está em uso. Por favor, escolha outro.'), code='email_in_use')

        return email

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if CadastroSindico.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError(_('Este CPF já está em uso. Por favor, escolha outro.'), code='cpf_in_use')

        if not cpf.isdigit() or len(cpf) != 11:
            raise forms.ValidationError(_('CPF inválido. Deve conter apenas números e ter 11 dígitos.'), code='invalid_cpf')

        return cpf
    
    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')
        if not data_nascimento:
            self.add_error('data_nascimento', _('Por favor, insira a data de nascimento.'))
        return data_nascimento

    def clean_inicio_mandato(self):
        inicio_mandato = self.cleaned_data.get('inicio_mandato')
        if not inicio_mandato:
            self.add_error('inicio_mandato', _('Por favor, insira a data de início do mandato.'))
        return inicio_mandato

    def clean_fim_mandato(self):
        fim_mandato = self.cleaned_data.get('fim_mandato')
        if not fim_mandato:
            self.add_error('fim_mandato', _('Por favor, insira a data de término do mandato.'))
        return fim_mandato

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user