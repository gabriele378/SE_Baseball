import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self.team = None
        self.stipendi = None
        self.anni = None

        self.G = nx.Graph()


    def numero_squadre(self):
        for team in self.team:
            n_squadre = team['NumeroSquadre']

        return n_squadre

    def neighbors(self, team):
        vicini = self.G.neighbors(team)

        return vicini

    def anni(self):
        return DAO.get_year()






    def crea_grafo(self, year):
        self.G.clear()

        self.stipendi = DAO.get_salary()
        for s in self.stipendi:
            somma_stipendi = s.somma_stipendi

            self.team = DAO.get_team(year)
            for team in self.team:
                self.G.add_node(team)

                for team2 in self.team:
                    if team2 != team:
                        self.G.add_edge(team, team2, weight = somma_stipendi)
