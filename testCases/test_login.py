import pytest
import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from datetime import datetime
from utilities.customLogger import LogGen

read_config = ReadConfig()

class Test_001_Login:

    baseURL = read_config.getApplicationURL()
    username = read_config.getUsername()
    password = read_config.getPassword()
    password_incorrecto = ReadConfig.getPassword_incorrecto()

    logger = LogGen.loggen()
    logger.info("Prueba de creación del archivo log")

    def test_LoginIncorrecto(self, setup):
        self.logger.info("****Test_001_Login****")
        self.logger.info("****Verifying Login incorrecto****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(3)  # Solo para diagnosticar el problema
        act_title = self.driver.title

        if act_title == "OrangeHRM":
            assert True
            self.logger.info("****HomePage Title test is passed****")
        else:
            fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nombre_archivo = f".\\Screenshots\\test_LoginIncorrecto_{fecha_hora}.png"
            self.driver.save_screenshot(nombre_archivo)
            self.logger.error("****HomePage Title test is failed****")
            assert False
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password_incorrecto)
        self.lp.clickLogin()
        time.sleep(3)  # Solo para diagnosticar el problema

        texto_error = self.lp.obtenerMensajeError()
        assert "Invalid credentials" in texto_error

    def test_login(self, setup):
        self.logger.info("****Verifying Login test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(3)  # Solo para diagnosticar el problema
        #print("URL:", self.driver.current_url)
        #print("Campos username:", len(self.driver.find_elements(By.NAME, "username")))
        #print("Campos por placeholder:", len(self.driver.find_elements(By.CSS_SELECTOR, "input[placeholder='Username']")))
        #print("Campos password:", len(self.driver.find_elements(By.NAME, "password")))

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        #act_title = self.driver.title
        assert self.lp.ingresoAlDashboard().text == "Dashboard"
        self.logger.info("****Login test is passed****")
        #if act_title == "OrangeHRM":
        #    assert True
        #else:
        #    self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
        #    assert False
