from datetime import datetime

class Evento:
    total_eventos = 0

    def __init__(self, titulo, data_hora, descricao):
        self.titulo = titulo
        self.data_hora = data_hora
        self.descricao = descricao
        self.is_concluido = False
        Evento.total_eventos += 1

    def isConcluido(self):
        if self.data_hora < datetime.now():
            self.is_concluido = True

    @classmethod
    def num_eventos(cls):
        return cls.total_eventos

    @staticmethod
    def valida_evento(nome, data_hora, descricao):
        return (
            isinstance(nome, str) and
            isinstance(data_hora, datetime) and
            isinstance(descricao, str)
        )

    def __str__(self):
        return (
            f"Evento: {self.titulo}, Data: {self.data_hora}, "
            f"Descrição: {self.descricao}, Concluído: {self.is_concluido}"
        )

    def __eq__(self, other):
        return self.data_hora == other.data_hora

    def __ne__(self, other):
        return self.data_hora != other.data_hora

    def __lt__(self, other):
        return self.data_hora < other.data_hora

    def __le__(self, other):
        return self.data_hora <= other.data_hora

    def __gt__(self, other):
        return self.data_hora > other.data_hora

    def __ge__(self, other):
        return self.data_hora >= other.data_hora
    
#Teste 
    
e1 = Evento("Teste 1", datetime(2024, 5, 20, 10, 0), "Evento teste")
e2 = Evento("Teste 2", datetime(2024, 6, 15, 12, 0), "Outro evento")

print(e1)
print(e2)
print("e1 < e2 ?", e1 < e2)
print("Número total de eventos:", Evento.num_eventos())
print("Validação:", Evento.valida_evento("Oi", datetime.now(), "desc"))