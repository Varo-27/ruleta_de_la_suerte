class Player:
    __name: str
    __round_points: int
    __total_points: int

    def __init__(self, name: str):
        self.__name = name
        self.__round_points = 0
        self.__total_points = 0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def total_points(self) -> int:
        return self.__total_points

    @property
    def round_points(self) -> int:
        return self.__round_points

    @round_points.setter
    def round_points(self, points: int) -> None:
        if points >= 0:
            self.__round_points = points
        else:
            raise ValueError("Los puntos no pueden ser negativos")

    def buy_vowel(self) -> None:
        self.__round_points -=500

    def win_panel(self) -> None:
        self.__total_points += self.__round_points

    def print_total_points(self) -> str:
        return f"{self.name} - {self.__total_points} puntos"

    def print_round_points(self) -> str:
        return f"{self.name} - {self.round_points} puntos"

    def __str__(self) -> str:
        return f"{self.name} - {self.round_points} puntos"