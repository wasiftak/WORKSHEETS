L = [11, 12, 13, 14]
L.append(50)
L.append(60)
print(L)
L.remove(11)
L.remove(13)
print(L)

L.sort()
print(L)
L.reverse()
print(L)

index = L.index(12)
print(f"12 found at index {index}")

length=len(L)
print(length)

sum=0
for i in L:
  if(i%2==0):
   sum=sum+i
print(f"sum of even numbers is {sum}")

sum=0
for i in L:
  if(i%2!=0):
   sum=sum+i
print(f"sum of odd numbers is {sum}")

L.clear()
print(L)
del L

  
