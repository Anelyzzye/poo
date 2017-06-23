class Persona:
    nombre = ""
    edad = 0
    peso = 0
    saludo = ""

    def asignaPersona(self):
        print self.nombre,self.edad,self.peso

persona1 = Persona()
persona1.nombre = "Alfredo Paz Bastida"
persona1.peso = 78
persona1.edad = 28
persona1.asignaPersona()

persona2 = Persona()
persona2.nombre = "Maribel"
persona2.peso = 88
persona2.edad = 28
persona2.asignaPersona()