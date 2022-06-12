import hashlib
import base64
import config
from cryptography.fernet import Fernet


def encode(message):
    key = config.secret.encode()
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()


def decode(message):
    key = config.secret.encode()
    f = Fernet(key)
    return f.decrypt(message).decode()
