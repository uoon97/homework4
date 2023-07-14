# homework4

## Build Images
- Service_1: docker build -t pre-homework:0.0 -f Dockerfile.service_1 ./  
- Service_2: docker build -t post-homework:0.0 -f Dockerfile.service_2 ./

## Run Container
- Service_1: docker run -it --name prehw_0.0 -v .../hw4/model:/model pre-homework:0.0
- Service_2: docker run -it --name posthw_0.0 -v .../hw4/model:/model -p 80:80 pre-homework:0.0
