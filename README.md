# cifar-service
To run it:
```shell
bash run.sh
```
To build image & run container
```bash
docker build . -t image-name
docker run -d \ 
           -p 80:5000 \ 
           –restart=always \
           –name container-name image-name
```