# CIS446 - Toy WEP Algorithm

This program implements the Toy WEP (tWEP) algorithm for encrypting and decrypting plain text messages. 

First, the user is prompted to enter the shared key and initialization vector (IV) that they desire to use for encryption, along with the plaintext string they desire to encrypt.

The `generateKeyStream()` function then combines the shared key and IV into one array, generating the keystream to be used for encryption.

The `encrypt()` function translates the plaintext string into ASCII and performs an XOR operation on the translated ASCII text and generated keystream values from the function above.

The `decrypt()` function takes the output from the `encrypt()` function and performs an XOR operation on the ciphertext using the generated keystream values. 

The outputs of all three functions are ultimately output to the terminal for the user.