#과제 1. 이메일 데이터 분석
import json

def parser_email(file_path):
    valid_emails = []
    invalid_emails = []
    domain_count = {}

    #파일 읽기 (예외 처리)
    try:
        with open(file_path, "r", encoding="utf-8")as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("파일을 찾을 수 없음")
        return

    #이메일 분류하기
    for line in lines:
        email = line.strip()

        #이메일 검사
        parts = email.split("@")
    
        if email.count("@") == 1 and len(parts) == 2 and parts[0] and parts[1]: #@이 한개 있고 @을 기준으로 2개로 나눠지는 경우
            userid, domain = parts
            
            if "." in domain and domain.startswith(".") == False and domain.endswith(".") == False: #도메인 영역 내 .이 있고 .이 도메인 시작과 끝에 위치하지 않은 경우
                valid_emails.append({"email": email, "userid": userid, "domain": domain})
                domain_count[domain] = domain_count.get(domain, 0) + 1
            else:
                invalid_emails.append(email)
        else:
            invalid_emails.append(email)

    #결과 저장
    result_data = {
        "valid_emails": valid_emails,
        "invalid_emails": invalid_emails,
        "domain_count": domain_count
    }

    try:
        with open("parsed_emails.json", "w", encoding="utf-8") as f:
            json.dump(result_data, f, ensure_ascii=False, indent=4)
            print("JSON 파일로 결과가 저장되었습니다.")
    except Exception as e:
        print("JSON 파일로 저장되지 않았습니다.")

# 실행
parser_email("emails.txt")





