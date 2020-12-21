import pytest
from module.get_body_text import  ParsePage_Selenium
from module import data_class

test_news_item = data_class.PageItem(
    title="test",
    article_type='',
    brand='',
    link = "https://cashropang.com/%EC%95%84%EC%9D%B4%EC%98%A4%ED%8E%98-%EC%8A%A4%ED%85%9C3-%EC%95%B0%ED%94%8C-50ml/"
)


# ParsePage_Selenium test
def test_ParsePage_Selenium():

    test_PageItemList = data_class.PageItemList([test_news_item])

    parse_obj = ParsePage_Selenium(test_PageItemList, driver_path="/Users/jogangmin/code/Source_code/page_crawling_module/config/geckodriver")
    # parse_obj.driver_generator()
    result = parse_obj.get_result()
    assert result == 'a'


