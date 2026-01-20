import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model


    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO

        year = self._view.dd_anno.value

        return self._model.crea_grafo(year)

    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        # TODO

    def popola_dd(self, e):
        anni = self._model.anni()  # chiama il metodo, non un attributo
        self._view.dd_anno.options.clear()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(str(anno)))
        self._view.update()




    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO

    """ Altri possibili metodi per gestire di dd_anno """""
    # TODO