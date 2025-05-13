"""
Script principal para ejecutar la aplicación Flask.
"""
import os
from musica_api import create_app
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env si existe
load_dotenv()

# Crear la aplicación
app = create_app()


if __name__ == "__main__":
    # TODO: Obtener puerto del ambiente o usar 5000 por defecto
    
    # TODO: Determinar si se debe usar modo debug
    
    # TODO: Ejecutar aplicación

    pass
