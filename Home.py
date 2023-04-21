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

def tabela_bd (nome_tabela_plural, nome_tabela):

    st.subheader(nome_tabela_plural)

    cnx = create_connection()
    cursor = cnx.cursor()
    query = "SELECT * FROM " + nome_tabela
    cursor.execute(query)
    resultado = cursor.fetchall()
    st.dataframe(resultado)
    cnx.commit()
    cursor.close()
    cnx.close()

def tab1():
    aba1, aba2 = st.tabs(["Médico","Especialidade"])
    
    with aba1:
    
        st.subheader("Cadastrar Médico")

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodEspec FROM especialidade")
        resultado = cursor.fetchall()
        valores = []

        for i in resultado:
            valores.append(i[0])

        with st.form(key="include_medico"):
            input_CodMed = st.text_input(label="Insira o Código do Médico", help = "insira um valor númerico de 7 digitos", max_chars = 7)
            input_name = st.text_input(label="Insira o nome do Médico")
            input_genero = st.selectbox(label="Selecione seu Gênero", options=["M", "F"])
            input_telefone = st.text_input(label="Insira o Telefone")
            input_email = st.text_input(label="Insira o Email")
            input_CodEspec = st.selectbox(label="Insira o Código da Especialidade", options = valores)
            input_button_submit = st.form_submit_button('Cadastrar')

        if input_button_submit:
            st.info(f'Código do Médico: {input_CodMed}')
            st.info(f'Médico: {input_name}')
            st.info(f'Gênero: {input_genero}')
            st.info(f'Telefone: {input_telefone}')
            st.info(f'Email: {input_email}')
            st.info(f'Código da Especialidade: {input_CodEspec}')

            cnx = create_connection()
            cursor = cnx.cursor()
            query = "INSERT INTO Medico (CodMed, NomeMed, Genero, Telefone, Email, CodEspec) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (input_CodMed, input_name, input_genero, input_telefone, input_email, input_CodEspec)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Médico adicionado com sucesso!")

        tabela_bd('Médicos', 'medico')
        
    with aba2:

        st.subheader("Cadastrar Especilidade")

        with st.form(key="include_especialidade"):
            input_CodEsp = st.text_input(label="Insira o Código da Especialidade", help = "insira um valor númerico de 7 digitos", max_chars = 7)
            input_name = st.text_input(label="Insira o nome da Especialidade")
            input_descricao = st.text_input(label="Descrição da Especialidade")
            input_button_submit = st.form_submit_button('Cadastrar')

        if input_button_submit:
            st.info(f'Código Especialidade: {input_CodEsp}')
            st.info(f'Nome: {input_name}')
            st.info(f'Descrição: {input_descricao}')

            cnx = create_connection()
            cursor = cnx.cursor()
            query = "INSERT INTO especialidade (CodEspec, NomeEspec, Descricao) VALUES (%s, %s, %s)"
            values = (input_CodEsp, input_name, input_descricao)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Especialidade adicionada com sucesso!")

        tabela_bd('Especialidade', 'especialidade')

                
def tab2():
    aba1, aba2 = st.tabs(["Médico", "Especialidade"])
                
    with aba1:

        st.subheader('Remover Médico')

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodMed FROM medico")
        resultado = cursor.fetchall()
        valores = []

        for i in resultado:
            valores.append(i[0])

        with st.form(key="Remover_medico"):
            input_CodMed = st.selectbox(label="Insira o Código do Médico", options = valores)
            input_name = st.text_input(label="Insira o nome do Médico")
            input_genero = st.selectbox(label="Selecione seu Gênero", options=["M", "F"])
            input_telefone = st.text_input(label="Insira o Telefone")
            input_email = st.text_input(label="Insira o Email")
            input_CodEspec = st.text_input(label="Insira o Código da Especialidade")
            input_button_submit = st.form_submit_button('Remover')

        if input_button_submit:
            st.info(f'Código do Médico: {input_CodMed}')
            st.info(f'Médico: {input_name}')
            st.info(f'Gênero: {input_genero}')
            st.info(f'Telefone: {input_telefone}')
            st.info(f'Email: {input_email}')
            st.info(f'Código da Especialidade: {input_CodEspec}')

            cnx = create_connection()
            cursor = cnx.cursor()
            query = "DELETE FROM medico WHERE CodMed=%s OR NomeMed=%s OR Genero=%s OR Telefone=%s OR Email=%s OR CodEspec=%s"
            values = (input_CodMed, input_name, input_genero, input_telefone, input_email, input_CodEspec)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Médico removido com sucesso!")

        tabela_bd('Médicos', 'medico')

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

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodEspec FROM especialidade")
        resultado = cursor.fetchall()
        valores = []

        for i in resultado:
            valores.append(i[0])

        with st.form(key="Remover_especialidade"):
            input_CodEsp = st.selectbox(label="Insira o Código da Especialidade", options = valores)
            input_name = st.text_input(label="Insira o nome da Especialidade")
            input_descricao = st.text_input(label="Descrição da Especialidade")
            input_button_submit = st.form_submit_button('Remover')

        if input_button_submit:
            st.info(f'Código Especialidade: {input_CodEsp}')
            st.info(f'Nome: {input_name}')
            st.info(f'Descrição: {input_descricao}')
            
            with create_connection() as cnx:
                delete_especialidades(cnx, input_CodEsp, input_name, input_descricao)

        tabela_bd('Especialidade', 'especialidade')


def tab3():
    aba1, aba2 = st.tabs(["Medico", "Especialidade"])

    with aba1:

        st.subheader('Alterar Médico')

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodMed FROM medico")
        resultado = cursor.fetchall()
        valores = []

        for i in resultado:
            valores.append(i[0])

        with st.form(key="update_medico"):
            input_Cod = st.selectbox(label="Insira o Código do Médico a ser alterado", options = valores)
            input_field = st.selectbox(label="Selecione o campo a ser alterado", options=["Código do Médico","Nome do Médico", "Genero", "Telefone", "Email", "Código da especialidade"])
            input_value = st.text_input(label="Insira o novo valor")
            input_button_submit = st.form_submit_button('Alterar')

        if input_button_submit:
            st.info(f'Código do Médico: {input_Cod}')
            st.info(f'Campo alterado: {input_field}')
            st.info(f'Novo valor: {input_value}')

            if input_field == "Código do Médico":
                input_field = "CodMed"
            if input_field == "Nome do Médico":
                input_field = "NomeMed"
            if input_field == "Código da especialidade":
                input_field = "CodEspec"

            query = f"UPDATE medico SET {input_field} = %s WHERE CodMed = %s"
            values = (input_value, input_Cod)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Médico alterado com sucesso!")

        tabela_bd('Médicos', 'medico')

    with aba2:

        st.subheader('Alterar Especialidade')

        cnx = create_connection()
        cursor = cnx.cursor()
        cursor.execute("SELECT CodEspec FROM especialidade")
        resultado = cursor.fetchall()
        valores = []

        for i in resultado:
            valores.append(i[0])
        
        with st.form(key="update_especialidade"):
            input_Cod = st.selectbox(label="Insira o Código da Especialidade a ser alterada", options = valores)
            input_field = st.selectbox(label="Selecione o campo a ser alterado", options=["Código do especialista","Nome da especialidade", "Descrição"])
            input_value = st.text_input(label="Insira o novo valor")
            input_button_submit = st.form_submit_button('Alterar')

        if input_button_submit:
            st.info(f'Código da especialidade: {input_Cod}')
            st.info(f'Campo alterado: {input_field}')
            st.info(f'Novo valor: {input_value}')

            if input_field == "Código da especialidade":
                input_field = "CodEspec"
            if input_field == "Nome da especialidade":
                input_field = "NomeEspec"
            if input_field == "Descrição":
                input_field = "Descricao"

            query = f"UPDATE especialidade SET {input_field} = %s WHERE CodEspec = %s"
            values = (input_value, input_Cod)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
            cnx.close()
            st.success("Especialidade alterada com sucesso!")

        tabela_bd('Especialidade', 'especialidade')

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
    st.title('Operações CRUD')
    st.markdown("---")

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
