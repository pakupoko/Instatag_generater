# Instatag_generater

## 개요
DJango로 구현한 인스타 사진 분류 및 태그 생성 웹 어플리케이션 입니다.

사진의 분류는 CNN의 학습을 통해 구현했습니다. 현재는 3종류의 사진만을 인식할 수 있습니다.(패션, 고양이, 음식)

태그 추천에 대해, 현재는 동일한 분류에 동일한 태그만 생성합니다. 생성되는 태그의 경우, 각 분류에서 좋아요 수가 가장 많은 사진의 태그를 기준으로 수집해두었습니다.

추후 업데이트를 통해, 태그 추천 또한 CNN기반의 머신 러닝을 통해 사진에 걸맞는 태그가 생성되도록 발전 시킬 예정입니다.

현재 깃헙 repo는 팀원이 설계한 알고리즘을 적용한 웹 어플리케이션 데이터만 존재합니다. 인스타 태그의 전처리 코드 및 모델 코드는 하단에 걸어둔 github 링크에서 확인하실 수 있습니다.

fork한 팀 프로젝트 소스 코드
https://github.com/pakupoko/-Hashtag-Lead-

## 구동
config/settings.py 에서 DB를 연동하고, 로그 데이터를 업로드할 스키마를 생성해야 합니다.

주요 라이브러리를 설치해야 합니다.

- Pillow == 6.1.0
- tensorflow == 1.14.0
- numpy == 1.17.2

버전 변동 시 추가로 업데이트 할 예정입니다. 이 부분에 대해 문제가 있다면 알려주세요. Readme에 업데이트 하겠습니다.

$python manage.py runserver 명령어를 통해 서버를 구축합니다. 생성된 주소로 들어가면 밑의 초기화면이 켜집니다.


![intro](./Readme_image/1.png)


상단에 Upload 버튼을 누르면 이미지 입력 페이지로 이동합니다.


![create](./Readme_image/2.png)


사진과 주요 설명을 입력하고 확인을 누르면 홈 화면에 사진이 추가됩니다.


![intro2](./Readme_image/3.png)


사진 하단부에 태그 생성 버튼을 누르면 태그가 생성됩니다.


![generate](./Readme_image/4.png)


오른쪽 상단의 검색 기능은 아직 작동하지 않습니다.
