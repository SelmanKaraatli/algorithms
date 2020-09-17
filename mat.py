import random
print("X     Y")
print("-------")
count = 0
sayac = 0
for _ in range(10):
  x = random.randint(1,2)
  y = random.randint(1,2)
  print(str(x) + "     " + str(y))
  if x == y:
    count += 1
  elif x != y:
    sayac += 1

print("------")

print("Number of x = y: " + str(count))
print("Number of x != y: " +str(sayac))