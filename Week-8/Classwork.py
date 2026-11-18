l1 = [1,2,3,4,5]
sum = 0
for i in l1:
  print(i)
  
print(l1[0])
print(l1[-1])

for i in l1:
  sum += i
  
print(sum)
average = sum /len(l1)
print(average)

# l1.sort()
# largest_num = l1[-1]
largest_num = l1[0]
for i in l1:
 if(i > largest_num):
  largest_num = i

print(largest_num)


#8
L = list(range(1,10))
countEven = 0
countOdd = 0

check_num = lambda x : "Even" if x % 0 ==0 else "Odd"
for i in L:
  check_num(i)
  
list1 = [2,3,2,3,4,5,6,64,2,21,1]
list2 = []

for i in list1:
  if i not in list2:
    list2.append(i)

#9    
def addlists(x,y):
  z = x.extend(y)
  return z

def addlists2(x,y):
  x =  x + y

#10

unsorted_num = [-1,-4,1,545,3,-33]
l1 = []
l2 = []

sort_num = lambda x : l1.append(x) if x >= 0 else l2.append(x)
for i in unsorted_num:
  sort_num(i)
  
for i in unsorted_num:
  if(i >= 0):
    l1.append(i)
  else:
    l2.append(i)

#11
listOfWords = ["Hello", "sss", "fdfadsaf"]
sort_words = []

for i in listOfWords:
  if len(i) > 4:
    sort_words.append(i)
    
#12
squares = [x**2 for x in range(0,5)]

#13

tup = (1,2,3)
y = list(tup)
y.append(4)
tup = tuple(y)

#14
if(20 in tup):
  print("20 is in tuple")
#15
def checkTup(a,tup):
  if (a in tup):
    return True