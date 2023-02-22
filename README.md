# SPA - app: comments

Django online service for comments. You can leave as many comments as you like and also comment on other comments.

## Check it out!

[Project deployed to Render](https://app-comment.onrender.com/)


## Installation

Python3 must be already installed

```shell
git clone https://github.com/hikehikehike/spa_app_comment/
python3 -m venv venv
sourse venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Installation with Docker hub

Docker must be already installed

```shell
docker pull hikehikehike/comment
docker run -p 8001:8000 hikehikehike/comment
```