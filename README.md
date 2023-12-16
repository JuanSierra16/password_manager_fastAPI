# password_manager_fastAPI
Proyecto de Gestión de Contraseñas: API para gestionar un sistema de almacenamiento de contraseñas. 
La API permite al usuario añadir nuevas contraseñas (la contraseña se genera aleatoriamente), 
visualizar las contraseñas guardadas, actualizar detalles de contraseñas existentes y eliminar contraseñas.

## Requisitos
- Python 3.8+
- pip

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/yourusername/your-repo-name.git
```

2. Navega al directorio del proyecto:

```bash
cd your-repo-name
```
   
4. (Opcional) Crea un entorno virtual:

```bash
python -m venv venv
```
  
6. Activa el entorno virtual:

```bash
   source venv/bin/activate  # En Unix o MacOS
   venv\Scripts\activate     # En Windows
```

   
8. Instala las dependencias del proyecto:
   
```bash
   pip install -r requirements.txt
```
   
# Uso
Ejecutar el siguiente comando comando en la terminal:

```bash
   uvicorn main:app --reload --port 8000
```

Abrir el navegador y dirigirse a la dirección:
```bash
   http://localhost:8000/docs#/
```

# Base de datos - SQLite
Las contraseñsa y la información de los usuarios se guarda en un archivo llamado database.sqlite el cual se crea automaticamente una vez se empieze a utlizar la API y las tablas se pueden visualizar utilizando la extension de VS Code SQLite Viewer.

Disfruta de la API.
