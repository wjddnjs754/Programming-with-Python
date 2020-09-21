#Date:2020/09/21
#BOJ 2884 "알람 시계"

A = input().split()
H = int(A[0])
M = int(A[1])

if M<45:
    if H==0:
        print("23 ", M+15)
    else:
        print(H-1," ", M+15)
else:
    print(H, (M-45))