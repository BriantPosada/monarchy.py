# Historia en Código: Linajes Reales

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Descripción

**Historia en Código: Linajes Reales** es un proyecto desarrollado en Python que permite explorar la monarquía inglesa y británica desde la Conquista Normanda (1066) hasta el reinado actual de Carlos III (2025). Este proyecto demuestra habilidades fundamentales de backend, como el manejo de estructuras de datos, manipulación de JSON, y creación de interfaces de usuario en consola. Los datos de los monarcas se almacenan en un archivo JSON (`monarchy.json`) y se consultan a través de un menú interactivo implementado en `history.py`.

El proyecto es ideal para mostrar competencias en desarrollo backend junior, incluyendo:
- Estructuración y manejo de datos en formato JSON.
- Implementación de lógica de búsqueda y filtrado.
- Creación de interfaces de usuario interactivas en consola.
- Documentación clara y profesional.

## Características

- **Listar monarcas**: Muestra todos los monarcas con sus reinados y casas reales.
- **Buscar monarca**: Permite buscar un monarca por nombre y muestra detalles como reinado, casa, antecesor y sucesor.
- **Mostrar linaje**: Traza el linaje de un monarca hacia sus antecesores, excluyendo períodos no monárquicos (interregnos).
- **Agrupar por casa**: Organiza los monarcas por dinastía (por ejemplo, Tudor, Stuart, Windsor).
- **Datos históricos completos**: Cubre desde Guillermo I (1066) hasta Carlos III (2022-presente), incluyendo interregnos como la Mancomunidad de Inglaterra (1649-1660).

## Tecnologías utilizadas

- **Python 3.8+**: Lenguaje principal para la lógica y el procesamiento de datos.
- **JSON**: Formato utilizado para almacenar los datos de los monarcas en `monarchy.json`.
- **Git**: Control de versiones para el desarrollo y publicación en GitHub.

## Instalación

Sigue estos pasos para ejecutar el proyecto localmente:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/BriantPosada/<nombre-repositorio>.git
   cd <nombre-repositorio>
   ```

2. **Requisitos**:
   - Asegúrate de tener Python 3.8 o superior instalado. Verifica con:
     ```bash
     python --version
     ```
   - No se requieren dependencias externas, ya que el proyecto usa únicamente la biblioteca estándar de Python.

3. **Archivos necesarios**:
   - `monarchy.json`: Contiene los datos de los monarcas.
   - `history.py`: Script principal con la lógica del programa.

4. **Ejecuta el programa**:
   ```bash
   python history.py
   ```

## Uso

Al ejecutar `python history.py`, se mostrará un menú interactivo con las siguientes opciones:

1. **Ver todos los monarcas**: Lista todos los monarcas con sus reinados y casas.
2. **Buscar monarca por nombre**: Ingresa un nombre (ej. "Carlos III") para ver detalles.
3. **Mostrar linaje (antecesor)**: Traza el linaje de un monarca hacia sus antecesores.
4. **Mostrar monarcas por casa**: Agrupa los monarcas por dinastía.
5. **Salir**: Termina el programa.

Ejemplo de interacción:
```
=== Historia en Código: Linajes Reales ===
1. Ver todos los monarcas
2. Buscar monarca por nombre
3. Mostrar linaje (antecesor)
4. Mostrar monarcas por casa
5. Salir
Elige una opción (1-5): 2
Nombre del monarca (ej: Carlos III): Isabel II

Isabel II:
Reinado: 1952-2022
Casa: Windsor
Antecesor: Jorge VI
Sucesor: Carlos III
```

## Estructura del proyecto

```
<nombre-repositorio>/
├── monarchy.json    # Datos de los monarcas en formato JSON
├── history.py      # Script principal con el menú interactivo
└── README.md       # Documentación del proyecto
```

### Formato de `monarchy.json`
El archivo `monarchy.json` contiene un diccionario con la siguiente estructura para cada monarca:
```json
{
  "Nombre": {
    "reinado": "AñoInicio-AñoFin",
    "casa": "NombreCasa",
    "antecesor": "NombreAntecesor",
    "sucesor": "NombreSucesor"
  }
}
```
Ejemplo:
```json
{
  "Carlos III": {
    "reinado": "2022-presente",
    "casa": "Windsor",
    "antecesor": "Isabel II",
    "sucesor": "-"
  }
}
```

## Posibles mejoras futuras

- **API REST**: Implementar una API con Flask o FastAPI para consultar los datos de los monarcas desde una interfaz web.
- **Base de datos**: Migrar los datos a SQLite o MongoDB para demostrar habilidades con bases de datos.
- **Visualización**: Agregar gráficos (ej. con Matplotlib) para mostrar líneas de tiempo de reinados o distribución de monarcas por casa.
- **Pruebas unitarias**: Incorporar pruebas con `unittest` para validar la funcionalidad del programa.
- **Interfaz web**: Crear un frontend simple con HTML/CSS/JavaScript para interactuar con los datos.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto, por favor:
1. Haz un fork del repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios y haz commit (`git commit -m "Añadir nueva funcionalidad"`).
4. Envía un pull request.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).

## Autor

[Briant Posada] - [Gmail](vladmirposada99@gmail.com)  
GitHub: [BriantPosada](https://github.com/BriantPosada)
