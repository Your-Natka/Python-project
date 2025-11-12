# Project "PhotoShare" 📷
### Як запустити додаток:

Створюємо віртуальне середовище.

python3 -m venv .venv
source .venv/bin/activate   # для Linux / Mac

# або

.venv\Scripts\activate   # для Windows PowerShell

Встановлюємо бібліотеки
pip install -r requirements.txt

# Запусти контейнер
docker-compose down             --- для перезапуску видаляємо старі контейнера
docker-compose up -d --build
docker ps

docker-compose logs -f web
 

# Запусти локально

uvicorn app.main:app --reload


<p align="center">
      <img src="https://i.pinimg.com/originals/0b/ba/ef/0bbaeface0390e5a675f97a812deeb0f.png" width="1010">
</p>

<p align="center">
   <img src="https://img.shields.io/badge/Language-Python-9cf">
   <img src="https://img.shields.io/badge/FastAPI-0.95.1-brightgreen">
   <img src="https://img.shields.io/badge/SQLAlchemy-2.0-orange">
   <img src="https://img.shields.io/badge/Pytest-7.3.0-informational">
   <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

## About ✨

#### PhotoShare 
PhotoShare is a web application that allows users to create an account, upload posts with photos, use hashtags, leave comments, and rate posts. The application is built using the FastAPI framework and uses SQLAlchemy as the database ORM.

## Deployment
- [Live PhotoShare](https://photoshare-ortursucceeh.koyeb.app/docs)

## Documentation 📗
 - [Documentation link](https://ortursucceeh.github.io/Project-PhotoShare/)


## Installation 💻
To run this project, follow these steps:

1. Clone this repository to your local machine;
2. Install the required packages by running ```pip install -r requirements.txt```
3. Set the required environment variables;
4. Start the server by running ```uvicorn main:app --reload```


## Usage 💠
This project exposes 40+ endpoints through a REST API. To access these APIs, use any API client, such as Postman or cURL. The API documentation can be found at [documentation](https://ortursucceeh.github.io/Project-PhotoShare/).


## Developers :octocat:

<div align="">
  <a href="https://github.com/ortursucceeh">ortursucceeh</a><br>
  <a href="https://github.com/Vasyl-Hlushchenko">Vasyl-Hlushchenko</a><br>
  <a href="https://github.com/Maria-hub746">Maria-hub746</a><br>
  <a href="https://github.com/Sunriseuk">Sunriseuk</a><br>
  <a href="https://github.com/AlexanderF048">AlexanderF048</a><br>
  <a href="https://github.com/Serhii-Kravchenko-2022">Serhii-Kravchenko-2022</a><br>
</div>


## License 🔱
Project "PhotoShare" is distributed under the MIT license.
