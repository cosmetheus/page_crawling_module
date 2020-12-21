from dataclasses import dataclass
from os import link


@dataclass
class PageItem:
    article_type : str
    brand : list[str]
    title : str
    link : str
    text : str = ""

    def get_row(self):
        """내장 csv라이브러리가 row를 기록할때 사용하는 형식으로 PageItem의 요소들을 반환
        
        :return: [self.name, self.link, self.text]
        """
    
        # return [self.name, self.link, self.text]
        return {
            "link":self.link,
            "text":self.text
        }
    

@dataclass
class PageItemList:
    page_item_list :list[PageItem]

