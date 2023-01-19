import source.entiti as _entite
import source.entiti.bien as _bien

import json


class Agent(_entite.Entite):
    def __init__(self):
        super().__init__()
        self.stock = {
        }
        self.sold = 10

    def aquerire_bien(self, bien: _bien.Bien):
        self.stock.update({bien: self.stock.get(bien,0)+1})

    def perdre_bien(self, bien: _bien = 0):
        pass
