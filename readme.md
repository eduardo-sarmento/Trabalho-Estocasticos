<p align="center"> 
  <img src="assets/ufes.png" alt="UFES Logo" height="80px">
</p>
<h1 align="center"> Cadeias de Markov em simulação de um jogo de Tênis </h1>
<h3 align="center"> André Altoé, Eduardo Sarmento e Elciney Junior </h3>
<h3 align="center"> Prof. Rodolfo da Silva Villaça </h3>
<h5 align="center"> Processos Estocásticos Aplicados à Computação - <a href="https://www.ufes.br/">Universidade Federal do Espirito Santo</a></h5>

<!-- TABLE OF CONTENTS -->
<h2 id="summary"> :book: Sumário</h2>

<details open="open">
  <summary>Sumário</summary>
  <ol>
    <li><a href="#sobre"> ➤ Sobre</a></li>
    <li><a href="#tecnologias"> ➤ Tecnologias</a></li>
    <li><a href="#cadeia-de-markov"> ➤ Cadeia de Markov</a></li>
    <li><a href="#como-rodar"> ➤ Como Rodar</a></li>
    <li><a href="#creditos"> ➤ Creditos</a></li>
  </ol>
</details>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="sobre"> :pencil: Sobre</h2>

<p align="justify"> 
Neste trabalho nos foi dado o objetivo de simular diferentes partidas de tênis representando o jogo por meio de uma cadeia de Markov, para então observar seu comportamento baseado na diferença da probabilidade de vitória dos adversários.
</p>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="tecnologias"> :hammer: Tecnologias</h2>

<ul>
    <li><img src="assets/python.png" height="16px"/>  Python</li>
    <li><img src="assets/pandas_white.svg" height="28px"/></li>
</ul>

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="cadeia-de-markov"> :loop: Cadeia de Markov</h2>

<p>A seguinte cadeia de Markov foi modelada dentro do sistema, no arquivo <b>markov.py</b></p>

<p align="center"> 
  <img src="assets/markovChain.png" alt="Cadeia de Markov" width="637">
</p>

<p>
    O mesmo funciona chamando a funçao <b>markovWalk</b> utilizando do seu estado atual e sua direção P ou Q, indicados no código como <b>markovWalkLeft</b> e <b>markovWalkRight</b> respectivamente.
</p>


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="como-rodar"> :nut_and_bolt: Como Rodar</h2>

<p> 
    Você pode rodar as simulações simplesmente digitando o seguinte comando em seu terminal:
</p>
<pre><code>$ python main.py</code></pre>


![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

<!-- ABOUT THE PROJECT -->
<h2 id="creditos"> :eyeglasses: Creditos</h2>

<h3>Execução</h3>
<ul>
    <li><a href="https://github.com/faakit/">André Altoé Santiago</a></li>
    <li><a href="https://github.com/eduardo-sarmento/">Eduardo Montagner de Moraes Sarmento</a></li>
    <li><a href="https://github.com/Elcineyjr/">Elciney Mendes Rangel Junior</a></li>
</ul>

<h3>Base Teórica</h3>
- Professor Rodolfo da Silva Villaça