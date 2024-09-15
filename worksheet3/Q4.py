def count(s):
  upper=0
  for i in s:
    if i.isupper():
      upper+=1
  lower=0
  for i in s:
    if i.islower():
      lower+=1
  print(f"No. of Upper case characters :{upper}")
  print(f"No. of Lower case Characters :{lower}")

count(input("enter the string:"))