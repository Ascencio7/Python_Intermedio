# Se crea la clase padre
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    
    def hablar(self):
        print(f'\n{self._nombre} hace un ruido.\n')
    
    def descripcion(self):
        print(f'\nNombre: {self._nombre}\nEdad: {self._edad}\n')
    
    
# Se crea la clase hija
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self._raza = raza
        
        
    # Se sobreescribe el metodo de hablar
    def hablar(self):
        print(f'\n{self._nombre} dice: !Guau, guau!\n')
    
    # Se agrega un metodo propio de la clase hija
    def mostrar_raza(self):
        print(f'\n{self._nombre} es de una raza llamada: {self._raza}\n')
    
    
# Se crean los objetos de la clase animal
animal_uno = Animal('Gato', 3)
animal_uno.descripcion()
animal_uno.hablar()

animal_dos = Animal('Perro', 5)
animal_dos.descripcion()
animal_uno.hablar()


# Se crea un objeto para la clase hija
perro_uno = Perro('Jack', 7, 'Pitbull')
perro_uno.descripcion()
perro_uno.hablar()
perro_uno.mostrar_raza()


"""
    En Python usando HERENCIA para el nombre de las variables NO SE PUEDEN
    DECLARA CON __ YA QUE SON PROPIEDADES PRIVADAS Y LA CLASE HIJA NO ACCEDERA A ELLAS.
    
    Solo se puede acceder de la clase hija si es sin guiones bajos o uno nada mas.
    
"""