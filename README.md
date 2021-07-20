# 1. SNS-Gallery 🖼

## 📌 프로젝트 명 : Gallery

- 여러 사용자들이 계정을 만들어 사진을 올리고 다같이 공유하는 커뮤니티

## 주요 기능

1. 사용자 **로그인 및 회원가입**
2. 사용자들의 **게시물 열람 및 작성**
3. **게시물 수정 및 삭제**

# 2. 기능

- 기능을 django의 **APP 단위로 구분**
1. **account**
    - 사용자 **로그인 및 회원가입**
2. **post**
    - 사용자들의 **게시물 열람 및 작성**
    - **게시물 수정 및 삭제**

# 3. 데이터 테이블

- Model에 작성할 class를 말한다.
1. 사용자 테이블(Account)은 django에서 제공해주는 UserFormCreation()을 이용하여 간단하게 구현할 것이다.

    ![Account](https://user-images.githubusercontent.com/50159740/126260830-28790dfc-ccbd-4729-a785-c8f9eaeb0f1e.png)

2. 게시물 테이블(Post)

    ![Post](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7b042327-c176-4aa9-bf20-eedf42646bb5/Untitled.png)

- 두 테이블 간의 관계 ( 1 : n )

    → 한명의 사용자는 여러개의 게시물을 등록할 수 있다.

    → 하나의 게시물은 한명의 사용자의 것이다.

    ![Relation](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2963236c-612b-49e8-a743-e633d9168ad3/Untitled.png)

# 4. 화면 설계(prototype)

### (1) index.html (메인화면, 모든 게시물 확인)

![index.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/67f01747-a9e6-4cb1-8792-7b4d7d75556a/Untitled.png)

```html
<body>
	<header></header>(반복)
	<main>
		<section>메인 소개</section>
		<section>게시물 올라오는 카드</section>
	</main>
	<footer></footer>(반복)
</body>
```

### (2) post.html (게시물 작성 화면)

![post.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b3b9c738-a073-42d1-adf9-e88f8469b769/Untitled.png)

```html
<body>
	<header></header>(반복)
	<main>
		<section>Posting</section>
	</main>
	<footer></footer>(반복)
</body>
```

### (3) post_update.html (게시물 수정 화면)

![post_update.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7b0b60b-8b92-4fc0-9a38-5e556e216556/Untitled.png)

```html
<body>
	<header></header>(반복)
	<main>
		<section>Post Update</section>
	</main>
	<footer></footer>(반복)
</body>
```

### (4) signup.html (회원가입 화면)

![signup.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6168b349-e43b-4e14-b297-f03ec43b5e4e/Untitled.png)

```html
<body>
	<header></header>(반복)
	<main>
		<section>Signup</section>
	</main>
	<footer></footer>(반복)
</body>
```

# 5. 구현

### 초기설정

- 가상환경 설치
- 장고 설치
- 프로젝트 생성
- APP 생성 (account, post)
- settings.py 파일에 APP 등록

## 1️⃣ 프론트엔드

### (1) template 생성

- **post**
    - index.html
    - post.html
    - post_update.html
- **account**
    - login.html
    - signup.html

### (2) view 안에 각각 html 파일을 랜더링할 함수 작성하기

- **post**

    ```python
    from django.shortcuts import render

    # Create your views here.
    def index(request):
        return render(request, 'index.html')

    def post(request):
        return render(request, 'post.html')

    def post_update(request, post_id):
        return render(request, 'post_update.html')
    ```

- **account**

    ```python
    from django.shortcuts import render

    # Create your views here.
    def login_view(request):
        return render(request, 'login.html')

    def signup_view(request):
        return render(request, 'signup.html')
    ```

### (3) url 분리 후 path 설정

- config안의 Url에서 include로 post, account url과 연결하기

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('post.urls')),
        path('account/', include('account.urls')),
    ]
    ```

- post, account 앱의 각각 [urls.py](http://urls.py) 파일을 생성

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('login/', views.login_view, name='login_view'),
        path('signup/', views.signup_view, name='signup_view'),
    ]
    ```

    ```python
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
        path('post/', views.post, name='post'),
        path('post_update/', views.post_update, name='post_update'),
    ]
    ```

### (4) 공통된 부분 → 템플릿 상속

- config 폴더에 templates 폴더 생성
- 해당 폴더에 base.html 생성
- base.html을 settings.py에 연결하기

    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': ['config/templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]
    ```

- **post**
- **account**

## 2️⃣ 백엔드

### ✏️ account 작업

[account > views.py]

```python
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(request=request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request=request, username=username, password=password)
      if user is not None:
        login(request, user)
      return redirect('index')
  else:
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
  logout(request)
  return redirect('index')

def signup_view(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
    return redirect('index')
  else:
    form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})
```

[account > [urls.py](http://urls.py)]

→ logout 패스 추가

```python
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signup/', views.signup_view, name='signup_view'),
]
```

[account > templates]

- account의 templates 내용 수정

    : 주석처리했던 {{ form.as_p }} 풀어주기

[config > templates]

- base.html의 내용 수정

    ```html
    <ul class="list-unstyled">
     {% if user.is_authenticated %}
     <h2 style="color:white;">{{ user.username }}님, 안녕하세요 :)</h2>
     <li><a href="{% url 'logout_view' %}" class="text-white">Logout</a></li>
     {% endif %}
     {% if not user.is_authenticated %}
     <li><a href="{% url 'login_view' %}" class="text-white">Login</a></li>
     <li><a href="{% url 'signup_view' %}" class="text-white">Signup</a></li>
     {% endif %}
    </ul>
    ```

    → user가 확인이 되면(로그인을 한 상태라면) logout을 보여주고, 아니면 login과 signup을 보여줄 것

### ✏️ post 작업

[post > models.py]

- model 만들기

    ```python
    from django.db import models
    from django.contrib.auth.models import User

    # Create your models here.
    class Post(models.Model):
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        description = models.CharField(max_length=500, null=True)
        pub_date = models.DateTimeField('date published')
        image = models.ImageField(upload_to="post/%Y/%m/%d", null=True)

        def __str__(self):
            return self.description
    ```

    - ImageField를 사용하기 위해서 Pillow를 설치한다. (pip install Pillow)
    - makemigration, migrate, createsuperuser
    - admin연결
- admin으로 들어가서 확인, 게시물 작성해보기

[post > index.html]

```html
{% if user.is_authenticated %}
<a href="{% url 'post' %}" class="btn btn-primary my-2">POST</a>
{% endif %}

...

			<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        {% for post in posts %}
        <div class="col">
          <div class="card shadow-sm">
            <!-- 이미지 자리 -->
            <img src="{{ post.image.url }}" width="100%" alt="{{ post.id }}">
            <div class="card-body">
              <p class="card-text">{{ post.description }}</p>
              <div class="d-flex justify-content-between align-items-center">
                {% if request.user == post.author %}
                <div class="btn-group">
                  <button type="button" class="btn btn-sm btn-outline-secondary" onclick="">Delete</button>
                  <button type="button" class="btn btn-sm btn-outline-secondary" onclick="">Edit</button>
                </div>
                {% endif %}
                <small class="text-muted">{{ post.author.username }}</small>
                <small class="text-muted">{{ post.pub_date }}</small>
              </div>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
```

[media 파일 설정]

- settings.py에서 media 파일 설정해주기

    ```python
    import os

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

- post의 [urls.py](http://urls.py)에서 media 파일 설정해주기

    ```python
    from django.urls import path
    from . import views

    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
        path('', views.index, name='index'),
        path('post/', views.post, name='post'),
        path('post_update/', views.post_update, name='post_update'),
    ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```

- index.html에 사진이 잘 나오는지 확인

[post > post.html]

```python
	<section class="py-5 text-center container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h3 class="fw-light">[ Posting ]</h3>
        <form action="{% url 'post' %}" enctype="multipart/form-data" method="POST">
            {% csrf_token %}
            <p>사진 업로드 : <input type="file" name="image"> </p>
            <p>설명 : <input type="text" name="description"> </p>
            <input type="submit" value="올리기">
        </form>
      </div>
    </div>
  </section>
```

[post > urls.py]

- [urls.py](http://urls.py) 설정 (이미 해줬으니 pass)

[post > views.py]

- views의 post 함수 작성

    ```python
    @login_required(login_url='login_view')
    def post(request):
      if request.method == 'POST':
        post = Post()
        post.description = request.POST['description']
        post.image = request.FILES['image']
        post.author = request.user
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('index')
      return render(request, 'post.html')
    ```

> **update, delete 기능 추가하기**

[post > views.py]

```python
@login_required(login_url='login_view')
def post_update(request, post_id):
  if request.method == 'POST':
    edit_post = Post.objects.get(id=post_id)
    edit_post.description = request.POST['description']
    edit_post.image = request.FILES['image']
    edit_post.author = request.user
    edit_post.pub_date = timezone.datetime.now()
    edit_post.save()
    return redirect('index')
  else:
    edit_post = Post.objects.get(id=post_id)
    return render(request, 'post_update.html', {'edit': edit_post})

@login_required(login_url='login_view')
def post_delete(request, post_id):
  post = Post.objects.get(id=post_id)
  post.delete()
  return redirect('index')
```

[post > urls.py]

- [urls.py](http://urls.py) 수정

    ```python
    path('post_update/<int:post_id>', views.post_update, name='post_update'),
    path('post_delete/<int:post_id>', views.post_delete, name='post_delete'),
    ```

[post > templates]

- ㅇㄹ

```python
<button type="button" class="btn btn-sm btn-outline-secondary" onclick=" location.href=`{% url 'post_delete' post.id %}` ">Delete</button>
<button type="button" class="btn btn-sm btn-outline-secondary" onclick=" location.href=`{% url 'post_update' post.id %}` ">Edit</button>
```
