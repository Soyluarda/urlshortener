# UrlShortener - Challange Project

- ## Installation
- create a directory and clone projects in it.
    - create a virtual environment and activate it.
        ```
        - virtualenv -p python3 venv
        - source venv/bin/activate
        ```
    - and after all the changes in models.py files you should run the following commands:
       ```
        pip3 install -r requirements.txt
        python3 manage.py migrate
        python3 manage.py runserver
       ```
    
- To run in the localhost:
    ```
    python3 manage.py runserver
    ```
- ## API
    - send GET request To list all the urls:
        - `urls/`
    - send POST request To create a new short-link:
        - `urls/`
          - send  parameter as 'url'
    - send GET request To redirect url:
        - `<shortcode>/`

### Notes
- `black` and `isort` are used for linting.
- Tests for services and all available endpoints are written.
- Database diagram graph & test coverage rate files added extras directory.
