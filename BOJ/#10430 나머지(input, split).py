#Date:2020/09/20
#BOJ 10430 "나머지"

M = input().split()
A=int(M[0])
B=int(M[1])
C=int(M[-1])
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)

#예제 입력: 1 2
#입력이 띄어쓰기 되어있기 때문에 split 사용