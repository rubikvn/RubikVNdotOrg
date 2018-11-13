import configparser

class ServerConfig():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('./RubikVNdotOrg/lib/config/rubikvn.cnf')

        self.key = config['Secret']['key']
        self.db_uname = config['Database']['mysql_username']
        self.db_password = config['Database']['mysql_password']

        self.oauth_client_id = config['OAuth2']['client_id']
        self.oauth_client_secret = config['OAuth2']['client_secret']
        self.oauth_callback_uri = config['OAuth2']['callback_uri']
