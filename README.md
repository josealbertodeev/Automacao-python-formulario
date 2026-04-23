# Automação de Formulário com Python

Este é um projeto simples de automação desenvolvido em Python utilizando a biblioteca `pyautogui`. O script abre o navegador Chrome, acessa uma página web específica e preenche um formulário automaticamente.

## 📂 Arquivos do Projeto

- `main.py`: O script principal que executa a automação passo a passo.
- `posicao.py`: Um script auxiliar utilizado para capturar as coordenadas exatas `(X, Y)` do mouse na tela. Útil para descobrir onde o `pyautogui` deve clicar.

## 🚀 Pré-requisitos

Para rodar este projeto, você precisará ter o Python instalado em seu computador e instalar a biblioteca `pyautogui`. 

Execute o seguinte comando no terminal para instalar as dependências:

```bash
pip install pyautogui
```

## ⚙️ Como usar

1. **Configurar coordenadas (Opcional):** Se o seu monitor tiver uma resolução ou tamanho diferente, talvez os cliques não aconteçam no lugar certo. Use o arquivo `posicao.py` para descobrir a posição correta dos campos no seu monitor. Para usá-lo, rode o script, posicione o mouse sobre o local desejado e aguarde 5 segundos.
2. **Rodar a automação:**
   Execute o script principal:
   ```bash
   python main.py
   ```
   **Importante:** Assim que o script iniciar, não mexa no mouse ou teclado até que a automação seja finalizada para evitar que a digitação ou os cliques aconteçam na janela errada.

## ⚠️ Observações
* O `pyautogui` interage diretamente com a sua tela, então a resolução ou o navegador padrão podem afetar os cliques predefinidos no arquivo `main.py`.
* A página usada no exemplo é `hashtagtreinamentos.com/curso-python`.
