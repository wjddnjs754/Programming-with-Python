#Date:2020/09/21
#BOJ 2753 "윤년"

A = int(input())
if (A%4==0 and A%100!=0) or A%400==0:
    print("1")
else:
    print("0")