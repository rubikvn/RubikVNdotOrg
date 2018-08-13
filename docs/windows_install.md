# Windows installation... Where to begin?

My experience developing on Windows without an IDE in the last few days has not been very pleasant.. So I have decided to stop wasting my time writing a batch script that could help automate the installation process, windows has discouraged me to. Thanks Bill Gates.

### Getting started

1. Before you can clone this project to your local computer, you need [Git:](https://git-scm.com/). Download and installation is easy, just go to their download page, choose a version that is compatible with your machine specs, and follow all the steps to install Git. NOTE: It is recommended that you choose Visual Studio Code as a default editor instead of Vim. And for the `Adjusting your PATH environment` options, choose `Use Git from the Windows Command Prompt`. You can go with default option for other settings.

2. Now you have Git. The next big thing you need to run the project is a programming language, namely Python. Go to [Python 3.6:](https://www.python.org/downloads/), which is their download page, get the installer and run it. Don't forget to set the path to python directory to your PATH environment variable. There's a setting option that helps you do that, don't skip it.

3. [MySQL:](https://www.mysql.com/downloads/). It took me quite a lot of time to get this thing up and running for the project. Go to the linked page, choose Windows in their download menu, click on `MySQL Installer` > `Looking for previous GA versions?` > **Choose `5.7.23`**. I highly emphasize on this because the newer version gave me buncha troubles when I run Django web server. You should choose to install the developer package, which basically includes everything we need for our project. Just click on `execute` or `next` when you see those buttons available. Leave the settings as is, choose the root password for MySQL server to be `admin`. And you're good to go.

Don't forget to set those three programs' bin folder to your PATH environment variable, so that you can use them via the command prompt, which is a crucial part of the project. Also, during installation, you might need to close command prompt and open it again, for some programs to take effect.

### Can I start developing now that I have those 3 things mentioned ready?

Nah. You still need to manually install some other stuffs, run a few scripts, to really get the back end to work. Sorry, but you chose to use Windows as your development environment, and ya it's annoying as fuck.

Sooo, this part assumes that you have Git, Python and MySQL on your computer, and you are able to use those 3 programs from your command prompt. That is, type in `git`, `python`, and `mysql` and a help message actually appears on your screen instead of an error saying that those 3 are not valid programs. Got it? Let's move along to the following steps:

1. First thing first, go to a folder where you would like to keep the `rubikvn` repository on your computer, open command prompt in that folder, and type:

```bash
git clone https://gitlab.com/rubikvn/rubikvn.git
```

You will be prompted to login using your Gitlab credentials, just enter your Gitlab username and password.

2. You don't have to install pip, which is good because it comes with the python installation. What you need to do is to install and set up a virtual environment for development. Enter the following:

```bash
pip install virtualenv
virtualenv rbvn-env
rbvn-env\Scripts\activate # NOTE: If you close your command prompt at any step from now on, you need to activate this script again.
pip install lib\mysqlclient-1.3.13-cp36-cp36m-win_amd64.whl
pip install Django==2.0.7
```

And finally, `pip freeze` to make sure 2 (or 3) python packages are installed in your virtual environment. This should be the output:

```bash
Django==2.0.7
pytz==2018.5
mysqlclient==1.3.13
```

3. Almost there! This step is quite simple yet may take a while because you need the internet, and a lot of MySQL scripts for that. First do:

```
mysql -u root -p
```

You will be prompted for your root account password. I hope it's `admin`, for simplicity. When you are in your mysql shell, do the followings:

```mysql
CREATE DATABASE IF NOT EXISTS wca;
CREATE DATABASE IF NOT EXISTS rubikvn;
SET @@global.sql_mode= 'NO_ENGINE_SUBSTITUTION';
quit
```

Okido, now you need to sync your database schema with Django. Enter these in your normal command prompt

```bash
python manage.py makemigrations
python manage.py migrate
```

Almost there™

Go to https://www.worldcubeassociation.org/results/misc/WCA_export.sql.zip, get the zip file, extract somewhere, move the WCA_export.sql file to the rubikvn folder, and enter:

```bash
mysql -u root --password=YOUR_PASSWORD_HERE wca < WCA_export.sql
mysql -u root --password=YOUR_PASSWORD_HERE < RubikVNdotOrg\db\vn_db_export.sql
```

Remove the unnecessary WCA_export.sql file, folder as well as the README file.

4. Actually run the server

```bash
python manage.py runserver
```

If you see no error message, it means the project is actually working. Congrats!!! Now you can start developing.

5. Finish development

```bash
deactivate
```

To exit virtual environment, or simply close the command prompt.

There will be a guide on how you should use Git for this project, it's really helpful besides just doing `git clone`. So stay tuned, or go watch a Youtube tutorial because they explain better than I do.
