# RSA_Encryption_Decryption
Python RSA Algorithm

# What is an RSA algo?

1. It stands for (Rivest–Shamir–Adleman).
2. It is an asymmetric encryption algorithm which means that there are two keys : Public and Private.
3. Public is accessible by all, but the private key is only known by the two communicating parties.

STEPS:
a. Select two prime numbers - p and q
b. Compute their product => ( n * q ) -------------------> Becomes the Public Key
c. Totient => phi( n ) = ( p - 1 ) * ( q - 1 )
d. Choose an e > 1  and co-prime to phi( n )
e. Find d such that: [ (d * e) % totient ] = 1
f. Encrypted Msg => c = (m ^ e) % n   [where m is the message entered by user for encryption]
g. Decrypted Msg => m = (c ^ d) % n

Note that the message input from the user should be same to the decrypted message.
Otherwise no use :LOL
