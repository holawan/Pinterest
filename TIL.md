## 오늘 배운점 

## 0330

### Django

- 다양한 앱을 django 내부에서 만들고 앱마다 자체적으로 가지고 있는 Front-end파일을 구축한다. 
- 그리고 해당 앱을 엮어서 웹 서비스를 구축한다.
- Django가 모여서  Docker의 컨테이너가 된다. 

#### Docker

- Django 컨테이너는 Django서비스의 일, MariaDB는 DB관련 일, Nginx는 서버 관련 일을 나눠서 진행한다. (MVC?)
- 이들이 모여서 Docker 시스템을 구축한다. 
- Docker를 구축하면 Vultr로 서버에 도커를 올린다.(AWS도 이용 가능)

#### MTV 패턴 

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

#### GIT 

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

## 0331

### HTML 

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

## 0404

### CSS 

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

  ![0404_디스플레이연습](TIL.assets/0404_디스플레이연습.PNG)

- Model

  - 장고에서 데이터베이스 사용이 편하도록 연동을 해주는 역할 
  - 개발에 있어 DB에 대해서 크게 신경쓰지 않도록 도와줌 
  - makemigration
    - models에서 만든 DB를 파이썬 파일과 연동

- HTTP Protocol
  - user와 server가 요청을 보내고 응답을 하면서 동작을 하는데, 여기서 GET과 POST를 사용해서 서버나 유저가 원하는 정보를 보낸다.
  - GET
    - 보통 조회의 기능
    - 조회를 할 때에는 새롭게 만드는 것보다 더 적은 코스트를 사용한다. 
    - 주소 안에 추가적인 파라미터를 넣어서 보내준다. 
      - ?는 파라미터가 시작한다는 표시 
  - POST
    - 수정이나 새로 만들 때 사용
    - 같은 주소를 보내더라도 추가적으로 바디라는 응답 내부 몸통에 데이터를 넣어서 보낸다. 
- Form
  - 서버에 보내는 요청 명세서
  - 글이나 파일 등을 포스트 바디안에 첨부하는데 그 데이터들이 Form 바디 안에 들어간다. 
  - action은 요청을 하려는 url
  - **CSRF_TOKEN**
    - 장고에서 POST를 보내려면 CSRF_TOKEN을 명시해야한다.
    - CSRF_TOKEN은 보안 기능을 한다. 

- DB SAVE

  - Send POST DATA

    - POST로 데이터를 보낼 때 데이터를 구분하기 위해 name을 설정할 수 있다.
    - 이 name을 기반으로 views.py에서 request.POST.get(name)으로 해당 데이터를 인식하고 사용할 수 있다.

    ```python
    ## hello_world.html
    <input type="text" name="hello_world_input">
    
    ## views.py
    
    temp = request.POST.get('hello_world_input')
    # DB를 구성한 모델을 가져온다. 
    
    
    new_hello_world = HelloWorld()
    #POST로 받아온 값을 DB에 추가해준다.
    #new_hello_world 인스턴스의 text에 temp를 저장 
    new_hello_world.text = temp
    new_hello_world.save()
            return render(request,'accountapp/hello_world.html',context={'hello_world_output': new_hello_world})
    
    ```

    ![0404_POST_TEST](TIL.assets/0404_POST_TEST.PNG)

  - Model에 있는 데이터 출력

  ```python
  ## Html
      {% if hello_world_list %}
      {% comment %} hello_world_output의 텍스트를 출력  {% endcomment %}
        <h1>{{hello_world_list}}</h1>
      {% endif %}
      
  #views.py
  # DB의 모든 객체 
  hello_world_list = HelloWorld.objects.all()
  return render(request,'accountapp/hello_world.html',context={'hello_world_list': hello_world_list})
      # POST 요청을 받으면 POST MEHTOD 표시 
      else :
  return render(request,'accountapp/hello_world.html',context={'hello_world_list': hello_world_list})
  ```

  ![0404_obects.all()](TIL.assets/0404_obects.all().PNG)

  - 페이지를 새로고침 할 때 아무것도 누르지 않았는데도, 마지막에 생성한 객체가 계속 반복적으로 생성됨 
    - why? views.py에서 POST가 있을 때 반복적으로 저장을 하기 때문에 
    - 해결을 위해 render를 하지 않고 그냥 페이지만 반환하게 redirect를 사용해야한다. 

  - POST로 데이터를 저장만 시키고, POST를 보내지 않을 때는 그냥 DB의 요소만 나열하게 한다...?

  - render 와 redirect 구분

    두 함수를 헷갈려 혼동하는 경우가 많습니다. 생각 외로 둘의 차이는 명확합니다. `render` 는 템플릿을 불러오고, `redirect` 는 URL로 이동합니다. URL 로 이동한다는 건 그 URL 에 맞는 views 가 다시 실행될테고 여기서 render 를 할지 다시 redirect 할지 결정할 것 입니다. 이 점에 유의해서 사용하신다면 상황에 맞게 사용하실 수 있을 겁니다.

## 0405

### Form

- Form(INPUT) -> Function(DB와 상호작용) -> HTML(OUTPUT)

- Form에서 요청을 보낼 때 현재까지는 제약이 없어 아무나 보낼 수 있었다.

  - 만약 우리가 가상 서버를 실제 서버로 올리면 아무나 글을 쓸 수 있게 하면 안된다.
  - 따라서 인증 시스템을 구축한다.

- 인증 (최소한의 보안)

  - 우리는 계정이 필요하다.
  - 계정 앱의 구성
    - 가입 - 로그인 - 계정정보 - 정보 수정 - 탈퇴 

- CRUD

  - 장고는 CRUD에 최적화되어 있는 앱 중 하나이다.
  - Class based View (장고)
    - 클래스에 기반한 모델
    - Create view (가입)
    - Read view (계정정보)
    - Update view (정보 수정)
    - Delete view (탈퇴)
    - 장고에서 몇가지 클래스를 상속 받으면 대부분의 기능을 장고가 제공한다.
  - Function Based View
    - 함수에 기반한 모델 

- Create view

  - Django에서 제공하는 CreateView를 사용한다

    - ```python
      class AccountCreateView(CreateView) :
          #파라미터 1 무슨 모델 ?
          model = User
          # 계정은 중요한 과정이기 때문에 기본적 템플릿을 제공한다.
          form_class = UserCreationForm
          # 계정을 만들 때 성공했으면 경로 지정 
          # reverse_lazy는 
          success_url = reverse_lazy('accountapp:hello_world')
          # 회원가입 할 때 볼 HTML 지정 
          template_name = 'accountapp/create.html'
      ```

  - 파라미터

    - model = User

      - first_name,last_name, email, is_staff 등이 이미 설정되어 있는 상태로 제공된다.

      ```python
      username = models.CharField(
              _('username'),
              max_length=150,
              unique=True,
              help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
              validators=[username_validator],
              error_messages={
                  'unique': _("A user with that username already exists."),
              },
          )
          first_name = models.CharField(_('first name'), max_length=150, blank=True)
          last_name = models.CharField(_('last name'), max_length=150, blank=True)
          email = models.EmailField(_('email address'), blank=True)
          is_staff = models.BooleanField(
              _('staff status'),
              default=False,
              help_text=_('Designates whether the user can log into this admin site.'),
          )
      ```

    - form_class = UserCreationForm

      - password 입력, 확인 등 검증 작업을 할 수 있다.

- django 기본 회원가입 form 이용해서 구현하기

```python
  <div style = "text-align: center">
    {% comment %} accountapp_crate로 연결해라  {% endcomment %}
    <form action="{% url 'accountapp:create' %}" method = "post">
      {% csrf_token %}
      {% comment %} 장고에서 제공하는 기본 폼 사용  {% endcomment %}
      {{ form }}
      <input type="submit" class = "btn btn-primary">
    </form>
  </div>
```

![0405_django_account_form](TIL.assets/0405_django_account_form.PNG)

- Login view

  ![0405_Login_view](TIL.assets/0405_Login_view.PNG)

- 로그인과 로그아웃 view를 만들고 Redirect할 경로를 찾아야한다.

- next가 존재하면 next로 간다.

- next가 없으면 setting 안에 있는 Login Redirect_URL로 간다. 

- Login Redirect_URL도 없으면 Default로 가서 에러가 난다. 

- 그래서 경로를 설정해줘야한다. 

- 가장 처음 받는 next 경로를 설정해주고, 

  ```python
  <a href="{% url 'accountapp:login' %}?next={{request.path}}">
  {% else %}
  <a href="{% url 'accountapp:logout' %}?next={{request.path}}">
  ```

- Login_redirect_url를 설정한다. 



### Render

- html 파일을 브라우저에게 보여줌

### Redirect

- 다른 url로 이동해줘 그럼 다른 url이 view에 요청을 보내 그럼 url이 render로 다시 보내줄거야 
- 만약 html을 직접 렌더링하지 않는 create나 delete 함수를 views.py에서 사용할때는 redirect를 사용해야한다.
- render를 사용하면 보여줄 html이 없기도 하고, html을 직접 렌더한다면 url이 꼬임 



## 0406

### Bootstrap

- Django에서 부트스트랩을 설치하려면 먼저 pip install을 해준다.

```
pip install django-bootstrap4
```

- Seetings.py에 등록해준다.
- 쓰고 싶은 html에 로드해준다. (스태틱처럼)

```html
{% load bootstrap4 %}
```

- form에 사용하려면

```html
{% bootstrap_form form %}
```

### CSS 스타일 변경이 즉시 작용되지 않을 때 

- **방법 1. 브라우저 캐시 삭제**
  - 경로 : 크롬 > 설정 > 개인정보 및 보안 > 쿠키 및 기타 사이트 데이터 > 모든 쿠키 및 사이트 데이터 보기 > 모두 삭제

- **방법 2. 링크 코드의 URL 변경**
  - CSS 파일을 링크하는 HTML 파일(PHP, JSP)을 열어 기존 CSS 파일의 URL 뒤에 **?after**를 붙이기



### Detail view

- 장고에서는 Detail View라고 한다. 다른데서는 Readview라고도 하는 모양

- DetailView 클래스를 상속 받아서 진행한다.

```python
class AccountDetailView(DetailView) :
    model = User 
    template_name = 'accountapp/detail.html'
```

- url에는 유저마다 세부 정보를 받아와야하니까 pk를 추가적으로 넣어준다.
- 클래스 내부에 target_user를 설정해야 하는데, 이는 다른 사람이 내 페이지를 들어왔을 때 내 페이지가 보이게 한다. target_user를 설정하지 않으면, 다른 사람이 my_page에 접근해도 그 사람 정보가 나타나게 된다..?
- 아니 다른 사람이 내 정보를 왜보는거지.... 인스타 피드 같은 느낌이라한다 일단 ^^

- context_object_name

  - 뷰에서 템플릿 파일에 전달하는 컨텍스트 변수명을 지정한다.

    ![0406_mypage](TIL.assets/0406_mypage.PNG)

### Update View

- 기본적으로 회원정보 수정이기 때문에 CreateView와 유사함 

```python
class AccountUpdateView(UpdateView) :
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    # 정보수정할 때  할 때 볼 HTML 지정 
    template_name = 'accountapp/update.html'
```

```html
#updateview
    <div class="mb-4">
      <h4>Change Info</h4> </div>
    <form action="{% url 'accountapp:update' user.pk %}" method = "post">
      {% csrf_token %}
      {% comment %} 장고에서 제공하는 기본 폼 사용  {% endcomment %}
      {% bootstrap_form form%}
      <input type="submit" class = "btn btn-primary">
    </form>
  </div>
```



- 다만, CreateForm를 그대로 사용하면 ID도 변경할 수 있게 나타남 

![0406_updateview](TIL.assets/0406_updateview.PNG)

- 일반적으로 ID는 변경 불가능하게 한다. 따라서 이를 비활성화하기 위해 UserCreateionForm이 아닌 새로운 Form을 이용한다.
- 새로운 forms.py를 만들어서 UserCreationForm을 상속받아 ID만 변경 불가능하게 만든다.

```python
from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm) :
    def __init__(self,*args,**kwargs) :
        super().__init__(*args, **kwargs) 
        # id를 변경 불가능하게 한다. 
        self.fields['username'].disabled = True 
```

![0406_updateview2](TIL.assets/0406_updateview2.PNG)

### Delete View

- Delete View를 이용한다.
- detail.html에 delete 기능을 만들어서 만약 본인이라면 탈퇴 버튼이 보이게 한다.
- 삭제 버튼을 누르면 삭제된다.

```python
#views.py
class AccountDeleteView(DeleteView) :
    model = User 
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
    
#delete.html
<form action="{% url 'accountapp:delete' pk=user.pk %}" method = "post">

#detail.html
 {% if target_user == user %}
    {% comment %} user 정보수정이 가능한 정보 수정 페이지를 표시  {% endcomment %}
    <a href="{% url 'accountapp:update' pk=user.pk %}">
    <p>
    Change Info
    </p>
    </a>
    <a href="{% url 'accountapp:delete' pk=user.pk %}">
    <p>Quit</p>
```

![0406_deleteview](TIL.assets/0406_deleteview.PNG)

### git reset 취소

- 오늘 리셋 잘못했다가 요단강 건널 뻔함 
  - 이유 커밋 한 번에 할려고;

먼저 reset부터 

### reset

```python
git log --oneline
```

하면 정보가 나온다. 

![gitlog](TIL.assets/gitlog.PNG)



여기서 위에서 2번째 커밋을 취소하고 싶으면 이렇게 치면된다.  

```python
git reset --hard 2a4978e
```

### 주의사항 

- 커밋을 취소하면 그 때까지 타이핑 했던 것들도 커밋 이전으로 다 파일이 돌아간다. 

#### 취소

```python
$git reflog 
```

 ![gitreflog](TIL.assets/gitreflog.PNG)

이렇게 나오는데, 나는 HEAD{3}에서 리셋을 잘못해서 파일이 다 날라가서 HEAD 4로 갔어야했다.

그러면 

```python
git reset --hard HEAD@{4}
```

이렇게 치면 된다. 



#### 만약 push 까지 해버렸다면, push 할 때

```python
git push -f
```

해야한다 컨플릭트나니까 .,.



## 0407

### 인증과정만들기

- 기존 과정에서는 로그인을 하지 않아도 url을 통해 update에 접근할 수 있었다.
- 따라서 user가 인증되어있을때만 접근할 수 있게 변경한다. 

```python
class AccountUpdateView(UpdateView) :
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'
    context_object_name = 'target_user'

    def get(self,*args, **kwargs) :

        if self.request.user.is_authenticated :
            return super().get(*args,**kwargs)
        else :
            return HttpResponseRedirect(reverse('accountapp:login'))
            
    def post(self,*args, **kwargs) :

        if self.request.user.is_authenticated :
            return super().get(*args,**kwargs)
        else :
            return HttpResponseRedirect(reverse('accountapp:login'))
```

