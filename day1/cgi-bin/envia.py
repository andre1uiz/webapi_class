#!/usr/local/bin/python
import cgi # Exemplo não irá funcionar pois biblioteca não existe mais na versão 3.13 :(

form = cgi.FieldStorage()
nome = form.getvalue("nome")
mensagem = form.getvalue("mensagem")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Enviado</title>")
print("<body>")
print("<h1>Enviado com sucesso!!</h1>")
print(f"<h2>{nome} - {mensagem}</h2>")
print("</body>")
print("</head>")
print("</html>")