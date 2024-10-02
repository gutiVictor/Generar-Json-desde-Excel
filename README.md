# Conversión de Excel a JSON

Este proyecto permite convertir un archivo Excel que contiene datos de productos en un formato JSON estructurado. Es útil para manejar datos de inventario y facilitar su integración en aplicaciones web o de backend.

## Estructura del Archivo Excel

El archivo Excel debe tener la siguiente estructura:

| Código   | Descripción                            | Referencia |
|----------|----------------------------------------|------------|
| 7200034  | COJIN ESTABILIZADOR EXTRASUAVE       | ABA0034    |
| 7200035  | COCHE PASEADOR                        | ABA0035    |
| 7200036  | COCHE MOISES PEQUEÑO                 | ABA0036    |
| ...      | ...                                    | ...        |

- **Código**: Identificador único del producto.
- **Descripción**: Nombre o descripción del producto.
- **Referencia**: Referencia interna o SKU del producto.

## Requisitos

Asegúrate de tener instalado Python y los siguientes paquetes:

- **pandas**: Para manipulación de datos.
- **openpyxl**: Para leer archivos Excel.

Puedes instalar las dependencias necesarias usando pip:

```bash
pip install pandas openpyxl



se ejecuta desde la terminal python index.py

