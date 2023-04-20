class LocalParent :
    """
    la classe parent des locals
    """
    def __init__(self,p_type_local = "", p_numero_local = "", p_Lieu_local = "", p_dimension_local = "",p_nbr_places = ""):
        """
        Le constructeur de la classe parent local
        """
        self.type_local = p_type_local              # Attribut public combo box
        self._numero_local = p_numero_local         # Attribut privé
        self.Lieu_local = p_Lieu_local              # Attribut public combo box
        self._dimension_local = p_dimension_local   # Attribut privé
        self._nbr_places = p_nbr_places             # Attribut privé

    # Les methodes getter et setter
    # Pour le numero local
    def _getNumeroLocal(self):
        return self._numero_local

    def _setNumeroLocal(self,pNumeroLocal):
        # Validation : composé d’une lettre suivi  d’un tiret  puis de 3 chiffres  : Exemple : F-230
        if pNumeroLocal[0].isalpha() and pNumeroLocal[1] == "-" and pNumeroLocal[2:4].isnumeric() and len(pNumeroLocal) == 4 :
            self._numero_local = pNumeroLocal
    # la proprité  du numero local
    NumeroLocal=property(_getNumeroLocal,_setNumeroLocal)

    # le getter et setter de la dimension du local
    def _getDimensionLocal(self):
        return self._dimension_local

    def _setDimensionLocal(self,pdimension):
        if pdimension > 0:
            self._dimension_local = pdimension

    # la propriété de la dimension local :
    DimensionLocal = property(_getDimensionLocal,_setDimensionLocal)
    # Pour nbr_places les méthodes d'accès
    def _getNbr_places(self):
        return self._nbr_places

    def _setNbr_places(self,valeurNbr_places):
        if valeurNbr_places > 0 and valeurNbr_places < 25:
            self._nbr_places = valeurNbr_places






