from django.db import models
from .model_bank import Account
from ..validations.validations_receiver import only_int


STATUS_CHOICES = [
        ('V','Validado'),
        ('R', 'Rascunho'),
    ]

PIX_KEY_CHOICES = [
        ('PHONE','Telefone'),
        ('CPF', 'CPF'),
        ('CNPJ', 'CNPJ'),
        ('EMAIL', 'Email'),
        ('ALKEY', 'Chave Aleatória'),
    ]


class Receiver(models.Model):
    name = models.CharField('Nome', max_length=250)
    cpf_cnpj = models.CharField('CPF/CNPJ',max_length=14, validators=[only_int])
    status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES)
    email = models.EmailField('E-mail', default='')
    key_type = models.CharField('Tipo de Chave Pix', max_length=5, choices=PIX_KEY_CHOICES)
    key = models.CharField('Chave Pix', max_length=250)
    account = models.ManyToManyField(Account, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Recebedor'
        verbose_name_plural = 'Recebedores'
        ordering = ['-name']