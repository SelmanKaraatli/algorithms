import random
print("X     Y")
print("-------")
count = 0
sayac = 0
buyuk1 = 0
buyuk2 = 0



for i in range(10):
  for _ in range(100):
    x = random.randint(1,2)
    y = random.randint(1,2)
    #print(str(x) + "     " + str(y))
    if x == y:
      count += 1
    elif x != y:
      sayac += 1

  print("------")

  print("Number of x = y: " + str(count))
  print("Number of x != y: " +str(sayac))
  if count > sayac:
    buyuk1 += 1
  elif sayac > count:
    buyuk2 += 1



  print("\n\n\n")

  count = 0
  sayac = 0
print("Times that x = y > x != y: " + str(buyuk1))
print("Times that x = y < x != y: " + str(buyuk2))
buyuk1 = 0
buyuk2 = 0