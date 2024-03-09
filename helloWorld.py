def welcome_message():

    nombre = input("Ingrese su nombre:")
    atencion = input("Qué fue lo que más te llamó la atención del curso?")
    print("Bienvenidos, ", nombre, " al curso de Django y React")

if __name__ == "__main__":
    welcome_message()  