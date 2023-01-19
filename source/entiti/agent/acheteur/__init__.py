import source.entiti.agent as _agent
import source.entiti.agent.vendeur as _vendeur
import source.entiti.bien as _bien


def generaion_acheteur(nb: int = 1, paterne: str = 'void'):
    for acheteur in range(nb):
        pass


class Acheteur(_agent.Agent):
    def __init__(self):
        super().__init__()

    def achete(self, sible: _vendeur.Vendeur, bien: _bien.Bien, prix):
        if sible.get_vend(bien, prix):
            self.sold -= prix

            sible.vend(bien, prix)
            self.aquerire_bien(bien)

