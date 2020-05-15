# Scraping utilizando Python

## Comenzando 🚀

_El siguiente manual detalla los pasos a seguir para obtener el titulo y la descripcion de las preguntas realizadas en el sitio de Stackoverflow en Español._

### Pre-requisitos 📋

_Para continuar con el instructivo se requiere tener instalado Python3, Pip y Virtualenv en tu maquina._

### Instalación 🔧

_Pasos a ejecutar en la Terminal_

_Crear entorno virtual_

```
virtualenv scrapy_entorno
```

_Activar entorno en Windows_

```
source Script/activate
```

_Descargar [Twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/) según el Sistema Operativo, navegar hasta la carpeta Download y ejecutar:_
```
sbogado@Equipo013043 MINGW64 ~/Downloads
$ pip install Twisted-20.3.0-cp37-cp37m-win32.whl
```
_Ahora instalamos Scrapy_

```
pip install scrapy
```
_Instalar bs4_
```
pip install bs4
```
_Verificamos que las herramientas esten instaladas_
```
scrapy --version
bs4 --version
```
## Ejecución
_Una vez construido el codigo, para comenzar la extracción ejecutar_

_Para obtener resultados en CSV:_
```
scrapy runspider stackoverflow.py -o stackoverflow.csv -t csv
```
_Para obtener resultados en JSON:_
```
scrapy runspider stackoverflow.py -o stackoverflow.json -t json
```
_Como resultado se debe generar un output especificado en el parametro -o (stackoverflow) y con el formato expecificado en -t (csv, json)_
## Construido con 🛠️

_Herramientas utilizadas para crear el proyecto_

* [Python3](https://www.python.org/downloads/) - El lenguaje top del 2020
* [Pip](https://pip.pypa.io/en/stable/installing/) - Manejador de paquetes de Python
* [Virtualenv](https://virtualenv.pypa.io/en/latest) - Usado para crear entornos virtuales
* [Twisted](https://pypi.org/project/Twisted/) - Permite instalar Scrapy sin errores
* [Scrapy](https://scrapy.org/) - Framework para la extracción automatizada de información desde la web

## Agradecimientos 📄

Este proyecto está basado en el tutorial publicado en [Youtube](https://www.youtube.com/watch?v=ViOFqeRgu5s&t=815s)

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Da las gracias públicamente 🤓.
* etc.



---
 Template construido con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊
