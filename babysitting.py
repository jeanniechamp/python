
babysitter = ["vaanya", "stephanie", "adellia", "charlie", "maeille"]
total = 0
for x in babysitter:
  income = input("how much money did," + x + " make? ")
  y= int(income) / int(4)
  print (y)
  total1p= int(y) / int(5)
  print (total1p)
  total = int(total) + int(total1p) 
print (total)