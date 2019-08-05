ans = ['1. 35','2. 36','3. 40','4. 44']
a = 0
print('If x =8 , then what is the value of 4(x+3)?')
for k in range(4):
    print(ans[k])
while True:
    n = int(input("Nhập đáp án "))
    if n == 4:
        print("Bingo")
        a +=1
        break
    else:
        print("Nope")
        break
ans2 = ['1.About 55','2.About 65','3.About 75','4.About 85']
print('Jack score these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?')
for v in range(4):
    print(ans2[v])
while True:
    m = int(input("Nhập đáp án "))
    if m == 2:
        print("Bingo")
        a +=1
        break
    else:
        print("Nope")
        break
print("You got", a ,"out of 2")