def welcome_message():

    nombre = input("Por favor ingrese su nombre: ")
    atencion = input("Qué fue lo que más te llamo la atención del curso: ")
    #ciudad = input("Por favor agrega tu ciudad: ")                 
    print("Bienvenido, ", nombre, " al curso de Django y React")
    print("Esperamos que aprendas mucho sobre ", atencion)
    #print("Esperamos que disfrutes tu estadia en ", ciudad) 

if __name__ == "__main__":
    welcome_message()  