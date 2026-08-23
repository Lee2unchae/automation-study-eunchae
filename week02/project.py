# 과제 2. 함수 활용 미니 프로젝트

# Project 1. 구구단 출력
# 숫자 입력받기
text1 = int(input("숫자 입력받아 구구단 출력: "))

# 구구단 출력하기
def gugudan(text1):
    for i in range(1, 10):
        print(text1, "x", i, "=", text1 * i)

gugudan(text1)

#------------------------------------------------------------------------------------------------
# Project 2. 회문 판별
def project2(text):
    # 문자열과 뒤집은 문자열이 같은지 비교하기
    if text == text[::-1]:
        return True
    else:
        return False

# 단어 입력받기
word = input("단어 입력: ")

# 결과 출력
if project2(word):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")

#------------------------------------------------------------------------------------------------
# Project 3. 단어 빈도 계산
def project3(text):
    words = text.split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
            
    return word_count

# 문장 입력받기
sentence = input("문장을 입력하세요: ")
result = project3(sentence)

# 결과 출력하기
for word, count in result.items(): #입력받은 문장에서 단어, 갯수 출력하기
    print(word, ":", count, "회")

#------------------------------------------------------------------------------------------------
# Project 4. 비밀번호 검증
def project4(password):
    # 1. 최소 길이 충족 (8자 이상 기준)
    password_length = len(password) >= 8
    
    # 2. 영문 및 숫자 포함 검사
    password_english = False
    password_number = False
    
    for char in password:
        if char.isalpha():
            password_english = True
        if char.isdigit():
            password_number = True
            
    # 3. 3가지 조건이 모두 참(True)이어야 사용 가능
    if password_length and password_english and password_number:
        return True
    else:
        return False

# 사용자 입력받기 및 실행
password = input("비밀번호 입력: ")

if project4(password):
    print("사용 가능한 비밀번호입니다.")
else:
    print("사용 가능하지 않은 비밀번호입니다.")

#------------------------------------------------------------------------------------------------
# Project 5. 이름 목록 정리
# 1. 과제 1의 문자열 처리 모듈 불러오기
import string_utils

def project5(name_list):
    names = []
    
    for name in name_list:
        # 과제 1 모듈 기능 사용
        change_name = string_utils.change_text1(name)
        names.append(change_name)
    
    # 정렬하기
    names.sort()
    return names

# 테스트용 불규칙한 이름 데이터
test_names = ["  eunChae ", " LEE", "  kim ", "choi", "GILDONG"]

# 실행하기
result = project5(test_names)
print(result)

#------------------------------------------------------------------------------------------------
# Project 6. 간단한 메뉴 프로그램
def project6():
    data_list = []  # 데이터를 저장할 리스트
    
    while True:
        print("1. 데이터 추가")
        print("2. 데이터 조회")
        print("3. 프로그램 종료")
        
        choice = input("원하는 동작을 입력하세요: ")
        
        if choice == "데이터 추가":
            item = input("추가할 데이터를 입력하세요: ")
            data_list.append(item)
            
        elif choice == "데이터 조회":
            if not data_list:
                print("저장된 데이터가 없습니다.")
            else:
                print("데이터 조회")
                for index, item in enumerate(data_list, 1):
                    print(item)
                    
        elif choice == "프로그램 종료":
            print("프로그램을 종료합니다.")
            break  # 반복문 종료
            
        else:
            print("잘못된 입력입니다.")

# 프로그램 실행하기
project6()