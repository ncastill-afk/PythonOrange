import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from utilities import ExcelUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

read_config = ReadConfig()


# Leer los datos del Excel antes de ejecutar las pruebas
def obtener_datos_login():
    path = ".//TestData/LoginData.xlsx"

    rows = ExcelUtils.getRowCount(path, 'LoginData')

    casos = []

    for r in range(2, rows + 1):
        username = ExcelUtils.readData(path, 'LoginData', r, 1)
        password = ExcelUtils.readData(path, 'LoginData', r, 2)
        expected = ExcelUtils.readData(path, 'LoginData', r, 3)

        casos.append(
            pytest.param(
                username,
                password,
                expected,
                id=f"fila-{r}-{username}-{expected}"
            )
        )

    return casos

class Test_002_DDT_Login:

    baseURL = read_config.getApplicationURL()
    #username = read_config.getUsername()
    #password = read_config.getPassword()
    #password_incorrecto = ReadConfig.getPassword_incorrecto()

    logger = LogGen.loggen()
    logger.info("Prueba de creación del archivo log")

    @pytest.mark.parametrize("username, password, expected", obtener_datos_login())
    def test_login(self, setup, username, password, expected):
        self.logger.info("****Test_002_DDT_Login****")
        self.logger.info("****Verifying Login test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        #path = ".//TestData/LoginData.xlsx"
        time.sleep(3)  # Solo para diagnosticar el problema

        self.lp = LoginPage(self.driver)

        #self.rows = ExcelUtils.getRowCount(path, 'LoginData')
        #print("Number of Rows i a Excel: ", self.rows)

        #for r in range(2, self.rows+1):
        #    self.username = ExcelUtils.readData(path, 'LoginData', r, 1)
        #    self.password =  ExcelUtils.readData(path, 'LoginData', r, 2)
        #    self.expected = ExcelUtils.readData(path, 'LoginData', r, 3)

        #    self.logger.info(f"Probando usuario: {self.username} - Resultado esperado: {self.expected}")

        #    extra = getattr(self, "extra", [])
        #    extra.append(f"Usuario: {self.username} | Resultado esperado: {self.expected}")
        #    self.extra = extra

        self.lp.setUsername(username)
        self.lp.setPassword(password)
        self.lp.clickLogin()
        time.sleep(5)

        if str(expected).strip().lower() == "pass":
            # Validar que el login sea exitoso
            dashboard = self.lp.ingresoAlDashboard()
            assert dashboard.text == "Dashboard", f"Se esperaba Dashboard para el usuario {username}"
            self.logger.info(f"Login exitoso para el usuario: {username}")
            # Cerrar sesión
            self.lp.clickLogout()
            #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))

        elif str(expected).strip().lower() == "fail":
            # Validar el mensaje de error
            texto_error = self.lp.obtenerMensajeError()
            assert "Invalid credentials" in texto_error, f"Mensaje de error inesperado para el usuario {username}"
            self.logger.info(f"Login rechazado correctamente para: {username}")

        else:
            assert False, f"Resultado esperado desconocido en Excel: {expected}"

        # Volver a la página de login para probar la siguiente fila
        #self.driver.get(self.baseURL)

#    @pytest.hookimpl(hookwrapper=True)
#    def pytest_runtest_makereport(self, item, call):
#        outcome = yield
#        report = outcome.get_result()

#        if report.when == "call":
#            report.user_properties.append(("Usuarios probados", str(getattr(self, "extra", []))))
