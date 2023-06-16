def apply_rot13(message):
    mapping = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                            'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm')
    return message.translate(mapping)


# pass the message. Same function can be called for both encryption and decryption
print(apply_rot13("Uryyb NOPnop"))
