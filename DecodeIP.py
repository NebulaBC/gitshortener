import sys
import hasher

encodedString = input("Please input the encoded string: ").encode()
print("The following ip has been decoded as: " + hasher.decode(encodedString))
