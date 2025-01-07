#1 Conectar com o banco de dados
from sqlite3 import connect

conn = connect("blog.db")
cursor = conn.cursor()

#2 definir e criar a table
conn.execute(
    """\
    CREATE TABLE if not exists post(
        id integer PRIMARY KEY AUTOINCREMENT,
        title varchar UNIQUE NOT NULL,
        content varchar NOT NULL,
        author varchar NOT NULL
    );
    """
)

#3 Criar os posts iniciais para alimentar o banco
posts = [
    {
        "title": "Python é eleita a linguagem mais popular",
        "content": """A linguagem Python foi eleita a mais popular pela revista tech masters e segue dominando o mundo.""",
        "author": "Satoshi Namamoto",
    },
    {
        "title": "Como criar um blog usando Python",
        "content": """\
            Neste tutorial você aprenderá como criar um blog utilizando Python.
        <pre>import make a blog</pre>
        """,
        "author": "Guido Van Rossum",
    },
]

#4 Inserimos os posts caso o banco de dados esteja vazio
count = cursor.execute("SELECT * FROM post;").fetchall()
if not count:
    cursor.executemany(
        """\
        INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author);
        """,
        posts,
    )
    conn.commit()

#5 Verificamos que foi realmente inserido
posts = cursor.execute("SELECT * FROM post;").fetchall()
assert len(posts) >= 2
