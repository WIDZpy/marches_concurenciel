import json

import numpy as np

import source.entiti.agent.vendeur as _vendeur
import source.entiti.bien as _bien
import source.entiti.agent.acheteur as _acheteur


def gen_acheteur(nb: int = 1, paterne: str = 'void') -> list[_acheteur.Acheteur]:
	"""Le paterne doit etre le chmein d'un fichier Json
	"""
	assert nb is int and nb > 0, "le nombre doit être un entié positif"
	parametre = _acheteur.DEFAULT_PARAMETRE.copy().update(json.loads(open(paterne).read()))

	result = []

	for acheteur in range(nb):
		sold = parametre.get("sold", 0)
		if sold is dict
		result.append(_acheteur.Acheteur(sold=sold,))

	return result
