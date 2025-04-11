
import os
import pandas as pd
import glob
from datetime import datetime, timedelta
import pandasql as ps
import re

# crea el modelo de datos con la data inicial
def create_model(origin, raw):
    '''
    origin: ruta de origen,
    raw: ruta de destino
    '''
    st = datetime.now()
    print('\n')
    print('Cargando datos en bruto ...')
    os.chdir(origin)
    archivos = glob.glob('*.csv')
    dfs = []
    for archivo in archivos:
        df = pd.read_csv(archivo, sep=',')
        dfs.append(df)
    dfs = pd.concat(dfs , axis = 0, names = list(df.columns))
    print('\n')
    print('Creando tablas parametricas del modelo de datos')
    # tablas parametricas
    station_id = pd.DataFrame(dfs.ID.unique(), columns=['station'])
    station_id['station_id'] =  station_id.reset_index().index + 1
    
    date_min = dfs.DATE.min()
    date_max = dfs.DATE.max()
    
    Dates_id = pd.DataFrame({'dates': [date_min + i for i in range( abs(date_max-date_min) * 3 )], 
                             'date_id': [i + 1 for i in range( abs(date_max-date_min) * 3 )]}
                            )
    
    element_id = pd.DataFrame({'element': dfs.ELEMENT.unique(),
                               'element_id': [i + 1 for i in range(len(dfs.ELEMENT.unique()))] })
    
    df_transform = ps.sqldf('''
                            SELECT dfs.* ,
                                   s.station_id,
                                   d.date_id,
                                   e.element_id                                   
                            FROM dfs
                            LEFT JOIN station_id AS s
                                 ON dfs.ID = s.station
                            LEFT JOIN Dates_id AS d
                                 ON dfs.DATE = d.dates
                            LEFT JOIN element_id AS e
                                 ON dfs.ELEMENT = e.element                                 
                            ''')
                            
    df_transform = df_transform[['station_id', 'date_id', 'element_id', 'DATA_VALUE', 'M_FLAG', 'Q_FLAG', 'S_FLAG',
           'OBS_TIME' ]]
    archivos_procesados = pd.DataFrame({'archivos_procesados': archivos})
    print('\n')
    print('Exportando modelo de datos ...')                  
    os.chdir(raw)    
    df_transform.to_csv('data_process.csv', sep=',', index = False)
    element_id.to_csv('element_id.csv', sep=',', index = False)
    Dates_id.to_csv('Dates_id.csv', sep=',', index = False)
    station_id.to_csv('station_id.csv', sep=',', index = False)
    archivos_procesados.to_excel('archivos_procesados.xlsx', index = False)
    print('\n')
    print('Creacion del modelo finalizada.')
    print('Tiempo de ejecución: ' + str(datetime.now() - st))
    
# Añade registros al modelo de datos utilizando la info en bruto nueva.
def add_rows(origin, raw):
    '''
    origin: ruta de origen,
    raw: ruta de destino
    '''
    st = datetime.now()
    print('\n')
    print('Cargando modelo de datos y datos en bruto ...')
    
    os.chdir(raw)
    archivos_procesados_ = pd.read_excel('archivos_procesados.xlsx')
    archivos_procesados = archivos_procesados_.archivos_procesados.unique()
    
    element_id = pd.read_csv('element_id.csv', sep=',')
    Dates_id = pd.read_csv('Dates_id.csv', sep=',')
    station_id = pd.read_csv('station_id.csv', sep=',')
    
    base = glob.glob('*process.csv')
    
    os.chdir(origin)
    archivos = glob.glob('*.csv')
    
    new_archivos = [x for x in archivos if x not in archivos_procesados]
    for archivo in new_archivos:
        print('archivo nuevo detectado: ', archivo)
    dfs = []
    
    for archivo in new_archivos:
        df = pd.read_csv(archivo, sep=',')
        dfs.append(df)
    dfs = pd.concat(dfs , axis = 0, names = list(df.columns))
    
    df_transform = ps.sqldf('''
                            SELECT dfs.* ,
                                   s.station_id,
                                   d.date_id,
                                   e.element_id                                   
                            FROM dfs
                            LEFT JOIN station_id AS s
                                 ON dfs.ID = s.station
                            LEFT JOIN Dates_id AS d
                                 ON dfs.DATE = d.dates
                            LEFT JOIN element_id AS e
                                 ON dfs.ELEMENT = e.element                                 
                            ''')
                            
    df_transform = df_transform[['station_id', 'date_id', 'element_id', 'DATA_VALUE', 'M_FLAG', 'Q_FLAG', 'S_FLAG',
           'OBS_TIME' ]]
    
    for archivo in base:
        num_archivo = re.findall(r'\d+', archivo)
        if len(num_archivo) == 0:
            num_archivo = 0
        else:
            num_archivo = int(num_archivo[-1]) 
    
    os.chdir(raw)
    df_transform.to_csv(str(num_archivo + 1)+'_data_process.csv', sep=',', index = False)
    
    # se agregan los nuevos archivos procesados al historial
    new_archivos = pd.DataFrame({'archivos_procesados': new_archivos})
    archivos_procesados = pd.concat([archivos_procesados_, new_archivos ], axis = 0)
    archivos_procesados.to_excel('archivos_procesados.xlsx', index = False)
    
    print('\n')
    print('nuevos datos agregados exitosamente')
    
    
    
    
    
    
    
    
    

