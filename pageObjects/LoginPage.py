from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    textbox_username = "username"
    textbox_password = "password"
    button_login_css = "button[type='submit']"
    dashboard_css = "h6.oxd-topbar-header-breadcrumb-module"
    texto_error = "//p[contains(@class,'oxd-alert-content-text')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def setUsername(self, username):
        #self.driver.find_element_by_name(self.textbox_username).clear
        #self.driver.find_element_by_name(self.textbox_username).send_keys(username)
        #print("URL actual:", self.driver.current_url)
        #print("Título:", self.driver.title)
        #print("HTML:", self.driver.page_source[:2000])
        campo = self.driver.find_element(By.NAME, self.textbox_username)
        campo.clear()
        campo.send_keys(username)

    def setPassword(self, password):
        #self.driver.find_element_by_name(self.textbox_password).clear
        #self.driver.find_element_by_name(self.textbox_password).send_keys(password)
        campo = self.driver.find_element(By.NAME, self.textbox_password)
        campo.clear()
        campo.send_keys(password)

    def clickLogin(self):
        #self.driver.find_element_by_css(self.button_login_css).click()
        self.driver.find_element(By.CSS_SELECTOR, self.button_login_css).click()

    def ingresoAlDashboard(self):
        #self.driver.find_element_by_css(self.dashboard_css)
        #return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.dashboard_css)))
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.dashboard_css)))
        #return self.driver.find_element(By.CSS_SELECTOR, self.dashboard_css)

    def obtenerMensajeError(self):
        #self.driver.find_element_by_link_text(self.texto_error)
        #return self.driver.find_element(By.XPATH, self.texto_error).text
        #return WebDriverWait(self.driver, 10).until(
        #    EC.visibility_of_element_located((By.XPATH, self.texto_error))).text
        elemento = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.texto_error)))
        return elemento.text

    def clickLogout(self):
        #self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab").click()
        #self.driver.find_element(By.LINK_TEXT, "Logout").click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-tab"))).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()

        # Esperar que aparezca nuevamente el login
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, self.textbox_username)))