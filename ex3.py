ans = ['1. 35','2. 36','3. 40','4. 44']

print('If x =8 , then what is the value of 4(x+3)')
for k in range(4):
    print(ans[k])
while True:
    n = int(input("Nhập đáp án "))
    if n == 4:
        print("Bingo")
        break
    else:
        print("Nope")
        