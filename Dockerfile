#FROM python:3.6
FROM registry.cn-shanghai.aliyuncs.com/wayneqll/cifar-service-parent
MAINTAINER Wayne Cao <wayne911@live.cn>

COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONPATH=$PYTHONPATH:/app/src

EXPOSE 5000

ENTRYPOINT ["gunicorn", "--config", "/app/rsc/gunicorn.conf", "app:app"]