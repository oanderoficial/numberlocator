#!/usr/bin/env python 
#codificação: utf-8 

import phonenumbers 

#import geocoder 

from phonenumbers import geocoder, carrier 

# especifique o número de telefone 

a =input("Digite o número de telefone:")

# região 

phonenumber = phonenumbers.parse(a)

# capturando a operadora 

operadora = carrier.name_for_number(phonenumber, 'pt-br')

#exibir a localização do número de telefone

regiao = geocoder.description_for_number(phonenumber, 'pt-br')

print("O estado é: " +regiao)
print("a Operadora é:" + operadora)