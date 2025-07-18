class Libro:
    # Atributos de clase (compartidos si no se sobrescriben en la instancia)
    Estado = 'No Registrado'

    def __init__(self):
        # Atributos de la instancia
        self.__Tamano = '17x24'
        self.__PrecioxPag = 300
        self.__PesoxPag = 0.8
        self.Paginas = 0
        self.PrecioVenta = 0
        self.Peso = 0
        self.Titulo = ''
        self.Tapa = ''
        self.URL = ''
        self.ISBN = ''

    def registrar_libro(self):
        # Actualizar el estado correctamente
        self.Estado = 'Registrado'

    def precio_x_pagina(self):
        return self.__PrecioxPag

    def peso_x_pagina(self):
        return self.__PesoxPag

    def tamano_libro(self):
        return self.__Tamano

    def datos_libro(self, num_pag, nombre, tipo_tapa, url_libro, isbn_libro):
        self.Paginas = num_pag
        self.PrecioVenta = self.precio_x_pagina() * num_pag
        self.Peso = self.peso_x_pagina() * num_pag
        self.Titulo = nombre
        self.Tapa = tipo_tapa
        self.URL = url_libro
        self.ISBN = isbn_libro
        self.registrar_libro()  # Cambia el estado a Registrado

    def recibe_datos_libro(self):
        print('\nIngrese los datos del libro:\n')
        nombre = input('Titulo del libro: ')
        num_pag = int(input('Numero de paginas: '))
        tipo_tapa = input('Tipo de tapa: ')
        url_libro = input('URL del libro: ')
        isbn_libro = input('ISBN del libro: ')
        self.datos_libro(num_pag, nombre, tipo_tapa, url_libro, isbn_libro)

    def muestra_datos_libro(self):
        print('\n========== DATOS DEL LIBRO ==========\n')
        print(f'Tamaño: {self.tamano_libro()}')
        print(f'Páginas: {self.Paginas}')
        print(f'Precio de venta: {self.PrecioVenta}')
        print(f'Peso: {self.Peso}')
        print(f'Precio por página: {self.precio_x_pagina()}')
        print(f'Peso por página: {self.peso_x_pagina()}')
        print(f'Título: {self.Titulo}')
        print(f'Tapa: {self.Tapa}')
        print(f'URL: {self.URL}')
        print(f'ISBN: {self.ISBN}')
        print(f'Estado: {self.Estado}')
        print('\n======================================\n')


# Uso del objeto
libro_uno = Libro()

# Ingreso de datos del libro
libro_uno.recibe_datos_libro()

# Mostrar los datos del libro
libro_uno.muestra_datos_libro()