import csv

# ============================================================
# TPI - Gestion de Datos de Paises en Python
# Programacion 1 - UTN
# ============================================================

# -------------------------
# CONSTANTES
# -------------------------
ARCHIVO_CSV = "paises.csv"


# ============================================================
# MODULO 1: MANEJO DE ARCHIVOS
# ============================================================

def cargar_paises(archivo):
    """
    Lee el archivo CSV y devuelve una lista de diccionarios.
    Cada diccionario representa un pais con sus datos.
    """
    paises = []

    try:
        with open(archivo, mode="r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                # Validamos que no haya campos vacios
                if not fila["nombre"] or not fila["poblacion"] or not fila["superficie"] or not fila["continente"]:
                    print(f"  [!] Fila ignorada por campos vacios: {fila}")
                    continue

                # Convertimos los datos numericos
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                }
                paises.append(pais)

        print(f"  [OK] Se cargaron {len(paises)} paises desde '{archivo}'.")

    except FileNotFoundError:
        print(f"  [ERROR] No se encontro el archivo '{archivo}'.")
    except ValueError as e:
        print(f"  [ERROR] Dato invalido en el CSV: {e}")

    return paises


def guardar_paises(paises, archivo):
    """
    Guarda la lista de paises en el archivo CSV.
    """
    try:
        with open(archivo, mode="w", encoding="utf-8", newline="") as f:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(f, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(paises)

        print(f"  [OK] Datos guardados en '{archivo}'.")

    except Exception as e:
        print(f"  [ERROR] No se pudo guardar el archivo: {e}")


# ============================================================
# MODULO 2: AGREGAR Y ACTUALIZAR
# ============================================================

def agregar_pais(paises):
    """
    Solicita los datos de un nuevo pais y lo agrega a la lista.
    No se permiten campos vacios.
    """
    print("\n--- AGREGAR PAIS ---")

    # Nombre
    while True:
        nombre = input("  Nombre del pais: ").strip()
        if nombre:
            break
        print("  [!] El nombre no puede estar vacio.")

    # Verificar que no exista ya
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"  [!] Ya existe un pais con el nombre '{nombre}'.")
            return

    # Poblacion
    while True:
        try:
            poblacion = int(input("  Poblacion: ").strip())
            if poblacion > 0:
                break
            print("  [!] La poblacion debe ser un numero positivo.")
        except ValueError:
            print("  [!] Ingresa un numero entero valido.")

    # Superficie
    while True:
        try:
            superficie = int(input("  Superficie (km²): ").strip())
            if superficie > 0:
                break
            print("  [!] La superficie debe ser un numero positivo.")
        except ValueError:
            print("  [!] Ingresa un numero entero valido.")

    # Continente
    while True:
        continente = input("  Continente: ").strip()
        if continente:
            break
        print("  [!] El continente no puede estar vacio.")

    # Crear y agregar el diccionario
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    guardar_paises(paises, ARCHIVO_CSV)
    print(f"  [OK] Pais '{nombre}' agregado correctamente.")


def actualizar_pais(paises):
    """
    Actualiza la poblacion y/o superficie de un pais existente.
    """
    print("\n--- ACTUALIZAR PAIS ---")
    nombre = input("  Nombre del pais a actualizar: ").strip()

    # Buscar el pais
    pais_encontrado = None
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            pais_encontrado = p
            break

    if pais_encontrado is None:
        print(f"  [!] No se encontro el pais '{nombre}'.")
        return

    print(f"  Pais encontrado: {pais_encontrado['nombre']}")
    print(f"  Poblacion actual: {pais_encontrado['poblacion']:,}")
    print(f"  Superficie actual: {pais_encontrado['superficie']:,} km²")

    # Actualizar poblacion
    while True:
        try:
            nueva_pob = input("  Nueva poblacion (Enter para mantener): ").strip()
            if nueva_pob == "":
                break
            nueva_pob = int(nueva_pob)
            if nueva_pob > 0:
                pais_encontrado["poblacion"] = nueva_pob
                break
            print("  [!] Debe ser un numero positivo.")
        except ValueError:
            print("  [!] Ingresa un numero entero valido.")

    # Actualizar superficie
    while True:
        try:
            nueva_sup = input("  Nueva superficie en km² (Enter para mantener): ").strip()
            if nueva_sup == "":
                break
            nueva_sup = int(nueva_sup)
            if nueva_sup > 0:
                pais_encontrado["superficie"] = nueva_sup
                break
            print("  [!] Debe ser un numero positivo.")
        except ValueError:
            print("  [!] Ingresa un numero entero valido.")

    guardar_paises(paises, ARCHIVO_CSV)
    print(f"  [OK] Pais '{pais_encontrado['nombre']}' actualizado.")


# ============================================================
# MODULO 3: BUSQUEDA
# ============================================================

def buscar_pais(paises):
    """
    Busca paises por nombre (coincidencia parcial o exacta).
    """
    print("\n--- BUSCAR PAIS ---")
    termino = input("  Ingresa el nombre (o parte del nombre): ").strip().lower()

    if not termino:
        print("  [!] Ingresa al menos un caracter para buscar.")
        return

    resultados = []
    for p in paises:
        if termino in p["nombre"].lower():
            resultados.append(p)

    if resultados:
        print(f"\n  Se encontraron {len(resultados)} resultado(s):\n")
        mostrar_tabla(resultados)
    else:
        print(f"  [!] No se encontraron paises con '{termino}'.")


# ============================================================
# MODULO 4: FILTROS
# ============================================================

def filtrar_por_continente(paises):
    """
    Filtra y muestra paises de un continente especifico.
    """
    print("\n--- FILTRAR POR CONTINENTE ---")
    continente = input("  Ingresa el continente: ").strip()

    if not continente:
        print("  [!] El continente no puede estar vacio.")
        return

    resultados = []
    for p in paises:
        if p["continente"].lower() == continente.lower():
            resultados.append(p)

    if resultados:
        print(f"\n  Paises en {continente.capitalize()}:\n")
        mostrar_tabla(resultados)
    else:
        print(f"  [!] No se encontraron paises en '{continente}'.")


def filtrar_por_rango_poblacion(paises):
    """
    Filtra paises cuya poblacion este dentro de un rango dado.
    """
    print("\n--- FILTRAR POR RANGO DE POBLACION ---")

    try:
        minimo = int(input("  Poblacion minima: ").strip())
        maximo = int(input("  Poblacion maxima: ").strip())
    except ValueError:
        print("  [!] Ingresa numeros enteros validos.")
        return

    if minimo > maximo:
        print("  [!] El minimo no puede ser mayor al maximo.")
        return

    resultados = []
    for p in paises:
        if minimo <= p["poblacion"] <= maximo:
            resultados.append(p)

    if resultados:
        print(f"\n  Paises con poblacion entre {minimo:,} y {maximo:,}:\n")
        mostrar_tabla(resultados)
    else:
        print("  [!] No se encontraron paises en ese rango de poblacion.")


def filtrar_por_rango_superficie(paises):
    """
    Filtra paises cuya superficie este dentro de un rango dado.
    """
    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")

    try:
        minimo = int(input("  Superficie minima (km²): ").strip())
        maximo = int(input("  Superficie maxima (km²): ").strip())
    except ValueError:
        print("  [!] Ingresa numeros enteros validos.")
        return

    if minimo > maximo:
        print("  [!] El minimo no puede ser mayor al maximo.")
        return

    resultados = []
    for p in paises:
        if minimo <= p["superficie"] <= maximo:
            resultados.append(p)

    if resultados:
        print(f"\n  Paises con superficie entre {minimo:,} y {maximo:,} km²:\n")
        mostrar_tabla(resultados)
    else:
        print("  [!] No se encontraron paises en ese rango de superficie.")


# ============================================================
# MODULO 5: ORDENAMIENTOS
# ============================================================

def ordenar_paises(paises):
    """
    Ordena la lista de paises por nombre, poblacion o superficie,
    en orden ascendente o descendente.
    """
    print("\n--- ORDENAR PAISES ---")
    print("  Ordenar por:")
    print("  1. Nombre")
    print("  2. Poblacion")
    print("  3. Superficie")

    opcion = input("  Opcion: ").strip()

    if opcion == "1":
        clave = "nombre"
    elif opcion == "2":
        clave = "poblacion"
    elif opcion == "3":
        clave = "superficie"
    else:
        print("  [!] Opcion invalida.")
        return

    print("  Orden:")
    print("  1. Ascendente")
    print("  2. Descendente")
    orden = input("  Opcion: ").strip()

    if orden == "1":
        descendente = False
    elif orden == "2":
        descendente = True
    else:
        print("  [!] Opcion invalida.")
        return

    # Ordenamiento con sorted() y funcion lambda
    paises_ordenados = sorted(paises, key=lambda p: p[clave], reverse=descendente)

    direccion = "descendente" if descendente else "ascendente"
    print(f"\n  Lista ordenada por {clave} ({direccion}):\n")
    mostrar_tabla(paises_ordenados)


# ============================================================
# MODULO 6: ESTADISTICAS
# ============================================================

def mostrar_estadisticas(paises):
    """
    Calcula y muestra estadisticas generales del dataset.
    """
    print("\n--- ESTADISTICAS ---")

    if not paises:
        print("  [!] No hay paises cargados.")
        return

    # Pais con mayor y menor poblacion
    mayor_pob = paises[0]
    menor_pob = paises[0]
    for p in paises:
        if p["poblacion"] > mayor_pob["poblacion"]:
            mayor_pob = p
        if p["poblacion"] < menor_pob["poblacion"]:
            menor_pob = p

    # Promedios
    total_pob = 0
    total_sup = 0
    for p in paises:
        total_pob += p["poblacion"]
        total_sup += p["superficie"]

    promedio_pob = total_pob // len(paises)
    promedio_sup = total_sup // len(paises)

    # Cantidad de paises por continente
    continentes = {}
    for p in paises:
        c = p["continente"]
        if c in continentes:
            continentes[c] += 1
        else:
            continentes[c] = 1

    # Mostrar resultados
    print(f"\n  Total de paises cargados : {len(paises)}")
    print(f"\n  Pais con MAYOR poblacion : {mayor_pob['nombre']} ({mayor_pob['poblacion']:,} hab.)")
    print(f"  Pais con MENOR poblacion : {menor_pob['nombre']} ({menor_pob['poblacion']:,} hab.)")
    print(f"\n  Promedio de poblacion    : {promedio_pob:,} hab.")
    print(f"  Promedio de superficie   : {promedio_sup:,} km²")

    print("\n  Paises por continente:")
    for continente, cantidad in continentes.items():
        print(f"    - {continente}: {cantidad} pais/es")


# ============================================================
# MODULO 7: UTILIDADES
# ============================================================

def mostrar_tabla(lista):
    """
    Muestra una lista de paises en formato de tabla en consola.
    """
    print(f"  {'NOMBRE':<25} {'POBLACION':>15} {'SUPERFICIE (km²)':>18} {'CONTINENTE':<12}")
    print("  " + "-" * 73)
    for p in lista:
        print(f"  {p['nombre']:<25} {p['poblacion']:>15,} {p['superficie']:>18,} {p['continente']:<12}")
    print()


def mostrar_todos(paises):
    """
    Muestra todos los paises cargados en el sistema.
    """
    print("\n--- LISTADO COMPLETO DE PAISES ---\n")
    if not paises:
        print("  [!] No hay paises cargados.")
    else:
        mostrar_tabla(paises)


# ============================================================
# MODULO 8: MENU PRINCIPAL
# ============================================================

def mostrar_menu():
    """
    Muestra el menu principal del sistema.
    """
    print("\n" + "=" * 50)
    print("   SISTEMA DE GESTION DE PAISES")
    print("=" * 50)
    print("  1. Mostrar todos los paises")
    print("  2. Agregar un pais")
    print("  3. Actualizar datos de un pais")
    print("  4. Buscar pais por nombre")
    print("  --- FILTROS ---")
    print("  5. Filtrar por continente")
    print("  6. Filtrar por rango de poblacion")
    print("  7. Filtrar por rango de superficie")
    print("  --- ORDENAR ---")
    print("  8. Ordenar paises")
    print("  --- ESTADISTICAS ---")
    print("  9. Ver estadisticas")
    print("  --- SALIR ---")
    print("  0. Salir del programa")
    print("=" * 50)


def main():
    """
    Funcion principal. Carga los datos e inicia el menu.
    """
    print("\nCargando datos...")
    paises = cargar_paises(ARCHIVO_CSV)

    while True:
        mostrar_menu()
        opcion = input("  Selecciona una opcion: ").strip()

        if opcion == "1":
            mostrar_todos(paises)
        elif opcion == "2":
            agregar_pais(paises)
        elif opcion == "3":
            actualizar_pais(paises)
        elif opcion == "4":
            buscar_pais(paises)
        elif opcion == "5":
            filtrar_por_continente(paises)
        elif opcion == "6":
            filtrar_por_rango_poblacion(paises)
        elif opcion == "7":
            filtrar_por_rango_superficie(paises)
        elif opcion == "8":
            ordenar_paises(paises)
        elif opcion == "9":
            mostrar_estadisticas(paises)
        elif opcion == "0":
            print("\n  ¡Hasta luego!\n")
            break
        else:
            print("  [!] Opcion invalida. Ingresa un numero del 0 al 9.")


# ============================================================
# PUNTO DE ENTRADA
# ============================================================
if __name__ == "__main__":
    main()
