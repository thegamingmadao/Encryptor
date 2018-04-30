from django.shortcuts import render
from . import aes_encryptor

# Create your views here.
def index(request):
	password = request.GET.get("pass")
	message = request.GET.get("message")
	if password and message:
		encrypted = aes_encryptor.encrypt(message, password)
		return render(request, 'encryptor/index.html', {
			'password': password,
			'message': message,
			'encrypted': encrypted
		})
	return render(request, 'encryptor/index.html', {
		'test': 'test'
	})

def decrypt(request):
	password = request.GET.get("pass")
	message = request.GET.get("message")
	if password and message:
		decrypted = aes_encryptor.decrypt(message, password)
		return render(request, 'encryptor/decrypt.html', {
			'password': password,
			'message': message,
			'decrypted': decrypted
		})
	return render(request, 'encryptor/decrypt.html', {
		'test': 'test'
	})