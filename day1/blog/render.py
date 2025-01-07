from database import conn
from pathlib import Path
# 1 obter os dados
cursor = conn.cursor()
fields = ("id", "title", "content", "author")
results = cursor.execute(
    """\
        SELECT * FROM post;
"""
)

#Duas maneiras de apresentar os resultados
#usando list comprehension
posts = [dict(zip(fields,post)) for post in results]
#print(posts)
#usando laço for
# for result in results:
#     print(dict(zip(fields,result)))

# 2 criar a pasta de destino do site
site_dir = Path("site")
site_dir.mkdir(exist_ok=True)

# 3 criar uma função para gerar URL com slug
def get_post_url(post):
    slug = post["title"].lower().replace(" ", "-")
    return f'{slug}.html'

# 4 Renderizar a página index.html
index_template = Path("list.template.html").read_text()
index_page = site_dir / Path("index.html")
post_list = [
    f"<li> <a href= '{get_post_url(post)}'> {post['title']} </a> </li>"
    for post in posts
]

index_page.write_text(
    index_template.format(post_list= "\n".join(post_list))
)

# 5 Renderizar as páginas do blog
for post in posts:
    post_template = Path("post.template.html").read_text()
    post_page = site_dir / Path(get_post_url(post))
    post_page.write_text(post_template.format(post=post))

print("site generated")
conn.close()