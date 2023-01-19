import source.entiti.bien as _bien
import source.entiti.agent as _agent


class Vendeur(_agent.Agent):
    def __init__(self):
        super().__init__()

    def vend(self, bien: _bien.Bien, prix, quantite: int = 1):
        self.sold += prix
        self.perdre_bien(bien, quantite)

    def get_vend(self, bien: _bien.Bien, prix, quantite: int = 1):
        return self.stock.get(bien, 0) >= quantite




