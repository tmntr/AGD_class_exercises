def cipher(plaintext,shift):
    ciphertext = ""
    if isinstance(shift,bool):
        raise TypeError("Shift cannot be a boolean value")
    for letter in plaintext:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            num = ord(letter)
            num += shift
            while num > ord("z"):
                num -= 26
            while num < ord("a"):
                num += 26
            ciphertext += chr(num)
        elif letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            num = ord(letter)
            num += shift
            while num > ord("Z"):
                num -= 26
            while num < ord("A"):
                num += 26
            ciphertext += chr(num)
        else:
            ciphertext += letter
    return ciphertext

#print(cipher('A',True))