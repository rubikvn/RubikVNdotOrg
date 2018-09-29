# RubikVN.org

Source code for https://rubikvietnam.org/

### Getting involved

Shoot me an email at <vttrung12@gmail.com> and tell me which part of the project you'd be interested in. Or simply clone this repo, make some changes, create a pull request. If approved, you are automatically part of the team.

For a temporary alternative to Project Wiki, check `docs/developer_guide.md`

### Current progress

* Website is up and running!
* You can now view rankings of Vietnamese speedcubers for all categories
* We need tremendous help to improve our front-end

### Cloning the repo & running the server (first time)

0. Before cloning the repository, installing and starting the development process, please make sure you have these few things installed on your computer (I personally prefer developing on a \*NIX environment):
  - **[Python 3.6:](https://www.python.org/downloads/)** Python version >= 3.6 is required to run the project, on Ubuntu 18.04, it is the default version when you use `python3`. For other operating systems or distributions however, you may need to specifically write `python3.6`.

  - **[MySQL:](https://www.mysql.com/downloads/)** Download and install MySQL before hand, and create a user `rubikvn01` (or whatever you choose, but you might have to edit the config file).

  - **[Git:](https://git-scm.com/)** We're using git for version control, so basic understanding of version control, git and github is required.

Those 3 things are essential for running the website, so make sure you have all of them ready before following the next steps.

1. Clone the repository:
```bash
git clone https://gitlab.com/rubikvn/rubikvn.git
```
OR use SSH
```bash
git clone git@gitlab.com:rubikvn/rubikvn.git
```

2. Run installation script to have the database set up and project requirements downloaded for you
```bash
cd rubikvn/
chmod 755 install.sh
./install.sh
```

3. Activate virtual environment
```bash
source rbvn-env/bin/activate
```
After that your terminal prompt will look like this:
```bash
(rbvn-env)
```

4. Run the server (on your localhost). Ctrl-C to stop the server
```bash
(rbvn-env) python3 manage.py runserver
```

5. Terminate virtualenv
```bash
(rbvn-env) deactivate
```
