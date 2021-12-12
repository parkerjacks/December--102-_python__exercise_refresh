""" 

3. Caesar Cipher

Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? Learn about it here: http://practicalcryptography.com/ciphers/caesar-cipher/

Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq" """ 



plain = "abcdefghijklmnopqrstuvwxyz"
cipher = "bcdefghijklmnopqrstuvwxyza" 


word = input("Please type a word.  ")

caesar_cipher = ""

for x in word: 

    plain_letter = plain.index(x) 

    cipher_letter = cipher[plain_letter]

    caesar_cipher = caesar_cipher + cipher_letter

print(caesar_cipher)