# Comments log

1.

Melnichuk Vladislav | ML-21 | Technopark | BMSTU
================================================

Homework2

Способ запуска проекта описан в "README.md"

Основная часть:

- [x] Оберните inference вашей модели в rest сервис на FastAPI, должен быть endpoint /predict (3 балла) **done**

- [x] Напишите endpoint /health, который должен возращать 200, если ваша модель готова к работе (такой чек особенно актуален, если делаете доп задание про скачивание из хранилища) (1 балл) **done**

- [x] Напишите unit тест для /predict (3 балла) **tests are test_main.py.**

- [x] Напишите скрипт, который будет делать запросы к вашему сервису (2 балла) **script is requests/make_online_request.py.**

- [x] Напишите Dockerfile, соберите на его основе образ и запустите локально контейнер (docker build, docker run). Внутри контейнера должен запускаться сервис, написанный в предыдущем пункте. Закоммитьте его, напишите в README.md корректную команду сборки (4 балла) **Dockerfile is realized, read README.md for more info and how to sturt docker image**

- [x] Опубликуйте образ в <https://hub.docker.com/>, используя docker push (вам потребуется зарегистрироваться) (2 балла) **Several versions of docker images were published (hub.docker.com), read README.md for more info**

- [x] Опишите в README.md корректные команды docker pull/run, которые должны привести к тому, что локально поднимется на inference ваша модель. Убедитесь, что вы можете протыкать его скриптом из пункта 3 (1 балл) **done**

- [x] Проведите самооценку - распишите в реквесте какие пункты выполнили и на сколько баллов, укажите общую сумму баллов (1 балл) **done**

Дополнительная часть:

- [x] Ваш сервис скачивает модель из S3 или любого другого хранилища при старте, путь для скачивания передается через переменные окружения (+2 доп балла) **Service download the model from Google Drive Storage (Disk) at startup, the path is passed through environment variables.**

- [x] Оптимизируйте размер docker image. (+2 доп балла) **Several tricks for docker optimization can be found in README.md in chapter: Optimization**

- [x] Сделайте валидацию входных данных (+2 доп балла). **Input data is validated, description in data_structure.py.**
