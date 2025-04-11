
import os
import pandas as pd
import glob
from datetime import datetime, timedelta
import pandasql as ps
from Funciones import *

ruta_orig = os.path.abspath(os.getcwd())
ruta_orig = ruta_orig.replace('\\', '/')
    
origin = ruta_orig + '/base'
raw =  ruta_orig + '/base_aws'

os.chdir(raw)
base = glob.glob('*process.csv')


if len(base) == 0:
    create_model(origin, raw)
else:
    add_rows(origin, raw)
