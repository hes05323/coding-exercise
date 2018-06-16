# 함수 functions
# 입력값 parameters, 반환값 return

def hello_friends(name):
    print("hello, {}".format(name))
    # 여기 hello 를 hi 로 한번만 변경해주면 아래 출력 값 전부 바꿀수 있다(함수의 힘)

name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"
name5 = "marco"
name6 = "jane"
name7 = "john"
name8 = "tom"

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)
# print("hello, {}".format(name1))
# print("hello, {}".format(name2))
# print("hello, {}".format(name3))
# print("hello, {}".format(name4))
# print("hello, {}".format(name5))
# print("hello, {}".format(name6))
# print("hello, {}".format(name7))
# print("hello, {}".format(name8))

# 1) 입력값 O, 반환값 O
def sum(a, b):
    return a + b

# 2) 입력값 O, 반환값 X
def hello_friends(name):
    print("hello, {}".format(name))

# num_0 = hello_friends(name)
# print(num_0) 반환값(return)이 없으니 변수에 담기지 않음. 에러남

# 3) 입력값 X, 반환값 O
def return_1():
    return "잘되지?"  # return을 한다는 것은 변수로 담을 수 있음, return 값이 없으면 변수로 담지 못함

num_1 = return_1()
print(num_1)

# 4) 입력값 X, 반환값 X
def hello_world():
    print("hello world")
