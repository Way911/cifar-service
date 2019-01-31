

GIT_SHA=`git rev-parse --short HEAD || echo "GitNotFound"`
TIME=`date +%Y%m%d%H%M%S`
IMAGE_TAG=$TIME-$GIT_SHA
echo $IMAGE_TAG

sudo docker build . -t registry-xxx.com/abc/cifar-service:$IMAGE_TAG

sudo docker login -u <username> -p <password> <registry-xxx.com>

sudo docker push registry-xxx.com/abc/cifar-service:$IMAGE_TAG

sudo docker tag registry-xxx.com/abc/cifar-service:$IMAGE_TAG \
                registry-xxx.com/abc/cifar-service
sudo docker push registry-xxx.com/abc/cifar-service

# webhook to tell aliyun container service to deploy the latest image
curl 'https://cs.console.aliyun.com/hook/trigger?triggerUrl=xxx==&secret=xxx'