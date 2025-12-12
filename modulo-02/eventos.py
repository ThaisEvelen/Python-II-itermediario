from abc import ABC, abstractmethod
from datetime import datetime, timedelta


# ============================
#   CLASSE ABSTRATA EVENTOABC
# ============================
class EventoABC(ABC):

    def __init__(self, titulo: str, descricao: str):
        self._titulo = titulo
        self._descricao = descricao

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def isConcluido(self):
        pass


# ============================
#   CLASSE DATAHORA
# ============================
class DataHora:
    FORMAT = '%d/%m/%Y, %H:%M'

    def __init__(self):
        self._data_hora = None

    # PROPRIEDADE
    @property
    def data_hora(self):
        return self._data_hora.strftime(DataHora.FORMAT)

    @data_hora.setter
    def data_hora(self, valor: str):
        try:
            self._data_hora = datetime.strptime(valor, DataHora.FORMAT)
        except ValueError:
            raise ValueError("Data inválida. Use o formato %d/%m/%Y, %H:%M")

    # MÉTODOS
    def isPassado(self):
        return self._data_hora < datetime.now()

    def somaDias(self, num_dias: int):
        nova_data = self._data_hora + timedelta(days=num_dias)
        return nova_data.strftime(DataHora.FORMAT)


# ============================
#   CLASSE EVENTO UNICO
# ============================
class EventoUnico(EventoABC):

    def __init__(self, titulo, descricao, data_hora_str):
        super().__init__(titulo, descricao)
        self._data_hora = DataHora()
        self._data_hora.data_hora = data_hora_str

    def isConcluido(self):
        return self._data_hora.isPassado()

    def editar_data_hora(self, nova_data: str):
        self._data_hora.data_hora = nova_data

    def __str__(self):
        return (
            f"Evento: {self._titulo}, "
            f"Data: {self._data_hora.data_hora}, "
            f"Descrição: {self._descricao}, "
            f"Concluído: {self.isConcluido()}"
        )


# ============================
#   CLASSE EVENTO RECORRENTE
# ============================
class EventoRecorrente(EventoABC):

    def __init__(self, titulo, descricao, data_hora_inicial, data_hora_final, intervalo_repeticao):
        super().__init__(titulo, descricao)
        self._datas = []  # lista de objetos DataHora

        # Criar a primeira data
        dh = DataHora()
        dh.data_hora = data_hora_inicial
        self._datas.append(dh)

        # Criar as demais datas
        while True:
            nova_data_str = self._datas[-1].somaDias(intervalo_repeticao)
            nova_data_dt = datetime.strptime(nova_data_str, DataHora.FORMAT)
            final_dt = datetime.strptime(data_hora_final, DataHora.FORMAT)

            if nova_data_dt > final_dt:
                break

            novo = DataHora()
            novo.data_hora = nova_data_str
            self._datas.append(novo)

    def isConcluido(self, indice):
        return self._datas[indice].isPassado()

    def editar_data_hora(self, data_antiga: str, data_nova: str):
        for dh in self._datas:
            if dh.data_hora == data_antiga:
                dh.data_hora = data_nova
                return True
        return False

    def __str__(self):
        texto = ""
        for i, dh in enumerate(self._datas):
            texto += (
                f"Evento: {self._titulo}, "
                f"Data: {dh.data_hora}, "
                f"Descrição: {self._descricao}, "
                f"Concluído: {self.isConcluido(i)}\n"
            )
        return texto.strip()
