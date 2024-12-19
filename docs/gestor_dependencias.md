# Gestor de dependencias

## Criterios de evaluación
Para seleccionar el gestor de dependencias más adecuado para este proyecto, se han considerado los siguientes criterios:

1. **Cumplimiento de estándares:** Preferencia por gestores que sigan el estándar [PEP 518](https://peps.python.org/pep-0518/), garantizando mejores prácticas y compatibilidad futura.

2. **Gestores activos:** Preferencia por herramientas activamente mantenidas y actualizadas para evitar problemas de tecnologías obsoletas.


## Poetry

Utiliza el estándar pyproject.toml ([PEP 518](https://peps.python.org/pep-0518/)), pero tiene una estructura personalizada **[tool.poetry]** que no es 100% compatible con  [PEP 518](https://peps.python.org/pep-0518/).
Documentación extensa, con una gran cantidad de recursos para realizar buenas prácticas (como tutoriales, artículos, foros).
En algunos casos puede ser más lento (ya que tambien se encarga de empaqutar el código mediante los archivos .whl) que alternativas más ligeras.


## Hatch

Permite utilizar múltiples entornos virtuales para un mismo proyecto(par poder utilizar diferentes configuraciones o versiones de Python).
Hace uso del estandar **pyproject.toml** ([PEP 518](https://peps.python.org/pep-0518/)) y tiene una estructura personalizada **[tool.hatch.envs.default]** que no es 100% compatible con [PEP 518](https://peps.python.org/pep-0518/).
Tiene una buena docmentación y recursos para realizar buenas prácticas (como tutoriales, artículos, foros), sin embargo menor que Poetry.


## PDM

Compatible con el estándar [PEP 518](https://peps.python.org/pep-0518/), utilizando pyproject.toml para gestionar las dependencias, entornos virtuales y empaquetado de código.
Es ligero y rápido, y enfocado en la simplicidad y el uso de archivos de bloqueo (pdm.lock) para garantizar versiones coherentes de las dependencias.
Tiene una buena documentación pero con una comunidad más pequeña que la de Poetry.

## Uv (Unified Python packaging)

Es un gestor muy moderno (empezó en agosto de este año), sin embargo en muchos foros de Reddit recominedan migrar de gestores como poetry y hatch a uv.
Un punto negativo es que no hay mucha documentación, debido al rápido ritmo de desarrollo de uv, por lo que si te surgen problemas, debes abrir un issue 
(se puede ver como tienen mas de 1000 abiertos de hace minutos u horas, respondend bastante rápido).



Elegiría PDM por su rapidez y simplicidad, aunque varias cumplen el estándar [PEP 518](https://peps.python.org/pep-0518/). Aunque Poetry destaca en documentación, es más lento, y Hatch tiene menos recursos. UV, aunque prometedor (es el mas rápido), aún es inmaduro.

