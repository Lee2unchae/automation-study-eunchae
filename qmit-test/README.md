# Qmit 자동화 테스트

# 1. 테스트 실행 방법
- 가상환경 활성화
.venv\Scripts\activate
- 의존성 패키지 설치
pip install -r requirements.txt
- Playwright 브라우저 설치
playwright install
- chromium, firefox, webkit 3개 브라우저 전체 테스트 실행
pytest --browser chromium --browser firefox --browser webkit

# 2. 실패 메시지의 기대값과 실제값
AssertionError: Page title expected to be '큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼'
E       Actual value: 큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼 
E       Call log:
E         - Expect "to_have_title" with timeout 5000ms
E           13 × locator resolved to <html lang="" class="content h-screen overflow-y-scroll relative p-0">…</html>
E              - unexpected value "큐밋! SW 테스트 프로젝트 아웃소싱 플랫폼"

# 3. 하드코딩 갯수
1개 (URL = "https://v369.dev.l-walk.com")

