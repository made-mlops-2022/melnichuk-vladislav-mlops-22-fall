# Comments log

1.

Melnichuk Vladislav | ML-21 | Technopark | BMSTU
================================================

MLOps | HW3

Способ запуска проекта описан в "README.md"

**[Screenshots of working AirFlow](https://github.com/made-mlops-2022/melnichuk-vladislav-mlops-22-fall/blob/homework3/airflow_ml_dags/screenshots/)**

![photo](https://github.com/made-mlops-2022/melnichuk-vladislav-mlops-22-fall/blob/homework3/airflow_ml_dags/screenshots/airflow_compilation.jpg)

**Основная часть:**

- [x] Поднимите airflow локально, используя docker compose. **done**

- [x] Реализуйте dag, который генерирует данные для обучения модели  (5 баллов) **done**

- [x] Реализуйте dag, который обучает модель еженедельно, используя данные за текущий день. (10 баллов) **done**

- [x] Реализуйте dag, который использует модель ежедневно (5 баллов) **done**

- [x] все даги реализованы только с помощью DockerOperator  (10 баллов) **done**

- [x] Традиционно, самооценка (1 балл) **done**

**Дополнительная часть**:

- [ ] Реализуйте сенсоры на то, что данные готовы для дагов тренировки и обучения (+3 доп балла)

- [ ] Протестируйте ваши даги <https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html> (+5 доп баллов)

- [ ] В `docker compose` так же настройте поднятие `mlflow` и запишите туда параметры обучения, метрики и артефакт (модель) (+5 доп баллов)

- [ ] Вместо пути в airflow variables используйте API Mlflow Model Registry. Даг для инференса должен подхватывать последнюю продакшен модель (+5 доп баллов)

- [ ] Настройте alert в случае падения дага <https://www.astronomer.io/guides/error-notifications-in-airflow> (+3 доп балла)

****Итого (самооценка): 31 балл**
