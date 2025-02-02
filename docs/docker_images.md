# Imagenes para el contenedor

## Criterios de evaluación

Para seleccionar la imagen de docker mas adecuada para este proyecto, se han considerado los siguientes criterios:


1. **Imágenes mantenidas:** Preferencia por herramientas activamente mantenidas y actualizadas para evitar problemas de tecnologías obsoletas.

2. Tambien se va a tener en cuenta el peso final de las imágenes(con todas las herramientas necesarias).


## [Ubuntu](https://hub.docker.com/_/ubuntu)
Está activamente mantenida con actualizaciones y versiones recientes, es una buena eleción para tener el sistema como base y ya ir añdiendo las herramientas necesarias. Pero tiene un peso final de **543MB**.

## [Debian](https://hub.docker.com/_/debian)
La última actualización fue de hace un par de semanas, por lo que esta activamente mantenido. En cuanto al peso varia dependiendo de la version que escojas, tenemos la base con un peso muy parecido a ubuntu, pero luego tenemos varias opciones slim: debian:bullseye-slim con un peso de **460MB**, debian:bookworm-slim con peso **568MB** y debian normal **656MB**.

## [Alpine](https://hub.docker.com/_/alpine)
La última actualización fue de hace unos días, siendo una herramieta activa y mantenida, con un peso mucho menor al de las anteriores, de tan solo 5MB de imagen base, sin funcionalides extra siendo mínima y eficiente. Pero con las herramientas,tiene un peso final de **114MB**.

## [Python](https://hub.docker.com/_/python)
Ya que estoy utilizando python, tenemos que ver esta opción en la que ya nos viene instalado python, pero hay diversas opciones, de las ya comentadas anteriormente como Alpine(muy ligera) peso final **85MB**, debian:bookworm-slim con peso final **163MB**, python:bullseye-slim con un peso final de **161MB**. Con la última acutalzición de días, por lo que esta mantenida.



## Conlusión

Hay varias opciones para elegir una imagen base para el proyecto. Las imágenes como Ubuntu, Debian o Alpine solo incluyen el sistema operativo, y todas están activamente mantenidas. Alpine destaca por ser la más ligera, pudiendo instalar Python y sus dependencias adicionales.

Debido a esto, me decantaré por la imagen oficial de Python sobre Alpine, ya que proporciona un mantenimiento activo y la inclusión de Python sin necesidad de instalaciones adicionales.

El peso de las imágenes finales estan [aquí](https://github.com/lmchaves/OrganizarTaller/tree/Objetivo-1/docs/imgs/peso_imagenes.png).