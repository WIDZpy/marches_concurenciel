import source.entiti as _entite
import source.entiti.bien as _bien

import json


class Agent(_entite.Entite):
    def __init__(self, sold):
        """un agent est une entité économique capable d'aquérire ou perdre des bien"""
        super().__init__()
        self.stock = {}
        self.sold = sold

    ##########################---bien---##########################

    def a_bien(self, bien: _bien.Bien, quantite: int = 1) -> bool:
        """:return: true si l'afent a en quentité sufisente le bien"""
        return self.stock.get(bien, 0) >= quantite

    def acquerir_bien(self, bien: _bien.Bien, quantite: int = 1) -> None:
        """
        fait aquérire une certaine quentité d'un objet BIen a l'agent
        """
        self.stock.update({bien: self.stock.get(bien, 0) + quantite})

    def perdre_bien(self, bien: _bien.Bien, quantite: int = 1):
        if self.a_bien(bien, quantite):
            self.stock[bien] = self.stock.get(bien) - quantite
        else:
            raise Exception(f"l' agent ne poséde pas ce bien dans les quantité sufisante"
                            f"\nquantité demendé : {quantite}\nquantité possédé : {self.stock[bien]}")


if __name__ == '__main__':
    a = Agent()
    a.pay(a)