from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode
import secrets

def generate_salt():
    return secrets.token_urlsafe(16)

def derive_key(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=salt.encode(),
        length=32,
        iterations=100000,
        backend=default_backend()
    )
    return urlsafe_b64encode(kdf.derive(password.encode()))

def hash_password(password):
    salt = generate_salt()
    key = derive_key(password, salt)
    return {'slt': salt, 'hsg-pswm': key}

def compare_passwords(stored_password, input_password):
    salt        = stored_password['slt']
    stored_key  = stored_password['hsg-pswm']
    input_key   = derive_key(input_password, salt)

    return stored_key == input_key
