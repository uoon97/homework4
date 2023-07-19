# homework4

![example workflow](https://github.com/uoon97/homework4/actions/workflows/test_service.yml/badge.svg?branch=master)

## Build Images
- Service_1: docker build -t pre-homework:0.0 -f Dockerfile.service_1 ./  
- Service_2: docker build -t post-homework:0.0 -f Dockerfile.service_2 ./

## Run Container
- Service_1: docker run -it --name prehw_0.0 -v .../hw4/model:/model pre-homework:0.0
- Service_2: docker run -it --name posthw_0.0 -v .../hw4/model:/model -p 80:80 post-homework:0.0


## Example
- after fork,
- git add & commit
- http://localhost:5001
