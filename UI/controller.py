from operator import truediv

import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self.grafo=None


    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO

        self.grafo=self._model.build_graph()



    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        # TODO
        squadra= self._view.dd_squadra.value
        if squadra is None:
            self._view.show_alert("Seleziona una squadra!")
            return
        try:
            id_squadra = int(squadra)
        except ValueError:
            self._view.show_alert("Errore nel valore della squadra")
            return

        if  self.grafo is None:
            self._view.show_alert("Crea grafo!")
            return


        componente=self._model.get_component(id_squadra)

        self._view.txt_risultato.controls.clear()

        for vicino,peso in componente:
            vicino_obj = self._model._idMap[vicino]
            self._view.txt_risultato.controls.append(ft.Text(f" {vicino_obj.team_code} ({vicino_obj.name}) - peso {peso}"))

        self._view.page.update()




    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO
        squadra= self._view.dd_squadra.value
        if squadra is None:
            self._view.show_alert("Seleziona una squadra!")
            return
        try:
            id_squadra = int(squadra)
        except ValueError:
            self._view.show_alert("Errore nel valore della squadra")
            return

        if  self.grafo is None:
            self._view.show_alert("Crea grafo!")
            return

        best_path,peso=self._model.best_path(id_squadra)

        self._view.txt_risultato.controls.clear()
        peso_totale=0
        for i in range(len(best_path) - 1):
            s1=best_path[i]
            s2=best_path[i+1]
            w=self._model.G[s1.id][s2.id]['weight']
            peso_totale+=w

            self._view.txt_risultato.controls.append(ft.Text(f" {s1.team_code} ({s1.name}) --> {s2.team_code} ({s2.name}) (peso {w})"))
        self._view.txt_risultato.controls.append(ft.Text(f"Peso totale: {peso_totale}"))
        self._view.page.update()






    """ Altri possibili metodi per gestire di dd_anno """""



    def popola_anno(self):
        anno=self._model.get_anno()

        self._view.dd_anno.options=[ft.dropdown.Option(a) for a in anno]

        self._view.page.update()





    def popola_lista_squadre_anno(self,e):

        try:
            anno = self._view.dd_anno.value
        except (ValueError, TypeError):
            self._view.show_alert("Inserisci un anno!")
            return

        squadre=self._model.get_squadre(anno)

        conteggio=len(squadre)


        self._view.txt_out_squadre.controls.clear()
        self._view.dd_squadra.options.clear()
        self._view.txt_out_squadre.controls.append(ft.Text(f"Numero di squadre: {conteggio}"))
        for s in squadre:
            if not s:
                self._view.alert("seleziona anno!")
            else:
                self._view.txt_out_squadre.controls.append(ft.Text(f"{s.team_code} ({s.name} )"))
                self._view.dd_squadra.options.append(
                    ft.dropdown.Option(
                        key=s.id,
                        text=f"{s.team_code} ({s.name})"
                    )
                )

        self._view.page.update()



