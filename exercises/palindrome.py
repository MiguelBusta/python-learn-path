# Your last Plain Text code is saved below:



# // 1.
# // "Amor a Roma","La ruta natural","Anita lavo la tina","Somos o no somos","Se ven sus naves","Yo hago yoga hoy"

def palindrome(test):
  """
  Function that returns True or False if the word is a palindrome
  """
  phrase = test.replace(" ", "").lower()
  print(phrase)
  for i in range(int(len(phrase)/2)):
    if phrase[i] != phrase[-i -1]: 
      return False
  return True

# // 2.
# // 7,8,5,4,10,1,9  = > punto medio de los numeros es 4
# // 1,5,9,2,1,3     => 9 es el punto medio de los numeros

def middleval(values):
  """
  Function that returns the value that unites equal sums of elements in both sides
  """
  for i in range(1, int(len(values))):
    print(f"derecha: {sum(values[i+1:])}")
    print(f"izq: {sum(values[:i])}")
    if sum(values[i+1:]) != sum(values[:i]):
      continue
    elif sum(values[i+1:]) == sum(values[:i]):
      return values[i]


def main():
  """
  Solution to problem 1
  """
  #s = "Amor a Roma"
  values = ["Amor a Roma","La ruta natural","Anita lavo la tina","Somos o no somos","Se ven sus naves","Yo hago yoga hoy"]
  for j in values:
    if palindrome(j):
      print(f"The phrase: {j} is palindrome\n")
    else:
      print(f"The phrase: {j} is not a palindrome\n")
      
  """
  Solution to problem 2
  """
  values1 = [7,8,5,4,10,1,9]
  mid1 = middleval(values1)
  print(f"The middle value is: {mid1}")
  values2 = [1,5,9,2,1,3]
  mid2 = middleval(values2)
  print(f"The middle value is: {mid2}")
  

main()
