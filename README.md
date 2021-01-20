# diagnosis_code_api
Backend Take Home Challenge. This project contains RESTful APIS that allows you to utilize an internationally recognized set of diagnosis codes. The APIs allow you to:
* Create a new diagnosis code record 
```/api/v1/codes/  POST REQUEST```

``` 
SAMPLE PAYLOAD
{
    "id": "A0229",
    "category_code": "A022",
    "diagnosis_code": "9",
    "short_description": "infection",
    "full_description": "Salmonella with other localized infection",
    "category_title": "Localized salmonella infections",
    "code_type": "icd-10"
}
```
* Edit an existing diagnosis code record
```/api/v1/codes  PUT REQUEST```
* List diagnosis codes in batches of 20(and paginate through the rest of the record)
```/api/v1/codes/  GET REQUEST```
```/api/v1/codes?page=1  GET REQUEST```
```/api/v1/codes?page=2  GET REQUEST```
* Retrieve diagnosis codes by ID
```/api/v1/codes/:ID  GET REQUEST```
* Delete diagnosis code by ID
```/api/v1/codes/:ID  Delete REQUEST```

## Fun Fact
* All API endpoints respond within 100ms
* Project includes unit tests for all api endpoints

## Technologies
* Python 3.7
* Django 3
* Django REST FRAMEWORK
* PostgreSQL
* Docker

### Setup
## Installation on Windows, Linux and Mac OS

* [Follow the guide here](https://help.github.com/articles/fork-a-repo) on how to clone or fork a repo

* [Follow the guide here](https://docs.docker.com/docker-for-windows/install/) on how to set up Docker for windows
* [Follow the guide here](https://docs.docker.com/engine/install/ubuntu/) on how to set up Docker for Linux
* [Follow the guide here](https://docs.docker.com/docker-for-mac/install/#:~:text=Install%20and%20run%20Docker%20Desktop,Applications%20folder%20to%20start%20Docker.) on how to set up Docker for Mac OS

* Run project using Docker in simple steps

  ```
  docker-compose up -d --build (Build project docker image and run container)
  
  docker-compose exec web python3 manage.py makemigrations (Make model migrations)
  
  docker-compose exec web python3 manage.py migrate (Migrate models to database)
  
  docker-compose exec web python3 manage.py loaddata diagnosis_codes.json (Load initial fixtures of 4678 diagnosis code records)
  
  docker-compose exec web python3 manage.py test (Run Unit Tests on API Endpoints)
  
  ```
* You can now visit the Browsable API page at http://127.0.0.1:8000/api/v1/codes/
