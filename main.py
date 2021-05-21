from Encrypter import Encrypter
from Decrypter import Decrypter
from PIL import Image
import base64
from Crypto.Cipher import AES
import pickle

def encrypt_and_save(filename,key):
  with open("./"+filename+".jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())
    x = Encrypter(encoded_string, key)
    cipher = x.encrypt_image()
    with open("./encrypted-images/" + filename, "wb") as fstream:
      pickle.dump(cipher, fstream)

def load_and_decrypt(filename,key):
  with open("./encrypted-images/"+filename, "rb") as cipher_file:
    mydata = pickle.load(cipher_file)
    x = Decrypter(mydata)
    image = x.decrypt_image(key)
    with open("./encrypted-images/"+filename+".jpg", "wb") as image_file:
      image_file.write(image)



encrypt_and_save("00001", "myPassword")
load_and_decrypt("00001", "myPassword")