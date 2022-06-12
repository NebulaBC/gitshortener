import hmac
import hashlib
import base64

secret = "123"

message = "Hello"

def strEncode(string):
    encoded_string = string.encode()
    return bytearray(encoded_string)

digest = hmac.new(strEncode(secret), strEncode(message), digestmod=hashlib.sha256).digest()
signature = base64.b64encode(digest).decode()
print(signature)
