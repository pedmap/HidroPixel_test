import numpy as np
import os
from osgeo import gdal
# from osgeo import gdal
from modulos_files.RDC_variables import RDCVariables
from modulos_files.global_variables import GlobalVariables


def rows_and_columns_from_rdc():
    """Esta função é utilizada para ler o número de linhas e colunas referente aos arquivos raster, tais 
    informações estão contidas nos arquivos .RDC"""

    file = r"C:\Users\joao1\OneDrive\Área de Trabalho\Calcula_Tc_SCS_decliv_indiv_grandesmatrizes_utm_LL\bacia.RDC"
    with open(file, 'r') as rdc_file:
        # Separando os dados do arquivo RDC em função das linhas que contém "rows" ou "columns"
        lines_columns = [line.strip() for line in rdc_file.readlines() if "rows" in line or "columns" in line]

        num_lines, num_columns = 0

        for line in lines_columns:
            if "rows" in line:
                num_lines = int(line.split(":")[-1].strip())
            elif "columns" in line:
                num_columns = int(line.split(":")[-1].strip())

        return num_lines, num_columns

def leh_bacia(file):
    """Esta função é utilizada para ler as informações da bacia hidrográfica (arquivo .rst)"""
    # Criando instâncias das classes
    global_vars = GlobalVariables()
    rdc_vars = RDCVariables()

    # Realizando a abertura do arquivo raster e coletando as informações referentes as dimensões do mesmo
    rst_file = gdal.Open(file)
    
    # Tratamento de erro: verifique se o arquivo foi aberto corretamente
    if rst_file is not None:

        # atualizando os valores das variáveis para coletar o numéro de linhas e colunas do arquivo raster lido
        rdc_vars.nlin = rst_file.RasterYSize
        rdc_vars.ncol = rst_file.RasterXSize

        # Lendo os dados raster como um array 
        dados_lidos_bacia = rst_file.GetRasterBand(1).ReadAsArray()

        # Reorganizando os dados lidos da bacia em uma nova matriz chamada bacia.
        global_vars.bacia = str(dados_lidos_bacia)
        print(type(global_vars.bacia))

        # Fechando o dataset GDAL
        rst_file = None
    else:
        print(f"Failed to open the raster file: {file}")

    return global_vars.bacia

def leh_caracteristica_dRios():
    """Esta função é utilizada para ler as informações acerca da característica dos rios de uma bacia hidrográfica (texto .rst)"""
    global_vars = GlobalVariables()

    # Abrindo o arquivo de texto (.txt) com as informações acerca das classes dos rios
    file = r"C:\Users\joao1\OneDrive\Área de Trabalho\Calcula_Tc_SCS_decliv_indiv_grandesmatrizes_utm_LL\caracteristicas_classes_rios.txt"
    with open(file, 'r', encoding='utf-8') as arquivo_txt:
        #  Atualizando as variáveis que dependem
        arquivo_txt.readline()
        global_vars.nclasses = int(arquivo_txt.readline().strip())  # com base no arquivo fornecido, o número de classes está na segunda linha!! (X)
        arquivo_txt.readline()
        # Inicializando as listas
        j_list = []
        Sclasse_list = []
        Mannclasse_list = []
        Rhclasse_list = []

        # Iterando sobre as linhas do arquivo
        for line in arquivo_txt:
            # Divide a linha nos espaços em branco e converte para float
            indice, Scla, Mann, Rh = map(float, line.split())

            # Adiciona os valores às listas
            j_list.append(indice)
            Sclasse_list.append(Scla)
            Mannclasse_list.append(Mann)
            Rhclasse_list.append(Rh)

        # Convertendo as listas em arrays e armazendo nas respectivas variáveis
        global_vars.j = np.array(j_list)
        global_vars.Sclasse = np.array(Sclasse_list)
        global_vars.Mannclasse = np.array(Mannclasse_list)
        global_vars.Rhclasse = np.array(Rhclasse_list)

    return global_vars.j, global_vars.Sclasse, global_vars.Mannclasse, global_vars.Rhclasse




file = r"C:\Users\joao1\OneDrive\Área de Trabalho\Calcula_Tc_SCS_decliv_indiv_grandesmatrizes_utm_LL\bacia.rst"
file2 = r"C:\Users\joao1\OneDrive\Área de Trabalho\Calcula_Tc_SCS_decliv_indiv_grandesmatrizes_utm_LL\bacia.RDC"
def leh_uso_manning ():
    """Esta função é utilizada para ler as informações acerca do uso do solo e o coeficiente de rugosidade de Manning (arquivo texto - .txt)"""
    # Criando instâncias das classes
    global_vars = GlobalVariables()
    rdc_vars = RDCVariables()
    # Onbtendo o arquivo de texto (.txt) com as informações acerca dos coeficientes De Manning para as zonas da bacia hidrográfica
    file = r'C:\Users\joao1\OneDrive\Área de Trabalho\Calcula_Tc_SCS_decliv_indiv_grandesmatrizes_utm_LL\relacao_uso_Manning.txt'

    # Criando variável extra, para armazenar os tipos de uso e coeficente de Manning
    uso_manning = []
    coef_maning = []
    # Abrindo o arquivo que contém o coeficiente de Manning para os diferentes usos do solo
    with open(file, 'r', encoding='utf-8') as arquivo_txt:
    #  Ignora a primeira linha, pois ela contém apenas o cabeçalho
        firt_line = arquivo_txt.readline()
        # Lê as informações de uso do solo e coeficiente de Manning 
        for line in arquivo_txt:
            # Coletando as informações de cada linha
            info = line.strip().split()

            # Armazenando os valores das linhas nas suas respectivas variáveis
            global_vars.usaux = int(info[0])
            coef_maning = float(info[1])

            # Adionado cada valor as suas respectivas variáveis
            uso_manning = np.append(uso_manning,global_vars.usaux)
            global_vars.Mann = np.append(global_vars.Mann,coef_maning)
        
    return uso_manning, global_vars.Mann
# Chamando a função
resultado_bacia = leh_bacia(file)
print(resultado_bacia)

# for global_vars.tt in range(1, global_vars.Nusomax + 1):
        #     line = arquivo_txt.readline()
        #     global_vars.usaux, global_vars.Mann[global_vars.usaux - 1] = map(float, line.strip().split())





