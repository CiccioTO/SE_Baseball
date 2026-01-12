
from dataclasses import dataclass


@dataclass
class Squadra:
    id: int = None
    year: int = None
    team_code: str = None
    name: str = None
    salario: int = None

    def __str__(self):

        return self.name if self.name else "Nessun Nome"

    def __repr__(self):
        return self.name if self.name else "Nessun Nome"

    def __hash__(self):
        return hash(self.id)
