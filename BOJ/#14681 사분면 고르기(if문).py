#Date:2020/09/21
#BOJ 14681 "사분면 고르기"

A = int(input())
B = int(input())
if A>0 and B>0:
    print("1")
elif A<0 and B>0:
    print("2")
elif A<0 and B<0:
    print("3")
else:
    print("4")