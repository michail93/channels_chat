1) Приложение работает на Python 3.6 с использованием django channels, 
соответственно перед установкой зависимостей   (```pip install -r requirements.txt```)  необходимо заранее установить 
python3.6-dev (```sudo apt-get install python3.6-dev```)

2) Сам блог доступен по ```localhost:8000/blog/```

3) Далее запустите, из директории где находится ```manage.py```,  следующую команду ```docker-compose up -d```

4) Запустите ```python manage.py runserver```