# Historia en Código: Linajes Reales
# Proyecto para demostrar habilidades de backend con datos históricos de monarcas ingleses y británicos

# Datos de monarcas (completo desde Guillermo I hasta Carlos III)

import json

def cargar_monarcas(archivo="monarchy.json"):
    try:
        with open(archivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File Not Found")
        return {}
monarcas = cargar_monarcas()
    


def mostrar_menu():
    """
    Muestra un menú interactivo para consultar información sobre los monarcas ingleses y británicos.
    Permite listar monarcas, buscar por nombre, mostrar linaje por antecesores, y agrupar por casa.
    """
    while True:
        print("\n=== Historia en Código: Linajes Reales ===")
        print("1. Ver todos los monarcas")
        print("2. Buscar monarca por nombre")
        print("3. Mostrar linaje (antecesor)")
        print("4. Mostrar monarcas por casa")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "1":
            print("\nLista de monarcas:")
            for nombre, info in monarcas.items():
                if "Interregno" not in nombre:  # Excluye interregnos de la lista
                    print(f"{nombre} ({info['reinado']}, Casa {info['casa']})")

        elif opcion == "2":
            nombre = input("Nombre del monarca (ej: Carlos III): ").strip()
            nombre = nombre.title()  # Normaliza entrada (primera letra mayúscula)
            if nombre in monarcas:
                info = monarcas[nombre]
                print(f"\n{nombre}:")
                print(f"Reinado: {info['reinado']}")
                print(f"Casa: {info['casa']}")
                print(f"Antecesor: {info['antecesor']}")
                print(f"Sucesor: {info['sucesor']}")
            else:
                print("Monarca no encontrado. Intenta de nuevo.")

        elif opcion == "3":
            nombre = input("Empezar linaje desde (ej: Carlos III): ").strip()
            nombre = nombre.title()
            if nombre in monarcas:
                print(f"\nLinaje de {nombre} (hacia antecesores):")
                actual = nombre
                while actual in monarcas and "Interregno" not in actual:
                    print(f"{actual} ← {monarcas[actual]['antecesor']}")
                    actual = monarcas[actual]['antecesor']
            else:
                print("Monarca no encontrado.")

        elif opcion == "4":
            print("\nMonarcas agrupados por casa:")
            casas = {}
            for nombre, info in monarcas.items():
                if "Interregno" not in nombre:  # Excluye interregnos
                    casa = info['casa']
                    if casa not in casas:
                        casas[casa] = []
                    casas[casa].append(f"{nombre} ({info['reinado']})")
            for casa, lista in casas.items():
                print(f"\nCasa {casa}:")
                for monarca in lista:
                    print(f"  - {monarca}")

        elif opcion == "5":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecuta el programa
if __name__ == "__main__":
    try:
        mostrar_menu()
    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario. ¡Adiós!")