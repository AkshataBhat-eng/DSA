class User:
    def __init__(self, id: int, username: str, email: str, password: str, role: str = "customer"):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role
        # role can be customer/admin

    @staticmethod
    def register_user(username: str, email: str, password: str, role: Optional[str] = "user"):
        #Register a new user
        # Check if the user already exist using the email comparing it with db entries
        # if exists give an error
        # if not, create new user
        # store user details in db by adding a new entry, hash the user passord with any library like bcrypt
        # return a response with message: User created

    @staticmethod
    def oauth_verify(oauth_token: str):
        #Verify Google OAuth token and issue JWT for the user
        # use necessary library/package for Oauth verifying the user with Google/facebook
        # get the oauth_token from the google/facebook sign-in
        # retrieve the email of the user using the oauth package 
        # check the Db entry for the email, if found, login the user and return the JWT access token 
        # if not, create a new entry in the DB and register the user - (password will be empty)
        # Return the error response if email retrival fails with message: Invalid OAuth token

    @staticmethod
    def login_user(email: str, password: str):
        #Login user and return JWT token
        # get the user's email and password
        # if email and password matches with DB entry, return the JWT access token to the user.
        # if not, return the error response with messagge: Invalid credentials.

    @staticmethod
    def create_access_token(user: 'User'):
        # Create JWT access token with role included.
        # create a payload with user-email, role, current time and expiry time
        # pass this payload along with secret_key and algorithm (HS256) to jwt.encode() function;
        # return the token    

    @staticmethod
    def forgot_password(email: str, new_password: str):
        # Reset user password
        # get the user email, match it with DB entry
        # if it matches, get the new password, hash it and store in db against the user entry and return response message: Password updated successfully
        # if not, return error response iwth message: Email not found
