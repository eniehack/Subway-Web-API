init:
    pip install pipenv
    pipenv install -d

test:
    pipenv run py.test tests