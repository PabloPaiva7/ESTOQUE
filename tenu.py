import streamlit as st
from supabase import create_client, Client

# Configuração do Supabase
SUPABASE_URL = "https://ymxvmwhtsqtjcmvsoqpw.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlteHZtd2h0c3F0amNtdnNvcXB3Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDQ3NDUwNzgsImV4cCI6MjA2MDMyMTA3OH0.ju75r5ixwbb6kjjSFbUrJhpzZ960NnrXaDLHelhtnaQ"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

st.set_page_config(page_title="Controle de Estoque", layout="wide")

# Inicializa a estrutura se não existir
if "estoque" not in st.session_state:
    st.session_state.estoque = []

# Funções
def carregar_produtos(filtro=None):
    produtos = st.session_state.estoque
    if filtro:
        return [p for p in produtos if filtro.lower() in p["nome"].lower()]
    return produtos

def adicionar_produto(nome, quantidade, preco):
    novo_id = st.session_state.estoque[-1]["id"] + 1 if st.session_state.estoque else 1
    st.session_state.estoque.append({
        "id": novo_id,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    })
    st.success("✅ Produto adicionado com sucesso!")

def atualizar_produto(id, quantidade, preco):
    for produto in st.session_state.estoque:
        if produto["id"] == id:
            produto["quantidade"] = quantidade
            produto["preco"] = preco
            st.success("✅ Produto atualizado!")
            break

def excluir_produto(id):
    st.session_state.estoque = [p for p in st.session_state.estoque if p["id"] != id]
    st.success("🗑️ Produto excluído!")

# Sidebar
with st.sidebar:
    st.title("🛒 Estoque Pro")
    st.markdown("Sistema de controle de estoque estilo SaaS.")
    aba = st.radio("📌 Selecione uma funcionalidade", ["📦 Listar Estoque", "➕ Adicionar Produto", "✏️ Atualizar Produto", "❌ Excluir Produto"])
    st.markdown("---")
    st.caption("💡 Desenvolvido com Streamlit")

# Páginas
st.title("📊 Painel de Controle de Estoque")

if aba == "📦 Listar Estoque":
    st.subheader("🔍 Buscar Produtos no Estoque")
    filtro_nome = st.text_input("Digite parte do nome do produto")
    produtos = carregar_produtos(filtro_nome)

    if produtos:
        st.write("Produtos encontrados:")
        st.dataframe(produtos, use_container_width=True)
    else:
        st.info("Nenhum produto encontrado com esse nome.")

elif aba == "➕ Adicionar Produto":
    st.subheader("📝 Novo Produto")
    with st.form("form_adicionar"):
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome do Produto")
        with col2:
            preco = st.number_input("Preço (R$)", min_value=0.0, format="%.2f")
        quantidade = st.number_input("Quantidade", min_value=0, step=1)
        submitted = st.form_submit_button("Adicionar Produto")
        if submitted:
            if nome.strip() == "":
                st.warning("⚠️ O nome do produto não pode estar vazio.")
            else:
                adicionar_produto(nome, quantidade, preco)

elif aba == "✏️ Atualizar Produto":
    st.subheader("🔧 Atualizar Produto Existente")
    produtos = carregar_produtos()
    ids = [p["id"] for p in produtos]
    if ids:
        id_selecionado = st.selectbox("Selecione o ID do Produto", ids)
        produto = next(p for p in produtos if p["id"] == id_selecionado)
        with st.form("form_atualizar"):
            col1, col2 = st.columns(2)
            with col1:
                quantidade = st.number_input("Nova Quantidade", value=produto["quantidade"], min_value=0, step=1)
            with col2:
                preco = st.number_input("Novo Preço", value=produto["preco"], min_value=0.0, format="%.2f")
            submitted = st.form_submit_button("Atualizar Produto")
            if submitted:
                atualizar_produto(id_selecionado, quantidade, preco)
    else:
        st.info("Nenhum produto cadastrado ainda.")

elif aba == "❌ Excluir Produto":
    st.subheader("⚠️ Excluir Produto do Estoque")
    produtos = carregar_produtos()
    ids = [p["id"] for p in produtos]
    if ids:
        id_selecionado = st.selectbox("Selecione o ID do Produto para Excluir", ids)
        produto = next(p for p in produtos if p["id"] == id_selecionado)
        st.warning(f"Tem certeza que deseja excluir **{produto['nome']}**?")
        if st.button("Confirmar Exclusão"):
            excluir_produto(id_selecionado)
    else:
        st.info("Nenhum produto para excluir.")

