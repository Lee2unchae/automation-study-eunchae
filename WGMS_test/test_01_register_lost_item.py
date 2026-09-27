from playwright.sync_api import Page, expect

URL = "https://ipocc.dev.holeinonecloud.com/auth/login"
USER_ID = "eunchae010"                        
USER_PW = "dldmsco1!"

# 1. 로그인 > 분실물등록 화면 접속 테스트
def test_WGMS_로그인(page: Page):
    # 로그인 페이지 접속
    page.goto(f"https://ipocc.dev.holeinonecloud.com/auth/login")
    
    # 로그인 동작
    page.get_by_placeholder("아이디를 입력하세요").fill(USER_ID)
    page.get_by_placeholder("비밀번호를 입력하세요").fill(USER_PW)
    
    # 로그인 버튼 클릭
    page.get_by_role("button", name="로그인").click()
    
    # 로그인 확인
    expect(page).to_have_url(f"https://ipocc.dev.holeinonecloud.com/layout/main")
    
    # 분실물등록 메뉴 클릭
    page.get_by_role("link", name="기타운영").click()
    page.get_by_role("link", name="분실물관리").click()
    page.get_by_role("link", name="분실물등록").click()
    
    # 분실물등록 화면 타이틀 또는 URL 확인
    expect(page.get_by_role("tab", name="분실물등록")).to_be_visible()