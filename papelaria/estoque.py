import csv
import os

ARQUIVO = "dados/produtos.csv"
CAMPOS = ["codigo", "nome", "preco", "quantidade"]

def eh_numero(texto):
    """Diz se o texto é um número positivo, aceitando vírgula ou ponto (ex.: 3,50)."""
    texto = texto.strip().replace(",", ".", 1)
    return texto.replace(".", "", 1).isdigit()

def validar_produto(nome, preco, quantidade):

"""Devolve a lista de erros encontrados. Lista vazia = produto válido."""
erros = []
if nome.strip() == "":
   erros.append("O nome não pode ficar vazio.")
if not eh_numero (preco) or float(preco.replace(",", ".", 1)) <= 0:
   erros.append("O preço precisa ser um número maior que zero.")
if not quantidade.strip().isdigit():
   erros.append("A quantidade precisa ser um número inteiro (0 ou mais).")
return erros
