# 1. Mamifero --> Domestico --> Perro

# Clase padre
class Mamifero:
    def __init__(self, nombre, edad, raza, sexo):
        # Atributos protegidos, que son accesibles en clases hijas
        self._nombre = nombre
        self._edad = edad
        self._raza = raza
        self._sexo = sexo

    def hablar(self):
        print(f'\n{self._nombre} hace un ruido.\n')

    def descripcion(self):
        print(f'\nNombre: {self._nombre}\nEdad: {self._edad}\nRaza: {self._raza}\nSexo: {self._sexo}\n')



# Clase hija Domestico
class Domestico(Mamifero):
    def __init__(self, nombre, edad, raza, sexo, tipo_alimentacion):
        super().__init__(nombre, edad, raza, sexo)
        self._tipo_alimentacion = tipo_alimentacion

    def domestico(self):
        print(f'\n{self._nombre} es un animal domestico y se alimenta de {self._tipo_alimentacion}.\n')



# Clase hija Perro
class Perro(Mamifero):
    def __init__(self, nombre, edad, raza, sexo, mezcla_perro='No'):
        super().__init__(nombre, edad, raza, sexo)
        self._mezcla_perro = mezcla_perro  # corregido

    # Sobreescribir hablar
    def hablar(self):
        print(f'\n{self._nombre} dice: ¡Guau!\n')

    # Método propio para mostrar detalles del perro
    def desc_perro(self):
        print(f'\nDatos del perro:')
        print(f'Nombre: {self._nombre}')
        print(f'Edad: {self._edad}')
        print(f'Raza: {self._raza}')
        print(f'Sexo: {self._sexo}')
        print(f'Raza Mezclada: {self._mezcla_perro}\n')



# Crear objetos para probar
mamifero_uno = Mamifero('Gato', 3, 'Siames', 'Macho')
mamifero_uno.hablar()
mamifero_uno.descripcion()

domestico_uno = Domestico('Conejo', 3, 'Mestizo', 'Macho', 'Vegetales')
domestico_uno.domestico()
domestico_uno.descripcion()

perro_uno = Perro('Pancha', 9, 'Pitbull', 'Hembra')
perro_uno.hablar()
perro_uno.desc_perro()


"""

    Aclararión:

        Los campos 'nombre', 'edad', 'raza' y 'sexo' en las clases Domestico y Perro:
            NO SE ESTÁN REPITIENDO dentro de las clases hijas.
        
        Estos campos son atributos de la clase padre. Las clases hijas los reciben como 
        parametros en su constructor para pasarlos con 'super()__init__' al constructor de Mamifero.
        
        Asi las clases hijas NO DUPLICAN ATRIBUTOS. Solo piden la informacion para inicializarlos 
        correctamente en la clase padre.
        
        Las clases hijas NO SABEN cómo se llama cada atributo en la clase padre ni tienen acceso al
        constructor automáticamente si no se les pasa.
        
        Les permite:
        
                1. Crear un 'Perro' se pueda definir el nombre, edad, raza y sexo y el atributo propio
                de la clase hija que es la 'mezcla_perro'.
                
                2. Los atributos de 'Mamifero' sean inicializados correctamente y existan en la instancia hija.
                
        
        No es repetición real. Las clases hijas solo piden estos parámetros para inicializar la clase padre.
        
        Es la forma enq ue 'super()' permite inicializar atributos heredados de forma clara y estructurada.
        
        Así puedes mantener el código organizado y que cada objeto cuente con todos sus atributos.
             
"""