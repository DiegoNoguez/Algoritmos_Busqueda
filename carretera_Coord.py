from math import sin, cos, acos

# =========================
# CLASE NODO
# =========================

class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = 0
        self.set_hijos(hijos)

    def set_hijos(self, hijos):
        if hijos is not None:
            self.hijos = hijos
            for h in self.hijos:
                h.padre = self

    def get_hijos(self):
        return self.hijos

    def get_padre(self):
        return self.padre

    def set_padre(self, padre):
        self.padre = padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    def en_lista(self, lista_nodos):
        for n in lista_nodos:
            if self.igual(n):
                return True
        return False

    def __str__(self):
        return f"{self.datos} -> {self.costo}"


# =========================
# DISTANCIA GEOGRÁFICA
# =========================

def geodist(lat1, lon1, lat2, lon2):
    grad_rad = 0.01745329
    rad_grad = 57.29577951

    longitud = lon1 - lon2

    val = (
        (sin(lat1 * grad_rad) * sin(lat2 * grad_rad))
        + (
            cos(lat1 * grad_rad)
            * cos(lat2 * grad_rad)
            * cos(longitud * grad_rad)
        )
    )

    return (acos(val) * rad_grad) * 111.32


# =========================
# HEURÍSTICA
# =========================

def heuristica(ciudad, solucion):
    lat1, lon1 = coord[ciudad]
    lat2, lon2 = coord[solucion]

    return int(geodist(lat1, lon1, lat2, lon2))


# =========================
# A*
# =========================

def buscar_solucion_A(conexiones, estado_inicial, solucion):

    nodos_visitados = []
    nodos_frontera = []

    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_costo(0)

    nodos_frontera.append(nodo_inicial)

    while len(nodos_frontera) != 0:

        # f(n) = g(n) + h(n)
        nodos_frontera = sorted(
            nodos_frontera,
            key=lambda x: x.get_costo()
            + heuristica(x.get_datos(), solucion)
        )

        nodo = nodos_frontera.pop(0)

        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo

        dato_nodo = nodo.get_datos()

        for destino, costo in conexiones[dato_nodo].items():

            hijo = Nodo(destino)

            hijo.set_costo(nodo.get_costo() + costo)

            hijo.set_padre(nodo)

            if not hijo.en_lista(nodos_visitados):

                if not hijo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo)

                else:
                    for n in nodos_frontera:
                        if (
                            n.igual(hijo)
                            and n.get_costo() > hijo.get_costo()
                        ):
                            nodos_frontera.remove(n)
                            nodos_frontera.append(hijo)

    return None


# =========================
# DATOS
# =========================

conexiones = {
    'JILOYORK': {'CDMX': 125, 'QRO': 513},
    'MORELOS': {'QRO': 524},
    'CDMX': {'JILOYORK': 125, 'QRO': 433, 'HGO': 491},
    'HGO': {'CDMX': 491, 'QRO': 433, 'MEXICALI': 309, 'MTY': 346},
    'QRO': {
        'SLP': 203,
        'MORELOS': 514,
        'JILOYORK': 513,
        'CDMX': 423,
        'MTY': 603,
        'SONORA': 437,
        'HGO': 356,
        'MEXICALI': 313,
        'AGS': 599
    },
    'SLP': {'AGS': 390, 'QRO': 203},
    'AGS': {'SLP': 390, 'QRO': 599},
    'SONORA': {'QRO': 437, 'MEXICALI': 394},
    'MEXICALI': {'MTY': 296, 'HGO': 309, 'QRO': 313},
    'MTY': {'MEXICALI': 296, 'QRO': 603, 'HGO': 346}
}

coord = {
    'JILOYORK': (19.57087, -99.31593),
    'MORELOS': (18.92256, -99.23495),
    'CDMX': (19.43280, -99.13334),
    'HGO': (20.60631, -99.24204),
    'QRO': (20.59344, -100.39005),
    'SLP': (22.15605, -100.96973),
    'AGS': (21.88698, -102.26257),
    'SONORA': (29.07296, -110.95591),
    'MEXICALI': (32.62387, -115.44288),
    'MTY': (25.67962, -100.32659),
}

# =========================
# EJECUCIÓN
# =========================

estado_inicial = 'JILOYORK'
solucion = 'MTY'

nodo_solucion = buscar_solucion_A(
    conexiones,
    estado_inicial,
    solucion
)

resultado = []

nodo = nodo_solucion

while nodo is not None:
    resultado.append(nodo.get_datos())
    nodo = nodo.get_padre()

resultado.reverse()

print("Ruta encontrada:")
print(resultado)

print("Costo total:")
print(nodo_solucion.get_costo())