import streamlit as st
import mysql.connector

st.set_page_config(
    page_title="Operações CRUD",
    page_icon="📄",
    layout="centered",
)

# Função para criar uma conexão com o banco de dados
def create_connection():                                        
    cnx = mysql.connector.connect(user='root',                  #########################################################################
                                password='SUA SENHA',           ########## ADICIONE SEUS DADOS DE CONEXÃO COM O BANCO DE DADOS ##########
                                host='localhost',               #########################################################################
                                database='clinicasmedicas')
    return cnx

st.title('Operações CRUD')
st.markdown("---")

def tab1():
    aba1, aba2 = st.tabs(["Médico","Especialidade"])
    
    with aba1:

        st.subheader("Cadastrar Médico")

        with st.form(key="include_medico"):
            input_CodMed = st.number_input(label="Insira o Código do Médico", format="%d", step=1)
            input_name = st.text_input(label="Insira o nome do Médico")
            input_genero = st.selectbox(label="Selecione seu Gênero", options=["M", "F"])
            input_telefone = st.text_input(label="Insira o Telefone")
            input_email = st.text_input(label="Insira o Email")
            input_CodEspec = st.text_input(label="Insira o Código da Especialidade")
            input_button_submit = st.form_submit_button('Cadastrar')

        if input_button_submit:
            st.write(f'Código do Médico: {input_CodMed}')
            st.write(f'Médico: {input_name}')
            st.write(f'Gênero: {input_genero}')
            st.write(f'Telefone: {input_telefone}')
            st.write(f'Email: {input_email}')
            st.write(f'Código da Especialidade: {input_CodEspec}')

            query = "INSERT INTO Medico (CodMed, NomeMed, Genero, Telefone, Email, CodEspec) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (input_CodMed, input_name, input_genero, input_telefone, input_email, input_CodEspec)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Médico adicionado com sucesso!")

    with aba2:

        st.subheader("Cadastrar Especilidade")

        with st.form(key="include_especialidade"):
            input_CodEsp = st.number_input(label="Insira o Código da Especialidade", format="%d", step=1)
            input_name = st.text_input(label="Insira o nome da Especialidade")
            input_descricao = st.text_input(label="Descrição da Especialidade")
            input_button_submit = st.form_submit_button('Cadastrar')

        if input_button_submit:
            st.write(f'Código Especialidade: {input_CodEsp}')
            st.write(f'Nome: {input_name}')
            st.write(f'Descrição: {input_descricao}')

            query = "INSERT INTO Medico (CodEspec, NomeEspec, Descricao) VALUES (%s, %s, %s)"
            values = (input_CodEsp, input_name, input_descricao)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Especialidade adicionada com sucesso!")
                
def tab2():
    aba1, aba2 = st.tabs(["Médico", "Especialidade"])
                
    with aba1:

        st.subheader('Remover Médico')

        with st.form(key="Remover_medico"):
            input_CodMed = st.number_input(label="Insira o Código do Médico", format="%d", step=1)
            input_name = st.text_input(label="Insira o nome do Médico")
            input_genero = st.selectbox(label="Selecione seu Gênero", options=["M", "F"])
            input_telefone = st.text_input(label="Insira o Telefone")
            input_email = st.text_input(label="Insira o Email")
            input_CodEspec = st.text_input(label="Insira o Código da Especialidade")
            input_button_submit = st.form_submit_button('Remover')

        if input_button_submit:
            st.write(f'Código do Médico: {input_CodMed}')
            st.write(f'Médico: {input_name}')
            st.write(f'Gênero: {input_genero}')
            st.write(f'Telefone: {input_telefone}')
            st.write(f'Email: {input_email}')
            st.write(f'Código da Especialidade: {input_CodEspec}')

            cnx = create_connection()
            cursor = cnx.cursor()
            query = "DELETE FROM medicos WHERE CodMed=%s OR NomeMed=%s OR Genero=%s OR Telefone=%s OR Email=%s OR CodEspec=%s"
            values = (input_CodMed, input_name, input_genero, input_telefone, input_email, input_CodEspec)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Médico removido com sucesso!")

    with aba2:

        def delete_especialidades(cnx, input_CodEsp, input_name, input_descricao):
            cursor = cnx.cursor()
            query = "DELETE FROM especialidade WHERE CodEspec = %s OR NomeEspec = %s OR Descricao = %s"
            values = (input_CodEsp, input_name, input_descricao)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            st.success("Especialidade removida com sucesso!")
        
        st.subheader("Remover Especilidade")

        with st.form(key="Remover_especialidade"):
            input_CodEsp = st.number_input(label="Insira o Código da Especialidade", format="%d", step=1)
            input_name = st.text_input(label="Insira o nome da Especialidade")
            input_descricao = st.text_input(label="Descrição da Especialidade")
            input_button_submit = st.form_submit_button('Remover')

        if input_button_submit:
            st.write(f'Código Especialidade: {input_CodEsp}')
            st.write(f'Nome: {input_name}')
            st.write(f'Descrição: {input_descricao}')
            
            with create_connection() as cnx:
                delete_especialidades(cnx, input_CodEsp, input_name, input_descricao)
        
def tab3():
    aba1, aba2 = st.tabs(["Medico", "Especialidade"])

    with aba1:
            
            st.title('Alterar Médico')

            with st.form(key="update_medico"):
                input_Cod = st.number_input(label="Insira o Código do Médico a ser alterado", format="%d", step=1)
                input_field = st.selectbox(label="Selecione o campo a ser alterado", options=["CodMed","NomeMed", "Genero", "Telefone", "Email", "CodEspec"])
                input_value = st.text_input(label="Insira o novo valor")
                input_button_submit = st.form_submit_button('Alterar')

            if input_button_submit:
                st.write(f'Código da Clinica: {input_Cod}')
                st.write(f'Campo a ser alterado: {input_field}')
                st.write(f'Novo valor: {input_value}')

                query = f"UPDATE Medico SET {input_field} = %s WHERE CodMed = %s"
                values = (input_value, input_Cod)
                cnx = create_connection()
                cursor = cnx.cursor()
                cursor.execute(query, values)
                cnx.commit()
                cursor.close()
                cnx.close()
                st.success("Médico alterado com sucesso!")

    with aba2:
            
            st.title('Alterar Especialidade')

            with st.form(key="update_especialidade"):
                input_Cod = st.number_input(label="Insira o Código da Especialidade a ser alterada", format="%d", step=1)
                input_field = st.selectbox(label="Selecione o campo a ser alterado", options=["CodEspec","NomeEspec", "Descricao"])
                input_value = st.text_input(label="Insira o novo valor")
                input_button_submit = st.form_submit_button('Enviar')

            if input_button_submit:
                st.write(f'Código da Clínica: {input_Cod}')
                st.write(f'Campo a ser alterado: {input_field}')
                st.write(f'Novo valor: {input_value}')

                query = f"UPDATE Medico SET {input_field} = %s WHERE CodEspec = %s"
                values = (input_value, input_Cod)
                cnx = create_connection()
                cursor = cnx.cursor()
                cursor.execute(query, values)
                cnx.commit()
                cursor.close()
                cnx.close()
                st.success("Especialidade alterada com sucesso!")

def tab4():
    
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

def main():
    cnx=create_connection()    
    cursor=cnx.cursor
    
    tabs = ["Cadastrar", "Remover", "Atualizar", "Criar"]
    selected_tab = st.sidebar.radio("Selecione a Operação", tabs)

    if selected_tab == "Cadastrar":
        tab1()
    elif selected_tab == "Remover":
        tab2()
    elif selected_tab == "Atualizar":
        tab3()
    elif selected_tab == "Criar":
        tab4()

if __name__ == "__main__":
    main()
