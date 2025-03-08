def generateKeystream(iv, key, plaintextLength):
    combined = iv + key
    
    keystream = []
    
    for i in range(plaintextLength):
        keystream.append((combined[i] + combined[i + 1] + combined[i + 2]) % 256)
        
    return keystream

def encrypt(plaintext, keystream):
    asciiText = [ord(c) for c in plaintext]
    
    ciphertext = []
    
    for i in range(len(plaintext)):
        ciphertext.append(asciiText[i] ^ keystream[i])
        
    return ciphertext

def decrypt(ciphertext, keystream):
    decryptedText = []
    
    for i in range(len(ciphertext)):
        decryptedASCII = ciphertext[i] ^ keystream[i]
        decryptedText.append(chr(decryptedASCII))
        
    return ''.join(decryptedText)

print('\n' + '-' * 46)
print("| Welcome to the Toy WEP Encryption Program! |")
print('-' * 46)
print("\nPlease enter your shared key and initialization vector (IV) values as integers separated by commas.")
print("For example, shared key [1, 2, 3, 4] should be entered as 1, 2, 3, 4")
key = input("Enter your key: ")
iv = input("Enter your IV: ")

print("\nPlease enter the plaintext string you desire to be encrypted.")
text = input("Enter your plaintext: ")

key = list(map(int, key.split(",")))
iv = list(map(int, iv.split(',')))

keystream = generateKeystream(iv, key, 2)
ciphertext = encrypt(text, keystream)
decryptedText = decrypt(ciphertext, keystream)

print('\n' + ' Ecryption Output '.center(46, '-'))
print("Shared Key: ", key)
print("IV: ", iv)
print("Plaintext: ", text)

print("\nKeystream: ", keystream)
print("Ciphertext: ", ciphertext)
print("Decrypted Text: ", decryptedText)
print('-' * 46 + '\n')