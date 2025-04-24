🛒 Estoque Pro – Sistema Simples e Eficiente de Controle de Estoque Estoque Pro é um sistema leve e prático de controle de estoque, desenvolvido com Streamlit e integrado ao Supabase. Com uma interface intuitiva e funcionalidades essenciais, permite o gerenciamento completo de produtos: você pode adicionar, atualizar, consultar e excluir itens com poucos cliques.

🚀 Principais Funcionalidades 📦 Consultar Estoque Pesquisa rápida por nome do produto.

Exibição em tabela com os resultados encontrados.

➕ Adicionar Produto Cadastro de novos produtos com:

Nome do produto

Quantidade

Preço

✏️ Atualizar Produto Edição de quantidade e preço de produtos existentes.

Seleção direta via ID.

❌ Excluir Produto Remoção de produtos com confirmação prévia para evitar erros.

🛠️ Tecnologias Utilizadas Python

Streamlit – Criação da interface interativa.

Supabase – Backend e armazenamento de dados.

Pandas – Manipulação de dados e tabelas.

🧠 Como funciona por trás O estoque é gerenciado em tempo real usando o st.session_state, garantindo uma experiência fluida e sem recarregamentos necessários. Cada item do estoque é representado por:

id: Identificador único.

nome: Nome do produto.

quantidade: quantidade em estoque.

preço: Preço por unidade.

📋 Exemplos de Uso ➕ Adicionar Produto Vá até a aba "Adicionar Produto".

Preencha os campos:

Nome: Cadeira

Quantidade: 10

Preço: R$ 150,00

Clique em Adicionar Produto.

✏️ Atualizar Produto Acesse a aba "Atualizar Produto".

Selecione o ID do produto.

Alterar os dados desejados.

Clique em Atualizar Produto.

❌ Excluir Produto Entre na aba "Excluir Produto".

Escolha o ID do produto.

Confirmar a exclusão.

Esse projeto já está disponível online via Streamlit Cloud, pronto para testes e validação! É ideal para pequenos negócios, feiras, estoques domésticos ou como base para um sistema mais robusto.
