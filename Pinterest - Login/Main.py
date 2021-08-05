from controller.LoginController import LoginController
from auth.AuthCredentials import AuthCredentials

class Main:

    def __init__(self):
        LoginController(AuthCredentials.email, AuthCredentials.password)

Main()