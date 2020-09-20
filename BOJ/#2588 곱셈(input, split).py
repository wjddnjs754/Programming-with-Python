#Date:2020/09/20
#BOJ 2588 "곱셈"

A = int(input())
B = input().split()
print(A*int(B[-1]))
print(A*int(B[-2]))
print(A*int(B[0]))



#예제 입력: 1 2
#입력이 띄어쓰기 되어있기 때문에 split 사용