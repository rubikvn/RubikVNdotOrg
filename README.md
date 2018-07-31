# RubikVN.org

Source code for the soon-to-be new rubikvn.org, written in python3.6

## Under development

### Cloning the repo & running the server

1. Clone the repository:
```bash
git clone https://gitlab.com/rubikvn/rubikvn.git
```
OR
```bash
git clone git@gitlab.com:rubikvn/rubikvn.git
```

2. Install and set up `virtualenv`
```bash
sudo python3 -m pip install virtualenv
virtualenv rbvn-env
source rbvn-env/bin/activate
```

3. Change directory to `rubikvn/`
```bash
(rbvn-env) cd rubikvn/
```

4. Install the dependencies
```bash
(rbvn-env) python3 -m pip install -r requirements.txt
```

5. Run the server (on your localhost), Ctrl-C to stop the server
```bash
(rbvn-env) python3 manage.py runserver
```

6. Terminate virtualenv
```bash
(rbvn-env) deactivate
```
