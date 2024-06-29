from django import forms
from .models import Checklist
from django.utils.dateparse import parse_date


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = '__all__'
        widgets = {
            'areas_comuns': forms.Select(choices=Checklist.AREAS_COMUNS_CHOICES),
            'areas_externas': forms.Select(choices=Checklist.AREAS_EXTERNAS_CHOICES),
            'condominio': forms.Select(choices=Checklist.CONDOMINIOS_CHOICES),
            'torre': forms.Select(choices=Checklist.TORRE_CHOICES),
            'andar': forms.Select(choices=Checklist.ANDAR_CHOICES),
            'upload': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'apartamento': forms.Select(choices=Checklist.APARTAMENTO_CHOICES),
            'outros': forms.TextInput(attrs={'placeholder': 'Especifique o local (ex: Condomínio X, Torre Y, Andar Z, corredor em frente a Área Comum: Academia )'}),
            'prioridade': forms.Select(choices=Checklist.PRIORIDADE_CHOICES),
            'categoria': forms.Select(choices=Checklist.CATEGORIA_CHOICES),
            'descricao_problema': forms.Textarea(attrs={'placeholder': 'Descreva o problema aqui...', 'rows': 4, 'cols': 50}),
            'autor_tipo': forms.Select(choices=[
                ('sindicoAdm', 'Síndico/Administrador'),
                ('morador', 'Morador'),
                ('outros', 'Outros'),
            ]),
        }

    #data do pocorrencia
    def clean_data_criacao_upload(self):
        data_criacao_upload = self.cleaned_data.get('data_criacao_upload')
        if data_criacao_upload:
            try:
                parse_date(data_criacao_upload)
            except ValueError:
                raise forms.ValidationError("Formato de data inválido. Use o formato DD-MM-AAAA.")
        return data_criacao_upload
    
    #data checklist(foto do checklist/ocorrencia)
   # def clean_data_checklist(self):
        data_checklist = self.cleaned_data.get('data_checklist')
        if data_checklist:
            try:
                parse_date(data_checklist)
            except ValueError:
                raise forms.ValidationError("Formato de data inválido. Use o formato DD-MM-AAAA.")
        return data_checklist
         
    def clean_imagem(self):
        upload = self.cleaned_data.get('upload')
        if upload:
            if not upload.name.endswith(('.jpeg', '.png', '.gif')):
                raise forms.ValidationError("Formato de arquivo de imagem inválido. Apenas JPEG, PNG e GIF são suportados.")
        return upload

    def clean_nome_autor(self):
        nome_autor = self.cleaned_data.get('nome_autor')
        if len(nome_autor) < 2:
            raise forms.ValidationError("Por favor, insira um nome válido.")
        if len(nome_autor) > 100:  # Limite máximo de 100 caracteres
            raise forms.ValidationError("O nome não pode ter mais de 100 caracteres.")
        return nome_autor
    
    def clean_descricao_problema(self):
        descricao_problema = self.cleaned_data.get('descricao_problema')
        if len(descricao_problema) > 500:  # Limite máximo de 500 caracteres
            raise forms.ValidationError("A descrição do problema não pode ter mais de 500 caracteres.")
        return descricao_problema
