# abs : 입력받은 숫자의 절댓값을 반환하는 함수
abs(-3) # 3

# all : 반복가능한 자료형 x를 인수로 받아, x가 모두 참이면 True, 하나라도 거짓이 있으면 False를 돌려준다.
# any는 하나라도 참이 있으면 True, 모두 거짓일 때만 False
all([1,2,3]) # True
all([1,2,3,0]) # False => 0은 거짓이기 때문

# chr : 아스키코드 값을 입력받아 해당하는 문자를 출력
chr(97) # 'a'

# dir : 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
dir([1,2,3]) # append, count, extend, index, insert, pop ...
dir({1:'a'}) # clear, copy, get, has_key, items, keys ...

# enumerate : 순서가 있는 자료형을 입력받아 인덱스 값을 포함하는 enumrate 객체를 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval : 실행가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 돌려주는 함수
eval("'hi' + 'a'") # hia

# map : 함수와 반복가능한 자료형을 입력으로 받아 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려준다.
def two_times(x):
    return x*2
list(map(two_times, [1,2,3,4])) # => [2,4,6,8]
# lambda식 표현:
list(map(lambda a: a*2, [1,2,3,4]))

# max : 반복가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수
# min : 반복가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수
max([1,2,3]) # => 3
min([1,2,3]) # => 1

