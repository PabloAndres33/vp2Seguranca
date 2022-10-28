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

#código responsável pela assinatura 
def sign_sha1(msg, key):
    return rsa.sign(msg.encode('ascii'), key, 'SHA-1')


generate_keys()
pubKey, privKey = load_keys()


privkeytext = input('Passar chave privada:')
if(privkeytext == "privkey.pem"):
    messagetext = input('Passar arquivo:')
    if(messagetext == 'texto.txt'):
      signature = sign_sha1(messagetext, privKey)  
      print('Arquivo assinado com sucesso!')
      #Criar arquivo _assinado
      with open('mensagem_assinado', 'wb') as f:
        f.write(signature)
else:
    print('Houve algum erro ao gerar assinatura digital.')

