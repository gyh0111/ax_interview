#
# Web Crawler
# URL news.ycombinator.com
# 글 목록을 가져와 출력
# 동일한 순서, 제목과 원글 링크 포함
#
# 순서
# 페이지 범위 정하기
# URL 읽기(읽기 실패시 처리, 구조 변경 확인)
# HTML 파싱(파싱 오류시 처리)
# 요소 담기
# print

import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com')

soup = BeautifulSoup(res.content, 'html.parser')

title_list = soup.find_all('title')

print(title_list)

for title in range(len(title_list)):
    print(title.get_text() + ' ' + title.url)

def down_url(link):
    #파일 저장 [글제목].html
    pass


for idx, title_ in enumerate(title_list, 1):
    print(idx, title_.text)
