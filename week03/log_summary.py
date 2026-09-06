#과제 3. 테스트 로그 분석
import json

#로그 불러오기
def load_log():
    try:
        with open("test_log.txt", "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print("[오류] test_log.txt 파일이 존재하지 않습니다.")
        return []

#로그 분석하기
def analyze_logs(logs):
    total_count = 0
    pass_count = 0
    fail_count = 0
    failed_tests = []
    
    for log in logs:
        log = log.strip()
        if not log:
            continue
            
        parts = log.split(",")
        
        if len(parts) == 3:
            test_name = parts[1].strip() #테스트명
            result = parts[2].strip().upper() #대소문자 구분 없이 처리하기 위해 대문자로 변환
            
            if result == "PASS" or result.startswith("PASS"): #결과가 PASS 또는 PASSED 등인 경우
                total_count += 1
                pass_count += 1
            elif result == "FAIL" or result.startswith("FAIL"): #결과가 FAIL 또는 FAILED 등인 경우
                total_count += 1
                fail_count += 1
                failed_tests.append(test_name)  # 결과가 FAIL인 경우 테스트 이름 저장
            else:
                print("잘못된 결과값 형식", [log]) # PASS/FAIL 외의 다른 값이 들어온 경우 처리
        else:
            print("잘못된 로그 형식", [log])
            
    #성공률 계산
    if total_count > 0:
        success_rate = pass_count / total_count * 100 #전체 데이터 갯수가 1개 이상이면 성공률 계산
    else:
        success_rate = 0.0 #0개면 성공률 0.0
    
    return {
        "total_count": total_count,
        "pass_count": pass_count,
        "fail_count": fail_count,
        "success_rate": round(success_rate, 2),
        "failed_tests": failed_tests
    }

#분석 결과 
def save_summary(summary_data):
    try:
        with open("summary.json", "w", encoding="utf-8") as f:
            json.dump(summary_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("JSON 저장에 실패했습니다.")

def main():
    logs = load_log()
    
    if logs:
        summary = analyze_logs(logs)
        
        print("전체 테스트 수 계산: ", summary['total_count'])
        print("PASS 개수 계산: ", summary['pass_count'])
        print("FAIL 개수 계산: ", summary['fail_count'])
        print("테스트 성공률 계산: ", summary['success_rate'], "%")
        print("실패한 테스트 목록 출력: ", summary['failed_tests'])
        
        # JSON 파일로 저장
        save_summary(summary)

main()