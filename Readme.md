## Installation Steps

Download or clone this repository  
Go to the directory

```
git clone https://github.com/Kotamyn/PageObjectPlaywright
cd PageObjectPlaywright
```

Create virtual environment for this project/directory and  Install the requirements     
```
make init
```

Run the tests
```
make tests
```

Run the tests + allure
```bash
make tests_allure or 
sh scripts/start_tests_allure.sh
```

## Docker
Build

Use the Docker command line
```bash
  docker build -t page_object_playwright:1.0 .
  docker run --name autotests page_object_playwright:1.0
```
Build containers
```bash
docker-compose up --build -d
```
