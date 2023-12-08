"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ MODULE FOR CREATION OF GENERAL VARIABLES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Objective: This file is responsible for creating the general variables necessary for the HidroPixel Plugin operation.
Author: João Vitor Dias
Supervisor: Adriano Rolim
Date of last update: 30/11/2023

"""
# IMPORTING 
import numpy as np

class GlobalVariables:
    """
    This class is responsible for creating the general variables necessary for the HidroPixel Plugin operation.
    """
    def __init__(self):
        """
        This method is responsible for creating the general variables necessary for the HidroPixel Plugin operation.
        """
        # Matrix's declaration
        self.dir = np.empty((0,0), dtype = np.int16)
        self.dren = np.empty((0,0), dtype = np.int16)   
        self.MDEint = np.empty((0,0), dtype = np.int16)
        self.cabeceira = np.empty((0,0), dtype = np.int16)
        self.bacia = np.empty((0,0), dtype = np.int16)
        self.usosolo = np.empty((0,0), dtype = np.int16)
        self.classerio = np.empty((0,0), dtype = np.int16)
        self.refcabtre = np.empty((0,0), dtype = np.int16)
        self.pixeldren = np.empty((0,0), dtype = np.int16)
        self.contaaux = np.empty((0,0))
        self.TREpix = np.empty((0,0), dtype = np.int16)
        self.CABEpix = np.empty((0,0), dtype = np.float16)
        self.numcabe = np.empty((0,0), dtype = np.float16)
        self.MEDreal = np.empty((0,0))
        self.MDE = np.empty((0,0), dtype = np.float64)
        self.DIST = np.empty((0,0), dtype = np.float64) # !
        self.DISTtre = np.empty((0,0), dtype = np.float64)# !
        self.TS = np.empty((0,0), dtype = np.float64)
        self.TScabe = np.empty((0,0), dtype = np.float64)
        self.TScabe2d = np.empty((0,0), dtype = np.float64)
        self.TSnaocabe2d = np.empty((0,0), dtype = np.float64)
        self.TStodos2d = np.empty((0,0), dtype = np.float64)
        self.contadren = np.empty((0,0), dtype = np.float16)
        self.TempoRio = np.empty((0,0), dtype = np.float64)
        self.TempoRioR = np.empty((0,0), dtype = np.float64)
        self.Lac = np.empty((0,0), dtype = np.float64)
        self.Lfoz = np.empty((0,0), dtype = np.float64)
        self.TempoTot = np.empty((0,0), dtype = np.float64)
        self.DECLIVpix = np.empty((0,0), dtype = np.float64)
        self.Somaaux = np.empty((0,0), dtype = np.float64)
        self.Somaauxpond = np.empty((0,0), dtype = np.float64)
        self.SomaauxDist = np.empty((0,0), dtype = np.float64)
        self.DECLIVpixjus = np.empty((0,0),dtype = np.float64)
        self.TSpix = np.empty((0,0), dtype = np.float64)
        self.TSpixacum = np.empty((0,0), dtype = np.float64)

        # vector's declaration
        self.lincontadren = np.array([], dtype = np.int16)
        self.colcontadren = np.empty([], dtype = np.int16)
        self.lincabe = np.empty([], dtype = np.int16)
        self.colcabe = np.empty([], dtype = np.int16)
        self.Sclasse = np.empty([], dtype = np.int16)
        self.usaux = np.empty([], dtype = np.int16)
        self.Mann = np.empty([], dtype = np.int16)
        self.Mannclasse = np.empty([], dtype = np.int16)
        self.Rhclasse = np.empty([], dtype = np.int16)
        self.dlin = np.empty((128), dtype = int)
        self.dcol = np.empty((128), dtype = int)
        
        # string's declaration
        self.texto1= ""
        self.texto2= ""
        self.texto7 = ""
        self.texto8 = ""
        self.subtipodecliv = ""
        self.unidaderef3 = ""

        # Int's variables declaration
        self.linaux = 0
        self.linhaux1 = 0
        self.linhaux0 = 0
        self.colaux = 0
        self.colaux1 = 0
        self.colaux0 = 0
        self.linaux2 = 0
        self.colaux2 = 0
        self.linaux3 = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.F = 0
        self.G = 0
        self.H = 0
        self.j = 0
        self.resplist =0
        self.cont = 0
        self.t = 0
        self.tt = 0
        self.Nusomax = 0
        self.tipo = 0    
        self.maxdir = 0
        self.Ntre = 0
        self.metro = 0
        self.Ttreaux = 0
        self.casserioaux = 0
        self.nclasses = 0
        self.ll = 0
        self.cc = 0
        self.pixel_ref_dren = 0
        self.numtreauxmax = 0


        # Real varibles declaration
        self.xmin = 0.0
        self.xmax = 0.0
        self.ymin = 0.0
        self.ymax = 0.0
        self.dx = 0.0
        self.Xesq = 0.0
        self.Xdir = 0.0
        self.Yinf = 0.0
        self.Ysup = 0.0
        self.Xres = 0.0
        self.Yres = 0.0
        self.Xres2 = 0.0
        self.diagonal = 0.0
        self.lado = 0.0
        self.auxdist = 0.0
        self.tamcam = np.float64(0.0)
        self.Ltreaux = np.float64(0.0)
        self.Streaux = np.float64(0.0)
        self.Lfozaux1 = np.float64(0.0)
        self.Lfozaux2 = np.float64(0.0)
        self.Velaux = np.float64(0.0)
        self.Rhaux = np.float64(0.0)
        self.naux = np.float64(0.0)
        self.Saux = np.float64(0.0)
        self.Laux = np.float64(0.0)
        self.P24 = np.float64(0.0)
        self.Taux = np.float64(0.0)        
        self.DISTtreaux = np.float64(0.0)   
        self.tamfoz = np.float64(0.0)
        self.Tempoauxac = np.float64(0.0)
        self.Tempoaux = np.float64(0.0) 
        self.auxTempoCanal = np.float64(0.0)
        self.Streaux2 = np.float64(0.0)
        self.Difcota = np.float64(0.0)   
        self.Lincr = np.float64(0.0)
        self.Smin = np.float64(0.0)
        self.tempocam = np.float64(0.0) 
        self.Smax = np.float64(0.0)

        # Int 4bytes
        self.numncabeaux = np.int32(0)
        self.Ncabec = np.int32(0)

