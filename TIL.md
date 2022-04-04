## 오늘 배운점 

### 0330

- Django
  - 다양한 앱을 django 내부에서 만들고 앱마다 자체적으로 가지고 있는 Front-end파일을 구축한다. 
  - 그리고 해당 앱을 엮어서 웹 서비스를 구축한다.
  - Django가 모여서  Docker의 컨테이너가 된다. 
  
- Docker
  - Django 컨테이너는 Django서비스의 일, MariaDB는 DB관련 일, Nginx는 서버 관련 일을 나눠서 진행한다. (MVC?)
  - 이들이 모여서 Docker 시스템을 구축한다. 
  - Docker를 구축하면 Vultr로 서버에 도커를 올린다.(AWS도 이용 가능)
  
- MTV 패턴 
  - Model
    - 모델은 장고와 데이터베이스가 통신하게 도와주는 도구이다. 
    - 객체를 만드는데 유저가 새로 가입하면 객체가 생김, 유저가 게시글을 쓰는 것도 객체. 
    - 데이터베이스에는 Row, columns가 있다. 
      - Article이라는 게시글이 있으면 그 안에 Title,article,image가 있는데 이가 DB에서는 Columns로 매칭된다. 
      - 모델을 설정하면 CRUD는 장고가 다 해준다. 
  - View
    - 장고의 계산을 담당하는 부분 
    - User가 Server에 Request를 보내면 Server는 응답을 위한 절차를 거친다. 그리고 응답을 보낸다. 
      - ex) 유저 로그인 ,유저가 보낸 요청이 유효한지, DB에서 가져오는 과정, 유저에게 되돌려주는 과정 
  - Template
    - 실질적으로 보이는 Front-end요소 
    - 유저는 웹사이트의 visual을 보는데 그 내부를 어떻게 구현하고 생성할 것인지 보여주는 방법 
      - ex) 유저가 게시글을 보고 싶을 때, HTML을 동적으로 반환 
  
- GIT 
  - Version Control System
  - 개발을 계속해서 진행할 때, 버전을 업데이트할텐데 버전 차이에서 문제나 필요를 해결해주는 역할을 할 수 있다.
  - git은 필수 ! 
    - 예를 들어 1.1부터 1.3까지 개발을 하게 되는데 1.3에서 에러가 생겼을 때, 롤백을 할 수 있다. 1.2로 
  - Branch
    - Main branch로 배포를 할 때, 1.1,1.2로 올라갈 때 추가적인 기능을 구현하고 싶을 수 있다. 기존에 영향을 주지 않으면서
    - 그럴 때 브랜치를 새로 파서 새로운 기능을 넣고 배포버전에 Merge로 합칠 수 있다. 
    - 팀워크를 할 때 커밋을 통해 누가 올렸는지 확인할 수 있고, 온라인 깃 저장소를 통해 오픈소스를 올려서 모두가 볼 수 있게하고 이슈를 개선할 수 있게한다. 
  - Command
    - add 
    - commit 
    - push
    - pull
    - branch
    - checkout

- environ

  - Django를 git에 배포할 때 Secret key가 있는데 이를 노출시키지 않게 하는 역할 
  - https://django-environ.readthedocs.io/en/latest/

  - Venv 폴더 내부에 해당 코드 복사

    - 주의사항 : SECRET_KEY = '' 이런식으로 띄어쓰기 금지 

    ```python
    DEBUG=on
    SECRET_KEY=나의 시크릿 키 넣어주기 
    DATABASE_URL=psql://urser:un-githubbedpassword@127.0.0.1:8458/database
    SQLITE_URL=sqlite:///my-local-sqlite.db 
    CACHE_URL=memcache://127.0.0.1:11211,127.0.0.1:11212,127.0.0.1:11213 
    REDIS_URL=rediscache://127.0.0.1:6379/1?
    client_class=django_redis.client.DefaultClient&password=ungithubbed-secret
    ```

  - settings.py에 해당 코드 복사 (BASE_DIR을 지우고 만들거나, BASE_DIR 위 아래에 코드 추가해줘도 됨 )

    ```python
    import os,environ
    env = environ.Env(
        # set casting, default value
        DEBUG=(bool, False)
    )
    
    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    # reading .env file
    environ.Env.read_env()
    ```

  - settings.py에서 SECRET_KEY 변경

    ```python
    SECRET_KEY = env('SECRET_KEY')
    ```

  - git ignore에 env 파일 추가

    ```pytohn
    .env
    ```

  

- 깃허브 팁 

  - 로컬에서 시간 되돌리기

  ```python
  git log --oneline 
  #깃에서 로그 확인 
  git reset -- hard ~num
  #원하는 만큼 커밋을 없앨 수 있다. 
  ```


### 0331

- HTML 

  - 장고에서는 extends와 include를 많이 쓴다. 용도가 살짝 다르다
    - extends : 미리 만들어놓은 HTML 템플릿을 가져와서 블록을 이용해 내용을 채워나간다. (바탕을 깔아준다. )
    - include : 조각을 가져와서 HTML에 추가한다. (더미를 가져와서 붙여준다. )
    - 즉, extends로 바탕을 만들고 include로 내용을 채워준다! 
  - HTML 뼈대 자체는 base로 만들고 head는 앱마다 다를 수 있기 때문에 따로 템플릿을 만들어서 include로 쓸 수 있다.
  - header와 footer도 재사용하고, body부분만 수정할 것이기 때문에 include로 빼준다.
  - border-radius는 블록의 가장자리에 공유를 줘서 부드럽게 만드는 것
  - base.html은 이제 베이스로 쓰고 앱 내부에 templates를 만든다.
    - templates 내부에 앱 이름과 같은 폴더를 다시 만들고 html파일을 그 안에 넣는데 그 이유는 앱 내부의  템플릿에서 html을 가져올 때, 어떤 앱에서 html을 가져왔는지 가독성 있게 확인할 수 있다.
  - 마진에 값을 두개 넣어주면 앞에는 상하, 뒤에는 좌우

  ``` html
   margin : 2rem 0;
  ```

- 구글 폰트 적용하는 법 

  - https://fonts.google.com/?subset=korean 접속
  - 상단 sentence 빈칸에 임의의 글 입력
  - 맘에드는 폰트 클릭
  - 링크 복사해서 head에 넣어주고 (부트스트랩 처럼)
  - 사용할 때는 아래 CSSrules to specify families 참고해서 sytle로 적용시키기 

- STATIC

  - https://docs.djangoproject.com/ko/4.0/howto/static-files/
  - STATIC_ROOT 설정 

  ```python
  STATIC_URL = '/static/'
  
  STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
  ```

  2.  베이스 디렉토리는 settings.py 경로에서 root폴더로 가서 그 폴더를 BASE_DIR로 하겠다.
  3. 즉, BASE_DIR 하위에 staticfiles에 추후 스태틱 파일들을 모으겠다.

- CSS

  - STATIC 폴더 안에 CSS파일을 만들고, head에서 링크를 받게한다. 
  - 공통된 요소들은 가시성 있게 클래스로 만들고 style을 css파일에서 준다. 

### 0404

- CSS 

  - Cascading Style Sheet 
  - CSS 우선 순위는 인라인 --> 내장 -> 링크 순서 

- DISPLAY

  - Block
    - HTML 태그 부모 최대 너비를 다 가져감 높이는 따로 설치하지 않는 이상 내용에 맞춰서 영역을 가짐
    - div는 기본적으로 display:block; 을 가지고 있다. 
  - Inline
    - 글씨의 높이와 영역만큼만 영역을 가져간다 추가하면 영역끼리 오른쪽으로 쌓인다.
    - span같은 경우에는 기본적으로 inline이다. 하지만 display block을 주면 블락으로 변경된다. 

  - Inline-block
    - 블럭이지만 Inline처럼 옆쪽으로 쌓인다. 
  - None
    - 요소가 존재하지 않는 것 
  - Hidden
    - 요소를 숨기는 것, 존재하지만 보이지 않는다.

- SIZE
  - px
    - 부모가 어떻게 되든 상관없이 크기가 고정된다. 
  - em
    - 부모가 커지는만큼 커진다. (부모가 1.5배 커지면 1.5배 커짐 )
    - 부모가 2개 있을 때 첫번째 부모가 2배가 되면 2번째 부모는 2배 자식은 4배가 된다. 
    - 따라서 문제가 발생할 수 있다.
  - **rem**
    - rem은 루트 HTML의 크기 변화에 대한 영향만 받는다.
    - 즉 반응형 웹에 적합하다. 
    - 1rem은 16px
  - %
    - 바로 위 부모 영향만 받는다 
