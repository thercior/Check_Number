import phonenumbers
from phonenumbers import carrier, geocoder
import tkinter

#Captura o número do celular
cel=input("Digite o número do seu celular abaixo (Padrão Brasil: +55XX9XXXXXXXX)\n")
celular = phonenumbers.parse(cel)

#Verifica se o número é Valido
celular_validate = phonenumbers.is_valid_number(celular)
if celular_validate:
    numero = f"Este número '{cel}' é valido e existe!"
else:
    numero = f"Este número '{cel} não existe"
    
#Verifica a operadora do celular
operadora = carrier.name_for_number(celular,lang='pt-br')

#Verifica o estado a que aquele número pertence
state_number = geocoder.description_for_number(celular,lang='pt-br')

print(f'O número de celular é \n {cel}')
print(numero)
print(f'A Operadora do celular {cel} é a {operadora}')
print(f'Este número é do estado {state_number}')