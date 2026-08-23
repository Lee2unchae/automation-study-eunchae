# 과제 1. 문자열 처리 모듈

# 문자열 앞뒤 공백 제거 및 소문자 변환
def change_text1(text):
    result = text.strip().lower()  # strip: 공백 제거 / lower: 소문자 변환
    return result

# 이메일 형태 확인
def check_email(email):
    result = "@" in email  # 문장 안에 @가 있는지 확인
    return result

# 이메일 일부 마스킹
def email_masking(email):
    parts = email.split("@") # 이메일을 @을 기준으로 분리
    id = parts[0] # 앞쪽은 id
    domain = parts[1] # 뒤쪽은 도메인

    # 분리한 이메일 중에 id 일부 마스킹 하기
    result = id[:2] + "*****@" + domain
    return result

# 문장의 단어 개수 계산
def count_text(text):
    result = text.split() # split : 공백을 기준으로 단어 분리
    return len(result) # 분리된 단어 갯수

# 문자열을 반대로 변환
def change_text2(text):
    result = text[::-1] #문자를 반대로 변환
    return result