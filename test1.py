 
        # # lendo os arquivos acerda da precipitação das últimas 24 horas
        # with open(arquivo, 'r', encoding = 'utf-8') as arquivo_txt:
        #     arquivo_txt.readline()
        #     dados_lidos_P24 = float(arquivo_txt.read()) # considerando que no arquivo só possui um valor de precipitação

        # # Armazenando o valor da precipitação de 24 horas em uma variável específica
        # self.global_vars.P24 = dados_lidos_P24
for i in range(1, 13):
    name = f"self.dlg.flow_tt.le_{i}_pg1.setText('')"  # Construir o nome da QLineEdit dinamicamente
    print(name)