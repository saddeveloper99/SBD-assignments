text = "Hello, World!"
fruit_list = ["apple", "banana", "durian"]
fruit_dict = {"apple": 1, "banana": 2, "durian": 3}

# 문자열

# 1. count
count = text.count("l")
print(count)  # 3

# 2. find
position = text.find("World")
position2 = text.find("gasgaega")  # 없을 경우 -1 리턴
print(position)  # 7
print(position2)  # -1

# 3. index
try:
    position = text.index("World")
    print(position)  # 7
except ValueError: # index는 없을 경우 ValueError
    print("찾는 문자열이 없습니다.")

# 4. join
joined_list = " ".join(fruit_list)
print(joined_list) # apple banana durian

# 5. upper
uppercase_text = text.upper()
print(uppercase_text) # HELLO, WORLD!

# 6. lower
lowercase_text = text.lower()
print(lowercase_text) # hello, world!

# 7. replace
replaced_text = text.replace("World", "Python")
print(replaced_text) # Hello, Python!

# 8. split
splited_text = text.split(",") # 결과를 리스트 형태로 반환
print(splited_text) # ['Hello', ' World!']



# 리스트

# 1. len
print(len(fruit_list)) # 3

# 2. del
del fruit_list[2] 
print(fruit_list) # ['apple', 'banana']

# 3. append
fruit_list.append("melon")
print(fruit_list) # ['apple', 'banana', 'melon']

# 4. sort
fruit_list.sort()
print(fruit_list) # ['apple', 'banana', 'melon']

# 5. reverse
fruit_list.reverse()
print(fruit_list) # ['melon', 'banana', 'apple']

# 6. index
print(fruit_list.index("banana")) # 1

# 7. insert
fruit_list.insert(2, "durian")
print(fruit_list) # ['melon', 'banana', 'durian', 'apple']

# 8. pop
fruit_list.pop(3) # apple을 삭제하면서 반환
print(fruit_list) # ['melon', 'banana', 'durian']

# 9. count
print(fruit_list.count("durian")) # 1
list_num = [1, 1, 2, 3, 4, 5] 
print(list_num.count(1)) # 2

# 10. extend
fruit_list.extend(["apple", "grape", "mango"])
print(fruit_list) # ['melon', 'banana', 'durian', 'apple', 'grape', 'mango']

# 11. += 연산자
numbers = [1, 2, 3]
numbers.insert(3, 4) # 3번째 인덱스에 4를 추가
numbers += [7, 8, 9] # 7,8,9를 리스트에 추가
print(numbers) # [1, 2, 3, 4, 7, 8, 9]



# 딕셔너리

# 1. 딕셔너리에 데이터 쌍 추가
fruit_dict["grape"] = 4
print(fruit_dict) # {'apple': 1, 'banana': 2, 'durian': 3, 'grape': 4}

# 2. del
del fruit_dict["grape"]
print(fruit_dict) # {'apple': 1, 'banana': 2, 'durian': 3}

# 3. items
print(fruit_dict.items()) # dict_items([('apple', 1), ('banana', 2), ('durian', 3)])

# 4. get
friut = fruit_dict.get("apple")
friut2 = fruit_dict.get("efafegaeh")

print(friut) # 1
print(friut2) # None
try:
    friut3 = fruit_dict["efafegaeh"] # 해당 Key가 없으므로 KeyError
    print(friut3)
except KeyError:
    print("해당하는 key가 없습니다.")
# 5. in
if "apple" in fruit_dict: 
    print("애플이다") # "apple"이 fruit_dict의 key중에 있으므로 "애플이다" 반환
else:
    print("애플이 없다")

# 6. clear
fruit_dict.clear()
print(fruit_dict) # {}
