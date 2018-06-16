dan = int(input("몇 단을 출력하시겠습니까? "))
while dan < 2 or dan >9:
    dan = int(input("몇 단을 출력하시겠습니까??? "))
for num in range(1,10):
    print("{} * {} = {}".format(dan,num,dan*num))
