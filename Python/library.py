# 내장함수, itertools, heapq, bisect, collections

# 2. itertools
# 반복되는 데이터를 처리하는 기능을 가진 포함하고 있는 메소드
# 대표적으로 permutations, combinations가 있다.

# 2-1. permutations
# iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산한다.(순열)
# permuataions는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
from itertools import permutations
from unittest import result
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)

# 2-2 combinations
# iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산한다(조합)
# combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
from itertools import combinations
data = ['A', 'B', 'C']
result1 = list(combinations(data, 2))
print(result1)

# 2-3 product
# iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우를 계산한다(순열). 다만 원소를 중복하여 뽑는다.
# product 객체를 초기화 할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다.
# combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
from itertools import product
data = ['A', 'B', 'C']
result2 = list(product(data,repeat = 2))
print(result2)

# 2-4 combinations_with_replacement
# iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우를 계산한다(조합). 다만 원소를 중복하여 뽑는다.
# combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
from itertools import combinations_with_replacement
data = ['A', 'B', 'C']
result3 = list(product(data,repeat = 2))
print(result3)

# 3. heapq
# heapq는 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용한다.
# 파이썬은 최소힙으로 구성되어 있으므로 원소를 힙에 넣었다 빼는 것만으로도 시간복잡도 O(NlogN)에 오름차순 정렬이 완료된다.
# 힙에 원소를 삽입할 때는 heapq.heappush(), 원소를 꺼내고자 할 때는 heapq.heappop() 메서드를 이용한다.
import heapq
def heapsort(iterable):
    h = []
    result4 = []
    for value in iterable:          # 최대 힙을 구현할 때는 
        heapq.heappush(h, value)    # heapq.heappush(h, -value) 와 
    
    for i in range(len(h)):
        result4.append(heapq.heappop(h))    # esult4.append(-heapq.heappop(h)) 를 해주면 된다.
    return result4

result4 = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result4)

# 4. bisect
# 이진 탐색을 쉽게 구현할 수 있다 => 정렬된 배열에서 특정 원소를 찾아야 할 때 매우 효과적으로 사용된다.
# bisect 라이브러리는 bisect_left()와 bisect_right() 함수가 가장 중요하게 사용되며, 시간복잡도 O(logN)에 동작한다.
# bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
from bisect import bisect_left, bisect_right
a = [1,2,4,4,8]
x = 4
print(bisect_left(a, 4))
print(bisect_right(a, 4))
# 또한 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때 효과적이다.
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a1 = [1,2,3,3,3,3,4,4,8,9]
print(count_by_range(a1, 4, 4))
print(count_by_range(a1, -1, 3))


# 5. collections
# 유용한 자료구조를 제공하는 라이브러리. deque와 Counter가 대표적.
# 5-1 deque
# deque는 리스트와 달리 가장 앞쪽에 원소를 삽입하거나 삭제할 때 시간복잡도가 O(1)이다.
# 따라서 연속적으로 나열된 데이터의 시작부분이나 끝 부분에 데이터를 삽입하거나 삭제할 때 효과적으로 사용할 수 있다.
# 첫 번째 원소를 제거할 때 popleft()를 사용하며, 마지막 원소를 제거할 때 pop()을 사용한다.
# 첫 번째 인덱스에 원소 x를 삽입할 때 appendleft(), 마지막 인덱스에 원소 x를 삽입할 때 append()를 사용한다.
from collections import deque
data = deque([2,3,4])
data.append(5)
data.appendleft(1)
print(data)
print(list(data))

# 5-2 Counter
# Counter는 등장 횟수를 세는 기능을 제공한다. 
# 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번 등장했는지를 알려준다.
from collections import Counter
counter = Counter(['red', 'blue', 'green', 'red', 'blue', 'blue'])
print(counter['blue'])
print(counter['green'])
print(dict(counter))


#6. Math
# 팩토리얼, 제곱근, 최대공약수 등을 계산해주는 메소드를 제공
import math
print(math.factorial(5))
print(math.sqrt(5)) # 5의 제곱근을 반환
print(math.gcd(21, 14)) # 두 수의 최대공약수를 반환