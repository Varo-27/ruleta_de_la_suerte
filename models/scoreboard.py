import json
import datetime

class Scoreboard:
    def __init__(self):
        self.scores = self.get_scores()

    def add_score(self, player_name: str, score: int):
        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M")
        self.scores.update({player_name: {"score": score, "date": f"{formatted_date}"}})


    @staticmethod
    def get_scores():
        try:
            with open("scores.json", "r") as f:
                return json.load(f)
        except:
            return {}

    def __str__(self):
        #Ordenar las puntuaciones
        sorted_scores = sorted(self.scores.items(), key=lambda item: item[1]["score"], reverse=True)

        #Maximo largo de nombre y puntaje
        max_len_name = max(len(player) for player in self.scores) + 4
        max_len_score = max(len(f"{self.scores[player]['score']}") for player in self.scores) + 8

        #Cabecera
        table = "|" + " Nombre ".center(max_len_name, "-")
        table += "|" + " Puntaje ".center(max_len_score, "-")
        table += "|------ Fecha -------|" + "\n"

        #Datos
        for player, value in sorted_scores:
            table += "|" + f"{player}".center(max_len_name, " ")
            table += "|" + f"{value['score']}".center(max_len_score) 
            table += "|  " + f"{value['date']}"
            table += "  |" + "\n"


        return table

    


s = Scoreboard()
s.add_score("albertos", 1567)
s.add_score("ae", 1995)
print(s)


