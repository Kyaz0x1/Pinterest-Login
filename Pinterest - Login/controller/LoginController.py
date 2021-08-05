from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from time import sleep
from colorama import Fore, init

class LoginController:

    def __init__(self, email, password):
        self.init_colorama()
        self.browse_in_website()
        sleep(3)
        self.login(email, password)
        sleep(5)
        self.get_profile()

    def init_colorama(self):
        init(autoreset = True)

    def browse_in_website(self):
        self.firefox = webdriver.Firefox()
        self.firefox.get('https://www.pinterest.com/')

    def login(self, email, password):
        btnLoginForm = self.firefox.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/button')
        btnLoginForm.click()

        txtEmail = self.firefox.find_element_by_xpath('//*[@id="email"]')
        txtEmail.send_keys(email)

        txtPassword = self.firefox.find_element_by_xpath('//*[@id="password"]')
        txtPassword.send_keys(password)

        btnLogin = self.firefox.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[5]/button')
        btnLogin.click()
        print(Fore.GREEN + 'Logado com sucesso!')

    def get_profile(self):
        try:
            myProfile = self.firefox.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div[5]/div[4]/div/a/div/div')
            myProfile.click()
            print(Fore.YELLOW + "Agora você está visualizando o seu perfil!")
        except NoSuchElementException:
            print(Fore.RED + 'Ocorreu um erro ao efetuar o login! Provavelmente as credenciais estão incorretas.')