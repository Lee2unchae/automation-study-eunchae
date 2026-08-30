#과제 2. 메모 관리 프로그램
import json

#메모 불러오기
def load_memo():
    try:
        with open("memos.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return [] #파일이 없으면 빈 리스트로 시작

#메모 저장하기
def save_memo(memos):
    try:
        with open("memos.json", "w", encoding="utf-8") as f:
            json.dump(memos, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("저장 중 오류 발생")

#메모 기능 구현
def main():
    memos = load_memo()

    while True:
        print("<메모 관리 프로그램>")
        print("1. 메모 추가")
        print("2. 전체 메모 조회")
        print("3. 메모 검색")
        print("4. 프로그램 종료")
        print("원하는 기능의 번호를 입력하세요")

        a = input()

        #1. 메모 추가
        if a == "1":
            print("추가할 메모를 입력하세요")
            add_memo = input()
            if add_memo:
                memos.append(add_memo)
                save_memo(memos)
                print("메모 저장 완료")
            else:
                print("빈 메모는 저장할 수 없습니다.")

        #2. 전체 메모 조회
        elif a == "2":
            if not memos:
                print("저장된 메모 없음")
            else:
                for i, memo in enumerate(memos, 1):
                    print("전체 메모 조회: ")
                    print(memo)

        #3. 메모 검색
        elif a == "3":
            if not memos:
                print("저장된 메모 없음")
            else:
                print("검색할 메모를 입력하세요")
                search = input()
                found = False

                for index, memo in enumerate(memos, 1):
                    # 대소문자 구분 없이 검색하기 위해 .lower() 사용
                    if search.lower() in memo.lower():
                        print("검색 결과: ", memo)
                        found = True  # 검색 결과를 찾았으므로 True로 변경
                
                # 끝까지 돌았는데 일치하는 메모가 하나도 없는 경우
                if not found:
                    print("검색 결과가 없습니다.")

        #4. 프로그램 종료
        elif a == "4":
            print("프로그램을 종료합니다.")
            break

        # 예외 (1~4 이외의 숫자 입력)  
        else:
            print("잘못된 입력입니다. 기능 번호를 확인해주세요.")

main()

    

    

