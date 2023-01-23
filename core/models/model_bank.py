from django.db import models


class Bank(models.Model):
    bank_name = models.CharField('Nome do Banco', max_length=250)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return self.bank_name

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'
        ordering = ['-bank_name']


class Agency(models.Model):
    agency_number = models.IntegerField('Agência')
    from_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, verbose_name='Banco')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return f'Agência: {self.agency_number} Banco: {self.from_bank}'

    class Meta:
        verbose_name = 'Agência'
        verbose_name_plural = 'Agência'


ACCOUNT_TYPE_CHOICES = [
        ('C','Corrente'),
        ('P', 'Poupança'),
    ]


class Account(models.Model):
    account_number = models.IntegerField('Conta')
    account_type = models.CharField('Tipo de conta', max_length=1, choices=ACCOUNT_TYPE_CHOICES)
    from_agency = models.ForeignKey(Agency, on_delete=models.CASCADE, verbose_name='Agência')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)

    def __str__(self):
        return f'Conta: {self.account_number} {self.from_agency}'

    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'

