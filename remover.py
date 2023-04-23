import streamlit as st
from app import *
from funcs import *

def remover():

    st.header('Operação de Remoção')
    st.markdown("---")

    aba1, aba2 = st.tabs(["Médico", "Especialidade"])
                
    with aba1:

        st.subheader('Remover Médico')

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodMed FROM medico")
        resultado = cursor.fetchall()
        valores = []
        
        with st.form(key="Remover_medico"):
            valores = [i[0] for i in resultado]
            input_CodMed = st.selectbox(label="Insira o Código do Médico", options = valores)
            input_button_submit = st.form_submit_button('Remover')

        if input_button_submit:
            st.info(f'Código do Médico: {input_CodMed}')

            cursor.execute("DELETE FROM medico WHERE CodMed =" + input_CodMed)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Médico removido com sucesso!")

        tabela_bd('Médicos', 'medico')

    with aba2:
    
        st.subheader("Remover Especilidade")

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodEspec FROM especialidade")
        resultado = cursor.fetchall()
        valores = []

        with st.form(key="Remover_especialidade"):
            valores = [i[0] for i in resultado]
            input_CodEsp = st.selectbox(label="Insira o Código da Especialidade", options = valores)
            input_button_submit = st.form_submit_button('Remover')

        if input_button_submit:
            st.info(f'Código Especialidade: {input_CodEsp}')

            cursor.execute("DELETE FROM especialidade WHERE CodEspec =" + input_CodEsp)
            cnx.commit()
            cursor.close()
            st.success("Especialidade removida com sucesso!")

        tabela_bd('Especialidade', 'especialidade')
