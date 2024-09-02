class Eletronico:
    def __init__(self, nome) -> None:
        self._nome = nome
        self._ligado = False

    def ligar(self):  # guard clause
        if not self._ligado:
            self._ligado = True

    def desligar(self):  # guard clause
        if not self._ligado:
            self._ligado = False


class Smartphone(Eletronico):
    def ligar(self):
        super().ligar()