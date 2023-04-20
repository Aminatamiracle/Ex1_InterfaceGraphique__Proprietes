from PyQt5.QtCore import pyqtSlot

import interfaceListeView
#importer la librairie QtWidgets de QtDesigner
from PyQt5 import QtWidgets
# Pour le gestionnairre d'événement
from PyQt5 import QtCore

class FenetreListView(QtWidgets.QDialog, interfaceListeView.Ui_Dialog):
    def __init__(self, parent = None):
        super(FenetreListView,self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        self.setWindowTitle("La liste des étudiants")


    # le gestionnaire d'événement du bouton Quitter
    @pyqtSlot()
    def on_btnQuitter_clicked(self):
        self.close()
