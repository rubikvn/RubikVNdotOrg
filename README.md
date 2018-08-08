# RubikVN.org

Source code for the soon-to-be new rubikvn.org, written in python3.6

## Under development

TODO: write scripts for other installation work besides `pip`

### Cloning the repo & running the server

**NOTE: Python version >= 3.6 is required to run the project, on Ubuntu 18.04, it is the default version when you use `python3`. For other operating systems or distributions however, you may need to specifically write `python3.6`**

1. Clone the repository:
```bash
git clone https://gitlab.com/rubikvn/rubikvn.git
```
OR use SSH
```bash
git clone git@gitlab.com:rubikvn/rubikvn.git
```

2. Install and set up `virtualenv`
```bash
cd rubikvn/
sudo python3 -m pip install virtualenv
virtualenv rbvn-env/ -p python3
source rbvn-env/bin/activate
```

3. Install the dependencies
```bash
(rbvn-env) python3 -m pip install -r requirements.txt
```

4. Run the server (on your localhost). Ctrl-C to stop the server
```bash
(rbvn-env) python3 manage.py runserver
```

5. Terminate virtualenv
```bash
(rbvn-env) deactivate
```
