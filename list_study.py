numbers1 = [2, 3, 4, 6, 7, 8, 9]
numbers1.insert(3, 5) # insert : 삽입 함수
numbers1.append(10) # append : 추가 함수
print(len(numbers1)) # len() : 갯수 확인 함수
print(numbers1)
del numbers1[4] # del : 삭제 함수
print(numbers1)

numbers2 = [5, 2, 4, 1, 9, 8, 10]
new_list = sorted(numbers2, reverse=True) # sorted : 정렬 함수 reverse : 반대 즉, reverse=True : 반대로 정렬하라
# sorted 함수는 기본 정수인 numbers2를 절대 건들지 않고 새로운 list를 만들어서 정렬할 뿐임. 그래서 print에 numbers2를 입력하면 numbers2가 그대로 나옴
print(new_list)

numbers2.sort() # sort는 numbers2 자체를 건드려서 정렬함. 그래서 print(numbers2.sort())를 하면 none 값이 나옴
print(numbers2)
numbers2.sort(reverse=True) # 반대로 정렬하고 싶으면 ()안에 reverse=True를 넣어주면 됨
print(numbers2)