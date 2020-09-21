#Date:2020/09/21
#BOJ 1330 "두 수 비교하기"

M = input().split()
A=int(M[0])
B=int(M[1])
if A>B:
    print(">")
elif A<B:
    print("<")
else:
    print("==")

#예제 입력: 1 2
#입력이 띄어쓰기 되어있기 때문에 split 사용