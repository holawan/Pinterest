## READEME

### Pinterest Project

- 구현 과정에서 공부한 점은 [TIL](https://github.com/holawan/Pinterest/blob/master/TIL.md) 파일에 기록해두었습니다.
- 배포 과정에서 공부한 점은 [TIL/Distribute](https://github.com/holawan/TIL/tree/master/Distribute)폴더 에 기록되어 있습니다.

#### 배포 주소

https://www.djangopractice.shop/

## 사용언어

- Python
- Django
- HTML
- CSS
- MariaDB



### 실행 방법 

- **해당 프로젝트에서 사용되는 SECRET_KEY와 데이터베이스는 보안처리 되어있으므로, 새로운 환경에서 Secret_key를 얻어서 실행해야 합니다.**

#### 가상환경 설치

```
python -m venv venv
```

#### 가상환경 실행

```
source venv/scripts/activate
```

#### 패키지 설치

```
pip install -r requirements.txt
```

#### 마이그레이션

```
python manage.py migrate
```

#### 실행

```
python manage.py runserver
```

