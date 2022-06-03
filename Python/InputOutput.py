import sys
# 데이터를 입력받을 때 input() 사용
# 여러개의 데이터를 입력받을 때 띄어쓰기로 구분해야하는 경우
list(map(int, input().split())) # => input()으로 입력받은 데이터를 split()을 이용해 공백으로 나눈 리스트로 바꾼 뒤 
# map을 이용하여 해당 리스트의 모든 원소에 int()함수를 적용한다. 최종적으로 그 결과를 list()로 다시 바꾼다.
# 반드시 외우자!

# 입력을 빠르게 받는 방법.
# sys 라이브러리에 정의되어 있는 sys.stdin.readline()함수를 이용.
sys.stdin.readline().rstrip() # readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로 입력되는데,
# 이 공백 문자를 지우려면 rstrip()함수를 사용해야 한다.

# 출력은 print() 사용.
# print()는 기본적으로 출력 후 줄 바꿈을 수행한다.