# Klondike-XP

## REQUIREMENTS
* Python3
* Modules:
    * Pytest
    * The src/ subdirectory

### How to install requirements on Ubuntu?
(copy & paste on your terminal)
```
sudo apt install python3 python3-venv python3-pip
git clone https://github.com/BlackCorsair/klodike-XP.git && cd klodike-XP
# create a virtualenv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 setup.py install
```

### How to run the tests?

For a single test suite:
```
pytest tests/ts_<name>.py
```

To run all tests:
```
pytest tests/*
# or
python3 setup.py test
```
