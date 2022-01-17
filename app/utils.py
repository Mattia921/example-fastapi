from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #Hashing Algorithm

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):                 #comparison between the user's password and the stored hashed password
    return pwd_context.verify(plain_password, hashed_password)