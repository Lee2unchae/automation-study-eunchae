import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경변수 읽기
user_id = os.getenv("USER_ID")
user_pw = os.getenv("USER_PW")
base_url = os.getenv("BASE_URL")

# 필수 설정값 개별 검증
missing_keys = []
if not user_id:
    missing_keys.append("USER_ID")
if not user_pw:
    missing_keys.append("USER_PW")
if not base_url:
    missing_keys.append("BASE_URL")

# 검증 결과에 따른 처리
if missing_keys:
    missing_str = ", ".join(missing_keys)
    print(f"[오류] 필수 환경변수가 누락되었습니다: {missing_str}")
    print("      .env 파일을 확인하여 해당 항목을 설정해 주세요.")
else:
    # 비밀번호 마스킹 처리
    masked_pw = user_pw[:2] + "*" * (len(user_pw) - 2) if len(user_pw) > 2 else "****"

    print(f"로그인 ID: {user_id}")
    print(f"로그인 Password: {masked_pw}")
    print(f"기본 접속 URL: {base_url}")