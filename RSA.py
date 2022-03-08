import sympy

def gcd(e,r):
  while(r != 0):
    e, r = r, e % r
  return e

# Encontrar o máximo divisor comum entre dois números inteiros diferentes de zero
def euclidGcd(e, r):
  for i in range(1, r):
    while(e != 0):
      b = r % e
      r = e
      e = b
  return e, r

# Cálculo de inverso modular
def extendedEuclidGcd(a, b):
  if(a % b == 0):
    return(b, 0, 1)
  else:
    gcd, s, t = extendedEuclidGcd(b, a % b)
    s = s - ((a // b) * t)
    return(gcd, t, s)

# Validação do cálculo de inverso modular
def modInverse(e, r):
  gcd, s, _ = extendedEuclidGcd(e, r)
  if(gcd != 1):
    return None
  else:
    return s % r

# Criptografa pelas chaves públicas E e N
def encrypt(pub_key,n_text):
  e, n = pub_key
  x = []
  m = 0
  for i in n_text:
    if(i.isupper()):
      m = ord(i) - 65
      c = (m ** e) % n
      x.append(c)
    elif(i.islower()):               
      m = ord(i) - 97
      c = (m ** e) % n
      x.append(c)
    elif(i.isspace()):
      x.append(400)
  return x

# Descriptografia pelas chaves privadas D e N
def decrypt(priv_key,c_text):
  d, n = priv_key
  txt = c_text
  x = ''
  m = 0
  for i in txt:
    if(i == '400'):
      x += ' '
    else:
      m = (int(i) ** d) % n
      m += 65
      c = chr(m)
      x += c
  return x

# Calcula a função totiente
def totient(p, q):
  return (p - 1) * (q - 1)

# Define P, Q e N, aleatoriamente, com valores entre 1 e 1000
def definirPQN():
  minPrime = 1
  maxPrime = 1000

  p = sympy.randprime(minPrime, maxPrime)
  q = sympy.randprime(minPrime, maxPrime)
  n = p * q

  while q == p:
    q = sympy.randprime(minPrime, maxPrime)
  
  return p, q, n

msg = "The information security is of significant importance to ensure the privacy of communications"

p, q, n = definirPQN()

totient = totient(p, q)

for i in range(1, 1000):
    if(gcd(i, totient) == 1):
        e = i

euclidGcd(e, totient)

d = modInverse(e, totient)

publicKey = (e, n)
privateKey = (d, n)

msgCifrada = encrypt(publicKey, msg)
msgDecifrada = decrypt(privateKey, msgCifrada)

print("------- Mensagem Cifrada: " + str(msgCifrada))
print("------- Mensagem Decifrada: " + msgDecifrada)
print("p: ", p)
print("q: ", q)
print("n: ", n)