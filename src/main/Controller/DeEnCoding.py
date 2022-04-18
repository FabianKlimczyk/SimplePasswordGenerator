cipherAlphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.;-_!?$%&()+#"


def encode(pw: str, shift: int) -> str:
    # encodes a password with simple caesar cipher
    result = ""
    for c in pw:
        cindex = (cipherAlphabet.index(c) + shift) % len(cipherAlphabet)
        result += cipherAlphabet[cindex]
    return result


def decode(encodepw: str, shift: int) -> str:
    # decodes a password with simple caesar cipher
    result = ""
    for c in encodepw:
        cindex = (cipherAlphabet.index(c) - shift) % len(cipherAlphabet)
        result += cipherAlphabet[cindex]
    return result


