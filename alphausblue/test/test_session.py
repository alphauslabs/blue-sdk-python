from os import environ, getenv

from alphausblue.connection.session import Session

class TestSession:

    def test_all_values_empty_defaults_used(self):

        # First, set up the environment variables we want to use for testing
        environ["ALPHAUS_CLIENT_ID"] = "test-client-id"
        environ["ALPHAUS_CLIENT_SECRET"] = "test-client-secret"
        environ["ALPHAUS_USERNAME"] = "test-username"
        environ["ALPHAUS_PASSWORD"] = "test-password"
        environ["ALPHAUS_AUTH_URL"] = "https://test.test"

        # Next, create the session
        sess = Session()

        # Finally, verify the fields on the session
        assert sess.ClientId == "test-client-id"
        assert sess.ClientSecret == "test-client-secret"
        assert sess.GrantType == "password"
        assert sess.LoginUrl == "https://test.test"
        assert sess.Username == "test-username"
        assert sess.Password == "test-password"
        assert sess.Scope == "openid"
    
    def test_all_values_empty_auth_url_missing_ripple_used(self):
        
        # First, set up the environment variables we want to use for testing
        environ["ALPHAUS_CLIENT_ID"] = "test-client-id"
        environ["ALPHAUS_CLIENT_SECRET"] = "test-client-secret"
        environ["ALPHAUS_USERNAME"] = "test-username"
        environ["ALPHAUS_PASSWORD"] = "test-password"
        delete_if_exists("ALPHAUS_AUTH_URL")
        
        # Next, create the session
        sess = Session()

        # Finally, verify the fields on the session
        assert sess.ClientId == "test-client-id"
        assert sess.ClientSecret == "test-client-secret"
        assert sess.GrantType == "password"
        assert sess.LoginUrl == "https://login.alphaus.cloud/ripple/access_token"
        assert sess.Username == "test-username"
        assert sess.Password == "test-password"
        assert sess.Scope == "openid"
    
    def test_all_values_empty_alphaus_creds_missing_ripple_used(self):
        
        # First, set up the environment variables we want to use for testing
        delete_if_exists("ALPHAUS_CLIENT_ID")
        delete_if_exists("ALPHAUS_CLIENT_SECRET")
        environ["ALPHAUS_USERNAME"] = "test-username"
        environ["ALPHAUS_PASSWORD"] = "test-password"
        environ["ALPHAUS_RIPPLE_CLIENT_ID"] = "test-ripple-client-id"
        environ["ALPHAUS_RIPPLE_CLIENT_SECRET"] = "test-ripple-client-secret"
        environ["ALPHAUS_RIPPLE_USERNAME"] = "test-ripple-username"
        environ["ALPHAUS_RIPPLE_PASSWORD"] = "test-ripple-password"
        environ["ALPHAUS_AUTH_URL"] = "https://test.test"
        
        # Next, create the session
        sess = Session()

        # Finally, verify the fields on the session
        assert sess.ClientId == "test-ripple-client-id"
        assert sess.ClientSecret == "test-ripple-client-secret"
        assert sess.GrantType == "password"
        assert sess.LoginUrl == "https://login.alphaus.cloud/ripple/access_token"
        assert sess.Username == "test-ripple-username"
        assert sess.Password == "test-ripple-password"
        assert sess.Scope == "openid"

    def test_all_values_empty_alphaus_and_ripple_creds_missing_wave_used(self):
        
        # First, set up the environment variables we want to use for testing
        delete_if_exists("ALPHAUS_CLIENT_ID")
        delete_if_exists("ALPHAUS_CLIENT_SECRET")
        environ["ALPHAUS_USERNAME"] = "test-username"
        environ["ALPHAUS_PASSWORD"] = "test-password"
        environ["ALPHAUS_RIPPLE_USERNAME"] = "test-ripple-username"
        environ["ALPHAUS_RIPPLE_PASSWORD"] = "test-ripple-password"
        delete_if_exists("ALPHAUS_RIPPLE_CLIENT_ID")
        delete_if_exists("ALPHAUS_RIPPLE_CLIENT_SECRET")
        environ["ALPHAUS_WAVE_CLIENT_ID"] = "test-wave-client-id"
        environ["ALPHAUS_WAVE_CLIENT_SECRET"] = "test-wave-client-secret"
        environ["ALPHAUS_WAVE_USERNAME"] = "test-wave-username"
        environ["ALPHAUS_WAVE_PASSWORD"] = "test-wave-password"
        environ["ALPHAUS_AUTH_URL"] = "https://test.test"

        # Next, create the session
        sess = Session()

        # Finally, verify the fields on the session
        assert sess.ClientId == "test-wave-client-id"
        assert sess.ClientSecret == "test-wave-client-secret"
        assert sess.GrantType == "password"
        assert sess.LoginUrl == "https://login.alphaus.cloud/access_token"
        assert sess.Username == "test-wave-username"
        assert sess.Password == "test-wave-password"
        assert sess.Scope == "openid"
    
    def test_all_values_empty_username_and_password_missing_client_credentials(self):
        
        # First, set up the environment variables we want to use for testing
        environ["ALPHAUS_CLIENT_ID"] = "test-client-id"
        environ["ALPHAUS_CLIENT_SECRET"] = "test-client-secret"
        delete_if_exists("ALPHAUS_USERNAME")
        delete_if_exists("ALPHAUS_PASSWORD")
        delete_if_exists("ALPHAUS_AUTH_URL")
        
        # Next, create the session
        sess = Session()

        # Finally, verify the fields on the session
        assert sess.ClientId == "test-client-id"
        assert sess.ClientSecret == "test-client-secret"
        assert sess.GrantType == "client_credentials"
        assert sess.LoginUrl == "https://login.alphaus.cloud/ripple/access_token"
        assert sess.Username == None
        assert sess.Password == None
        assert sess.Scope == "openid"
    
    def test_all_values_provided_populated(self):

        # First, create the session with values provided
        sess = Session(
            client_id = "test-func-client-id",
            client_secret = "test-func-client-secret",
            grant_type = "grant",
            scope = "jwt",
            username = "test-func-username",
            password = "test-func-password",
            login_url = "https://test.func.test")
            
        # Finally, verify the fields on the session
        assert sess.ClientId == "test-func-client-id"
        assert sess.ClientSecret == "test-func-client-secret"
        assert sess.GrantType == "grant"
        assert sess.LoginUrl == "https://test.func.test"
        assert sess.Username == "test-func-username"
        assert sess.Password == "test-func-password"
        assert sess.Scope == "jwt"
    
    def test_access_token_works(self):

        # First, get the client ID and secret from the Ripple tester environment variables
        # If the variables could not be found then print a message and exit
        client_id = getenv("RIPPLE_TESTER_CLIENT_ID_PROD")
        client_secret = getenv("RIPPLE_TESTER_CLIENT_SECRET_PROD")
        if not (client_id and client_secret):
            print("Client ID and secret not found, exiting")
            return

        # Next, create the session from the client ID and secret
        sess = Session(
            client_id = client_id,
            client_secret = client_secret)
        
        # Finally, attempt to get an access token; this should not fail
        token = sess.access_token()
        print("Token {0}: ".format(token))

def delete_if_exists(key):
    if key in environ:
        del environ[key]