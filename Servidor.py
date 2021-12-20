import ee
import geemap
import pandas as pd
import datetime
from datetime import timedelta

def mensaje():
    print ("puntos de fuejo")

def descarga():

    #Intialize the library
    ee.Initialize()
    # Import the USGS ground elevation image.
    elv = ee.Image('USGS/SRTMGL1_003')
    #Get the information of the image.
    print(elv.getInfo())
            

if __name__ == '__main__':
    descarga()
            

