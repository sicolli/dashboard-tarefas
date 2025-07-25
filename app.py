import streamlit as st
import pandas as pd

if "tarefas" not in st.session_state:
    st.session_state["tarefas"] = []

st.title("📋 Dashboard de Tarefas")

with st.form("form_tarefa", clear_on_submit=True):
    titulo = st.text_input("Título da tarefa")
    status = st.selectbox("Status", ["Pendente", "Em andamento", "Concluída"])
    prioridade = st.selectbox("Prioridade", ["Baixa", "Média", "Alta"])
    submit = st.form_submit_button("Adicionar")

    if submit and titulo:
        st.session_state["tarefas"].append({
            "Título": titulo,
            "Status": status,
            "Prioridade": prioridade
        })

st.sidebar.header("Filtros")
status_filtro = st.sidebar.multiselect("Filtrar por status", ["Pendente", "Em andamento", "Concluída"])
prioridade_filtro = st.sidebar.multiselect("Filtrar por prioridade", ["Baixa", "Média", "Alta"])

df = pd.DataFrame(st.session_state["tarefas"])

if not df.empty:
    if status_filtro:
        df = df[df["Status"].isin(status_filtro)]
    if prioridade_filtro:
        df = df[df["Prioridade"].isin(prioridade_filtro)]

    st.subheader("📌 Tarefas")
    st.dataframe(df.reset_index(drop=True))
else:
    st.info("Nenhuma tarefa adicionada ainda.")
