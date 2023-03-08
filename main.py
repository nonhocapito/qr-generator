import qrcode
import random

def gen_random_string():
	random_string=str(random.randint(1000,9999))
	return random_string

def qr_generator(stringa):
	img=qrcode.make(stringa)
	img.save("qr-"+gen_random_string())
	
cond=True

while cond==True:
	input_str=input("Inserire testo/URL: ")
	qr_generator(input_str)
	print("QR generato.\n")
	print(80*"-")
	
