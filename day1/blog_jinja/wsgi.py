# # import cgi #não irá funcionar a partir daqui devido a versão do python
# from database import conn
# from jinja2 import Environment, FileSystemLoader
# import json

# env = Environment(loader=FileSystemLoader("templates"))

# def get_posts_from_database(post_id=None):
#     cursor = conn.cursor()
#     fields = ("id", "title", "content", "author")

#     if post_id:
#         results = cursor.execute("SELECT * FROM post WHERE id = ?;", post_id)
#     else:
#         results = cursor.execute("SELECT * FROM post;")
#     return [dict(zip(fields, post)) for post in results]



# def add_new_post(post):
#     cursor = conn.cursor()
#     cursor.execute(
#         """INSERT INTO post (title, content, author)
#         VALUES (:title, :content, :author)""", post
#     )
#     conn.commit()

# def application(environ, start_response):
#     body = b"Content not found"
#     status = "404 Not Found"

#     # Processar o request
#     path = environ["PATH_INFO"]
#     method = environ["REQUEST_METHOD"]

#     if path == "/" and method == "GET":
#         posts = get_posts_from_database()
#         body = render_template(
#             "list.template.html", 
#             post_list=posts
#         )
#         status = "200 OK"

#     elif path == "/api" and method == "GET":
#         posts = get_posts_from_database()
#         body = json.dumps(posts).encode("utf-8")
#         status = "200 OK"        
        

#     elif path.split("/")[-1].isdigit() and method == "GET":
#         post_id = path.split("/")[-1]
#         body = render_template(
#             "post.template.html",
#             post = get_posts_from_database(post_id=post_id)[0]
#         )
#         status = "200 OK"

#     elif path == "/new" and method == "GET":
#         body = render_template("form.template.html")
#         status = "200 OK"
    
#     elif path == "/new" and method == "POST":
#         # O exemplo não funciona por estar no python 3.13
#         # biblioteca cgi foi removida
#         # form = cgi.FieldStorage(
#         #     fp=environ["wsgi.input"],
#         #     environ=environ,
#         #     keep_blank_values=1
#         # )
#         # post = {"title":..., "content": ..., "author": ...,}
#         post = {item.name: item.value for item in form.list}
#         add_new_post(post)
#         body = b"New post created with sucess!!!"
#         status = "201 Created"

#     # Criar o response

#     headers = [("Content-type", "text/html")]
#     start_response(status, headers)
#     return [body]

##################################
from database import conn
from dog import Dog

app = Dog()

@app.route("^/$", template="list.template.html")
def post_list():
    posts = get_posts_from_database()
    return {"post_list" : posts}

@app.route("^/api$", template="list.template.html")
def post_list_api():
    posts = get_posts_from_database()
    return {"post_list" : posts}, "200 OK", "application/json"

@app.route(r"^/(?P<id>\d{1,})$", template="post.template.html")
def post_detail(id):
    post = get_posts_from_database(post_id=id)[0]
    return {"post": post}

@app.route("^/new$", template="form.template.html")
def new_post_form():
    return {}

@app.route("^/new$", method="POST")
def new_post_add(form):
    post = {item.name: item.value for item in form.list}
    add_new_post(post)
    return "New post created successfully! ;)", "201 Created", "text/plain"

#Controllers
def get_posts_from_database(post_id=None):
    cursor = conn.cursor()
    fields = ("id", "title", "content", "author")

    if post_id:
        results = cursor.execute("SELECT * FROM post WHERE id = ?;", post_id)
    else:
        results = cursor.execute("SELECT * FROM post;")
    return [dict(zip(fields, post)) for post in results]

def add_new_post(post):
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO post (title, content, author)
        VALUES (:title, :content, :author)""", post
    )
    conn.commit()

if __name__ == "__main__":
    app.run()