import streamlit as st
from app import *
from conexao import *

def criar():
    
    novas_areas = []
    areas_tipos = []
    num_novas_areas = st.number_input("Adicione o Nome da coluna ?", min_value=1, max_value=10, value=1)
    nome_tabela = st.text_input(f"Informe o nome da Tabela")

    for i in range(num_novas_areas):
        nova_area = st.text_input(f"Digite o nome da Coluna {i+1}", value="None")
        area_tipo = st.text_input(f"Digite o tipo de Valor (Ex: VARCHAR(52), INT, CHAR(2)...)")
        novas_areas.append(nova_area)
        areas_tipos.append(area_tipo)

    primary_key = st.text_input("Nome da Coluna chave ?")
    if st.button("Criar tabela"):

        columns = [(primary_key, 'INT NOT NULL PRIMARY KEY AUTO_INCREMENT')]
        for area, tipo in zip(novas_areas, areas_tipos):
            columns.append((area, tipo))
        table_exists = False
        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]

        if nome_tabela in tables:
            table_exists = True
        cursor.close()
        cnx.close()

        if not table_exists:
            query = f"CREATE TABLE {nome_tabela} ({', '.join([f'{col[0]} {col[1]}' for col in columns])})"
            cnx = create_connection()
            cursor = cnx.cursor()
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Tabela criada com sucesso!")
        else:
            st.warning("A tabela já existe no banco de dados.")