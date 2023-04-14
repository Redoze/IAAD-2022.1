from os import write
import streamlit as st;

st.title("Incluir Médico")

with st.form(key="include_medico"):
    input_CodMed = st.number_input(label="Insira o Código do Médico", format="%d", step=1)
    input_name = st.text_input(label="Insira o nome do Médico")
    input_genero = st.selectbox(label="Selecione seu Gênero", options=["M", "F"])
    input_telefone = st.number_input(label="Insira o Telefone",format="%d", step=1)
    input_email = st.text_input(label="Insira o Email")
    input_CodEspec = st.number_input(label="Insira o Código da Especialidade", format="%d", step=1)
    input_button_submit = st.form_submit_button('Enviar')

if input_button_submit:
    st.write(f'Código do Médico: {input_CodMed}')
    st.write(f'Médico: {input_name}')
    st.write(f'Gênero: {input_genero}')
    st.write(f'Telefone: {input_telefone}')
    st.write(f'Email: {input_email}')
    st.write(f'Código da Especialidade: {input_CodEspec}')
