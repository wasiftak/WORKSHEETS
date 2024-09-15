def prime(n):
    if n < 2:
        return False
    for i in range(2,int (n**0.5)+1):
      if n % i == 0:
        return False
    else:
     return True

for n in range(600,801):
  if prime(n):
    print(n)

#NUMBERS BETWEEN 100 AND 1000 DIV BY 7 & 9
def num(n):
    if n%7==0 and n%9==0:
        return True

for n in range(100,1001):
   if num(n):
     print(n)