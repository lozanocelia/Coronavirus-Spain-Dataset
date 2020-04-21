import json
import csv

# Comprobar integridad de datos diarios nuevos en cada comunidad autonoma.
def test_prev(current, prev):
    prev_casos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    errors = False
    # Para cada informe diario...
    for i in range(0, len(data['InformesDiarios'])):
        # Para cada comunidad autonoma...
        j = 0
        for comunidad_autonoma in data['InformesDiarios'][i]['ComunidadesAutonomas']:
            casos = data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma][current]
            if casos is not None and data['InformesDiarios'][i-1]['ComunidadesAutonomas'][comunidad_autonoma][current] is not None:
                if(casos - prev_casos[j] != data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma][prev]):
                    errors = True
                    print("Comunidad Autonoma: " + str(comunidad_autonoma))
                    print("Fecha: " + str(data['InformesDiarios'][i]['Fecha']))
                    print("Prev: " + str(prev_casos[j]))
                    print("Actu: " + str(casos))
                    print("New: " + str(data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma][prev]))
                    print("Should be: " + str(casos - prev_casos[j]))
                    print("")
                    data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma][prev] = casos - prev_casos[j]
            if casos is not None:
                prev_casos[j] = casos
            j += 1
    if not errors:
        print("No hay errores en " + prev)

# Calcular datos diarios nuevos a partir de datos de mes anterior en cada comunidad autonoma.
def create_prev(current, prev):
    prev_casos = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    # Para cada informe diario...
    for i in range(0, len(data['InformesDiarios'])):
        # Para cada comunidad autonoma...
        j = 0
        for comunidad_autonoma in data['InformesDiarios'][i]['ComunidadesAutonomas']:
            casos = data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma][current]
            if casos is not None and data['InformesDiarios'][i-1]['ComunidadesAutonomas'][comunidad_autonoma][current] is not None:
                data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma][prev] = casos - prev_casos[j]
                # Sort by key
                # data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma] = OrderedDict(sorted(data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma].items()))
            if casos is not None:
                prev_casos[j] = casos
            j += 1
    print("Se ha creado/corregido la clave " + prev)

# Calcular cantidad total sumando las cantidades de cada comunidad autonoma.
def create_total(key):
    bool = None
    # Para cada informe diario...
    for i in range(0, len(data['InformesDiarios'])):
        total = 0
        # Para cada comunidad autonoma...
        for comunidad_autonoma in data['InformesDiarios'][i]['ComunidadesAutonomas']:
            if data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma][key] is not None:
                total += data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma][key]
                bool = True
            else:
                bool = False
        if bool:
            data['InformesDiarios'][i]['Total' + key] = total

# Abrir archivo para leer datos.
with open('DataSet.json') as f:
    data = json.load(f)

# Calcular casos nuevos de cada comunidad autonoma a partir de los casos de este dia y del anterior.
create_prev("Casos", "CasosNuevos")
test_prev("Casos", "CasosNuevos")
print("")
# Calcular curados nuevos de cada comunidad autonoma a partir de los curados de este dia y del anterior.
create_prev("Curados", "CuradosNuevos")
test_prev("Curados", "CuradosNuevos")
print("")
# Calcular uci nuevos de cada comunidad autonoma a partir de los uci de este dia y del anterior.
create_prev("IngresosUCI", "IngresosUCINuevos")
test_prev("IngresosUCI", "IngresosUCINuevos")
print("")
# Calcular fallecidos nuevos de cada comunidad autonoma a partir de los fallecidos de este dia y del anterior.
create_prev("Fallecidos", "FallecidosNuevos")
test_prev("Fallecidos", "FallecidosNuevos")
print("")
# Calcular hospitalizados nuevos de cada comunidad autonoma a partir de los hospitalizados de este dia y del anterior.
create_prev("Hospitalizados", "HospitalizadosNuevos")
test_prev("Hospitalizados", "HospitalizadosNuevos")
print("")
# Calcular cantidades totales diarias.
create_total("Casos")
create_total("CasosNuevos")
create_total("IngresosUCI")
create_total("IngresosUCINuevos")
create_total("Fallecidos")
create_total("FallecidosNuevos")
create_total("Curados")
create_total("CuradosNuevos")
create_total("Hospitalizados")
create_total("HospitalizadosNuevos")

# Abrir archivo para escribir datos nuevos.
with open('DataSet.json', 'w') as outfile:
    json.dump(data, outfile, indent=4, ensure_ascii=False)


# Obtener array con fechas del dataset.
def get_dates():
    dates = ["Comunidad Autonoma"]
    for i in range(0, len(data['InformesDiarios'])):
        dates.append(data['InformesDiarios'][i]['Fecha'])
    return dates


# Obtener array con nombres de cada comunidad autonoma.
def get_autonommous_community(comunidad_autonoma, key):
    d = [data['InformesDiarios'][0]['ComunidadesAutonomas'][comunidad_autonoma]["Nombre"]]
    for i in range(0, len(data['InformesDiarios'])):
        if data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma][key] is None:
            d.append("null")
        else:
            d.append(data['InformesDiarios'][i]['ComunidadesAutonomas'][comunidad_autonoma][key])
    return d


# Obtener numero total de cantidades.
def get_totals(key):
    d = ["Total"]
    for i in range(0, len(data['InformesDiarios'])):
        if data['InformesDiarios'][i]['Total' + key] is None:
            d.append("null")
        else:
            d.append(data['InformesDiarios'][i]['Total' + key])
    return d


# Crear csv con datos de una clave (Ej: Curados, Casos, CasosNuevos...)
def generate_csv_from(key):
    res = [get_dates()]
    # Para cada comunidad autonoma...
    for comunidad_autonoma in data['InformesDiarios'][0]['ComunidadesAutonomas']:
        res.append(get_autonommous_community(comunidad_autonoma, key))
    res.append(get_totals(key))
    with open(key + ".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(res)

# Generar csv para cada una de estas claves.
generate_csv_from("Casos")
generate_csv_from("CasosNuevos")
generate_csv_from("Curados")
generate_csv_from("CuradosNuevos")
generate_csv_from("Fallecidos")
generate_csv_from("FallecidosNuevos")
generate_csv_from("Hospitalizados")
generate_csv_from("HospitalizadosNuevos")
generate_csv_from("IngresosUCI")
generate_csv_from("IngresosUCINuevos")
