import rsa

#gerar as chaves
def generate_keys():
    (pubKey, privKey) = rsa.newkeys(1024)
    with open('pubkey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM'))

    with open('privkey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM'))

# carregar as chaves
def load_keys():
    with open('pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey

#código responsável pela criptografia
def encrypt(msg, key):
    return rsa.encrypt(msg.encode('ascii'), key)

#código responsável pela descriptografia
def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

generate_keys()
pubKey, privKey = load_keys()

message = 'testando o rsa'
ciphertext = encrypt(message, pubKey)


plaintext = decrypt(ciphertext, privKey)

print(f'Texto cifrado: {ciphertext}')

if plaintext:
    print(f'Mensagem: {plaintext}')
else:
    print('Não foi possível descriptografar a mensagem.')

