from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QFileDialog

# Initialize Qt resources from file resources.py
from .resources import *

# Import the code for the dialog
from .hidroPixel_dialog import HidroPixelDialog
from .modulos_files import global_variables,RDC_variables
import os.path
import sys, os
from osgeo import ogr

# Importing libs
import numpy as np


def carregaArquivos(self):
        """Esta função é utilizada para adicionar layers no projeto"""
        self.abrir_arquivo = str(QFileDialog.getOpenFileName(caption="Escolha uma camada!", filter="Shapefiles (*.shp)")[0])
        
        # verificar se abrir_camada for diferente de vazio: executa a função de adicionar
        if (self.abrir_arquivo != ''):
            self.iface.addVectorLayer(self.abrir_arquivo, os.path.splitext(os.path.basename(self.abrir_arquivo))[0], "ogr")
            self.dlg.lineEdit.setText(self.abrir_arquivo)