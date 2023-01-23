import re
from django.core.exceptions import ValidationError

def validate_pix_key(key_type, key):
    cpf = '^[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2}$'
    cnpj = '^[0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2}$'
    phone = '^((?:\+?55)?)([1-9][0-9])(9[0-9]{8})$'
    email = '^[A-Z0-9+_.-]+@[A-Z0-9.-]+$'
    aleatory_key = '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'

    if key_type == 'CPF':
        return re.search(cpf, key)
    elif key_type == 'CNPJ':
        return re.search(cnpj, key)
    elif key_type == 'PHONE':
        return re.search(phone, key)
    elif key_type == 'EMAIL':
        return re.search(email, key)
    elif key_type == 'ALKEY':
        return re.search(aleatory_key, key)

def only_int(value):
    if value.isdigit() == False:
        raise ValidationError('Apenas números')

