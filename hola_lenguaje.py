import os

def main():
    nombre = os.getenv("USERNAME")
    print(f"Hola {nombre} desde Github!")
    languaje = os.getenv("FAVORITE_LANGUAGE")
    print(f"Tu lenguaje favorito es {languaje}!")

if __name__ == "__main__":
    main()