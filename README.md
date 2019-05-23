# Klondike-XP

## REQUIREMENTS
* Python3
* Modules:
    * Pytest
    * The src/ subdirectory

### How to install requirements on Ubuntu?
(copy & paste on your terminal)
```
sudo apt install python3 python3-pip
git clone https://github.com/BlackCorsair/klodike-XP.git && cd klodike-XP
pip install -e src/.
pip install -r requirements.txt
```

### How to run the tests?

For a single test suite:
```
pytest tests/ts_<name>.py
```

To run all tests:
```
pytest tests/*
```
