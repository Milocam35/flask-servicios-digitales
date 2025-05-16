# Proyecto Para Empresa De Servicios Financieros Digitales

Realizada con:

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

# Prerrequisitos:

1.  **Tener instalado Git:**
    [Link de descarga](https://git-scm.com/downloads)

2.  **Tener instalado Python 3 en su última versión:**
    [Link de descarga](https://www.python.org/downloads/)

# Para inicializar el proyecto deberás:

1.  **Clonar el proyecto:**
    Abre tu terminal o símbolo del sistema, navega a la carpeta donde deseas guardar el proyecto (por ejemplo, tu escritorio) y ejecuta el siguiente comando:

    ```bash
    git clone git@github.com:Milocam35/flask-servicios-digitales.git
    ```

2.  **Navegar al directorio del proyecto:**
    Una vez que la clonación haya finalizado, ingresa al directorio del proyecto con el siguiente comando:

    ```bash
    cd flask-servicios-digitales
    ```

3.  **Crear un entorno virtual:**
    Es altamente recomendado crear un entorno virtual aislado para gestionar las dependencias del proyecto. Ejecuta el siguiente comando:

    ```bash
    python3 -m venv venv
    ```

    (En algunos sistemas, podrías necesitar usar `python` en lugar de `python3`).

4.  **Activar el entorno virtual:**
    Antes de instalar las dependencias, debes activar el entorno virtual. El comando varía según tu sistema operativo:

    * **Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```

    * **Windows (CMD):**
        ```bash
        venv\Scripts\activate
        ```

    * **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```

    Una vez activado, verás el nombre del entorno virtual (`(venv)`) al principio de tu línea de comandos.

5.  **Instalar las dependencias:**
    El proyecto incluye un archivo `requirements.txt` que lista todas las bibliotecas necesarias. Instala estas dependencias utilizando pip (el gestor de paquetes de Python):

    ```bash
    pip install -r requirements.txt
    ```

    Este comando leerá el archivo `requirements.txt` e instalará todas las librerías especificadas.

6.  **Ejecutar el servidor de desarrollo de Flask:**
    Finalmente, para iniciar la aplicación Flask, ejecuta el siguiente comando:

    ```bash
    python3 main.py
    ```

    Esto iniciará un servidor de desarrollo local. Generalmente, verás una salida indicando la dirección y el puerto donde se está ejecutando la aplicación (por ejemplo, `http://127.0.0.1:5000/`). Abre esta dirección en tu navegador para ver la aplicación en funcionamiento.

¡Con estos pasos, deberías tener tu proyecto de Flask en funcionamiento en tu entorno local!
