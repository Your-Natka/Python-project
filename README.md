# Project "PhotoShare" 📷

# Запусти локально

uvicorn app.main:app --reload

### пере встановлюємо бібліотеки Poetry

Очищаємо старий lock-файл:

rm poetry.lock

Створюємо новий lock-файл і встановлюємо залежності:

poetry lock
poetry install

### Як запустити додаток у:

Створюємо віртуальне середовище.

python3 -m venv .venv
source .venv/bin/activate   # для Linux / Mac

# або

.venv\Scripts\activate   # для Windows PowerShell

Встановлюємо бібліотеки

pip install -r requirements.txt

### 🔄 Оновити контейнер після змін
docker-compose down
docker-compose up --build

docker-compose logs -f web

### 🗄 Зупинити контейнери
docker-compose down


### Увійти в контейнер PostgreSQL
psql -h localhost -U postgres -d photoshare

1️⃣ Показати всі записи
SELECT * FROM users;

2️⃣ Показати структуру таблиці
\d users
\d photos
\d comments
\d ratings
\d tags
\d photo_tags
\d transformed_links
\d alembic_version

3️⃣ Пошук конкретного користувача
SELECT * FROM users WHERE email='natka@example.com';



Коли попрацювали і зробили якісь зміни і нам треба зробити PR то ми виконуємо крок покрокові:

git add .
git commit -m '...(Тут буде назва вашого коментаря)'
git push
git push origin (назва вашої гілки)
Переходимо на гілку девелопер git checkout developer
git merge --no-ff (назва вашої гілки) -m '...(Короткий опис PR)'
git push origin developer
Виходимо віртуального середовища за допомогою команди: deactivate

📸 PhotoShare — REST API для обміну світлинами

FastAPI | PostgreSQL | SQLAlchemy | JWT | Cloudinary | Docker | Docker Compose

### 📑 Зміст

Опис проєкту

Основні можливості

Технології

Встановлення та запуск

Структура проєкту

Аутентифікація

Робота зі світлинами

Коментарі

Профіль користувача

Ролі користувачів

Рейтинг

Пошук та фільтрація

Тести

Docker та Docker Compose

Деплой

Контакти

### 1️⃣ Опис проєкту

PhotoShare — це REST API сервіс для збереження, обміну та обробки світлин.
Передбачено ролі користувачів, коментарі, рейтинги, генерація трансформованих зображень і QR-кодів, а також модерація та адміністрування.

### 2️⃣ Основні можливості
✔ Аутентифікація (JWT)

Реєстрація / логін

Реалізовано refresh + access tokens

Підтримка ролей: User, Moderator, Admin

Перший користувач автоматично стає Admin

Logout з чорним списком токенів (blacklist)

✔ Світлини

Завантаження фото на Cloudinary

CRUD операції над світлинами

До 5 тегів (створюються автоматично)

Трансформації зображень (набори Cloudinary)

Генерація URL та QR-кодів трансформованих фото

Перегляд фото за унікальним лінком

✔ Коментарі

Користувачі можуть коментувати світлини

Можуть редагувати лише свої коментарі

Модератор / адміністратор можуть видаляти

Зберігаємо created_at та updated_at

✔ Рейтинг

Оцінювання фото від 1 до 5

Один рейтинг від користувача

Заборонено оцінювати свої фото

Модератори / адміни можуть видаляти рейтинги

Автоматичне обчислення середнього значення

✔ Пошук та фільтрація

Пошук за ключовим словом

Пошук за тегами

Фільтр за датою або рейтингом

Для модераторів: фільтр за користувачами

✔ Профіль

Публічний профіль за username

Приватний профіль для редагування інформації

Статистика: кількість фото, дата реєстрації, тощо

Адмін може банити користувачів

### 3️⃣ Технології

FastAPI

PostgreSQL

SQLAlchemy / Alembic

Cloudinary

Python-Jose / Passlib / JWT

qrcode

Docker / Docker Compose

Pytest

### 4️⃣ Встановлення та запуск
🔧 1. Клонування репозиторію 
git clone https://github.com/Your-Natka/Python-project.git
cd Python-project

🔧 2. Створення .env
DATABASE_URL=postgresql+psycopg2://user:password@db:5432/photoshare
SECRET_KEY=your_secret
ALGORITHM=HS256
CLOUDINARY_NAME=...
CLOUDINARY_API_KEY=...
CLOUDINARY_API_SECRET=...

### 🔧 3. Запуск через Docker Compose
docker-compose up --build


API буде доступне на:
👉 http://localhost:8080

Документація Swagger:
👉 http://localhost:8080/docs

### Дерево проекту
├── -H
├── Dockerfile
├── ERROR
├── README.md
├── alembic
│   ├── README
│   ├── __pycache__
│   │   └── env.cpython-311.pyc
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-311.pyc
│   │   ├── __init__.cpython-312.pyc
│   │   ├── __init__.cpython-313.pyc
│   │   ├── main.cpython-311.pyc
│   │   ├── main.cpython-312.pyc
│   │   ├── main.cpython-313.pyc
│   │   ├── schemas.cpython-311.pyc
│   │   ├── schemas.cpython-312.pyc
│   │   ├── tramsform_schemas.cpython-311.pyc
│   │   └── tramsform_schemas.cpython-312.pyc
│   ├── conf
│   │   ├── __pycache__
│   │   ├── config.py
│   │   └── messages.py
│   ├── database
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── connect_db.py
│   │   └── models.py
│   ├── main.py
│   ├── repository
│   │   ├── __pycache__
│   │   ├── comments.py
│   │   ├── hashtags.py
│   │   ├── posts.py
│   │   ├── ratings.py
│   │   ├── transform_post.py
│   │   └── users.py
│   ├── routes
│   │   ├── __pycache__
│   │   ├── auth.py
│   │   ├── comments.py
│   │   ├── hashtags.py
│   │   ├── posts.py
│   │   ├── ratings.py
│   │   ├── transform_post.py
│   │   └── users.py
│   ├── schemas.py
│   ├── services
│   │   ├── __pycache__
│   │   ├── auth.py
│   │   ├── email.py
│   │   ├── roles.py
│   │   └── templates
│   └── tramsform_schemas.py
├── docker-compose.yml
├── docs
│   ├── Makefile
│   ├── build
│   │   ├── doctrees
│   │   └── html
│   ├── make.bat
│   └── source
│       ├── conf.py
│       └── index.rst
├── example.env
├── migrations
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 5997d1478345_increase_url_length.py
│       ├── 680fb28a8181_init.py
│       ├── 6e8308e59b8f_add_comments_and_blacklist.py
│       └── 9467ecb82664_change_back_to_url.py
├── poetry.lock
├── pyproject.toml
├── requirements.txt
├── test.db
└── tests
    ├── __init__.py
    ├── __pycache__
    │   ├── __init__.cpython-311.pyc
    │   └── conftest.cpython-311-pytest-8.4.2.pyc
    ├── auth
    │   ├── __pycache__
    │   └── test_route_auth.py
    ├── comments
    │   ├── __pycache__
    │   ├── test_repository_comments.py
    │   └── test_route_comments.py
    ├── conftest.py
    ├── hashtags
    │   ├── __pycache__
    │   ├── test_repository_hashtags.py
    │   └── test_route_hashtags.py
    ├── posts
    │   ├── __pycache__
    │   ├── test_repository_posts.py
    │   └── test_route_posts.py
    ├── rating
    │   ├── __pycache__
    │   ├── test_repository_ratings.py
    │   └── test_route_ratings.py
    ├── transformations
    │   ├── __pycache__
    │   ├── test_repository_transform_post.py
    │   └── test_route_transform_post.py
    └── users
        ├── __pycache__
        ├── test_repository_users.py
        └── test_route_users.py

### 6️⃣ Аутентифікація

Опис та основні маршрути:

🔹 {POST} /auth/signup

Опис:

Створює нового користувача. Якщо це перший користувач у БД → він стає admin.

Приклад запиту:
POST /auth/signup
Content-Type: application/json

{
  "username": "natusia",
  "email": "natusia@example.com",
  "password": "StrongPassword123!"
}

Приклад відповіді:
{
  "id": 1,
  "username": "natusia",
  "email": "natusia@example.com",
  "role": "admin",
  "created_at": "2025-01-01T12:00:00"
}

🔹 {POST} /auth/login

Опис:

Повертає access_token та refresh_token.
Користувач повинен бути активним (не забаненим).

Приклад запиту:
POST /auth/login
Content-Type: application/json

{
  "username": "natusia",
  "password": "StrongPassword123!"
}
Приклад відповіді:
{
  "access_token": "eyJhbGci...",
  "refresh_token": "eyJhbGc...",
  "token_type": "bearer"
}

🔹 {POST} /auth/logout — Вихід
Опис:

Access-token додається у чорний список до часу завершення його дії.
Токен у request header:

Authorization: Bearer <access_token>

Приклад відповіді:
{
  "message": "Successfully logged out"
}

🔹 {POST} /auth/refresh

Як працюють ролі та залежності (Depends)
Опис:

Приймає refresh_token → повертає новий access_token.

Приклад запиту:
POST /auth/refresh
Content-Type: application/json

{
  "refresh_token": "eyJhbGc..."
}

Приклад відповіді:
{
  "access_token": "new_access_token",
  "token_type": "bearer"
}

### Ролі та залежності (Depends)

У проєкті використовуються ролі:

Роль	             Можливості
user	             CRUD своїх фото, коментарі, рейтинг
moderator	         видаляти коментарі і рейтинги
admin	             CRUD усіх фото, бан користувачів

### 7️⃣ Робота зі світлинами

Опис та основні маршрути:

🔹 {POST} /photos/ — завантаження фото

Опис:

Завантажує зображення у Cloudinary та створює запис у БД.
До 5 тегів. Немає — не обов'язково.

Тіло multipart/form-data:
file: <image>
description: "Моя перша світлина"
tags: "nature,flowers"

Приклад відповіді:
{
  "id": 10,
  "url": "https://cloudinary.com/.../photo.jpg",
  "description": "Моя перша світлина",
  "tags": ["nature", "flowers"],
  "owner": "natusia"
}

🔹 {GET} /photos/{id} — отримання фото

Приклад відповіді:
{
  "id": 10,
  "url": "...",
  "owner": "natusia",
  "created_at": "2025-01-02T15:00:00"
}

🔹 {DELETE} /photos/{id}

Admin → може видаляти будь-які
User → тільки свої

🔹 {PUT} /photos/{id}

PUT /photos/10
{
  "description": "Оновлений опис"
}

🔹 {POST} /photos/transform/{id}

Опис:

Створення окремого посилання на трансформовану світлину.

Приклад:
POST /photos/transform/10
{
  "transformation": "rotate_90"
}

Приклад відповіді:
{
  "id": 100,
  "photo_id": 10,
  "url": "https://cloudinary.com/.../rotate_90/photo.jpg",
  "qr_code_url": "/media/qrcodes/100.png"
}


### 8️⃣ Коментарі

Опис та основні маршрути:

🔹 {POST} /comments/{photo_id}

POST /comments/10
{
  "text": "Чудове фото!"
}

Відповідь:
{
  "id": 55,
  "text": "Чудове фото!",
  "owner": "natusia",
  "created_at": "2025-01-03T10:00:00"
}

🔹 {PUT} /comments/{comment_id}

User → може редагувати лише свій коментар

PUT /comments/55
{
  "text": "Дуже гарне фото!"
}

🔹 {DELETE} /comments/{comment_id} (moder/admin)

Moderator — може

Admin — може

User — ❌ не може

9️⃣ Профіль

Опис та основні маршрути:

🔹 {GET} /users/profile/{username} — Публічний профіль

{
  "username": "natusia",
  "photos_count": 12,
  "registered_at": "2025-01-01T12:00:00",
  "bio": "Photographer"
}

🔹 {GET} /users/me — Особиста інформація

Треба токен.

{
  "username": "natusia",
  "email": "natusia@example.com",
  "bio": "Photographer",
  "is_active": true
}

🔹 {PUT} /users/me — Редагувати власний профіль
PUT /users/me
{
  "bio": "I love nature"
}

### 🔟 Ролі

Таблиця:

Роль	Доступ
User	свої фото, коментарі
Moderator	видаляти коментарі/рейтинг
Admin	повний доступ + бан

🔹 Призначення ролі (ADMIN)
PATCH /users/make_role/{email}
{
  "role": "moderator"
}

🔹 Бан користувача (ADMIN)
PATCH /users/ban/{email}

### 1️⃣1️⃣ Рейтинг

Опис та основні маршрути:

🔹 {POST} /rating/{photo_id}

User → може оцінювати лише чужі фото
Тільки 1 раз

POST /rating/10
{
  "value": 5
}

🔹 {DELETE} /rating/{id} (moder/admin)

Moder/Admin → можуть видаляти рейтинг

### 1️⃣2️⃣ Пошук

Опис та основні маршрути:
🔹 {GET} /search?q=keyword

GET /search/by_tag/nature

🔹 {GET} /search/by_tag/{tag}

Фільтри: &sort=date або &sort=rating

### 1️⃣3️⃣ Фільтрування:

За датою:

GET /search?q=flower&sort=date

За рейтингом:

GET /search?q=flower&sort=rating


Для модератора:

GET /search/users?username=natusia


### 1️⃣4️⃣ Тести

Опис:
Потрібно:

Юніт-тести для роутів

Тести авторизації

Тести ролей

Тести CRUD фото/коментарів/рейтингів

Покриття > 90%

Запуск:

pytest --cov=app

### 1️⃣5️⃣ Docker та Docker Compose

Включити:

Dockerfile

docker-compose.yml
де запускається:

FastAPI

PostgreSQL

Alembic-вставки при старті

### 1️⃣6️⃣ Деплой

Рекомендовані платформи:

Koyeb

Fly.io

Railway

Render

README містить:

Як зібрати образ

Як запустити міграції

Як змінити змінні оточення

### Контакти

