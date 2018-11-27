# RubikVN.org

Source code for https://rubikvietnam.org/

### Getting involved

Shoot me an email at <vttrung12@gmail.com> and tell me which part of the project you'd be interested in. Or simply clone this repo, make some changes, create a pull request. If approved, you will be invited to the team.

### Current progress

* The website is temporarily unavailable for front-end remake and further development of our back-end. Any progress will be announced on this repository.
  * At the moment, our main focus is to design a user-friendly front-end.

#### Implemented functions
* Ranking display of speedcubers from Vietnam for all categories.
* Login system via OAuth integration with WCA website.
* TravisCI has been set up for this repository, which means we need more testing!

### Cloning the repo & running the server (first time)

0. Before cloning the repository, installing and starting the development process, please make sure you have these few things installed on your computer (I personally prefer developing on a \*NIX environment):
  - **[Python 3.6:](https://www.python.org/downloads/)** Python version >= 3.6 is required to run the project, on Ubuntu 18.04, it is the default version when you use `python3`. For other operating systems or distributions however, you may need to specifically write `python3.6`.

  - **[MySQL:](https://www.mysql.com/downloads/)** *Disclaimer: Version 5.7 is used for production. Latest versions of MySQL may or may not work*. Download and install MySQL before hand, and create a user `rubikvn01` (or whatever you choose, but you might have to edit the config file). *NOTE: If you think this is too inconvenient, file an issue so that I know to make changes to accessing the database*

  - **[Git:](https://git-scm.com/)** We're using git for version control, so basic understanding of version control, git and github is required.

Those 3 things are essential for running the website, so make sure you have all of them ready before following the next steps.

1. Clone the repository:
```bash
git clone https://github.com/RubikVN/RubikVNdotOrg.git
```

2. Run installation script to have the database set up and project requirements downloaded for you. *NOTE: The installation script tends to be erroneous, so please file an issue on this repository if you spot a bug*
```bash
cd rubikvn/
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
