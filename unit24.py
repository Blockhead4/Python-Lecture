'''
Unit 24 심사문제 1: 특정 단어 개수 세기
표준 입력으로 문자열이 입력됩니다. 
입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요
(input에서 안내 문자열은 출력하지 않아야 합니다). 
단, 모든 문자가 소문자인 'the'만 찾으면 되며 'them', 'there', 'their' 등은 포함하지 않아야 합니다.
'''

# Answer:
import string
paragraph = str(input())
ls = paragraph.split()

words = []
for s in ls:
    words.append(s.strip(string.punctuation))

print(words.count('the'))


'''
Unit 24 심사문제 2: 특정 단어 개수 세기
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 
각 가격은 ;(세미콜론)으로 구분되어 있습니다. 
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요
(input에서 안내 문자열은 출력하지 않아야 합니다). 
이때 가격은 길이를 9로 만든 뒤 오른쪽으로 정렬하고 천단위로 ,(콤마)를 넣으세요.
'''

# Answer:
prices = str(input())
ls = list(map(int, prices.split(';')))
ls.sort()

for v in ls[::-1]:
    print('{:>9,}'.format(v))