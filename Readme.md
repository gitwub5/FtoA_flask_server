## Khuthon Flask 프로젝트
- - - - -
### 쿠톤 주제: 교육의 정보화
-> 공부 내용(요약본)을 문제로 만들어주는 플랫폼 개발 
+ 서비스명: FtoA (F2A)
+ 의미: F만 받던 나도 이 서비스로 매일 복습하면 A대 맞을 수 있다!
+ 취지: 암기를 싫어하는 당신을 위한 최고의 도구
**문제유형1** 빈칸 추론 
**문제유형2** 키워드 기반 새로운 문제 생성
- - - - -
+ 프로젝트는 가상환경에서 진행되였습니다.
+ **virtualenv 가상환경 생성**
    
    **가상환경 설치 & 생성**
    
    ```
    $ sudo pip3 install virtualenv
    ```
    
    virtualenv를 설치했다면 프로젝트 폴더에서 가상환경을 생성하고 켜주자!
    
    ```
    $ virtualenv myenv
    $ source myenv/bin/activate
    ```
    - ****가상 환경인지 확인하기****
    - ****가상 환경에서 플라스크 설치하기****

    ```python
    (venv) pip install flask
    ```

+ requirements.txt에서 필요한 패키지들을 설치하십시오.
