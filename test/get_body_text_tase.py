import pytest
from module.get_body_text import ParsePage
from module import data_class

test_news_item = data_class.NewsItem(
    name="test",
    link="http://www.yakup.com/news/?nid=246818&mode=view"
)

    
parse_page_obj = ParsePage(test_news_item)
    

def test_get_page():
    parse_page_obj.get_page()

    result = parse_page_obj.page_text
    assert result == 'a'

def test_get_body():
    parse_page_obj.get_page()
    parse_page_obj.get_body_text()

    result = parse_page_obj.page_body_bs4
    assert result == 'a'

def test_get_inner_text():
    parse_page_obj.get_page()
    parse_page_obj.get_body_text()
    
    result = parse_page_obj.get_inner_text()
    assert result == 'a'
