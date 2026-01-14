# Automação de Cadastro de Produtos (PyAutoGUI + Pandas)

Este projeto automatiza o **cadastro de produtos em um site** preenchendo um formulário no navegador de forma automática, a partir de um arquivo **CSV**.  
Foi desenvolvido para fins **didáticos e de portfólio**, demonstrando automação de tarefas repetitivas com Python.

## Demonstração do que o script faz
- Abre o Google Chrome
- Acessa a página de login
- Realiza login (usuário/senha)
- Lê o arquivo `produtos.csv`
- Cadastra cada produto no formulário do site, linha a linha

---

## Tecnologias utilizadas
- **Python 3**
- **PyAutoGUI** (automação por mouse/teclado)
- **Pandas** (leitura e manipulação do CSV)
- **Time** (controle de espera/carregamento)

---

## Estrutura do projeto (sugestão)

├── automacao.py
├── auxiliar.py
├── produtos.csv
└── README.md

---

## Como executar

### 1) Criar e ativar ambiente virtual (opcional, recomendado)
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate


2) Instalar dependências

pip install pyautogui pandas

3) Ajustar arquivo CSV


O arquivo produtos.csv deve conter as colunas esperadas pelo script, por exemplo:
	•	codigo
	•	marca
	•	tipo
	•	categoria
	•	preco_unitario
	•	custo
	•	obs

(Use exatamente os nomes que seu código usa nas linhas tabela.loc[linha, "coluna"].)

4) Executar

python main.py

Configuração importante: coordenadas (x, y)

Como o PyAutoGUI trabalha por posição na tela, você precisa ajustar as coordenadas do seu monitor para:
	•	Campo de e-mail
	•	Campo(s) do formulário
	•	Botões (se houver)

Como descobrir coordenadas
	1.	Abra o site manualmente
	2.	Passe o mouse por cima do local que quer clicar
    3.	Rode no Python:

import pyautogui, time
time.sleep(5)
print(pyautogui.position())

	4.	Copie o (x, y) e coloque no seu script.

Limitações (leia antes)

Este tipo de automação é frágil, porque depende do que está na tela. Pode quebrar se:
	•	mudar resolução / escala do Windows
	•	mudar zoom do navegador
	•	o site mudar layout
	•	aparecer pop-up/anúncio/cookies
	•	a página carregar mais devagar

Recomendação: para automação web mais estável e profissional, considere migrar para Playwright ou Selenium.

Boas práticas recomendadas (para evitar bugs)
	•	Use Ctrl + L antes de digitar o link (garante foco na barra de endereços)
	•	Use time.sleep() ou pyautogui.PAUSE para aguardar carregamento
	•	Evite mexer no mouse/teclado durante a execução
	•	Mantenha o navegador sempre na mesma posição/tamanho

Aviso de segurança

Não suba credenciais reais no repositório (e-mail/senha).
Use variáveis de ambiente ou um arquivo .env ignorado pelo Git quando for evoluir o projeto.

Autor

Ygor B. Ferreira

