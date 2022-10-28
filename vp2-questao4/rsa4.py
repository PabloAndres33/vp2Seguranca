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
    return rsa.sign(msg, key, 'SHA-1')

#código responsável pela validação da assinatura
def verify_sha1(msg, signature, key):
    try:
        return rsa.verify(msg, signature, key) == 'SHA-1'
    except:
        return False

generate_keys()
pubKey, privKey = load_keys()


privkeytext = input('Passar chave pública:')
if(privkeytext == "pubkey.pem"):
    messagetext = input('Passar arquivo assinado:')
    if(messagetext == 'mensagem_assinado'):
      signature = open(messagetext).read() 
      if verify_sha1(messagetext, signature, pubKey):
        print('Assinatura é válida!')
      else:
        print('Assinatura não é valida.')
    else:
        print('Houve algum erro no arquivo.')
else:
    print('Houve algum erro ao verificar arquivo contendo assinatura digital.')

