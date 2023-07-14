#FCS Assignment 1, question 1
#Name: Shivam Agarwal
#Roll number: 2020123
from Crypto.Cipher import Salsa20
import gmpy2
import os
import random

def gcd(a,b):
    while True:
        if a == 0:
            return b
        else:
            b = b % a
            a,b = b,a


def multiplicative_inverse(e, phi):
    r1 = phi
    r2 = e
    t1 = 0
    t2 = 1

    while r2 > 0:
        quotient = r1 // r2
        remainder = r1 % r2
        r1 = r2
        r2 = remainder

        t = t1 - quotient * t2
        t1 = t2
        t2 = t

    if r1 == 1:
        return t1 % phi




def alice_generates_symmetric_key():
    '''
    A function that returns a 16 byte string to be used as the key for Salsa20.
    This key should be used to encrypt Bob and Alice's communications.
    But before that, it needs to be sent to Bob.

    Input: NA
    Return: the symmetric key (byte string)
    '''
    symmetric_key = os.urandom(16)
    return symmetric_key


def bob_generates_asymmetric_keys(p ,q):
    '''
    A function that takes in prime numbers p and q and generates
    the public and private keys for Bob as per RSA. Note that you are
    not allowed to use loops to find e or d.

    Input: p, q (upto 1023 digits long)
    Return: Bob's public key and private key ((e,n), (d,n)) as a tuple
    '''

    phi = (p-1)*(q-1)
    n = p*q

    e = 65537
    # print(gcd(e, phi))
    while gcd(e, phi) != 1:
        e = random.randint(2,phi-1)
    # print(e)
    d = multiplicative_inverse(e, phi)
    # print(d)
    return ((e, n), (d, n))

    pass

def alice_sends_symmetric_key(k, e, n):
    '''
    A function that Alice uses to encrypt the symmetric key
    using Bob's public key. The ciphertext is sent to Bob.

    Input: the symmetric key k, Bob's public key e, n.
    Return: encrypted ciphertext
    '''
    ciphertext = []
    # p = []
    for c in k:
        # p += [c]
        ciphertext += [pow(c, e, n)]
    # print(p)
    return ciphertext


    pass

def bob_decrypts_symmetric_key(c, d, n):
    '''
    A function that Bob uses to decrypt the ciphertext c using his private key.
    The decrypted message would give him the symmetric key.

    Input: the ciphertext c, Bob's private key d, n.
    Return: the symmetric key (byte string)
    '''
    # plaintext = []
    key = b''
    for i in c:
        k = pow(i, d, n)
        # plaintext += [k]
        key += k.to_bytes(1, byteorder='little')
    # print(plaintext)
    return key

    pass

def bob_sends_message(m, k):
    '''
    A function that takes a message m, shared key k and uses Salsa20 to encrypt m.

    Input: the message m (a byte string), the shared key k (byte string)
    Return: encrypted ciphertext
    '''

    cipher = Salsa20.new(key= k)
    ciphertext = cipher.nonce + cipher.encrypt(m)
    return ciphertext

    pass

def alice_decrypts_message(c_, k):
    '''
    A function that takes an encrypted message c_, shared key k and uses Salsa20 to decrypt c_.

    Input: the ciphertext c_, the shared key k (byte string)
    Return: plaintext message
    '''
    cipher = Salsa20.new(key=k, nonce=c_[:8])
    plaintext = cipher.decrypt(c_[8:])
    return plaintext
    pass
#
if __name__=="__main__":
    # p, q and the message m will be taken as inputs from the user.
    # print(alice_generates_symmetric_key())
    # print(bob_generates_asymmetric_keys(419,431))
    # c = alice_sends_symmetric_key(b'\xe6\x08<\xb8\xfb\xf1\xf7OD\xb9|=\xcc\x8e>\x19',65537,180589)
    # print(c)
    # print(bob_decrypts_symmetric_key(c,39973 ,180589 ))
    # print(bob_sends_message(b'2134234',b'4\xc3*\x1bg\x1a\x19l&\xba\x8ayha\xa0\xcf'))
    # print(alice_decrypts_message(b'\x12\n4T\xcb\xfaa\x1b\x9c\xed\xc2`Z\xd8\xc1', b'4\xc3*\x1bg\x1a\x19l&\xba\x8ayha\xa0\xcf'))
    pass

