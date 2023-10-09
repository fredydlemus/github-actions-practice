import os

def main():
    nombre = os.getenv("USERNAME")
    print(f"Hola {nombre} desde Github!")
    languaje = os.getenv("FAV_LANG")
    print(f"Tu lenguaje favorito es {languaje}!")

if __name__ == "__main__":
    main()