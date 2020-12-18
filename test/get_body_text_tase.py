import pytest
from module.get_body_text import ParsePage, ParsePage_Selenium
from module import data_class

test_news_item = data_class.PageItem(
    title="test",
    article_type='',
    brand='',
    published_at='',
    # link = "http://www.beautynury.com/m/news/view/89191"
    # link = "https://biz.chosun.com/site/data/html_dir/2020/12/10/2020121002251.html?utm_source=urlcopy&utm_medium=share&utm_campaign=biz"
    # link = "http://www.beautynury.com/m/news/view/91051"
    # link = "https://m.sportschosun.com/news.htm?id=202011270100251100016722&ServiceDate=20201126#_enliple"
    # link = "https://biz.chosun.com/site/data/html_dir/2020/05/13/2020051301255.html?utm_source=urlcopy&utm_medium=share&utm_campaign=biz"
    link = "https://www.mk.co.kr/news/business/view/2020/05/507875/"
)

    
parse_page_obj = ParsePage(test_news_item)
    

def test_get_page():
    parse_page_obj.get_page()

    assert parse_page_obj.page_html == 'a'

def test_get_body():
    parse_page_obj.get_page()
    parse_page_obj.get_body_text()

    result = parse_page_obj.page_body_bs4
    assert result == 'a'

def test_get_inner_text():
    parse_page_obj.get_page()
    parse_page_obj.get_body_text()
    
    result = parse_page_obj.get_inner_text()
    assert result.text == 'a'


# ParsePage_Selenium test
def test_ParsePage_Selenium():

    test_PageItemList = data_class.PageItemList([test_news_item])

    parse_obj = ParsePage_Selenium(test_PageItemList)
    # parse_obj.driver_generator()
    result = parse_obj.get_result()
    assert result == 'a'


