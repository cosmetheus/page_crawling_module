# page_crawling_module
page_crawling_module은 입력된 페이지의 링크들에 접속해 패이지의 body text를 모두 가져와 
저장하는 프로그램입니다.
(가져오는 텍스트의 특수문자는 모두 제거됩니다.)

## Usage
### note
* 가상환경에서 동작시킬것을 권장합니다.
* python 3.9 이상의 환경에서 작동시킬것을 권장합니다.

### insatll dependence library

`./config/requirements_dev.txt` : 테스트,개발환경 설정 관련 라이브러리
`./config/requirements.txt` : 기능 수행을 위해 필요한 라이브러리


```pip install -r <library txt file> ``` 로 설치할수 있습니다.

### define `input.csv`

|텍스트타입|브랜드|제목|날자|URL|
|---|:---:|:---:|:---:|:---:|
|< article type >|< brand >|< title >|< published at >|< link >
|< article type >|< brand >|< title >|< published at >|< link >
.
.
.

원하는 값을 입력하세요

### setting save location
```main.py``` 의 run_selenium 함수의 파라메터를 조작하여 
* ```input.xlsx``` 파일의 경로
* 결과가 저장될 파일경로
* 결과파일 이름
* geckodriver의 경로를 설정할수 있습니다.

### run program
main.py 프로그램을 파이썬으로 실행시키면 프로그램이 실행되고 지정된 위치에 결과가 저장됩니다.
`````` 
venv) ➜python ./main.py
``````

### sample code
`````` python
# 모듈 사용 예제 코드

from module import data_class
from module.file_parse import FileHandler
from module.get_body_text import  ParsePage_Selenium

def run_selenium(
    input_file_path : str,
    output_file_path : str ,
    output_file_name: str,
    geckodriver_path : str, 
):

    """  
    FileHandler로 탐색할 액셀파일의 값을 읽어온뒤 
    액셀 파일에 있는 페이지링크로 패이지를 탐색후 
    body 태그에 있는 텍스트를 모두 가져온다.(갸져온 텍스트는 특수문자(줄바꿈 포함) 이 제거되있음)
    이후 FileHandler를 이용해 저장한다.

    :param input_file_path: 프로그램이 읽어올 링크가 포함된 .xlsx 파일 포멧은 README.md 참조 
    :type input_file_path: str

    :param output_file_path: 결과물이 저장될 파일 경로
    :type output_file_path: str

    :param output_file_name: 결과물 파일의 이름
    :type output_file_name: str

    :param geckodriver_path: geckodriver의 파일 경로 
    :type geckodriver_path: str
    """
    
    # excel 파일을 읽어옴
    excel_sheet = FileHandler.open_excel_file_list(file_path= input_file_path)

    # row들을 dataclass로 변환후 리스트업
    page_item_list = FileHandler.get_sheet_data(excel_sheet)

    # selenium 으로 페이지 파싱
    ParsePage_Selenium(page_item_list = page_item_list, driver_path = geckodriver_path).get_result()

    # 결과 파일생성
    FileHandler.write_csv(file_path = output_file_path ,file_name = output_file_name ,page_item_list= page_item_list)

if __name__ == "__main__":
    run_selenium(
        input_file_path = "input.xlsx",
        output_file_path = ".",
        output_file_name = "output_text",
        geckodriver_path = "config/geckodriver",
    )
``````

### result

|link|text|
|---|:---:|
|< link >|<body_text>
|< link >|<body_text>
.
.
.
