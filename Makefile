# Ruta donde se encuentra pdm instalado
PDM_PATH = $(HOME)/.local/bin/pdm

# Instalar pdm si no está disponible
install_pdm:
		if ! command -v $(PDM_PATH) &> /dev/null; then \
				echo "Instalando pdm..."; \
				pip install --user pdm; \
		fi


# Instalar dependencias, asegurando que el proyecto esté inicializado
install: install_pdm 
		$(PDM_PATH) install

# Ejecutar pruebas con pytest
test:
		$(PDM_PATH) run pytest

# Ejecutar python -m py_compile para revisar solo la sintaxis del código
check:
		$(PDM_PATH) run python -m py_compile $(shell find src -name "*.py") || exit 1
		@echo "La comprobación de sintaxis ha finalizado sin errores."


# Limpiar el entorno virtual
clean:
		$(PDM_PATH) venv remove in-project
