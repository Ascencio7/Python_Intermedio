# Libro --> Novela --> Romantica

class Libro:
    def __init__(self, titulo, autor, num_pags):
        self._titulo = titulo
        self._autor = autor
        self._num_pags = num_pags
        
    def get_titulo(self):
        print(f'\nNovela: {self._titulo} de {self._autor}\n')
        

class Novela(Libro):
    def __init__(self, titulo, autor, num_pags, genero = 'Sin género especificado'):
        super().__init__(titulo, autor, num_pags)
        self._genero = genero
        
    def get_genero(self):
        print(f'\nLa novela {self._titulo} de {self._autor} es del genero {self._genero}\n')
        

class Romantica(Libro):
    def __init__(self, titulo, autor, num_pags, genero = 'Sin género especificado'):
        super().__init__(titulo, autor, num_pags)
        self._genero = genero
        
    def novela_romantica(self):
        if self._genero == 'Romántica'.lower():
            print(f'\n{self._titulo} de {self._autor} es una novela romanticista\n')
        else:
            print(f'\nLa novela {self._titulo} de {self._autor} no es una novela romanticista\n')
            
            
novela_romantica = Romantica('IT', 'Stephen King', '1500', 'Terror')
novela_romantica.novela_romantica()