import copy

import networkx as nx

from database.dao import DAO
from model.squadra import Squadra


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self.G = nx.Graph()
        self._idMap = {}
        self.soluzione_best=[]
        self.squadre= []
        self.K=3


    def get_squadre(self, anno):

        self.squadre= DAO.get_squadre(anno)


        return self.squadre

    def get_anno(self):
        anno=DAO.get_anno()

        return anno





    def build_graph(self):
        self.G.clear()

        if len(self.squadre)==0:
            print(f"impossibile creare grafo")
            return

        self.G.add_nodes_from([s.id for s in self.squadre])

        for s in self.squadre:
            self._idMap[s.id] = s

        for i in range(0, len(self.squadre)):
            for j in range(i + 1, len(self.squadre)):
                s1 = self.squadre[i]
                s2 = self.squadre[j]


                peso = (s1.salario or 0) + (s2.salario or 0)

                if s1.id in self._idMap and s2.id in self._idMap:
                    self.G.add_edge(s1.id, s2.id, weight=peso)

        return self.G

    def get_component(self, squadra):

        result=[]
        vicini=self.G[squadra]

        for vicino in vicini:

            peso=vicini[vicino]['weight']
            result.append((vicino, peso))

        result.sort(key=lambda x: x[1], reverse=True)

        return result

    def best_path(self,start):
        self.soluzione_best=[]
        self.best_weight=0
        self.ricorsione([start],0,float("inf"))
        lista_oggetti=[]
        for soluzione in self.soluzione_best:
            lista_oggetti.append(self._idMap[soluzione])
        return lista_oggetti, self.best_weight


    def ricorsione(self,percorso,peso,ultimo_peso):

        if peso>self.best_weight:
            self.best_weight=peso
            self.soluzione_best=copy.deepcopy(percorso)
        last = percorso[-1]

        vicini=self.get_component(last)
        counter=0
        for vicino, p in vicini:
            if vicino in percorso:
                continue
            if p<=ultimo_peso:
                percorso.append(vicino)
                counter+=1
                self.ricorsione(percorso, p + peso, p)
                percorso.pop()
                if counter==self.K:
                    break


















