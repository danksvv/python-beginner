import importlib.util
import os


def main():
    while True:
        print("\n--- check module ---")
        print("1. Comprobar módulo")
        print("2. Salir")
        option = input("Selecciona una opción: ")
        if option == "1":
            module_name = input("Introduce el nombre del módulo a comprobar: ").lower()
            if importlib.util.find_spec(module_name) is not None:
                print(f"✅ El módulo '{module_name}' está instalado.")
            else:
                print(f"❌ El módulo '{module_name}' no está instalado.")
                option = input("Desear instalarlo? (s/n)").lower()
                if option == "s":
                    os.system(f"pip install {module_name}")
                else:
                    print("No se instalará el módulo")

        elif option == "2":
            print("Saliendo...")
            break


if __name__ == "__main__":
    main()
