import math
from operator import itemgetter


def distancia(coord1, coord2):
    lon = coord1[0]
    lon2 = coord2[1]
    lat1 = coord1[0]
    lat2 = coord2[1]

    return math.sqrt(
        (lat1 - lat2) ** 2 +
        (lon - lon2) ** 2
    )


def en_ruta(rutas, cliente):

    for ruta in rutas:
        if cliente in ruta:
            return ruta

    return None


def peso_ruta(ruta, pedidos):

    total = 0

    for cliente in ruta:
        total += pedidos[cliente]

    return total


def es_exterior(ruta, cliente):

    return ruta[0] == cliente or ruta[-1] == cliente


def vrp_voraz(coord, pedidos, almacen, max_carga):

    # =====================
    # PASO 1
    # Calcular ahorros
    # =====================

    ahorros = {}

    for c1 in coord:
        for c2 in coord:

            if c1 == c2:
                continue

            if (c2, c1) in ahorros:
                continue

            d_c1_c2 = distancia(coord[c1], coord[c2])
            d_c1_almacen = distancia(coord[c1], almacen)
            d_c2_almacen = distancia(coord[c2], almacen)

            ahorro = (
                d_c1_almacen +
                d_c2_almacen -
                d_c1_c2
            )

            ahorros[(c1, c2)] = ahorro

    # =====================
    # PASO 2
    # Ordenar ahorros
    # =====================

    ahorros = sorted(
        ahorros.items(),
        key=itemgetter(1),
        reverse=True
    )

    rutas = []

    # =====================
    # PASO 3
    # Construcción
    # =====================

    for (i, j), ahorro in ahorros:

        ruta_i = en_ruta(rutas, i)
        ruta_j = en_ruta(rutas, j)

        # ---------------------------------
        # Ninguno pertenece a una ruta
        # ---------------------------------

        if ruta_i is None and ruta_j is None:

            if peso_ruta([i, j], pedidos) <= max_carga:
                rutas.append([i, j])

        # ---------------------------------
        # i está en ruta y j no
        # ---------------------------------

        elif ruta_i is not None and ruta_j is None:

            if es_exterior(ruta_i, i):

                if (
                    peso_ruta(ruta_i, pedidos)
                    + pedidos[j]
                    <= max_carga
                ):

                    if ruta_i[0] == i:
                        ruta_i.insert(0, j)
                    else:
                        ruta_i.append(j)

        # ---------------------------------
        # j está en ruta y i no
        # ---------------------------------

        elif ruta_i is None and ruta_j is not None:

            if es_exterior(ruta_j, j):

                if (
                    peso_ruta(ruta_j, pedidos)
                    + pedidos[i]
                    <= max_carga
                ):

                    if ruta_j[0] == j:
                        ruta_j.insert(0, i)
                    else:
                        ruta_j.append(i)

        # ---------------------------------
        # Ambos en rutas distintas
        # ---------------------------------

        elif ruta_i != ruta_j:

            if (
                es_exterior(ruta_i, i)
                and
                es_exterior(ruta_j, j)
            ):

                carga_total = (
                    peso_ruta(ruta_i, pedidos)
                    +
                    peso_ruta(ruta_j, pedidos)
                )

                if carga_total <= max_carga:

                    nueva_ruta = None

                    # fin - inicio
                    if ruta_i[-1] == i and ruta_j[0] == j:
                        nueva_ruta = ruta_i + ruta_j

                    # inicio - fin
                    elif ruta_i[0] == i and ruta_j[-1] == j:
                        nueva_ruta = ruta_j + ruta_i

                    # inicio - inicio
                    elif ruta_i[0] == i and ruta_j[0] == j:
                        nueva_ruta = list(reversed(ruta_i)) + ruta_j

                    # fin - fin
                    elif ruta_i[-1] == i and ruta_j[-1] == j:
                        nueva_ruta = ruta_i + list(reversed(ruta_j))

                    if nueva_ruta:

                        rutas.remove(ruta_i)
                        rutas.remove(ruta_j)

                        rutas.append(nueva_ruta)

    # =====================
    # PASO 4
    # Clientes faltantes

    clientes_ruteados = set()
    for ruta in rutas:
        clientes_ruteados.update(ruta)
    faltantes = set(coord.keys()) - clientes_ruteados
    for cliente in faltantes:
        rutas.append([cliente])
    return rutas



# PRUEBA

if __name__ == "__main__":
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
        'MTY': (25.67962, -100.32659)
    }

    pedidos = {
        'JILOYORK': 10,
        'MORELOS': 7,
        'CDMX': 13,
        'HGO': 11,
        'QRO': 15,
        'SLP': 8,
        'AGS': 6,
        'SONORA': 7,
        'MEXICALI': 8,
        'MTY': 14
    }

    almacen = (19.958027304170262,-99.548943194897)
    max_carga = 40
    rutas = vrp_voraz(
        coord,
        pedidos,
        almacen,
        max_carga
    )
    print("\nRUTAS ENCONTRADAS\n")
    for i, ruta in enumerate(rutas, start=1):
        carga = peso_ruta(ruta, pedidos)
        print(
            f"Ruta {i}: "
            f"{' -> '.join(ruta)} "
            f"(Carga={carga})"
        )