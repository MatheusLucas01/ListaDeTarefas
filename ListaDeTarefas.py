import streamlit as st
import pandas as pd
import random



# Inicializa a lista de tarefas no estado de sessão
if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

def adicionar_tarefa():
    """Adiciona uma nova tarefa à lista."""
    st.subheader('Adicionar Tarefa')
    nova_tarefa = st.text_input('Digite a nova tarefa:')

    if st.button('Adicionar'):
        if nova_tarefa.strip():  # Verifica se a entrada não está vazia
            st.session_state.tarefas.append(nova_tarefa.strip())
            st.success('Tarefa adicionada com sucesso!')
            exibir_tarefas()
        else:
            st.error('Digite uma tarefa válida.')

def exibir_tarefas():
    """Exibe todas as tarefas cadastradas."""
    st.subheader('Tarefas:')
    if st.session_state.tarefas:
        tarefas_df = pd.DataFrame({
            'Tarefas': st.session_state.tarefas
        })
        st.table(tarefas_df)
    else:
        st.info('Nenhuma tarefa cadastrada ainda.')

def remover_tarefas():
    """Remove uma tarefa específica da lista."""
    st.subheader('Remover Tarefa')
    remover_tarefa = st.selectbox('Selecione a tarefa a ser removida:', st.session_state.tarefas)
    
    if st.button('Remover'):
        if remover_tarefa.strip().lower() in map(str.lower, st.session_state.tarefas):
            if remover_tarefa in st.session_state.tarefas:
                st.session_state.tarefas.remove(remover_tarefa)
                st.success('Tarefa removida com sucesso!')
                exibir_tarefas()
            else:
                st.error('Essa tarefa não existe.')
        else:
            st.error('Digite uma tarefa válida.')

def main():
    st.set_page_config(layout='centered', page_icon="iconesite.png", page_title="Lista de Tarefas", initial_sidebar_state="expanded") # layout da página no centro

    with open("style.css") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    
    st.title("Bem vindo ao Gerenciador de Tarefas")
    # Opções do usuário
    col1, col2 = st.columns([1, 2])  # Define duas colunas com proporções 1:3

    with col1:
        st.image(image='logo.jpg')  # Ícone ou imagem (opcional)

    # Opções do usuário
    with st.sidebar:
        st.logo('logo.jpg')
        opcoes = ['😁 Adicionar Tarefa', '👀 Exibir Tarefas', '😮 Remover Tarefas']
        escolha = st.selectbox("Escolha uma opção:", opcoes)


    if escolha == '😁 Adicionar Tarefa':
        adicionar_tarefa()
    elif escolha == '👀 Exibir Tarefas':
        exibir_tarefas()
    elif escolha == '😮 Remover Tarefas':
        remover_tarefas()

if __name__ == "__main__":
    main()
