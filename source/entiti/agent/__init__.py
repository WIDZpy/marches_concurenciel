import source.entiti as _entite
import source.entiti.bien as _bien

import json


class Agent(_entite.Entite):
    def __init__(self):
        super().__init__()
        self.stock = {}
        self.sold = 10

    def acquerir_bien(self, bien: _bien.Bien, quantite: int = 1):
        self.stock.update({bien: self.stock.get(bien, 0) + quantite})

    def a_bien(self, bien: _bien.Bien, quantite: int = 1):
        return self.stock.get(bien, 0) >= quantite

    def perdre_bien(self, bien: _bien.Bien, quantite: int = 1):
        if self.a_bien(bien, quantite):
            self.stock[bien] = self.stock.get(bien) - quantite
        else:
            raise Exception(f"l' agent ne poséde pas ce bien dans les quantité sufisante"
                            f"\nquantité demendé : {quantite}\nquantité possédé : {self.stock[bien]}")


