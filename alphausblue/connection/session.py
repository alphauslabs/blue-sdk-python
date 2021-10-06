from os import getenv
import requests

ALPHAUS_CLIENT_ID = "ALPHAUS_CLIENT_ID"
ALPHAUS_CLIENT_SECRET = "ALPHAUS_CLIENT_SECRET"
ALPHAUS_USERNAME = "ALPHAUS_USERNAME"
ALPHAUS_PASSWORD = "ALPHAUS_PASSWORD"
ALPHAUS_AUTH_URL = "ALPHAUS_AUTH_URL"

ALPHAUS_RIPPLE_CLIENT_ID = "ALPHAUS_RIPPLE_CLIENT_ID"
ALPHAUS_RIPPLE_CLIENT_SECRET = "ALPHAUS_RIPPLE_CLIENT_SECRET"
ALPHAUS_RIPPLE_USERNAME = "ALPHAUS_RIPPLE_USERNAME"
ALPHAUS_RIPPLE_PASSWORD = "ALPHAUS_RIPPLE_PASSWORD"
ALPHAUS_WAVE_CLIENT_ID = "ALPHAUS_WAVE_CLIENT_ID"
ALPHAUS_WAVE_CLIENT_SECRET = "ALPHAUS_WAVE_CLIENT_SECRET"
ALPHAUS_WAVE_USERNAME = "ALPHAUS_WAVE_USERNAME"
ALPHAUS_WAVE_PASSWORD = "ALPHAUS_WAVE_PASSWORD"

LOGIN_URL_RIPPLE = "https://login.alphaus.cloud/ripple/access_token"
LOGIN_URL_WAVE = "https://login.alphaus.cloud/access_token"
LOGIN_URL_RIPPLE_NEXT = "https://loginnext.alphaus.cloud/ripple/access_token"
LOGIN_URL_WAVE_NEXT = "https://loginnext.alphaus.cloud/access_token"

class Session(object):
    """
    Session contains all the functionality necessary to manage connections to the Blue API
    """

    def __init__(self, client_id: str = None, client_secret: str = None, grant_type: str = None, 
        scope: str = None, username: str = None, password: str = None, login_url: str = None):
        """
        Creates a new Session object from the data necessary to connect to the Blue API.
        @param client_id: The ID of the client registered with Blue
        @param client_secret: The secret associated with the client ID, registered with Blue
        @param grant_type: The grant type to associate with the request. If no value is
            provided then the value will be assumed based on the credentials provided:
            - "client_credentials" if no username and password could be found for the
                credentials provided
            - "password" if a username and password could be found
        @param scope: The scope associated with the request. If no value is provided then
            the value "openid" will be assumed
        @param username: The username to authenticate with the Blue API
        @param password: The password associated with the username being authenticated
        @param login_url: The login URL being authenticated against. If the appropriate client
            credentials could be found or were provided, then this value will be used. If no
            credentials were provided, then the value for the URL will be assumed based on the
            note included below. If credentials were provided, but hte URL was not defined then
            its value will be pulled from the ALPHAUS_AUTH_URL environment variable. If this value
            is not defined then the LOGIN_URL_RIPPLE will be used.

        If no value is provided for client_id or client_secret, then various combinations of
        values will be checked, in the following order:
        - ALPHAUS_CLIENT_ID and ALPHAUS_CLIENT_SECRET will be used for the client credentials.
            If the username and password were provided then these will be used. Otherwise, the
            values will be pulled from the ALPHAUS_USERNAME and ALPHAUS_PASSWORD environment variables.
        - ALPHAUS_RIPPLE_CLIENT_ID and ALPHAUS_RIPPLE_CLIENT_SECRET will be used for the client
            credentials. In this case, the username and password will be pulled from the ALPHAUS_RIPPLE_USERNAME
            and ALPHAUS_RIPPLE_PASSWORD environment variables and the login URL will be set to the LOGIN_URL_RIPPLE.
        - ALPHAUS_WAVE_CLIENT_ID and ALPHAUS_WAVE_CLIENT_SECRET will be used for the client credentials.
            In this case, the username and password will be pulled from the ALPHAUS_WAVE_USERNAME
            and ALPHAUS_WAVE_PASSWORD environment variables and the login URL will be set to the LOGIN_URL_WAVE.
        """

        # Helper function that produces either the value provided, or the value associated
        # with the environment variable name if the value was None
        def _get_local_credential_from_env(value: str, env_key: str) -> str:
            return getenv(env_key) if value is None else value
        
        # Helper function that produces either the value provided or the alternative if the
        # value was None
        def _get_local_credential_from_choices(value: str, alternative: str) -> str:
            return alternative if value is None else value
        
        # Helper function that attempts to retrieve the client credentials if they were not set
        def _update_auth_details(client_id_key: str, client_secret_key: str, username_key: str, password_key: str, url: str) -> None:

            # If the client ID and secret are both present then there's nothing to do here so return
            if not (self.ClientId and self.ClientSecret):

                # The client ID and secret were not provided so attempt to retrieve them from the
                # associated environment variables that were provided
                self.ClientId = getenv(client_id_key)
                self.ClientSecret = getenv(client_secret_key)

                # If we found the client credentials then also attempt to get the username and
                # password from the associated environment variables. Also, set the URL
                if self.ClientId and self.ClientSecret:
                    self.Username = getenv(username_key)
                    self.Password = getenv(password_key)
                    self.LoginUrl = url

        # First, set the client credentials, scope and login URL from the values received with the function call
        # or pulled from the appropriate values or environment variables if not provided
        self.ClientId = _get_local_credential_from_env(client_id, ALPHAUS_CLIENT_ID)
        self.ClientSecret = _get_local_credential_from_env(client_secret, ALPHAUS_CLIENT_SECRET)
        self.Scope = _get_local_credential_from_choices(scope, "openid")
        self.Username = _get_local_credential_from_env(username, ALPHAUS_USERNAME)
        self.Password = _get_local_credential_from_env(password, ALPHAUS_PASSWORD)
        self.LoginUrl = _get_local_credential_from_choices(
            _get_local_credential_from_env(login_url, ALPHAUS_AUTH_URL), LOGIN_URL_RIPPLE)

        # Next, update the client credentials if they were not provided in a cascading order
        _update_auth_details(ALPHAUS_RIPPLE_CLIENT_ID, ALPHAUS_RIPPLE_CLIENT_SECRET, 
            ALPHAUS_RIPPLE_USERNAME, ALPHAUS_RIPPLE_PASSWORD, LOGIN_URL_RIPPLE)
        _update_auth_details(ALPHAUS_WAVE_CLIENT_ID, ALPHAUS_WAVE_CLIENT_SECRET,
            ALPHAUS_WAVE_USERNAME, ALPHAUS_WAVE_PASSWORD, LOGIN_URL_WAVE)

        # Finally, update the grant type if it was not provided
        if grant_type is None:
            if self.Username and self.Password:
                self.GrantType = "password"
            else:
                self.GrantType = "client_credentials"
        else:
            self.GrantType = grant_type

    def access_token(self) -> str:
        """
        Authenticates the user with the Blue API using the credentials provided.
        @returns: An access token that can be used with secured GRPC requests or
            REST requests to access Blue API endpoints
        """

        # First, insert the base fields into the form data
        form = [
            ("client_id", self.ClientId),
            ("client_secret", self.ClientSecret),
            ("grant_type", self.GrantType),
            ("scope", self.Scope)
        ]

        # Next, if the grant type is password then add the username and password
        # to the form data as well
        if self.GrantType == "password":
            form.extend(("username", self.Username), ("pass"))
        
        # Now, attempt to post the form request with a timeout of 60s. If the response
        # code from this request is not in a 2xx then throw an exception
        resp = requests.post(self.LoginUrl, timeout = 60, data = form)
        if resp.status_code < 200 or resp.status_code >= 300:
            raise Exception(resp.status_code)
        
        # Finally, attempt to extract the access token from the response. If we couldn't
        # find it then throw an exception
        mapping = resp.json()
        if "access_token" in mapping:
            return mapping["access_token"]
        else:
            raise Exception("Cannot find access token")
