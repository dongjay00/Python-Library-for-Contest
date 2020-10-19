# 조합
from itertools import combinations

arr = ['A', 'B', 'C']

result = list(combinations(arr, 2)) # 2개를 뽑는 모든 조합 구하기
print(result)

# [('A', 'B'), ('A', 'C'), ('B', 'C')]