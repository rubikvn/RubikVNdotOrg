import configparser

class ServerConfig():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('./RubikVNdotOrg/lib/config/rubikvn.cnf')

        # Django secret key
        self.key = config['Secret']['key']

        # Database credentials
        self.db_uname = config['Database']['mysql_username']
        self.db_password = config['Database']['mysql_password']

        # OAuth2 application information
        self.oauth_client_id = config['OAuth2']['client_id']
        self.oauth_client_secret = config['OAuth2']['client_secret']
        self.oauth_callback_uri = config['OAuth2']['callback_uri']
        self.oauth_default_scope = config['OAuth2']['default_scope']
        self.oauth_base_url_authorize = config['OAuth2']['base_url_authorize']
        self.oauth_base_url_fetch_token = config['OAuth2']['base_url_fetch_token']
        self.oauth_base_url_api = config['OAuth2']['base_url_api']
