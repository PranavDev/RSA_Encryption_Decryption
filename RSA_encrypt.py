import random
import math

def get_prime():
  flag = 0
  while(flag!=1):
    count = 0
    num = random.randint(1,50)
    for i in range(1,num+1):
      if(num%i==0):
        count+=1
    if(count==2):
      flag = 1
  return num


def prime(n):
  count = 0
  for i in range(1,n+1):
    if(n%i==0):
      count+=1
  if(count==2):
    return True
  else:
    return False


def coprime(totient):
  flag = 0
  num = 1
  while(flag!=1):
    num+=1
    if(totient%num!=0 and prime(num)):
      flag = 1
  return num


def get_d(e, totient):
  val = 0
  for i in range(0,10000):
    val = (i*e)%totient
    if(val==1):
      break;
  return i
    

def encrypt_msg(msg, e, n):
  E_msg = int(math.pow(int(msg),int(e))%n)
  return E_msg
  

def decrypt_msg(enc_msg, d, n):
  D_msg = int(math.pow(int(enc_msg),int(d))%n)
  return D_msg


#main_function
msg = input("Enter Number : ")
print("MSG : ",msg)
p = get_prime()
q = get_prime()
print(p," ",q)

n  = p*q
totient = (p-1)*(q-1)
print("totient = ",totient)
e = coprime(totient)
print("e = ",e)

d = get_d(e,totient)
print("d = ",d)

enc_msg = encrypt_msg(msg, e, n);
print("Encrypted Msg : ",enc_msg)

recov_msg = decrypt_msg(enc_msg, d, n)
print("Decrypted Msg : ",recov_msg)

