import source.entiti.bien as _bien
import source.entiti.agent as _agent


class Vendeur(_agent.Agent):
    def __init__(self):
        super().__init__()

    def vend(self, bien: _bien.Bien, prix):
        self.sold += prix
        self.perdre_bien(bien)

    def get_vend(self, bien: _bien.Bien, prix):
        return# testé si le vendeur a le bien




