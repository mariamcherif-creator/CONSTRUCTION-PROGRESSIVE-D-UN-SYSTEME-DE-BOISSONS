class Boisson(ABC):
 
    @abstractmethod
    def cout(self):
        pass
 
    @abstractmethod
    def description(self):
        pass
 
    # PARTIE 4 : Combinaison de boissons avec l'opérateur +
    # Retourne une nouvelle BoisssonCombinee qui regroupe les deux.
    def __add__(self, other):
        return BoissonCombinee(self, other)