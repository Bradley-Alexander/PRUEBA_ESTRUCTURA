class Factura:
    def __init__(self):
        self.__id = 0
        self.__fecha = ''
        self.__total = ''
    
    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _total(self):
        return self.__total

    @_total.setter
    def _total(self, value):
        self.__total = value

    @property
    def serialize(self):
        return {
            'id': self._id,
            'fecha': self._fecha,
            'total': self._total
        }

    def deserializar(self, data):
        factura = Factura()
        factura._id = data['id']
        factura._fecha = data['fecha']
        factura._total = data['total']
        return factura
    
    def __str__(self):
        return f"Fecha Factura: {self._fecha} Total Fatura: {self._total}"