# numberlocator

Este código Python solicita que o usuário insira um número de telefone e, em seguida, usa a biblioteca phonenumbers para identificar a operadora e a região do número de telefone inserido.

O código começa importando a biblioteca phonenumbers e duas funções dela: geocoder e carrier. Em seguida, solicita que o usuário insira um número de telefone.

O código usa a função parse da biblioteca phonenumbers para analisar o número de telefone inserido e extrair sua região. A função name_for_number é usada para identificar a operadora do número de telefone, especificando o idioma como "pt-br" para obter o nome da operadora em português. A função description_for_number é usada para extrair a descrição da localização do número de telefone, especificando o idioma como "pt-br" para obter a descrição em português.

Por fim, o código exibe a região e a operadora do número de telefone inserido usando as informações obtidas pelas funções name_for_number e description_for_number.
