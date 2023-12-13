'''
pip install pycryptodome
'''


import os

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA

# НЕ ЗАБУДЬТЕ ЗАКОММЕНТИРОВАТЬ ЭТОТ КОД ПРИ РАСШИФРОВКЕ, ЧТОБЫ НЕ СОЗДАВАЛИСЬ НОВЫЕ КЛЮЧИ
key = RSA.generate(2048)
privateKey = key.export_key()
publicKey = key.publickey().export_key()

# save private key to file
with open('private.pem', 'wb') as f:
    f.write(privateKey)

# save public key to file
with open('public.pem', 'wb') as f:
    f.write(publicKey)

print('Private key saved to private.pem')
print('Public key saved to public.pem')
print('Done')


def encrypt(dataFile='text.txt', publicKeyFile='public.pem'):
    '''
    use EAX mode to allow detection of unauthorized modifications
    '''
    # read data from file
    with open(dataFile, 'rb') as f:
        data = f.read()

    # convert data to bytes
    data = bytes(data)

    # read public key from file
    with open(publicKeyFile, 'rb') as f:
        publicKey = f.read()

    # create public key object
    key = RSA.import_key(publicKey)
    sessionKey = os.urandom(16)

    # encrypt the session key with the public key
    cipher = PKCS1_OAEP.new(key)
    encryptedSessionKey = cipher.encrypt(sessionKey)

    # encrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    []

    # save the encrypted data to file
    [fileName, fileExtension] = dataFile.split('.')
    encryptedFile = fileName + '_encrypted.' + fileExtension
    with open(encryptedFile, 'wb') as f:
        [f.write(x) for x in (encryptedSessionKey, cipher.nonce, tag, ciphertext)]
    print('Encrypted file saved to ' + encryptedFile)


def decrypt(encryptedFile='text_encrypted.txt', privateKeyFile='private.pem'):
    # read private key from file
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()

    # create private key object
    key = RSA.import_key(privateKey)

    # read the encrypted data from file
    with open(encryptedFile, 'rb') as f:
        encryptedSessionKey, nonce, tag, ciphertext = [f.read(x) for x in (key.size_in_bytes(), 16, 16, -1)]

    # decrypt the session key with the private key
    cipher = PKCS1_OAEP.new(key)
    sessionKey = cipher.decrypt(encryptedSessionKey)

    # decrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce=nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    # save the decrypted data to file
    [fileName, fileExtension] = encryptedFile.split('_encrypted.')
    decryptedFile = fileName + '_decrypted.' + fileExtension
    with open(decryptedFile, 'wb') as f:
        f.write(data)
    print('Decrypted file')


# encrypt()
# decrypt()