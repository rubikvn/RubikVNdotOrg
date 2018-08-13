# RubikVN.org

Source code for the soon-to-be new rubikvn.org, written in Python3.6

### Getting involved

##### Basic tasks
You need to understand what programming is, what is source code, how to comment, etc. You can learn on the work, since we are also doing the same thing, but don't expect us to teach you everything from the start, there are already plenty tutorials and documentations on the Internet that I'm sure provide more insights than we do. If you want to contribute to a certain part of the project, contact us, see what is required to fulfill the job, start working on it (or if you don't know how to, watch a Youtube tutorial, then come back), submit you work and BOOM, you're a part of the team.

##### Backend
First and foremost, Git, and a familiarity with the command line!!! Secondly, a basic knowledge of Python programming language, especially Python3 is required, as well as object-oriented programming in general. You don't really need to know the framework or database structure, but I would highly appreciate if you do.

##### Frontend
Same thing, Git, and please know how to use a command line. You'll need Html, CSS, Javascript, and [this](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/). I will specify which directory you'll be working on, but a general rule of thumb is any directory that looks like 'static/' or 'templates/'.

##### What even is Django?
Django is the web framework we will be using for the website. Since Python is supposed to be more comprehensible for the newbies, and Django is a very powerful framework to handle some of the features we are thinking of. When you clone the repo, you need to install Django to be able to run the website, but it is already structured like a typical Django project, which looks like this:

```
rubikvn/
    .git/
    docs/
    ranking/
    RubikVNdotOrg/
    scripts/
    .gitignore
    install.sh
    manage.py
    README.md
    requirements.txt
```
The idea here is RubikVNdotOrg consists of all config files for our website. It's like the index page of our back end. The big project will be made of multiple smaller "apps", like `ranking/`, each app directory will have both the back end and front end code in it, but they are put in separate subdirectories, so it is pretty clear where you should put your code. When you clone the directory from gitlab, follow the [instructions](#cloning-the-repo-running-the-server-first-time) below, and don't delete anything.

### Current progress

TODO:

### Cloning the repo & running the server (first time)

0. Before cloning the repository, installing and starting the development process, please make sure you have these few things installed on your computer (I personally prefer developing on a \*NIX environment):
  - **[Python 3.6:](https://www.python.org/downloads/)** Python version >= 3.6 is required to run the project, on Ubuntu 18.04, it is the default version when you use `python3`. For other operating systems or distributions however, you may need to specifically write `python3.6`.

  - **[MySQL:](https://www.mysql.com/downloads/)** Download and install MySQL before hand, with a username `root` and use `admin` as password. Of course, you're free to choose a better password for your own good, but you might need to manually change a few things in our code base after that. I will edit our code so that you can use whatever password you want on your machine, but not now. After MySQL installation, disable admin privilege requirement to run the program, and we're good to go.

  - **[Git:](https://git-scm.com/)** We're using git for version control, so basic understanding of version control, git and gitlab is required.

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
