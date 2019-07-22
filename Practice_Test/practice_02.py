'''
Practice 2. 문자열 및 파일

1 .앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부른다.
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 이다.
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마인가?
'''

# Answer:
# palin = []
# for i in range(100, 1000):
#     for k in range(100, 1000):
#         check = str(i*k)
#         if check == check[::-1]:
#             palin.append(int(check))

# print(max(palin))


'''
2. 시저 암호는, 고대 로마의 황제 줄리어스 시저가 만들어 낸 암호인데,
예를 들어 알파벳 A를 입력했을 때, 그 알파벳의 n개 뒤에 오는 알파벳이 출력되는 것이다.
예를 들어 바꾸려는 단어가 'CAT"고, n을 5로 지정하였을 때 "HFY"가 되는 것이다.
어떠한 암호를 만들 문장과 n을 입력했을 때 암호를 만들어 출력하는 프로그램을 작성하시오.
- 입력 : 화면에서 문자열과 n값을 입력받는다. (예: ROSE 5)
- 출력 : 암호화된 문자열을 출력
'''

# Answer:
# s, n = str(input()), int(input())
# ls_s = list(s)

# new_string = ''
# for v in ls_s:
#     if ord(v)+n <= 90:
#         new_string += chr(ord(v)+n)
#     else:
#         new_string += chr(ord(v)+n-26) 

# print(new_string)


'''
3. Linux 명령어인 grep 을 윈도우스에서 만들어 보시오.
입력 형태
찾을 문자열: public
찾을 파일명: f:/Workspace/Egov/xxx.java

출력 형태
13: public class ClassA {
16:     public int number;
'''

# Answer:
# find_string, file_path = map(str, input().split())

# with open(file_path, 'r') as file:
#     for num, line in enumerate(file, start=1):
#         if find_string in line:
#             print(f'{num}: {line}')

'''
4. 텍스트를 파일에서 읽어 단어의 개수를 세는 프로그램 Word Count를 작성하시오.
입력은 텍스트 파일이고, 구분자는 마침표(‘.’), 쉽표(‘,’), 공백(‘ ‘)이다.
출력은 총 단어수와 가장 많이 나온 순서대로 단어 10개와 그 단어의 빈도이다.
'''

# Answer:
# txtfile = str(input())

# with open(txtfile, 'r') as file:
#     words = []
#     for line in file:
#         words.extend(line.split())
#     key = []
#     val = []
#     for word in words:
#         key.append(word)
#         val.append(words.count(word))
#     dic = dict(zip(key,val))
#     word_count = list(dic.items())
#     word_count = sorted(word_count, key=lambda x:x[1], reverse=True)
    
# print(f'총 단어수: {len(words)}')
# for i in range(10):
#     print(f'단어:{word_count[i][0]:>10s}, 빈도:{word_count[i][1]:<10d}')

'''
5. 다음의 지시대로 폴더와 파일을 프로그램에서 만드시오.
랜덤으로 1, 2, 3 중 하나를 내용으로 갖는 txt 파일100개를 
하나의 디렉토리(c:/Temp/Ex04) 안에 생성하는 코드를 작성하시오.
(파일 제목은 4자리 정수를 랜덤으로 할당. ex - 1382.txt , 0201.txt , 9012.txt , ......... )
제목이 0000~3333 인 txt 파일은 low 폴더로, 3334~6666인 txt 파일은 mid 폴더로, 
6667~9999 인 파일은 high 폴더로 이동시키는 코드를 작성하시오.
low, mid, high 폴더 안에 제목이 1, 2, 3 인 폴더를 각각 만들고, 
txt 파일 안의 내용에 따라 txt파일을 폴더안으로 이동시켜 분류하시오.
결론적으로 c:/Temp/Ex04 폴더 밑에는 low, mid, high 폴더 3개가 생기고, 
이 각각의 폴더에는 1, 2, 3 폴더가 각각 생기고 이 폴더밑에 파일이 들어 있어야 함.
'''

# Answer:
# import random

# for _ in range(100):
#     filenames = '{:0>4}.txt'.format(random.randint(0,9999))
#     file_number = int(filenames[:4])
    
#     if file_number <= 3333:
#         path = 'low/'    
#     elif file_number <= 6666:
#         path = 'mid/'
#     else:
#         path = 'high/'
        
#     rn = str(random.randint(1,3))
    
#     with open(path+rn+'/'+filenames, 'w') as file:
#         file.write(rn)

'''
6. Binary 파일을 16진수 값으로 출력하는 HexaDump 프로그램을 작성하시오.

입력 형태
찾을 파일명: C:/Temp/james.p

출력 형태
00000000:  00 01 44 E4 00 01 64 E4  41 42 43 11 00 61 F4 E4  ..D...d. ABC..a..
00000010:  41 42 63 13 00 62 F4 E5  00 01 46 E9 FF 01 65 E2  ABc..b.. ..F...e. 
00000020:
'''

# Answer:
import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathmatics': 85, 'science': 82}
 
with open('james.p', 'wb') as file:    # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

def group(a, *ns):
    for n in ns:
        a = [a[i:i+n] for i in range(0, len(a), n)]
    return a

def join(a, *cs):
    return [cs[0].join(join(t, *cs[1:])) for t in a] if cs else a

def hexdump(data):
    to_hex = lambda c: '{:02X}'.format(c)
    to_chr = lambda c: chr(c) if 32 <= c < 127 else '.'
    make = lambda f, *cs: join(group(list(map(f, data)), 8, 2), *cs)
    hs = make(to_hex, '  ', ' ')
    cs = make(to_chr, ' ', '')
    for i, (h, c) in enumerate(zip(hs, cs)):
        print ('{:010X}: {:48}  {:16}'.format(i * 16, h, c))

with open ('james.p','rb') as file:
    data=file.read()
    hexdump(data)