from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .database import engine
from .routers import post, user, auth, vote

############################################
print(database.SQLALCHEMY_DATABASE_URL)


#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
def root():
    return {"message": "Hello World (modified)!"}


"""
my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1},
            {"title": "favorite foods", "content": "I like pizza", "id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
"""

"""
#Path Operations 
@app.get("/")
#IT IS THE DECORATOR: IT CREATES THE ENDPOINT OF THE FUNCTION. It is called on the already created FastAPI INSTANCE (app)
#Within the brackets we have the PATH, the path that we must access from the URL 
#the get method: is one of the possible HTTP methods

def root():
    
    1): Async it is optional (so we can delete it)
    2): the name of the fun should be as much descriptive as possible
    3)RETURN:  is the message that is returned back to the user 
    
    return {"message": "Hello World"}
"""


















