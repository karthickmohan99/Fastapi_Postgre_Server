from passlib.context import CryptContext
myctx = CryptContext(
    schemes=["sha256_crypt", "des_crypt"]
)


def hash_password(password: str):
    return myctx.hash(password)

def verify_hash(password,hash_password):
    return myctx.verify(password,hash_password)