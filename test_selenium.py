import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test_selenium():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test1(self):
    
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Abre la pagina
    self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    # Espera que la pagina cargue (segundos)
    time.sleep(3)
    # Maximizar tamaño de la pestaña
    self.driver.set_window_size(1382, 736)
    # Espera a que el boton "Enviar" este presente
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[@type=\'submit\']")))
    # Llenar el formulario de logueo y hacer click en sl boton "Enviar"
    self.driver.find_element(By.XPATH, "//input[@name=\'username\']").send_keys("Admin")
    self.driver.find_element(By.XPATH, "//input[@name=\'password\']").send_keys("admin123")
    self.driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    # Espera 3 segundos y espera que este presente el texto en pantalla "Dashboard"
    time.sleep(3)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//h6[text()=\'Dashboard\']")))
    # Click en el apartado del menu "Recruitment"
    self.driver.find_element(By.XPATH, "//*[text()=\'Recruitment\']").click()
    # Espera 3 segundos y espera que este presente el texto en pantalla "Recruitment"
    time.sleep(3)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//h6[text()=\'Recruitment\']")))
    # Click en el a boton "Add"
    self.driver.find_element(By.XPATH, "//button[contains(.,\' Add\')]").click()
    # Espera 3 segundos y espera que este presente el textbox "firstName"
    time.sleep(3)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//input[@name=\'firstName\']")))
    # Llenar el formulario para los campos:
    #firstName
    self.driver.find_element(By.XPATH, "//input[@name=\'firstName\']").send_keys("Oscar")
    #middleName
    self.driver.find_element(By.XPATH, "//input[@name=\'middleName\']").send_keys("Julian")
    #lastName
    self.driver.find_element(By.XPATH, "//input[@name=\'lastName\']").send_keys("Duque Ramos")
    # Click en el select "Vacancy" y posterior seleccion de la opcion "Payroll Administrator"
    self.driver.find_element(By.XPATH, "//*[@class=\'oxd-select-text-input\']").click()
    self.driver.find_element(By.XPATH, "//*[text()=\'Payroll Administrator\']").click()
    # Espera 3 segundos
    time.sleep(3)
    # Llenar el formulario para los campos:
    #Email
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div[2]/div[2]/div/div/form/div[3]/div/div/div/div[2]/input").send_keys("judura172@gmail.com")
    #Contact number
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input").send_keys("3126983584")
    # Carga de archivo desde pagina
    self.driver.find_element(By.XPATH, "//input[@type=\'file\']").send_keys("C:\Proyectos\SeleniumTest\DocsCargaPy\Test1-Automatizacion.pdf")
    # Espera 3 segundos
    time.sleep(3)
    # Despliegue de calendario y posterior seleccion de opcion "Today" y click en sl boton "Enviar"
    self.driver.find_element(By.XPATH, "//input[@placeholder=\'yyyy-dd-mm\']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\--today").click()
    self.driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    # Espera 3 segundos y espera que este presente el boton "Shortlist" y posteriormente lo clickea
    time.sleep(3)   
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(.,\'Shortlist\')]")))
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Shortlist\')]").click()
    # Espera 3 segundos y espera que este presente el boton "Save" y posteriormente lo clickea
    time.sleep(3)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(.,\'Save\')]")))
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Save\')]").click()
    # Espera 5 segundos y valida que este presente en pantalla el boton "Schedule Interview" y posteriormente lo clickea
    time.sleep(10)
    elements = self.driver.find_elements(By.XPATH, "//button[contains(.,\'Schedule Interview\')]")
    assert len(elements) > 0
    self.driver.find_element(By.XPATH, "//button[contains(.,\'Schedule Interview\')]").click()
    # Espera 5 segundos y espera que este presente el label "Interview Title"
    time.sleep(5)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//label[contains(.,\'Interview Title\')]")))
    # Llenar el formulario para los campos:
    #Interview Title
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/input").send_keys("Test Titulo Entrevista")
    #Interviewer
    # Busqueda de entrevistador
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div/div[2]/div/div/input").click()    
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div/div[2]/div/div/input").send_keys("Orange")
    # Espera 5 segundos para que carguen las opciones
    time.sleep(5)
    # Seleccionar opcion por medio de teclas (Flecha abajo + Enter)
    self.driver.find_element(By.XPATH, "//div[@id=\'app\']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div/div[2]/div/div/input").send_keys(Keys.DOWN + Keys.ENTER)
    #Date y posterior seleccion de opcion "Today"
    #self.driver.find_element(By.XPATH, "//input[@placeholder=\'yyyy-dd-mm\']").click()
    #self.driver.find_element(By.CSS_SELECTOR, ".\\--today").click()
    self.driver.find_element(By.XPATH, "//input[@placeholder=\'yyyy-dd-mm\']").send_keys("2024-11-11")
    #Time y posterior seleccion de opcion "PM" 
    #self.driver.find_element(By.XPATH, "//input[@placeholder=\'hh:mm\']").click()
    #self.driver.find_element(By.XPATH, "//input[@value=\'PM\']").click()
    self.driver.find_element(By.XPATH, "//input[@placeholder=\'hh:mm\']").send_keys("11:00 AM")
    # Click en sl boton "Save"
    self.driver.find_element(By.XPATH, "//button[@type=\'submit\']").click()
    # Espera 5 segundos y espera que este presente el boton " Mark Interview Passed" y posteriormente lo clickea
    time.sleep(5)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(.,' Mark Interview Passed ')]")))
    self.driver.find_element(By.XPATH, "//button[contains(.,' Mark Interview Passed ')]").click()
    # Espera 5 segundos y espera que este presente el boton "Save" y posteriormente lo clickea
    time.sleep(5)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(.,'Save')]")))
    self.driver.find_element(By.XPATH, "//button[contains(.,'Save')]").click()
    # Espera 5 segundos y espera que este presente el boton "Offer Job" y posteriormente lo clickea
    time.sleep(5)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(.,'Offer Job')]")))
    self.driver.find_element(By.XPATH, "//button[contains(.,'Offer Job')]").click()
    # Espera 5 segundos y espera que este presente el boton "Save" y posteriormente lo clickea
    time.sleep(5)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(.,'Save')]")))
    self.driver.find_element(By.XPATH, "//button[contains(.,'Save')]").click()
    # Espera 5 segundos y espera que este presente el boton "Hire" y posteriormente lo clickea
    time.sleep(5)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(.,'Hire')]")))
    self.driver.find_element(By.XPATH, "//button[contains(.,'Hire')]").click()
    # Espera 5 segundos y espera que este presente el boton "Save" y posteriormente lo clickea
    time.sleep(5)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(.,'Save')]")))
    self.driver.find_element(By.XPATH, "//button[contains(.,'Save')]").click()
    # Espera 5 segundos
    time.sleep(5)
    # Valida el cambio de estado a "Hired"
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//p[contains(.,'Status: Hired')]")))
    # Click en el apartado del menu "Recruitment"
    self.driver.find_element(By.XPATH, "//*[text()='Recruitment']").click()
    # Espera 5 segundos y espera que este presente el texto en pantalla "Recruitment"    
    time.sleep(5)
    WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located((By.XPATH, "//h6[text()=\'Recruitment\']")))
    # Encontrar postulado en tabla bajo el mismo div
    elements = self.driver.find_elements(By.XPATH, "//div[@role=\'row\']")
    assert len(elements) > 0
    self.vars["nombre"] = self.driver.find_element(By.XPATH, "//*[contains(text(),\'Oscar Julian Duque Ramos\')]").text
    if self.driver.execute_script("return (arguments[0]===\"Oscar Julian Duque Ramos\")", self.vars["nombre"]):
      print("{}".format(self.vars["nombre"]))
      print("Encontre el registro")
    else:
      print("Sali del if")
    
    """ Trate de realizar la busqueda por una tabla normal, pero al ser divs no entra en cada uno, lo dejo comentado
    # Encontrar postulado como contratado
    # Encuentra la tabla por su xpath
    table = self.driver.find_element(By.XPATH, "//div[@class='oxd-table']")
    # Encuentra todas las filas de la tabla
    rows = table.find_elements(By.XPATH, "//div[@role='row']")
    # Define los valores que quieres validar
    valor1 = "Oscar Julian Duque Ramos"
    valor2 = "Hired"
    # Recorre cada fila y valida si contiene ambos valores
    found = False
    for row in rows:
        # Encuentra todas las celdas (td) en la fila
        cells = row.find_elements(By.XPATH, "//div[@role='cell']")        
        # Extrae el texto de cada celda
        cell_texts = [cell.text for cell in cells]

        # Verifica si ambos valores estan presentes en los textos de las celdas
        if valor1 in cell_texts and valor2 in cell_texts:
            found = True
            print(f"Se encontró la fila con {valor1} y {valor2}.")
            break
    if not found:
        print(f"No se encontró ninguna fila que contenga {valor1} y {valor2}.")"""
    self.driver.quit()