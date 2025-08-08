# Proyecto de Pruebas Automatizadas con Selenium (Tarea 4)

Este repositorio contiene una suite de pruebas automatizadas desarrollada para el sitio web **`saucedemo.com`** como parte de la "Tarea 4: Pruebas Automatizadas".

El proyecto fue construido utilizando Python, Selenium WebDriver y Pytest.

## Características Principales

* **Cobertura Completa:** Automatización de 5 historias de usuario a través de 8 casos de prueba distintos.
* **Tipos de Pruebas:** Implementación de pruebas de Camino Feliz, Pruebas Negativas y Pruebas de Limites para cada flujo principal.
* **Diseño Profesional:** Uso del patron de diseño **Page Object Model (POM)** con una Página Base (`BasePage`) para centralizar la lógica de interacción y esperas.
* **Reportes Detallados:** Generacion automatica de un reporte de ejecución en formato **HTML**, que muestra el resultado de cada prueba.
* **Evidencia Visual por Paso:** Captura de pantalla automática después de **cada accion** (clic, escribir texto), organizadas en carpetas separadas por cada caso de prueba.
* **Ejecución Ordenada:** Las pruebas se ejecutan en un orden logico predefinido (Login -> Carrito -> Checkout) para una demostración clara.

## 💻 Tecnologías Utilizadas

* **Lenguaje:** Python
* **Automatizacion:** Selenium WebDriver
* **Framework de Pruebas:** Pytest
* **Plugins:**
    * `pytest-html` para la generación de reportes.
    * `pytest-ordering` para controlar el orden de ejecucion.

## 🚀 Como Empezar

Sigue estos pasos para clonar y ejecutar el proyecto en tu máquina local.

### **Pre-requisitos**

* Tener Python instalado en Windows.
* Tener Google Chrome instalado.

### **Instalacion**

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
    cd TU_REPOSITORIO
    ```

2.  **Crea y activa un entorno virtual:**
    ```powershell
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```powershell
    pip install -r requirements.txt
    ```

4.  **Descarga el WebDriver:**
    * Asegurate de tener el archivo `chromedriver.exe` correspondiente a tu versión de Google Chrome en la carpeta raiz del proyecto.

## ▶️ Como Ejecutar las Pruebas

Para ejecutar la suite de pruebas completa y generar el reporte HTML, usa el siguiente comando en tu terminal (PowerShell o CMD):

```powershell
pytest --html=reports/report.html --self-contained-html
```

* Las pruebas se ejecutaran a una velocidad lenta para poder apreciar cada paso.
* El reporte final se guardará en la carpeta `reports/`.
* Las capturas de pantalla de cada paso se guardarán en `reports/screenshots/`.

## Estructura del Proyecto

```
├── pages/                # Contiene las clases del Page Object Model
│   ├── base_page.py      # Clase base con metodos reutilizables (clic, escribir, etc.)
│   └── ...
├── tests/                # Contiene los archivos con los casos de prueba
│   ├── conftest.py       # Configuracion del driver de Selenium
│   └── ...
├── reports/              # Carpeta donde se genera el reporte HTML
│   └── screenshots/      # Carpeta donde se guardan las capturas de pantalla
├── chromedriver.exe      # El controlador de Chrome
├── pytest.ini            # Archivo de configuracion de Pytest
└── requirements.txt      # Lista de dependencias del proyecto
```

## Autor

* **Enrique** - *Desarrollo de la suite de automatización*