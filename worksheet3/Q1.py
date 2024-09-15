def difference():
  n = int(input("enter the number:"))
  if n <= 17:
    return 17 - n
  else:
    return (17 - n) * 2
  
print(difference())


def test(n):
  if (100<=n<=1000) or n==2000:
    return True
  else:
    return False

n=int(input("enter the number:"))
print(test(n))


def reverse_string(s):
    return s[::-1]

s=input('enter the string:')
print(reverse_string(s))