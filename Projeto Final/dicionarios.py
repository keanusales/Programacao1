# Dicionarios
reg = {1: "Acre", 2: "Alagoas", 3: "Amapá", 4: "Amazonas", 5: "Bahia", 6: "Ceará",
  7: "Distrito Federal", 8: "Espírito Santo", 9: "Goiás", 10: "Maranhão", 11: "Mato Grosso",
  12: "Mato Grosso do Sul", 13: "Minas Gerais", 14: "Paraná", 15: "Paraíba", 16: "Pará",
  17: "Pernambuco", 18: "Piauí", 19: "Rio Grande do Norte", 20: "Rio Grande do Sul", 21: "Rio de Janeiro",
  22: "Rondônia", 23: "Roraima", 24: "Santa Catarina", 25: "Sergipe", 26: "São Paulo", 27: "Tocantins"}

forn = {1: "AliExpress", 2: "Amazon", 3: "Alibaba", 4: "Mercado Livre", 5: "Yakao", 6: "Megafort", 7: "iOffer"}

dados = {'cod': "", 'prod': "", 'preco': "", 'qtd_adquirida': "", 'regiao': "",
  'qualidade': "", 'fabricante': "", 'fornecedor': "", 'lote': "",'valid': "", 'qtd_vendas': ""}

quali = {1: "Péssima qualidade", 2: "Baixa qualidade", 3: "Média qualidade",
  4: "Boa qualidade", 5: "Ótima qualidade"}

types = {
  1: "update produtos set prod = ? where cod = ?",
  2: "update produtos set preco = ? where cod = ?",
  3: "update produtos set qtd_adquirida = ? where cod = ?",
  4: "update produtos set regiao = ? where cod = ?",
  5: "update produtos set qualidade = ? where cod = ?",
  6: "update produtos set fabricante = ? where cod = ?",
  7: "update produtos set fornecedor = ? where cod = ?",
  8: "update produtos set lote = ? where cod = ?",
  9: "update produtos set validade = ? where cod = ?",
  10: "update produtos set qtd_vendida = ? where cod = ?"
}