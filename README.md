# ElectricPika
"Script en Python para consultar y guardar información de Pokémon usando la API de PokeAPI."

# Pokedex Python Script 🐾

Este proyecto consiste en un script en Python para consultar y guardar información sobre Pokémon utilizando la API de [PokeAPI](https://pokeapi.co/). Este programa permite a los usuarios obtener detalles como el nombre, peso, altura, tipos, habilidades y una imagen de un Pokémon específico.

## ¿Cómo funciona el proyecto? 🌟

1. **Interacción con la API**: Utilizamos solicitudes HTTP para recuperar información detallada sobre Pokémon desde PokeAPI.
2. **Estructuración de datos**: Procesamos los datos en formato JSON para extraer información clave.
3. **Almacenamiento**: Creamos un directorio llamado `pokedex` donde se guardan los datos de cada Pokémon en archivos JSON organizados.
4. **Interfaz sencilla**: El usuario puede ingresar el nombre del Pokémon directamente en la terminal para obtener los resultados.

## Bibliotecas necesarias 📋

Para ejecutar este proyecto, necesitarás instalar las siguientes bibliotecas:

- **requests**: Para enviar solicitudes HTTP a la API.
- **os**: Incluida en la biblioteca estándar de Python, para manejar el sistema de archivos.
- **json**: También parte de la biblioteca estándar, para manipular datos en formato JSON.

Instala las dependencias necesarias ejecutando el siguiente comando en tu terminal:

```bash
pip install requests
