#!/usr/local/bin/python
#Exemplo de criação de template html para adicionar dados variaveis
#carregar os dados
dados = [{"nome": "Bruno", "cidade": "Viana"},
        {"nome": "Guido", "cidade": "Amsterdan"}
]
#processar
template = """\
<html>
<body>
    <ul>
        <li>Nome: {dados[nome]}</li>
        <li>Cidade: {dados[cidade]}</li>
</body>
</html>
"""
#renderizar

for item in dados:
    print(template.format(dados = item))