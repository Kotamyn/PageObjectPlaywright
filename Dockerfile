
FROM --platform=linux/amd64 python:3.11-slim

WORKDIR /page_object_playwright/

ENV PATH=$PATH:/page_object_playwright/.local/bin

COPY . /page_object_playwright/

RUN apt-get update \
    && apt-get -y install libnss3 libatk-bridge2.0-0 libdrm-dev libxkbcommon-dev libgbm-dev libasound-dev libatspi2.0-0 libxshmfence-dev \
   # && apt-get install -y wget && apt-get install -y unzip \
    && pip install --upgrade pip 

# Install allurectl
# ENV ALLURECTL_VERSION=2.15.1
# RUN wget https://github.com/allure-framework/allurectl/releases/download/${ALLURECTL_VERSION}/allurectl_linux_386 -O /usr/bin/allurectl  \  
#    && chmod +x /usr/bin/allurectl \
#    && /usr/bin/allurectl -v

# Install allure
# ENV ALLURE_VERSION=2.24.1
# RUN apt-get install -y default-jre \
#    && wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.zip \ 
#    && mkdir /opt/allure \
#    && unzip allure-commandline-${ALLURE_VERSION}.zip -d /opt/allure \
#    && export PATH=$PATH:/opt/allure/allure-${ALLURE_VERSION}/bin

#ENV PATH=$PATH:/opt/allure/allure-${ALLURE_VERSION}/bin

RUN pip install poetry \ 
    && poetry init \ 
    && cat requirements.txt | xargs poetry add \
    && poetry run playwright install \
    && poetry run playwright install-deps 

CMD [ "poetry", "run", "pytest" ]
