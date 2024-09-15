def outer():
  def inner():
    print("Hello, World!")
  inner()
  return 'inner loop accessed'

print(outer())


def student():
 a='wasif'
 b='vandan'
 c='vansh' 
 return a,b,c

print(student())