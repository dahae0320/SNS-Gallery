# 1. SNS-Gallery ๐ผ

## ๐ ํ๋ก์ ํธ ๋ช : Gallery

- ์ฌ๋ฌ ์ฌ์ฉ์๋ค์ด ๊ณ์ ์ ๋ง๋ค์ด ์ฌ์ง์ ์ฌ๋ฆฌ๊ณ  ๋ค๊ฐ์ด ๊ณต์ ํ๋ ์ปค๋ฎค๋ํฐ

## ์ฃผ์ ๊ธฐ๋ฅ

1. ์ฌ์ฉ์ **๋ก๊ทธ์ธ ๋ฐ ํ์๊ฐ์**
2. ์ฌ์ฉ์๋ค์ **๊ฒ์๋ฌผ ์ด๋ ๋ฐ ์์ฑ**
3. **๊ฒ์๋ฌผ ์์  ๋ฐ ์ญ์ **

# 2. ๊ธฐ๋ฅ

- ๊ธฐ๋ฅ์ django์ **APP ๋จ์๋ก ๊ตฌ๋ถ**
1. **account**
    - ์ฌ์ฉ์ **๋ก๊ทธ์ธ ๋ฐ ํ์๊ฐ์**
2. **post**
    - ์ฌ์ฉ์๋ค์ **๊ฒ์๋ฌผ ์ด๋ ๋ฐ ์์ฑ**
    - **๊ฒ์๋ฌผ ์์  ๋ฐ ์ญ์ **

# 3. ๋ฐ์ดํฐ ํ์ด๋ธ


- Model์ ์์ฑํ  class๋ฅผ ๋งํ๋ค.
1. ์ฌ์ฉ์ ํ์ด๋ธ(Account)์ django์์ ์ ๊ณตํด์ฃผ๋ UserFormCreation()์ ์ด์ฉํ์ฌ ๊ฐ๋จํ๊ฒ ๊ตฌํํ  ๊ฒ์ด๋ค.

	![Account](https://user-images.githubusercontent.com/50159740/126265603-e4041c88-dc0a-437e-a56e-c5af16ded818.png)

2. ๊ฒ์๋ฌผ ํ์ด๋ธ(Post)

	![Post](https://user-images.githubusercontent.com/50159740/126265600-a0e8937b-87e2-41ab-9718-ebf7614f0501.png)

- ๋ ํ์ด๋ธ ๊ฐ์ ๊ด๊ณ ( 1 : n )

    โ ํ๋ช์ ์ฌ์ฉ์๋ ์ฌ๋ฌ๊ฐ์ ๊ฒ์๋ฌผ์ ๋ฑ๋กํ  ์ ์๋ค.

    โ ํ๋์ ๊ฒ์๋ฌผ์ ํ๋ช์ ์ฌ์ฉ์์ ๊ฒ์ด๋ค.

    ![Relation](https://user-images.githubusercontent.com/50159740/126265597-aa09a4b4-48b3-4360-b8e9-2d2c0cb14dec.png)

# 4. ํ๋ฉด ์ค๊ณ(prototype)

### (1) index.html (๋ฉ์ธํ๋ฉด, ๋ชจ๋  ๊ฒ์๋ฌผ ํ์ธ)

![index](https://user-images.githubusercontent.com/50159740/126261538-f439b089-c80a-4c7d-9fda-8b86ef3b869d.png)

```html
<body>
	<header></header>(๋ฐ๋ณต)
	<main>
		<section>๋ฉ์ธ ์๊ฐ</section>
		<section>๊ฒ์๋ฌผ ์ฌ๋ผ์ค๋ ์นด๋</section>
	</main>
	<footer></footer>(๋ฐ๋ณต)
</body>
```

### (2) post.html (๊ฒ์๋ฌผ ์์ฑ ํ๋ฉด)

![postHtml](https://user-images.githubusercontent.com/50159740/126261537-59f698bc-574b-4e0a-bb49-ed08069b6f25.png)

```html
<body>
	<header></header>(๋ฐ๋ณต)
	<main>
		<section>Posting</section>
	</main>
	<footer></footer>(๋ฐ๋ณต)
</body>
```

### (3) post_update.html (๊ฒ์๋ฌผ ์์  ํ๋ฉด)

![post_update](https://user-images.githubusercontent.com/50159740/126261534-dfb6b485-32af-40f6-9aa0-252f2fbf9783.png)

```html
<body>
	<header></header>(๋ฐ๋ณต)
	<main>
		<section>Post Update</section>
	</main>
	<footer></footer>(๋ฐ๋ณต)
</body>
```

### (4) signup.html (ํ์๊ฐ์ ํ๋ฉด)

![signup](https://user-images.githubusercontent.com/50159740/126261530-7fa47ee4-31b6-459e-bea5-40fd08dd6635.png)

```html
<body>
	<header></header>(๋ฐ๋ณต)
	<main>
		<section>Signup</section>
	</main>
	<footer></footer>(๋ฐ๋ณต)
</body>
```

# 5. ๊ตฌํ

### ์ด๊ธฐ์ค์ 

- ๊ฐ์ํ๊ฒฝ ์ค์น
- ์ฅ๊ณ  ์ค์น
- ํ๋ก์ ํธ ์์ฑ
- APP ์์ฑ (account, post)
- settings.py ํ์ผ์ APP ๋ฑ๋ก

## 1๏ธโฃ ํ๋ก ํธ์๋

### (1) template ์์ฑ

- **post**
    - index.html
    - post.html
    - post_update.html
- **account**
    - login.html
    - signup.html

### (2) view ์์ ๊ฐ๊ฐ html ํ์ผ์ ๋๋๋งํ  ํจ์ ์์ฑํ๊ธฐ

- **post**

    ```python
    from django.shortcuts import render

    # Create your views here.
    def index(request):
        return render(request, 'index.html')

    def post(request):
        return render(request, 'post.html')

    def post_update(request):
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

### (3) url ๋ถ๋ฆฌ ํ path ์ค์ 

- config์์ Url์์ include๋ก post, account url๊ณผ ์ฐ๊ฒฐํ๊ธฐ

    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('post.urls')),
        path('account/', include('account.urls')),
    ]
    ```

- post, account ์ฑ์ ๊ฐ๊ฐ [urls.py](http://urls.py) ํ์ผ์ ์์ฑ

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

### (4) ๊ณตํต๋ ๋ถ๋ถ โ ํํ๋ฆฟ ์์

- config ํด๋์ templates ํด๋ ์์ฑ
- ํด๋น ํด๋์ base.html ์์ฑ

    ```html
    {% load static %}

    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
        <meta name="generator" content="Hugo 0.84.0">
        <title>Portfoilo</title>

        <link rel="canonical" href="https://getbootstrap.com/docs/5.0/examples/album/">
        
        <!-- Bootstrap core CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        
        <meta name="theme-color" content="#7952b3">

        <style>
          .bd-placeholder-img {
            font-size: 1.125rem;
            text-anchor: middle;
            -webkit-user-select: none;
            -moz-user-select: none;
            user-select: none;
          }

          @media (min-width: 768px) {
            .bd-placeholder-img-lg {
              font-size: 3.5rem;
            }
          }
        </style>

        
      </head>
      <body>
        
    <header>
      <div class="collapse bg-dark" id="navbarHeader">
        <div class="container">
          <div class="row">
            <div class="col-sm-8 col-md-7 py-4">
              <h4 class="text-white">About</h4>
              <p class="text-muted">Add some information about the album below, the author, or any other background context. Make it a few sentences long so folks can pick up some informative tidbits. Then, link them off to some social networking sites or contact information.</p>
            </div>
            <div class="col-sm-4 offset-md-1 py-4">
              <ul class="list-unstyled">
                <!-- {% if user.is_authenticated %} -->
                <h2 style="color:white;">[์ฌ์ฉ์]๋, ์๋ํ์ธ์ :)</h2>
                <li><a href="#" class="text-white">Logout</a></li>
                <!-- {% endif %} -->
                <!-- {% if not user.is_authenticated %} -->
                <li><a href="#" class="text-white">Login</a></li>
                <li><a href="#" class="text-white">Signup</a></li>
                <!-- {% endif %} -->
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="navbar navbar-dark bg-dark shadow-sm">
        <div class="container">
          <a href="#" class="navbar-brand d-flex align-items-center">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" aria-hidden="true" class="me-2" viewBox="0 0 24 24"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>
            <strong>Portfoilo</strong>
          </a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarHeader" aria-controls="navbarHeader" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
        </div>
      </div>
    </header>

    <main>

          {% block content %}
          {% endblock %}

    </main>

    <footer class="text-muted py-5">
      <div class="container">
        <p class="float-end mb-1">
          <a href="#">Back to top</a>
        </p>
        <p class="mb-1">Album example is &copy; Bootstrap, but please download and customize it for yourself!</p>
        <p class="mb-0">New to Bootstrap? <a href="/">Visit the homepage</a> or read our <a href="/docs/5.0/getting-started/introduction/">getting started guide</a>.</p>
      </div>
    </footer>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
          
      </body>
    </html>
    ```

- base.html์ settings.py์ ์ฐ๊ฒฐํ๊ธฐ

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
    - index.html

        ```html
        {% extends 'base.html' %}

        {% block content %}
        {% load static %}
         <section class="py-5 text-center container">
            <div class="row py-lg-5">
              <div class="col-lg-6 col-md-8 mx-auto">
                <h1 class="fw-light">Portfoilo</h1>
                <!-- ์ด๋ฏธ์ง ์ถ๊ฐํ๊ธฐ -->
                <img src="#" alt="profile" height="200px">
                <br><br>
                <p class="lead text-muted">๊ธ์ ์ฐ๊ณ  ์ฌ๋๋ค๊ณผ ์ํตํ์ธ์.</p>
                <p>
                  <a href="#" class="btn btn-primary my-2">POST</a>
                </p>
              </div>
            </div>
          </section>

          <div class="album py-5 bg-light">
            <div class="container">

              <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">

                <div class="col">
                  <div class="card shadow-sm">
                    <!-- ์ด๋ฏธ์ง ์๋ฆฌ -->
                    <img src="" width="100%" alt="">
                    <div class="card-body">
                      <p class="card-text">์ค๋ช</p>
                      <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                          <button type="button" class="btn btn-sm btn-outline-secondary" onclick="">Delete</button>
                          <button type="button" class="btn btn-sm btn-outline-secondary" onclick="">Edit</button>
                        </div>
                        <small class="text-muted">์์ฑ์</small>
                        <small class="text-muted">์์ฑํ ๋ ์ง</small>
                      </div>
                    </div>
                  </div>
                </div>

              </div>

            </div>
          </div>

        {% endblock %}
        ```

    - post.html

        ```html
        {% extends 'base.html' %}

        {% block content %}

          <section class="py-5 text-center container">
            <div class="row py-lg-5">
              <div class="col-lg-6 col-md-8 mx-auto">
                <h3 class="fw-light">[ Posting ]</h3>
                <form action="#" enctype="multipart/form-data" method="POST">
                    {% csrf_token %}
                    <p>์ฌ์ง ์๋ก๋ : <input type="file" name="image"> </p>
                    <p>์ค๋ช : <input type="text" name="description"> </p>
                    <input type="submit" value="์ฌ๋ฆฌ๊ธฐ">
                </form>
              </div>
            </div>
          </section>

        {% endblock %}
        ```

    - post_update.html

        ```html
        {% extends 'base.html' %}

        {% block content %}

          <section class="py-5 text-center container">
            <div class="row py-lg-5">
              <div class="col-lg-6 col-md-8 mx-auto">
                <h3 class="fw-light">[ Post Update ]</h3>
                <form action="#" enctype="multipart/form-data" method="POST">
                    {% csrf_token %}
                    <p>์ฌ์ง ์๋ก๋ : <input type="file" name="image"> </p>
                    <p>์ค๋ช : <input type="text" name="description" value=""> </p>
                    <input type="submit" value="์ฌ๋ฆฌ๊ธฐ">
                </form>
              </div>
            </div>
          </section>

        {% endblock %}
        ```

- **account**
    - login.html

        ```html
        {% extends 'base.html' %}

        {% block content %}
          <section class="py-5 text-center container">
            <div class="row py-lg-5">
              <div class="col-lg-6 col-md-8 mx-auto">
              <a href="{% url 'index' %}">๋์๊ฐ๊ธฐ</a>
                <form action="" method="POST">
                  {% csrf_token %}
                  <!-- {{ form.as_p }} -->
                  <input type="submit" value="์ ์ถ">
                </form>
              </div>
            </div>
          </section>
        {% endblock %}
        ```

    - signup.html

        ```html
        {% extends 'base.html' %}

        {% block content %}
          <section class="py-5 text-center container">
            <div class="row py-lg-5">
              <div class="col-lg-6 col-md-8 mx-auto">
              <a href="{% url 'index' %}">๋์๊ฐ๊ธฐ</a>
                <form action="" method="POST">
                  {% csrf_token %}
                  <!-- {{ form.as_p }} -->
                  <input type="submit" value="์ ์ถ">
                </form>
              </div>
            </div>
          </section>
        {% endblock %}
        ```

## 2๏ธโฃ ๋ฐฑ์๋

### โ๏ธ account ์์

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

โ logout ํจ์ค ์ถ๊ฐ

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

- account์ templates ๋ด์ฉ ์์ 

    : ์ฃผ์์ฒ๋ฆฌํ๋ {{ form.as_p }} ํ์ด์ฃผ๊ธฐ

[config > templates]

- base.html์ ๋ด์ฉ ์์ 

    ```html
    <ul class="list-unstyled">
     {% if user.is_authenticated %}
     <h2 style="color:white;">{{ user.username }}๋, ์๋ํ์ธ์ :)</h2>
     <li><a href="{% url 'logout_view' %}" class="text-white">Logout</a></li>
     {% endif %}
     {% if not user.is_authenticated %}
     <li><a href="{% url 'login_view' %}" class="text-white">Login</a></li>
     <li><a href="{% url 'signup_view' %}" class="text-white">Signup</a></li>
     {% endif %}
    </ul>
    ```

    โ user๊ฐ ํ์ธ์ด ๋๋ฉด(๋ก๊ทธ์ธ์ ํ ์ํ๋ผ๋ฉด) logout์ ๋ณด์ฌ์ฃผ๊ณ , ์๋๋ฉด login๊ณผ signup์ ๋ณด์ฌ์ค ๊ฒ

### โ๏ธ post ์์

[post > models.py]

- model ๋ง๋ค๊ธฐ

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

    - ImageField๋ฅผ ์ฌ์ฉํ๊ธฐ ์ํด์ Pillow๋ฅผ ์ค์นํ๋ค. (pip install Pillow)
    - makemigration, migrate, createsuperuser
    - admin์ฐ๊ฒฐ
- admin์ผ๋ก ๋ค์ด๊ฐ์ ํ์ธ, ๊ฒ์๋ฌผ ์์ฑํด๋ณด๊ธฐ

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
            <!-- ์ด๋ฏธ์ง ์๋ฆฌ -->
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

[media ํ์ผ ์ค์ ]

- settings.py์์ media ํ์ผ ์ค์ ํด์ฃผ๊ธฐ

    ```python
    import os

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```

- post์ [urls.py](http://urls.py)์์ media ํ์ผ ์ค์ ํด์ฃผ๊ธฐ

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

- index.html์ ์ฌ์ง์ด ์ ๋์ค๋์ง ํ์ธ

[post > post.html]

```python
	<section class="py-5 text-center container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h3 class="fw-light">[ Posting ]</h3>
        <form action="{% url 'post' %}" enctype="multipart/form-data" method="POST">
            {% csrf_token %}
            <p>์ฌ์ง ์๋ก๋ : <input type="file" name="image"> </p>
            <p>์ค๋ช : <input type="text" name="description"> </p>
            <input type="submit" value="์ฌ๋ฆฌ๊ธฐ">
        </form>
      </div>
    </div>
  </section>
```

[post > urls.py]

- [urls.py](http://urls.py) ์ค์  (์ด๋ฏธ ํด์คฌ์ผ๋ pass)

[post > views.py]

- views์ post ํจ์ ์์ฑ

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

> **update, delete ๊ธฐ๋ฅ ์ถ๊ฐํ๊ธฐ**

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

- [urls.py](http://urls.py) ์์ 

    ```python
    path('post_update/<int:post_id>', views.post_update, name='post_update'),
    path('post_delete/<int:post_id>', views.post_delete, name='post_delete'),
    ```
[post > templates]

- ํด๋ฆญ ์ด๋ฒคํธ

```python
<button type="button" class="btn btn-sm btn-outline-secondary" onclick=" location.href=`{% url 'post_delete' post.id %}` ">Delete</button>
<button type="button" class="btn btn-sm btn-outline-secondary" onclick=" location.href=`{% url 'post_update' post.id %}` ">Edit</button>
```

- post_update.html

```python
{% extends 'base.html' %}

{% block content %}

  <section class="py-5 text-center container">
    <div class="row py-lg-5">
      <div class="col-lg-6 col-md-8 mx-auto">
        <h3 class="fw-light">[ Post Update ]</h3>
        <form action="{% url 'post_update' edit.id %}" enctype="multipart/form-data" method="POST">
            {% csrf_token %}
            <p>์ฌ์ง ์๋ก๋ : <input type="file" name="image"> </p>
            <p>์ค๋ช : <input type="text" name="description" value="{{ edit.description }}"> </p>
            <input type="submit" value="์ฌ๋ฆฌ๊ธฐ">
        </form>
      </div>
    </div>
  </section>

{% endblock %}
```
- ์ ๋ถ ๋ค ์์ฑํ views.py

    ```python
    from django.shortcuts import render, redirect
    from .models import Post
    from django.utils import timezone
    from django.contrib.auth.decorators import login_required

    # Create your views here.
    def index(request):
      posts = Post.objects.all().order_by('-pub_date')
      return render(request, 'index.html', {'posts': posts})

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
