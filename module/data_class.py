from dataclasses import dataclass


@dataclass
class NewsItem:
    name : str
    link : str
    text : str = ""

    def get_csv_row(self):
        """내장 csv라이브러리가 row를 기록할때 사용하는 형식으로 NewsItem의 요소들을 반환
        
        :return: [self.name, self.link, self.text]
        """
    
        # return [self.name, self.link, self.text]
        return {

        }
    

@dataclass
class NewsItemList:
    news_item_list :list[NewsItem]

