
from logging import log
from bs4 import BeautifulSoup
from module import data_class  
import bs4
import requests
import re
import sys
from config.logconfig import logger
from unicodedata import normalize


class ParsePage:
    """
    객체를 생성할때 page_url을 받아 page_url이 가지고있는 파
    """
    def __init__(self, news_item : data_class.NewsItem):
        self.news_item = news_item
        self.page_html : str
        self.page_body_heml : bs4.element.Tag
        
    def get_page(self):
        
        # self.page_url의 url로 페이지 정보를 가져와 requests객체로 만듬
        try:
            page_link = self.news_item.link.strip()
            
            logger.info(f"search  page : {page_link}")
            page_obj = requests.get(page_link)
            
            # 결과를 self.page_html 저장
            self.page_html = page_obj.text
        
        except Exception as error:
            logger.exception(error)
            sys.exit(error)


    def get_body_text(self):
        # requests로 가져온 페이지의 html로 bs4 객체 생성
        soupe = BeautifulSoup(self.page_html, 'html.parser')
        
        # bs4를 이용하여 tag_name : body부분을 추출
        if soupe.find('body') != None:
            # self.page_body_heml = soupe.find('body')
            self.page_body_heml = soupe.select('body')[0]
        else:
            raise ValueError(f"fail get body \n origin_text : {self.page_html}")
             
        
    def get_inner_text(self):
        # self.page_body_heml 중 내용부분만 문자열로 추출
        body_text = self.page_body_heml.text

        # 특수문자가 제거된 문자열을 result에 할당
        # regex: [^모든한글|띄어쓰기|모든숫자|모든영어]
        
        try:
            # 글자 꺠진경우
            normalize_text = normalize('NFC', body_text)
            change_text = normalize_text.encode('ISO-8859-1').decode('cp949','ignore')
            body_text = change_text
        except UnicodeEncodeError :
            # 정상 출력의 경우
            pass

        result = re.sub("[^가-힣ㄱ-ㅎ|\ |0-9|a-zA-Z]","",body_text)
        
        self.news_item.text = result
        return self.news_item

    def parsing(self):
        self.get_page()
        self.get_body_text()
        result = self.get_inner_text()

        return result

