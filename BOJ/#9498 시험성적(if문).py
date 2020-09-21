#Date:2020/09/21
#BOJ 9498 "시험 성적"

A = int(input())
if 100>=A>=90:
    print('A')
elif 90>A>=80:
    print('B')
elif 80>A>=70:
    print('C')
elif 70>A>=60:
    print('D')
else:
    print('F')   

#예제 입력: 1 2
#입력이 띄어쓰기 되어있기 때문에 split 사용