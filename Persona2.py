# coding=utf-8
class Persona:
    nombre = ""
    edad = 0
    email = ""

#aquí defino un constructor, __init__ es un método predefinido de Python no lo debes de tratar de modificar
    def __init__(self, nombre, edad, email):
        self.edad = edad
        self.nombre = nombre
        self.email = email
#aquí defino un método
    def mostrarCredencial(self):
        print "Tu nombre es: ", self.nombre
        print "Tu edad es: ", self.edad
        print "Tu email es: ", self.email
#aquí defino al objeto y a su instancia
newPersona = Persona("Alfredo", 28, "ejemplo@hotmail.com")
newPersona.mostrarCredencial()