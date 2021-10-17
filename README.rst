**API_Yatube**
=====


Добро пожаловать в проект api_yatube! Это сервис, позволяющий делать HTTP запросы к базе данных сервиса блогов "Yatube" через интерфейс REST API.
Реализована возможность создавать, изменять, просматривать записи и комментарии к ним разных авторов, а так же подписываться на авторов и просматривать группы, в которых собраны посты определённой тематики.

**Как запустить проект:**
-----

Клонировать репозиторий и перейти в него в командной строке:

.. code-block:: text

 git clone https://github.com/RWSNTi/api_final_yatube.git

Перейти в созданный репозиторий:

.. code-block:: text

 cd api_final_yatube

Cоздать и активировать виртуальное окружение:

.. code-block:: text

 python -m venv venv
 source venv/scripts/activate

Обновить установщик расширений pip

.. code-block:: text

 python -m pip install --upgrade pip

Установить зависимости из файла requirements.txt:

.. code-block:: text

 pip install -r requirements.txt
 
Выполнить миграции и собрать файлы статики:

.. code-block:: text

 python manage.py migrate
 python manage.py collectstatic

Запустить проект:

.. code-block:: text

 python manage.py runserver

**Документация с примерами запросов и ответов будет доступна после развёртывания и запуска проекта по ссылке http://127.0.0.1:8000/redoc**
