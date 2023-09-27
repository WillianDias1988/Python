from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"produto": "Mouse", "qtd": 250, "qtdVendas": 10},
    2: {"produto": "Teclado", "qtd": 50, "qtdVendas": 5},
    3: {"produto": "Monitor", "qtd": 100, "qtdVendas": 8},
    4: {"produto": "MousePad", "qtd": 25, "qtdVendas": 2},
    5: {"produto": "Notebook", "qtd": 15, "qtdVendas": 1}
}


@app.get("/")
def home():
    return "Sejá bem vindo a minha primeira api"


@app.get("/Vendas")
def QtdVendas():
    return {"Qtdvendas": len(vendas)}


@app.get("/Vendas/{id_venda}")
def VendasID(id_venda: int):
    if (id_venda in vendas):
        return vendas[id_venda]
    else:
        return " "
