# Load las bibliotecas necesarias
try:

    from app_Abstract.gestionRegistros import GestionRegistros
    from app_Config.config import ConfigurarAplicacion
    
except Exception as e:
    print(f'Falta algun modulo {e}')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Lista de tablas a crear
lista_tablas = [
    #'TABLA_ESTADO',
    #'TABLA_PROVINCIA',
    #'TABLA_TIPO_CUERPO',
    #'TABLA_TIPO_CUOTA',
    #'TABLA_TIPO_DOCUMENTO',
    #'TABLA_TIPO_MONEDA',
    #'TABLA_TIPO_MOVIMIENTO',
    #'TABLA_TIPO_ORIGEN',
    #'TABLA_TIPO_PAGO',
    #'TABLA_TIPO_REGISTRO',
    #'TABLA_TIPO_SUB_REGISTRO',
    #'TABLA_TIPO_TITULAR',
    #'TABLA_API_TOKEN_USER',
    #'TABLA_API_ESTADOS',
    #'TABLA_API_TAREAS',
    #'TABLA_API_ESTADOS_TAREAS',
    #'TABLA_API_TOKEN',
    #'TABLA_API_AUMOSO',
    #'TABLA_API_REGISTROS',
    #'TABLA_ALTAIMPOSITIVA',
    #'TABLA_ALTAIMPOSITIVATITULAR',
    #'TABLA_ANULACIONTRAMITESSELLOS',
    #'TABLA_ANULACIONTRAMITESSELLOSDETALLE',
    #'TABLA_BAJAIMPOSITIVA',
    #'TABLA_BAJAIMPOSITIVATITULAR',
    #'TABLA_CAMBIOTITULARIDAD',
    #'TABLA_CAMBIOTITULARIDADTITULAR',
    #'TABLA_ENCABEZADO',
    #'TABLA_IMPUESTOAUTOMOTOR',
    #'TABLA_IMPUESTOSELLOS',
    #'TABLA_IMPUESTOSELLOSPARTES',
    #'TABLA_IMPUESTOSELLOSPARTESTIPOTRAMITE',
    'TABLA_INFORMACIONVEHICULO',
    'TABLA_INFORMACIONVEHICULOTITULAR',
    #'TABLA_INFORMACIORADICACION',
    #'TABLA_PIE',
    #'TABLA_RELACION_ARBA_SUCERP_MARCA',
    #'TABLA_PROCESOIMPORTACIONEXPORTACION',
    #'TABLA_API_LOG',
]


# Obtengo el conector a la base de datos
data_Input = GestionRegistros(ambiente=ConfigurarAplicacion.ENV_GX)

# inspeccionamos la lista

try:
        for elemento in lista_tablas:

            #data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS[elemento]['objeto'])
            valor  = data_Input.__getattribute__(ConfigurarAplicacion.LISTA_TABLAS[elemento]['objeto'])


            if ConfigurarAplicacion.ENV_GX in ConfigurarAplicacion.ENV_LABEL_ON:

                texto = ''

                # we iterate through the fields of the table record
                for x in range(0, len(valor._fields)):

                    # we build the text variable
                    texto += f'\"{valor._fields[x].lower()}\" text is \'{valor.__getattribute__(valor._fields[x]).comment}\''

                    if x != (len(valor._fields) - 1):
                        texto += ' ,'

                # we build the sentencia variable
                sentencia = f'LABEL ON COLUMN {valor._dalname} ({texto})'

                # execute the sql statement
                data_Input.db.executesql(sentencia)

                data_Input.db.commit()


            print(f'Nombre de la Tabla ({valor})')


except Exception as inst:
    print(inst)







