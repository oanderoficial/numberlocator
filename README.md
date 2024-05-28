# numberlocator

Usando Python para descobrir operadora e região de um número de telefone.

<strong> Biblioteca: </strong>
```
pip install phonenumbers
```

<strong> 📦 Download: </strong> https://pypi.org/project/phonenumbers/

```python
import phonenumbers
```

<strong> # import geocoder, carrier </strong> 
```python
from phonenumbers import geocoder, carrier
```

<strong> Especifique o número de telefone  </strong>

```python
a =input("Digite o número de telefone:")
```
<strong> Região </strong>
```python
phonenumber = phonenumbers.parse(a)
```

<strong> Capturando a operadora  </strong> 
```python
operadora = carrier.name_for_number(phonenumber, 'pt-br')
```
<strong> Exibir a localização do número de telefone </strong>
```python
regiao = geocoder.description_for_number(phonenumber, 'pt-br')

print("O estado é: " +regiao)
print("a Operadora é:" + operadora)
```
