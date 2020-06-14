# -*- coding: utf-8 -*-
'''
Created on Sat Jun 13 12:10:23 2020

@author: Joabe
'''

import pandas as pd
import matplotlib.pyplot as plt

Sudeste = ['SP', 'RJ', 'MG', 'ES']
Sul = ['PR', 'SC', 'RS']
Centro_Oeste = ['DF', 'GO', 'MT', 'MS']
Norte = ['AC', 'AM', 'AP', 'PA', 'RO', 'RR', 'TO']
Nordeste = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']
regions = [Sudeste, Sul, Centro_Oeste, Norte, Nordeste]
regions_name = ['Sudeste', 'Sul', 'Centro_Oeste', 'Norte', 'Nordeste']


for index, regions_var in enumerate(regions):

    df_trabalhadores = pd.DataFrame()

    for state in regions_var:
        print(10*'-' + 'CALCULANDO DADOS PARA O ESTADO: '+ state + 10*'-')
        name_csv = 'D_ETL_IMO_EXTRACAO_SINE_ABERTO_TRABALHADORES_' + state + '.csv'
        df_temp = pd.read_csv(name_csv, sep=';', encoding='iso-8859-1')
        df_trabalhadores = pd.concat([df_trabalhadores, df_temp])
    
    # Analise da escolaridade   
    
    series_categ = df_temp['ESCOLARIDADE'].value_counts()
    series_categ_porc = df_temp['ESCOLARIDADE'].value_counts(normalize = True) * 100
    
    labels = series_categ_porc.index.tolist()
    sizes = series_categ_porc.to_numpy()
    
    fig1, ax1 = plt.subplots()
    name1 = 'escolaridade_trabalhadores_regiao_' + regions_name[index]
    plt.xticks(rotation=45)
    series_categ.plot.bar(x = 'Escolaridade dos trabalhadores: Região ' + str(regions_var), fontsize=8, rot=20)
    ax1.set_title('Escolaridade dos trabalhadores: Região ' + regions_name[index])
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()  
    plt.show()
    plt.pause(0.1)
    fig1.savefig(name1 + '.png', dpi = 600)   # save the figure to file
    plt.close(fig1)    # close the figure window
    
    name2 = 'escolaridade_trabalhadores_porcentagem_regiao_' + regions_name[index]
    fig2, ax2 = plt.subplots()
    pie = ax2.pie(sizes, autopct='%1.1f%%', pctdistance = 1.1, labeldistance = 1.1)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.legend(pie[0], labels, loc='upper right', bbox_to_anchor = (1,1))
    ax2.set_title('Escolaridade dos trabalhadores (%): Região ' + regions_name[index])
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()  
    plt.show()
    plt.pause(0.1)
    fig2.savefig(name2 + '.png', dpi = 600)   # save the figure to file
    plt.close(fig2)    # close the figure window
    
    # Analise sobre estudo  
    
    series_categ = df_temp['ESTUDANTE'].value_counts()
    series_categ_porc = df_temp['ESTUDANTE'].value_counts(normalize = True) * 100
    
    labels = series_categ_porc.index.tolist()
    sizes = series_categ_porc.to_numpy()
    
    fig1, ax1 = plt.subplots()
    name1 = 'estudante_trabalhadores_regiao_' + regions_name[index]
    plt.xticks(rotation=0)
    series_categ.plot.bar(x = 'Trabalhador estudadando? Região ' + str(regions_var), fontsize=8, rot=0)
    ax1.set_title('Trabalhadores que estão estudando: Região ' + regions_name[index])
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()  
    plt.show()
    plt.pause(0.1)
    fig1.savefig(name1 + '.png', dpi = 600)   # save the figure to file
    plt.close(fig1)    # close the figure window
    
    name2 = 'estudante_trabalhadores_porcentagem_regiao_' + regions_name[index]
    fig2, ax2 = plt.subplots()
    pie = ax2.pie(sizes, autopct='%1.1f%%', pctdistance = 1.1, labeldistance = 1.1)
    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax2.legend(pie[0], labels, loc='upper right', bbox_to_anchor = (1,1))
    ax2.set_title('Trabalhadores que estão estudando (%): Região ' + regions_name[index])
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()  
    plt.show()
    plt.pause(0.1)
    fig2.savefig(name2 + '.png', dpi = 600)   # save the figure to file
    plt.close(fig2)    # close the figure window

    # Análise de preenchimento - Qntdade de informações não preenchidas
    series_nan = df_trabalhadores.isnull().sum(axis = 0)
    series_nan_porc = series_nan / len(df_trabalhadores) * 100
    df_nan = pd.concat([series_nan, series_nan_porc], axis=1)
    df_nan.rename(columns={0: "Valores absolutos de NaN", 1: "Valores percentuais de NaN"}, inplace = True)
    df_nan.to_excel('nan_data_excel_'+regions_name[index]+'.xlsx')
    df_nan.to_csv('nan_data_csv_'+regions_name[index]+'.csv')
    



