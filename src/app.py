from dataclasses import dataclass
from interface import Repositorio


@dataclass
class App:
    repositorio: Repositorio
