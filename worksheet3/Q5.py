def distinct(in_list):
  return list(set(in_list))

my_list=[2,3,5,2,3,4,5,6,7,8,9,10]
print(distinct(my_list))


def print_even(n):
  for i in n:
    if i%2==0:
      print(i)
n= [2,4,1,3,5,6,8,7]
print(print_even(n))