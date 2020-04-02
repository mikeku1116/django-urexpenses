# django-urexpenses #

## 專案介紹 ##

本專案UrExpenses是一個記帳網站，透過Django ModelForm來進行開發，具有基本的CRUD(Create-Read-Update-delete)功能，可以搭配[[Django教學7]透過Django ModelForm快速開發CRUD應用程式教學](https://www.learncodewithmike.com/2020/03/django-modelform.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

有了pipenv套件管理工具後，就可以執行以下指令，來安裝專案所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，並且啟動本地端伺服器：

`$ pipenv shell`

`$ python manage.py runserver`

## 執行畫面 ##

開啟瀏覽器，在本地端伺服器的網址後面加上 /expenses (例：http://127.0.0.1:8000/expenses/) 後，即可看到首頁畫面。

![Alt text](https://1.bp.blogspot.com/-SOg8L7Gtlwc/XoB7GRMS7pI/AAAAAAAABr8/Srgy1kxmhhANha9chc78Ii7Y7euDWm5ZQCKgBGAsYHg/s1600/UrExpenses.PNG "Optional title")