# Gestor de tareas

## Criterios de evaluación
Para elegir el gestor de tareas más adecuado, se han considerado los siguientes criterios:

1. **Facilidad de uso y configuración:** Herramientas sencillas de instalar y configurar, con una curva de aprendizaje accesible (evaluadas en base a la cantidad de pasos necesarios para comprender la herramienta y la claridad de la documentación).
2. **Complejidad añadida:** Se penalizan herramientas que introducen más complejidad de la necesaria para el proyecto, como dependencias adicionales o sintaxis excesivamente compleja.


## Invoke

Es basada en Python (inspirado en ruby Rake), por lo que se pueden escribir las tareas utilizando Python, proporcionando una mayor integración en el código del proyecto.
Permite ejecutar comandos de shell y definir/organizar funciones de tareas desde un archivo tasks.py. 

## Paver

Paver es una herramienta basada en python que sigue las líneas de Make y Rake. Incluyendo herramientas especifícas para proyectos de Python (como soporte para paquetes y entornos). Sin embargo, tiene una comunidad más pequeña en comparación con herramientas como Make, lo que puede dificultar la resolución de problemas.

## Make

Make es una herramienta de automatización de tareas que no está limitada a un solo lenguaje de programación, por lo que puede ser utilizada en proyectos escritos en cualquier lenguaje, con una comunidad activa y una documentación extensa (muchos recursos). Solo es necesario crear un archivo específico (Makefile) para definir las tareas a ejecutar.

 
## Just 

Just es una herramienta de automatización de tareas que permite definir comandos de manera sencilla a través de un archivo justfile, similar a Make, Just es más fácil de escribir y entender (lenguaje más "cotidiano" ).  Es independiente del lenguaje de programación, lo que permite integrarlo en proyectos de Python y otros lenguajes sin problema. Make  tiene una comunidad más grande, lo que se traduce en más recursos, tutoriales y una mejor documentación, lo que facilita su adopción y resolución de problemas.

Se opta por Make debido a su simplicidad, independencia del lenguaje de programación y amplia comunidad. Aunque Invoke es una buena opción para proyectos puramente Python, Make ofrece mayor flexibilidad (no se limita a apliaciones solamente de python).

