import configparser

class ServerConfig():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('./RubikVNdotOrg/config/rubikvn.cnf')

        self.key = config['Secret']['key']
        self.db_uname = config['Database']['mysql_username']
        self.db_password = config['Database']['mysql_password']
