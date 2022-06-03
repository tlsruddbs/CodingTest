
dic = {'name':'신경윤', '소속':'의료IT공학과', '나이':'25'}
dic['born'] = '청주'
print(dic)
# print(dic.index('나이'))

for k in dic.keys():
    print(k)
    
dic.values() # 값 객체를 얻는다
vallist = list[dic.values()] # 값 객체를 리스트로 변환

dic.items() # 키 값 쌍 객체를 얻는다