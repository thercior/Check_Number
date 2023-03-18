# Check_Number - Verificador de número de celular

## Sobre
O <b>Check_number</b> é uma aplicação rápida e simples para verificar a operadora e a região a que pertence o número de celular digitado.

## Pré-requisitos
É necessário instalar as bibliotecas utilizadas no projeto. Para isto, execute o comando abaixo na raiz do projeto:

<code>pip install -r requirements.txt </code>

A Biblioteca <b>tkinter</b> é nativa e já vem com o python. Portanto, basta apenas importar.

## Utilização
Para executar o programa, basta utilizar qualquer IDE que você utiliza, ou pode executar diretamente do terminal.

Para executar do terminal, navegue até a raiz do projeto, e em seguida digite:
* Para Windows: <code>python checknumber.py</code>
* Para Linux: <code>python3 checknumber.py</code>

Após isso, é solicitado que você informe o número. O número deve ser informado no seguinte padrão:

<code>"Sinal de mais +" "Seguido do código do Páis" "Código da região/estado" "Número de celular, sem ponto, traço"</code>

Exemplo:

        
        +5588999999999
        + - sinal de mais
        55 - código do páis (no caso Brasil)
        88 - código da região/estado (no caso, Ceará)
        999999999 - número do celular
        

Após inserir o número, é informado no terminal o número digitado, se ele é um número válido ou não, a Operadora do celular bem como a região/estado a qual pertence. Conforme a imagem a seguir:

<img align="left" alt="Img" src="https://dsm01pap005files.storage.live.com/y4m5_lsWrvurOrL_2Q5jD60XTzogjp4qltnGNB8SZlGsyCvn0-XpqWpuiSXHjoQxjvMzQ19aXrHsQvOUl1oOANvyaJLZ6NOHzJpuxX6KlA-YLT3yjYMZuadlDNDmHk0K9ZLXEVx6GvNoTjJ9wG03GD_exR1p4vDGhZjoVgJcvy-lhvJBjLLhR1TYIq6ljcls4HTNo70-adLVWptrvknkztfqJkHDPXNOeZo31nPHletXYQ?encodeFailures=1&width=292&height=98">
