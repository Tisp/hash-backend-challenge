# Hash Backend Challenge 

## Sobre
Este repositório contém uma resolução para o teste [Hash Backend Challenge](https://github.com/hashlab/hiring/tree/master/challenges/pt-br/new-backend-challenge).

## Depêndencias
 * python 3+
 * python-pip
 * Docker

## Instalação e Execução
1. Build imagens
```shell
docker compose build
```
2. Arquivo de configuração:
Dentro do arquivo `src/config.py` estão as configurações da aplicação, podendo ser setadas via variáveis de ambiente
```python
GRPC_SERVER = getenv("GRPC_CONNECT_URL", "hash-discount-service:50051")
BLACK_FRIDAY_DATE = getenv("BLACK_FRIDAY_DATE", "2021-11-27")
```
OBS: As variáveis já estão configuradas para seream executadas com `docker compose`

3.Executando a aplicação
```shell
 FLASK_ENV="<development>|<production>" docker compose up -d
```
OBS: Selecione a variável de ambiente para subir os containers, caso seja omitido será selecionado a variável `production`

4. Executando testes
```shell
docker compose run hash-checkout-service pytest --cov-config=.coveragerc --cov=.  ./tests/
```


### Testando a aplicação
Testando o endpoint `checkout`:

```shell
curl --location --request POST 'http://127.0.0.1:9091/checkout' \
--header 'Accept-Encoding: application/json' \
--header 'Content-Type: application/json' \
--data-raw '{
    "products": [
        {
            "id": 1,
            "quantity": 3
        }
    ]
}'
```
