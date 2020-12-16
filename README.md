# page_crawling_module
page_crawling_module은 프로젝트 안에 input.csv파일에 페이지의 제목과 링크를 입력하면
링크 패이지의 body text를 모두 가져오는 프로그램입니다.

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

|제목|링크|
|---|:---:|
|<page_title>|<page_link>
|<page_title>|<page_link>
.
.
.

원하는 값을 입력하세요

### setting save location

`./config/setting` 파일에는 저장파일과 `input.csv`의 경로를 변경할 수 있습니다.

`./config/setting`의 기본설정
```
# 탐색할 news list 파일 경로
SEARCH_FILE_PATH = "input.csv"
# 저장할 파일 경로
SAVE_FILE_PATH = "."
```

### run program
main.py 프로그램을 파이썬으로 실행시키면 프로그램이 실행되고 지정된 위치에 결과가 저장됩니다.
