# 순열
from itertools import permutations

arr = ['A', 'B', 'C']

result = list(permutations(arr, 3)) # 3개를 뽑는 모든 순열 구하기
print(result)

# [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]  