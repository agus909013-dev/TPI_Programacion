# TPI_Programacion
# Gestión de Datos de Países en Python

**Trabajo Práctico Integrador - Programación 1**
Universidad Tecnológica Nacional - Tecnicatura Universitaria en Programación a Distancia

---

## Descripción

Aplicación de consola desarrollada en Python 3 que permite gestionar información sobre países del mundo. El sistema lee datos desde un archivo CSV y ofrece un menú interactivo con funcionalidades de búsqueda, filtrado, ordenamiento y estadísticas.

---

## Integrantes

| Nombre | Rol |
|---|---|
| Agus Schmaedke | Desarrollador |
| Roberto Duprat | Desarrollador |

---

## Tecnologías utilizadas

- Python 3.x
- Módulo `csv` (biblioteca estándar)
- Sin dependencias externas

---

## Estructura del proyecto

```
/
├── gestion_paises.py   # Código fuente principal
├── paises.csv          # Dataset base de países
└── README.md           # Este archivo
```

---

## Instrucciones de uso

### 1. Requisitos previos

Tener instalado Python 3 en el sistema. Para verificarlo:

```bash
python --version
```

### 2. Clonar o descargar el repositorio

```bash
git clone https://github.com/[USUARIO]/[REPOSITORIO].git
cd [REPOSITORIO]
```

### 3. Ejecutar el programa

Asegurate de que `gestion_paises.py` y `paises.csv` estén en la misma carpeta, luego ejecutá:

```bash
python gestion_paises.py
```

---

## Menú de opciones

Al ejecutar el programa se muestra el siguiente menú:

```
==================================================
   SISTEMA DE GESTIÓN DE PAÍSES
==================================================
  1. Mostrar todos los países
  2. Agregar un país
  3. Actualizar datos de un país
  4. Buscar país por nombre
  --- FILTROS ---
  5. Filtrar por continente
  6. Filtrar por rango de población
  7. Filtrar por rango de superficie
  --- ORDENAR ---
  8. Ordenar países
  --- ESTADÍSTICAS ---
  9. Ver estadísticas
  --- SALIR ---
  0. Salir del programa
==================================================
```

---

## Ejemplos de entradas y salidas

### Mostrar todos los países (opción 1)

```
Seleccioná una opción: 1

--- LISTADO COMPLETO DE PAÍSES ---

  NOMBRE                          POBLACIÓN   SUPERFICIE (km²) CONTINENTE
  -------------------------------------------------------------------------
  Argentina                      45,376,763          2,780,400 América
  Japón                         125,800,000            377,975 Asia
  Nigeria                       211,400,708            923,768 África
  Alemania                       83,149,300            357,022 Europa
```

### Agregar un país (opción 2)

```
Seleccioná una opción: 2

--- AGREGAR PAÍS ---
  Nombre del país: Francia
  Población: 67413000
  Superficie (km²): 551695
  Continente: Europa
  [OK] País 'Francia' agregado correctamente.
```

### Buscar país por nombre (opción 4)

```
Seleccioná una opción: 4

--- BUSCAR PAÍS ---
  Ingresá el nombre (o parte del nombre): arg

  Se encontraron 1 resultado(s):

  NOMBRE                          POBLACIÓN   SUPERFICIE (km²) CONTINENTE
  -------------------------------------------------------------------------
  Argentina                      45,376,763          2,780,400 América
```

### Filtrar por continente (opción 5)

```
Seleccioná una opción: 5

--- FILTRAR POR CONTINENTE ---
  Ingresá el continente: Europa

  Países en Europa:

  NOMBRE                          POBLACIÓN   SUPERFICIE (km²) CONTINENTE
  -------------------------------------------------------------------------
  Alemania                       83,149,300            357,022 Europa
```

### Ordenar países (opción 8)

```
Seleccioná una opción: 8

--- ORDENAR PAÍSES ---
  Ordenar por:
  1. Nombre
  2. Población
  3. Superficie
  Opción: 2
  Orden:
  1. Ascendente
  2. Descendente
  Opción: 2

  Lista ordenada por población (descendente):

  NOMBRE                          POBLACIÓN   SUPERFICIE (km²) CONTINENTE
  -------------------------------------------------------------------------
  Nigeria                       211,400,708            923,768 África
  Japón                         125,800,000            377,975 Asia
  Alemania                       83,149,300            357,022 Europa
  Argentina                      45,376,763          2,780,400 América
```

### Ver estadísticas (opción 9)

```
Seleccioná una opción: 9

--- ESTADÍSTICAS ---

  Total de países cargados : 4

  País con MAYOR población : Nigeria (211,400,708 hab.)
  País con MENOR población : Argentina (45,376,763 hab.)

  Promedio de población    : 116,431,692 hab.
  Promedio de superficie   : 1,109,791 km²

  Países por continente:
    - América: 1 país/es
    - Asia: 1 país/es
    - África: 1 país/es
    - Europa: 1 país/es
```

### Ejemplo de validación de error

```
  Población: abc
  [!] Ingresá un número entero válido.
  Población: -500
  [!] La población debe ser un número positivo.
  Población: 50000000
```

---

## Dataset base (paises.csv)

```csv
nombre,poblacion,superficie,continente
Argentina,45376763,2780400,América
Japón,125800000,377975,Asia
Nigeria,211400708,923768,África
Alemania,83149300,357022,Europa
