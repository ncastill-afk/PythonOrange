# OrangeHRM - Python Automation Testing

## Descripción

Proyecto de automatización de pruebas funcionales para la aplicación web **OrangeHRM**, desarrollado como parte de un portafolio de **QA Automation**.

El proyecto utiliza **Python, Selenium WebDriver y Pytest**, aplicando el patrón de diseño **Page Object Model (POM)** y la técnica **Data-Driven Testing (DDT)** para ejecutar pruebas de inicio de sesión utilizando datos almacenados en archivos Excel.

El objetivo es validar diferentes escenarios de autenticación, mejorar la mantenibilidad del código y generar reportes automáticos de los resultados de las pruebas.

## Aplicación bajo prueba

- **Aplicación:** OrangeHRM

- **URL:** https://opensource-demo.orangehrmlive.com/

- **Tipo de pruebas:** Pruebas funcionales automatizadas.

- **Módulo automatizado:** Login.

## Tecnologías y herramientas

**Tecnología / Herramienta** |	**Versión**	| **Descripción**
|----------------------------|--------------|-----------------|
| Python                     |	3.14.6	    | Lenguaje de programación. |
| Selenium WebDriver         |	4.52.0	    | Automatización de navegadores web. |
| Pytest                     |	9.2.0       | Framework de ejecución de pruebas. |
| Pytest-HTML                |	4.2.0	    | Generación de reportes HTML. |
| Pytest-xdist               |	3.8.0	    | Ejecución paralela de pruebas. |
| OpenPyXL                   |	3.1.5	    | Lectura y manipulación de archivos Excel. |
| Chrome                     |	156	        | Navegador utilizado para las pruebas. |
| PyCharm                    |	2026.2.3	| Entorno de desarrollo. |
| Git                        |	2.45.1.windows.1	| Control de versiones. |
| GitHub |	—	| Repositorio del proyecto. |

## Arquitectura del proyecto

Se utiliza el patrón **Page Object Model (POM)** para separar los elementos y acciones de la página web de la lógica de los casos de prueba.
``` text
PythonOrange/
│
├── Configurations/
│   └── config.ini
│
├── Logs/
│   └── automation.log
│
├── Reports/
│   └── report.html
│
├── Screenshots/
│   └── test_LoginIncorrecto_2026-10-30_11-53-00.png
│
├── pageObjects/
│   └── LoginPage.py
│
├── testCases/
│   ├── conftest.py
│   ├── test_login.py
│   └── test_login_ddt.py
│
├── TestData/
│   └── LoginData.xlsx
│
├── utilities/
│   ├── ExcelUtils.py
│   ├── customLogger.py
│   └── readProperties.py
│
├── pytest.ini
├── requirements.txt
└── README.md
```

## Funcionalidades automatizadas

1. Login exitoso

- Acceder a la aplicación OrangeHRM.

- Ingresar un usuario y contraseña válidos.

- Hacer clic en el botón Login.

- Verificar que se muestre el Dashboard.

- Cerrar sesión mediante la opción Logout.

2. Login con credenciales incorrectas

- Ingresar un usuario o contraseña incorrectos.

- Hacer clic en Login.

- Verificar que se muestre el mensaje Invalid credentials.

3. Data-Driven Testing (DDT)

Se utiliza un archivo Excel para almacenar los datos de prueba y ejecutar diferentes escenarios de autenticación.

Archivo: TestData/LoginData.xlsx

La hoja LoginData contiene los siguientes campos:

| Username | Password | Expected
|----------|----------|-------------|
| Admin    | Contraseña válida | Pass |

| Admin    | Contraseña incorrecta | Fail |

Los datos son leídos mediante la biblioteca OpenPyXL.

Se utiliza pytest.mark.parametrize para ejecutar cada registro como un caso de prueba independiente.

4. Logging

Se utiliza el módulo logging de Python para registrar información durante la ejecución de las pruebas.

El archivo de log se genera en:

Logs/automation.log

Se registran eventos como:

- Inicio de ejecución de pruebas.

- Usuario que se está probando.

- Resultado esperado.

- Login exitoso.

- Login rechazado.

5. Reportes HTML

Se utiliza pytest-html para generar reportes de ejecución en formato HTML.

El reporte permite consultar:

- Casos de prueba ejecutados.

- Resultados PASSED y FAILED.

- Duración de las pruebas.

- Información de ejecución.

Ubicación:

Reports/report.html

## Configuración del proyecto

1. Clonar el repositorio

git clone [URL_DEL_REPOSITORIO](https://github.com/ncastill-afk/PythonOrange)

Ingresar a la carpeta:

cd PythonOrange

2. Crear un entorno virtual

python -m venv .venv

Activar el entorno virtual en Windows PowerShell:

.venv\Scripts\Activate.ps1

3. Instalar las dependencias

pip install -r requirements.txt

4. Configurar los parámetros

Revisar el archivo:

Configurations/config.ini

Este archivo contiene los parámetros de configuración de la aplicación, como la URL y las credenciales utilizadas por las pruebas.

## Ejecución de las pruebas

## Ejecutar todas las pruebas

pytest -v -s

## Ejecutar pruebas de login

pytest -v -s testCases/test_login.py

## Ejecutar pruebas DDT

pytest -v -s testCases/test_login_ddt.py

## Generar reporte HTML

pytest -v -s --html=Reports/report.html --self-contained-html

## Ejecutar pruebas en paralelo

pytest -v -s -n=2

## Buenas prácticas aplicadas

- Separación de responsabilidades mediante Page Object Model.

- Reutilización de métodos para interactuar con los elementos de la aplicación.

- Uso de esperas explícitas (WebDriverWait).

- Separación de los datos de prueba del código de automatización.

- Implementación de Data-Driven Testing.

- Validación de resultados mediante assertions.

- Registro de eventos mediante logging.

- Generación de reportes HTML.

- Uso de entornos virtuales de Python.

## Objetivos de aprendizaje

Este proyecto permite aplicar y fortalecer conocimientos en:

- Automatización de pruebas funcionales con Selenium WebDriver.

- Programación en Python orientada a pruebas.

- Framework Pytest.

- Diseño Page Object Model (POM).

- Data-Driven Testing (DDT).

- Manipulación de archivos Excel con OpenPyXL.

- Manejo de logs y reportes de ejecución.

- Control de versiones con Git y GitHub.

## Autor Nadia Castillo

Proyecto desarrollado como parte de un portafolio de QA Automation, con el objetivo de demostrar conocimientos prácticos en automatización de pruebas funcionales utilizando Python y Selenium WebDriver.