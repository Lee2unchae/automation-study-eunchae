# 과제 1. 문자열 처리 모듈

import string_utils

sample_text = "  Hi my name is Eunchae LEE  "
sample_email1 = "eunchae010naver.com"
sample_email2 = "eunchae010@naver.com"

# 공백 제거 및 소문자 변환
main1 = string_utils.change_text1(sample_text)
print("공백제거/소문자:", main1)

# 이메일 형태 확인
main2 = string_utils.check_email(sample_email1)
print("이메일 형태 확인:", main2)

# 이메일 마스킹
main3 = string_utils.email_masking(sample_email2)
print("이메일 마스킹:", main3)

# 단어 개수 계산
main4 = string_utils.count_text(sample_text)
print("단어 개수:", main4)

# 문자열 반전
main5 = string_utils.change_text2(sample_text)
print("문자열 반전:", main5)