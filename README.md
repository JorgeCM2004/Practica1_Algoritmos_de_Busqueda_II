# Jorge Camacho Mejías - Práctica 1 - Python

## Crear Entorno de Ejecución

Para comenzar la práctica debemos crear un entorno donde se pueda ejecutar:

### 1. Instalación de Python.

Para instalar python nos dirigiremos a nuestro navegador de confianza y buscaremos la página oficical de python:
![alt text](./Images/WebPython.png)

E instalaremos la versión 3.12.4 para nuestro sistema operativo:
![alt text](./Images/VersionPython.png)

❗Es de suma importancia que en la instalación se seleccione la casilla de añadir al PATH❗

Si la instalación se ha realizado correctamente al abrir una terminal y ejecutar el codigo:

```bash
python --version
```

Deberia salir algo tal que:
![alt text](./Images/ComprobarPythonInstalado.png)


### 2. Creación y activación de venv.

Tras haber instalado correctamente la versión de python deseada, procederemos a crear un entorno virtual para que todas las descargas de librerias que realicemos sean almacenadas en el entorno y no en la version "base" de python.

Para ello nos dirigiremos a la carpeta clonada y usaremos el siguiente comando:
```bash
python -m venv nombre_del_entorno
```
