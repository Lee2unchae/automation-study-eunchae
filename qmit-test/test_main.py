from playwright.sync_api import Page, expect

URL = "https://v369.dev.l-walk.com"

def test_메인_페이지_타이틀(page: Page):
    page.goto(URL)
    expect(page).to_have_title("큐밋! 타이틀 다르게 적기")

def test_로그인_버튼이_보인다(page: Page):
    page.goto(URL)
    expect(page.get_by_role("button", name="로그인")).to_be_visible()

def test_스토어(page: Page): 
    page.goto(URL)
    page.get_by_role("link", name="스토어").click() # 화면 이동
    expect(page).to_have_title("소프트웨어 테스팅 라이프 사이클") # 타이틀 확인

def test_큐밋소개_버튼_확인(page: Page):
    page.goto(URL)
    expect(page.get_by_role("button", name="큐밋소개")).to_be_visible() # 버튼 확인
