# Proyecto Odoo colaborativo - ETHEREAL

Proyecto de implantación de Odoo para la empresa simulada ETHEREAL.

## Objetivo
Configurar un entorno compartido de Odoo para que varios miembros del grupo puedan trabajar sobre la misma base de datos y responder a las necesidades de la empresa.

## Tecnologías usadas
- Odoo 17
- PostgreSQL (Neon)
- Docker
- GitHub

## Estructura del proyecto
- `custom_addons/`: módulos personalizados
- `config/`: configuración de Odoo
- `docker-compose.yml`: arranque del entorno
- `.env.example`: ejemplo de variables necesarias para conectarse a la base de datos

## Cómo levantar el proyecto
1. Clonar el repositorio
2. Crear un archivo `.env` a partir de `.env.example`
3. Rellenar las credenciales necesarias
4. Ejecutar:

```bash
docker compose up