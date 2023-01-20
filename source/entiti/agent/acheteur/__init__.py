import source.entiti.agent as _agent
import source.entiti.agent.vendeur as _vendeur
import source.entiti.bien as _bien


def generaion_acheteur(nb: int = 1, paterne: str = 'void'):
    for acheteur in range(nb):
        pass


class Acheteur(_agent.Agent):
    def __init__(self):
        super().__init__()

    def peux_achete(self, prix):
        return prix >= self.sold

    def achete(self, sible: _vendeur.Vendeur, bien: _bien.Bien, prix: int, quantite: int = 1):
        if self.peux_achete(prix):
            if sible.get_vend(bien, prix, quantite):
                self.sold -= prix

                sible.vend(bien, prix, quantite)
                self.acquerir_bien(bien)


if __name__ == '__main__':
    ach = Acheteur()
    ven = _vendeur.Vendeur()
    bie = _bien.Bien()

    ven.acquerir_bien(bie, 10)
    print(ven.stock, ach.sold)
    ach.achete(ven, bie, prix=10, quantite=10)
    print(ven.stock, ach.sold)
    ach.achete(ven, bie, prix=10, quantite=10)
    print(ven.stock, ach.sold)






