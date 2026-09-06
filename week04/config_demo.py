import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

# 환경변수 읽기
user_id = os.getenv("USER_ID")
user_pw = os.getenv("USER_PW")
base_url = os.getenv("BASE_URL")

# 프로그램 실행에 반드시 필요한 설정값이 없는 경우 사용자가 원인을 알 수 있도록 처리
if not user_id or not user_pw or not base_url:
    print("필요한 설정값이 없습니다.")
else:
    # 비밀번호 마스킹 처리
    masked_pw = user_pw[:2] + "*" * (len(user_pw) - 2) if len(user_pw) > 2 else "****"

    print(f"로그인 ID: {user_id}")
    print(f"로그인 Password: {masked_pw}")
    print(f"기본 접속 URL: {base_url}")