# Proyecto ETL - Optimización de Base de Datos desde Archivo CSV

## Descripción del Proyecto

Este proyecto realiza un proceso ETL (Extracción, Transformación y Carga) sobre los datos de la Red Global de Climatología Histórica - Diaria, un conjunto de datos proporcionado por la NOAA (National Oceanic and Atmospheric Administration).

Los datos contienen observaciones diarias de estaciones meteorológicas alrededor del mundo, incluyendo temperaturas máximas, mínimas, precipitaciones, nevadas y otras variables climáticas. Para este proyecto se trabajó específicamente con los datos 
correspondientes al año 1884 ya que el tamaño de la informacion hace imposible cargar en el repositorio.

Adicionalmente, el proyecto genera una carpeta llamada `archivos nuevos` donde se podrá almacenar y analizar información adicional en el futuro.

> *Nota:* Debido a restricciones de conectividad y permisos en AWS, este proyecto se desarrolló y ejecutó de forma local, simulando las operaciones que normalmente se realizarían en un entorno AWS S3.

---

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/Almintar/ETL-optimización de datos.git

---

# Resumen del formato del día

Los archivos anuales están formateados para que cada observación esté representada por una sola fila con los siguientes campos:



ID = Código de identificación de estación de 11 caracteres. Consulte la sección "ghcnd-stations" a continuación para obtener una explicación.

AÑO/MES/DÍA = fecha de 8 caracteres en formato AAAAMMDD (por ejemplo, 19860529 = 29 de mayo de 1986)

ELEMENTO = Indicador de 4 caracteres del tipo de elemento

VALOR DE DATOS = valor de datos de 5 caracteres para ELEMENTO

M-FLAG = Bandera de medición de 1 carácter

Q-FLAG = Bandera de calidad de 1 carácter

S-FLAG = 1 carácter Bandera de origen

OBS-TIME = hora de observación de 4 caracteres en formato hora-minuto (es decir, 0700 = 7:00 am)

Los campos están delimitados por comas y cada fila representa un día de estación.



# Resumen de ELEMENT

Los cinco elementos fundamentales son:



PRCP = Precipitación (décimas de mm)

NIEVE = Nevadas (mm)

SNWD = Profundidad de nieve (mm)

TMAX = Temperatura máxima (décimas de grados C)

TMIN = Temperatura mínima (décimas de grados C)

Consulte la sección Explicación completa de los elementos a continuación para obtener una descripción completa.



M-FLAG

MFLAG es la bandera de medición. Hay diez valores posibles:



En blanco = no hay información de medición aplicable

B = total de precipitación formado a partir de dos totales de 12 horas

D = precipitación total formada a partir de cuatro totales de seis horas

H = representa la temperatura horaria más alta o más baja (TMAX o TMIN) o el promedio de valores horarios (TAVG)

K = convertido de nudos

L = la temperatura parece estar retrasada con respecto a la hora de observación informada

O = convertido de octanas

P = identificado como “cero presunto faltante” en DSI 3200 y 3206

T = rastro de precipitación, nevada o profundidad de nieve

W = convertido del código WBAN de 16 puntos (para la dirección del viento)

Q-FLAG

Q-FLAG es el indicador de calidad de la medición. Hay catorce valores posibles:



En blanco = no falló ninguna verificación de garantía de calidad

D = comprobación de duplicados fallida

G = comprobación de espacio fallida

I = no pasó la comprobación de consistencia interna

K = verificación de racha/valor frecuente fallida

L = verificación fallida de la duración del período de varios días

M = comprobación de consistencia mega fallida

N = comprobación de cero fallida

O = verificación de valores atípicos climatológicos fallida

R = comprobación de rango rezagado fallida

S = comprobación de consistencia espacial fallida

T = comprobación de consistencia temporal fallida

W = temperatura demasiado cálida para la nieve

X = comprobación de límites fallida

Z = marcado como resultado de una investigación oficial de Datzilla

Bandera S

S-FLAG es la bandera de origen de la observación. Hay veintinueve valores posibles (incluyendo espacios en blanco, mayúsculas y minúsculas):



En blanco = Sin fuente (es decir, falta el valor de los datos)

0 = Resumen cooperativo del día de EE. UU. (NCDC DSI-3200)

6 = Resumen cooperativo del día del CDMP (NCDC DSI-3206)

7 = Resumen cooperativo del día de EE. UU. – Transmitido vía WxCoder3 (NCDC SI-3207)

A = Datos en tiempo real del Sistema Automatizado de Observación de la Superficie de EE. UU. (ASOS) (desde el 1 de enero de 2006)

a = Datos australianos de la Oficina Australiana de Meteorología

B = datos de ASOS de EE. UU. de octubre de 2000 a diciembre de 2005 (NCDC DSI-3211)

b = Actualización de Bielorrusia

C = Medio Ambiente Canadá

E = Evaluación y conjunto de datos del clima europeo (Klein Tank et al., 2002)

F = Datos del Fuerte de EE. UU.

G = Sistema Mundial de Observación del Clima (GCOS) oficial u otros datos proporcionados por el gobierno

H = Datos en tiempo real del Centro Climático Regional de las Altas Llanuras

I = Recopilación internacional (datos no estadounidenses recibidos a través de contactos personales)

K = Resumen cooperativo del día de EE. UU., datos digitalizados a partir de formularios de observadores en papel (desde 2011 hasta la actualidad)

M = Extracto mensual de METAR (datos adicionales de ASOS)

N = Colaboración Comunitaria contra la Lluvia, el Granizo y la Nieve (CoCoRaHS)

Q = Datos de varios países africanos que habían sido “puestos en cuarentena”, es decir, retenidos para su divulgación pública hasta que se concedió el permiso de los respectivos servicios meteorológicos.

R = Base de datos de la red de referencia del NCEI (Red de referencia climática y Red de referencia climática regional)

r = Instituto Panruso de Investigación de Información Hidrometeorológica - Centro Mundial de Datos

S = Resumen Global del Día (NCDC DSI-9618). NOTA: Los valores «S» se derivan de informes sinópticos horarios intercambiados a través del Sistema Mundial de Telecomunicaciones (SMT). Los valores diarios obtenidos de esta manera pueden diferir significativamente de los datos diarios reales, especialmente en cuanto a precipitación (por lo tanto, úselos con precaución).

s = Administración Meteorológica de China/Centro Nacional de Información Meteorológica/Centro de Datos Climáticos ( http://cdc.cma.gov.cn )

T = Datos de SNOwpack TELemtry (SNOTEL) obtenidos del Servicio de Conservación de Recursos Naturales del Departamento de Agricultura de los EE. UU.

U = Datos de la estación meteorológica automática remota (RAWS) obtenidos del Centro climático regional occidental

u = Actualización de Ucrania

W = Resumen WBAN/ASOS del día a partir de los datos de superficie integrados (ISD) del NCDC.

X = Resumen de primer orden del día de EE. UU. (NCDC DSI-3210)

Z = Adiciones o reemplazos oficiales de Datzilla

z = actualización de Uzbekistán

Cuando hay datos disponibles para el mismo tiempo de más de una fuente, se elige la fuente de mayor prioridad según el siguiente orden de prioridad (de mayor a menor): - Z, R, 0, 6, C, X, W, K, 7, F, B, M, r, E, z, u, b, s, a, G, Q, I, A, N, T, U, H, S



Explicación completa de los elementos variables

Como se mencionó anteriormente, los cinco elementos principales son:



PRCP = Precipitación (décimas de mm)

NIEVE = Nevadas (mm)

SNWD = Profundidad de nieve (mm)

TMAX = Temperatura máxima (décimas de grados C)

TMIN = Temperatura mínima (décimas de grados C)

Los otros elementos son:



ACMC = Nubosidad promedio de medianoche a medianoche a partir de datos del ceilómetro de 30 segundos (porcentaje)



ACMH = Nubosidad promedio de medianoche a medianoche a partir de observaciones manuales (porcentaje)



ACSC = Nubosidad promedio desde el amanecer hasta el atardecer según datos del ceilómetro de 30 segundos (porcentaje)



ACSH = Nubosidad promedio desde el amanecer hasta el atardecer según observaciones manuales (porcentaje)



AWDR = Dirección media diaria del viento (grados)



AWND = Velocidad media diaria del viento (décimas de metro por segundo)



DAEV = Número de días incluidos en el total de evaporación multidía (MDEV)



DAPR = Número de días incluidos en el total de precipitación multidía (MDPR)



DASF = Número de días incluidos en el total de nevadas de varios días (MDSF)



DATN = Número de días incluidos en la temperatura mínima multidiaria (MDTN)



DATX = Número de días incluidos en la temperatura máxima multidiaria (MDTX)



DAWM = Número de días incluidos en el movimiento del viento de varios días (MDWM)



DWPR = Número de días con precipitación distinta de cero incluidos en el total de precipitación de varios días (MDPR)



EVAP = Evaporación del agua de la bandeja de evaporación (décimas de mm)



FMTM = Tiempo de la milla más rápida o del viento más rápido en 1 minuto (horas y minutos, es decir, HHMM)



FRGB = Base de la capa de suelo congelado (cm)



FRGT = Parte superior de la capa de suelo congelado (cm)



FRTH = Espesor de la capa de suelo congelado (cm)



GAHT = Diferencia entre la altura del río y la del nivel del mar (cm)



MDEV = Total de evaporación multidía (décimas de mm; utilizar con DAEV)



MDPR = Total de precipitación de varios días (décimas de mm; utilizar con DAPR y DWPR, si están disponibles)



MDSF = Total de nevadas en varios días



MDTN = Temperatura mínima multidiaria (décimas de grados C; utilizar con DATN)



MDTX = Temperatura máxima multidiaria (décimas de grados C; utilizar con DATX)



MDWM = Movimiento del viento en varios días (km)



MNPN = Temperatura mínima diaria del agua en una bandeja de evaporación (décimas de grados C)



MXPN = Temperatura máxima diaria del agua en una tanqueta de evaporación (décimas de grados C)



PGTM = Tiempo de ráfaga máxima (horas y minutos, es decir, HHMM)



PSUN = Porcentaje diario de posible luz solar (porcentaje)



SN*# = Temperatura mínima del suelo (décimas de grados C) donde:



* corresponde a un código para cobertura del suelo



0 = desconocido



1 = hierba



2 = barbecho



3 = suelo desnudo



4 = hierba bromo



5 = césped



6 = mantillo de paja



7 = estiércol de hierba



8 = lodo desnudo



# corresponde a un código para la profundidad del suelo.



1 = 5 centímetros



2 = 10 centímetros



3 = 20 centímetros



4 = 50 centímetros



5 = 100 centímetros



6 = 150 centímetros



7 = 180 centímetros



SX*# = Temperatura máxima del suelo (décimas de grados C) donde:



* corresponde a un código de cobertura del suelo (ver arriba)

# corresponde a un código para la profundidad del suelo (ver arriba)

TAVG = Temperatura media (décimas de grados C) [Nótese que TAVG de la fuente 'S' corresponde a un promedio para el período que finaliza a las 2400 UTC en lugar de la medianoche local]



THIC = Espesor del hielo sobre el agua (décimas de mm)



TOBS = Temperatura en el momento de la observación (décimas de grados C)



TSUN = Total de horas de sol diarias (minutos)



WDF1 = Dirección del viento más rápido en 1 minuto (grados)



WDF2 = Dirección del viento más rápido en 2 minutos (grados)



WDF5 = Dirección del viento más rápido en 5 segundos (grados)



WDFG = Dirección de la ráfaga máxima de viento (grados)



WDFI = Dirección del viento instantáneo más alto (grados)



WDFM = Dirección del viento en la milla más rápida (grados)



WDMV = movimiento del viento en 24 horas (km)



WESD = Equivalente de agua de nieve en el suelo (décimas de mm)



WESF = Equivalente de agua de las nevadas (décimas de mm)



WSF1 = Velocidad del viento más rápida en 1 minuto (décimas de metro por segundo)



WSF2 = Velocidad del viento más rápida en 2 minutos (décimas de metro por segundo)



WSF5 = Velocidad del viento más rápida en 5 segundos (décimas de metro por segundo)



WSFG = Velocidad máxima del viento en ráfagas (décimas de metro por segundo)



WSFI = Velocidad instantánea más alta del viento (décimas de metros por segundo)



WSFM = Velocidad del viento en milla más rápida (décimas de metro por segundo)



WT** = Tipo de clima donde ** tiene uno de los siguientes valores:



01 = Niebla, niebla helada o niebla helada (puede incluir niebla intensa)

02 = Niebla espesa o niebla helada (no siempre se distingue de la niebla)

03 = Trueno

04 = Granizados, aguanieve, nieve granulada o granizo pequeño

05 = Granizo (puede incluir granizo pequeño)

06 = Glaseado o escarcha

07 = Polvo, ceniza volcánica, polvo en suspensión, arena en suspensión u obstrucción en suspensión

08 = Humo o neblina

09 = Nieve que sopla o se acumula

10 = Tornado, tromba marina o nube de embudo

11 = Vientos fuertes o dañinos

12 = Soplado de aerosol

13 = Niebla

14 = Llovizna

15 = Llovizna helada

16 = Lluvia (puede incluir lluvia helada, llovizna y llovizna helada)

17 = Lluvia helada

18 = Nieve, bolitas de nieve, granos de nieve o cristales de hielo

19 = Fuente de precipitación desconocida

21 = Niebla terrestre

22 = Niebla helada o niebla helada

WV** = Clima en los alrededores donde ** tiene uno de los siguientes valores:



01 = Niebla, niebla helada o niebla helada (puede incluir niebla intensa)

03 = Trueno

07 = Ceniza, polvo, arena u otra obstrucción soplada

18 = Nieve o cristales de hielo

20 = Lluvia o chubasco de nieve

FORMATO DEL archivo “ghcnd-stations.txt”

Hay más de 106.200 estaciones listadas en un archivo aparte. Disponible aquí:



http://noaa-ghcn-pds.s3.amazonaws.com/ghcnd-stations.txt



La siguiente tabla describe la estructura de cada fila de ghcnd-stations.txt



Variable	Columnas	Tipo	Ejemplo

IDENTIFICACIÓN	1-11	Personaje	EI000003980

LATITUD	13-20	Real	55.3717

LONGITUD	22-30	Real	-7.3400

ELEVACIÓN	32-37	Real	21.0

ESTADO	39-40	Personaje	

NOMBRE	42-71	Personaje	CABEZA DE MALIN

BANDERA GSN	73-75	Personaje	GSN

BANDERA HCN/CRN	77-79	Personaje	

Identificación de la OMM	81-85	Personaje	03980

Estas variables tienen las siguientes definiciones:



ID = el código de identificación de la estación.



Los dos primeros caracteres indican el código de país FIPS

El tercer carácter es un código de red que identifica el sistema de numeración de estaciones utilizado.

0 = no especificado (estación identificada por hasta ocho caracteres alfanuméricos)

1 = Número de identificación basado en el programa Colaborativo Comunitario de Lluvia, Granizo y Nieve (CoCoRaHS). Para garantizar la coherencia con GHCN Daily, todos los números de los ID originales de CoCoRaHS se han completado para que tengan cuatro dígitos. Además, se han eliminado los caracteres "-" y "_" para garantizar que los ID no superen los 11 caracteres cuando van precedidos de "US1". Por ejemplo, el ID de CoCoRaHS "AZ-MR-156" se convierte en "US1AZMR0156" en GHCN-Daily.

C = Número de identificación de la Red Cooperativa de EE. UU. (últimos seis caracteres del ID diario de GHCN)

E = Número de identificación utilizado en el conjunto de datos no combinados de ECA&D

M = ID de la Organización Meteorológica Mundial (últimos cinco caracteres del ID diario de GHCN)

N = Número de identificación utilizado en los datos suministrados por un Centro Meteorológico o Hidrológico Nacional

R = Identificador de la estación meteorológica automática remota interinstitucional de EE. UU. (RAWS)

S = Identificador de la estación SNOwpack TELemtry (SNOTEL) del Servicio de Conservación de Recursos Naturales de EE. UU.

W = Número de identificación WBAN (últimos cinco caracteres del ID diario de GHCN)

Los ocho caracteres restantes contienen el ID de la estación real.

LATITUD = latitud de la estación (en grados decimales).



LONGITUD = longitud de la estación (en grados decimales).



ESTADO = código postal de EE. UU. para el estado (solo para estaciones de EE. UU. y Canadá).



NOMBRE = nombre de la estación.



BANDERA GSN = indicador que indica si la estación forma parte de la Red de Superficie del SMOC (GSN). La bandera se asigna mediante la comparación del número del campo WMOID con la lista oficial de estaciones GSN. Hay dos valores posibles:



En blanco = estación no GSN o número de estación WMO no disponible

GSN = estación GSN

BANDERA HCN/CRN = bandera que indica si la estación forma parte de la Red de Climatología Histórica de EE. UU. (HCN). Hay tres valores posibles:



En blanco = No es miembro de la Climatología Histórica de EE. UU. ni de las Redes de Referencia Climática de EE. UU.

HCN = Estación de la Red de Climatología Histórica de EE. UU.

CRN = Red de Referencia Climática de EE. UU. o Estación de la Red Climática Regional de EE. UU.

El ID OMM es el número de la Organización Meteorológica Mundial (OMM) para la estación. Si la estación no tiene número OMM (o aún no se le ha asignado uno), el campo estará en blanco.
