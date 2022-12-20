Melnichuk Vladislav | ML-21 | Technopark | BMSTU
================================================

**Homework №4 | Kubernetes "Production ready" project to solve the problem of heart disease classification**

# Setup

~~~
# setup virtual environment
python -m venv .venv
source .venv/bin/activate
cd kubernetes

pip install -r requirements.txt
~~~

# Start and run

~~~
# Start Cluster
# minikube start
kubectl get po -A
kubectl cluster-info

# Deploy manifests
kubectl apply -f online-inference-pod.yaml
# kubectl apply -f <MANIFEST_NAME>.yaml

kubectl apply -f online-inference-deployment-blue-green.yaml
kubectl apply -f online-inference-deployment-rolling-update.yaml
kubectl apply -f online-inference-pod.yaml
kubectl apply -f online-inference-pod-probes.yaml
kubectl apply -f online-inference-pod-resources.yaml
kubectl apply -f online-inference-replicaset.yaml


# Checking pod status
kubectl get pods

kubectl get pods --watch

# Configuring ports
kubectl port-forward pods/online-inference 12000:12000

# Show visualization
minikube dashboard
~~~

# Stop and uninstall
~~~
# stop kuberctl

cd ..

# uninstall virtual environment (part)
deactivate
rm -r .venv

# uninstall virtual environment (full)
deactivate
rm -r .venv | rm -r outputs | rm -r .ipynb_checkpoints
~~~

# Solution

Kubernetes запускается, как часть функционала Docker Desktop for Windows (Windows10 + WSL2 + Ubuntu20.04 + VS Code (extension: Kubernetes Kind). Скриншоты можно найти в папке screenshots. Kubernetes поднимается локально на 80 порту (<http://localhost:80>).

# Answers to homework questions

3. Пропишите Requests / Limits и напишите, зачем это нужно в описании PR:

Requests / Limits нужны для управления ресурсами. Ресурсы тратятся на то, что нужно и не тратятся на то, что не нужно.
Requests / Limits - это минимальные / максимальные требования к ресурсам для контейнера.

4. Добавьте Liveness и Readiness пробы и посмотрите, что будет происходить. Напишите в описании -- чего вы этим добились:

READY (состояние) показывается только после задержки. Через минуту приложение перезапускается: закрывается и запускается заново. И все по кругу заново идет.

5. Ответьте на вопрос, что будет, если сменить docker образ в манифесте и одновременно с этим: уменьшить / увеличить число реплик. Поды с какими версиями образа будут внутри кластера?

При уменьшении числа реплик просто удаляется часть реплик. Версия реплик не меняется. При увеличении числа реплик просто добавляются новые реплики из другой версии образа. Версии предыдущих реплик не меняется.

6. Опишите [Deployment] для вашего приложения:

a) Существует момент времени, когда на кластере существуют и все старые поды и все новые:

Настройки в этом случае должны быть следующими: maxSurge = 3, maxUnavailable = 0. Сначала запускаются новые Pod'ы. После этого закрываются старые. Поэтому существует короткий временной отрезок, когда запущены и новые и старые Pod'ы.

б) Одновременно с поднятием новых версий, гасятся старые:

Настройки в этом случае должны быть следующими: maxSurge = 1, maxUnavailable = 0.
Одновременно запускаются и новые и старые Pod'ы.

# Self-review

- [x] 1. Разверните Kubernetes (5 баллов). **done**

- [x] 2. Напишите простой Pod manifest для вашего приложения, назовите его online-inference-pod.yaml. Приложите скриншот, где видно, что все поднялось (4 балла). **done**

- [x] Пропишите Requests / Limits и напишите, зачем это нужно в описании PR. Закоммитьте файл online-inference-pod-resources.yaml (2 балла). **done**

- [x] Модифицируйте свое приложение так, чтобы оно стартовало не сразу (с задержкой 20-30 секунд) и падало спустя минуту работы (3 балла). **done**

- [x] Сделайте 3 реплики вашего приложения (3 балла). **done**

- [x] Опишите [Deployment] для вашего приложения (3 балла). **done**

**Result**: 20 баллов
