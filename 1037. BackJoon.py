# 약수의 개수
count = int(input())

# N의 약수 목록
nums = list(map(int, input().split(' ')))

# input Data를 오름차순으로 정렬함
nums.sort()
'''
9의 약수 : [3]
10의 약수 : [5, 2]
16의 약수 : 3, [8, 4, 2]
18의 약수 : [9, 6, 3, 2]
20의 약수 : [10, 5, 4, 2]
22의 약수 : [11, 2]
24의 약수 : [12, 8, 6, 4, 3, 2]
...
64의 약수 : [32, 16, 8, 8, 4,2]
'''

# 맨 앞 원소와 맨 뒤 원소를 곱하면 N을 구할 수 있음
print(nums[0]*nums[-1])
