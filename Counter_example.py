# 등장 횟수를 세는 기능 제공
# iterable한 객체가 주어질 때, 내부의 원소가 몇 번씩 등장했는지 알려줌
# 사전 자료형으로 반환
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 3
print(counter['green']) # 1
print(dict(counter)) # {'red': 2, 'blue': 3, 'green': 1}