#while loops
n = 5

while n > 0 :
    print(n)
    n = n-1;
print("end")

m = 5
while True:
    if m == 0:
        break;
    print (m)
    m = m - 1;
print("Begin")

#for loops
for i in [5,4,3]:
    print("for",i)
    print(type(i));

friends = ["CC","VK"]
for x in friends :
    print ("Happy new year", x)

#print square
for i in range(1,4):
    for j in range(1,4):
        print("x", end="")
    print();

#using loop to check the largest number
temp = -1
for i in [3,4,8,12,3,1,0,91,90,100]:
    if temp < i:
        print ("largest number updated to ", i, "before number = ",temp);
        temp = i
print("Max Number for temp = ",temp)
