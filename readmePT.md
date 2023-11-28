# PySolidGUI: Interface Gráfica para o Programa Solid

O PySolidGUI é uma interface gráfica baseada no código Solid, criado por Dennis Milbert ([https://geodesyworld.github.io/SOFTS/solid.htm](https://geodesyworld.github.io/SOFTS/solid.htm)), que permite realizar o cálculo do deslocamento terrestre devido ao efeito de maré em um determinado dia e coordenada terrestre.

A interface foi escrita em Python, utilizando a biblioteca PyQt5, enquanto o backend para os cálculos de deslocamento terrestre foi reproduzido em Fortran90, baseado no código original em Fortran de Dennis Milbert.  

O código original Solid foi alterado apenas em sintaxe para permitir sua utilização em comunicação com Python, através de sub-rotinas em Fortran90. Para entender seu funcionamento, consulte o manual do Solid: [https://geodesyworld.github.io/SOFTS/solid.htm](https://geodesyworld.github.io/SOFTS/solid.htm).

Se desejar utilizar as rotinas em código, o arquivo [pysolid.py](solid/pysolid.py) pode ser utilizado como um módulo. O tutorial/readme para sua utilização em módulo pode ser encontrada em [solid/readme.md](solid/readme.md). Como também o [mapplot.py](map/mapplot.py), o readme pode ser encontrado em [map/readme.md](map/readme.md)

Para acompanhar as atualizações, mesmo que eu não acredite que haverá alguma, pode seguir o projeto [aqui](https://github.com/tanusszabo/PySolidGUI). Para mais informações, entre em contato, Tanus Szabo (tanus.szabo@cnpem.br).

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests) para melhorar o PySolid.

- Versão 1.0
- Última atualização: 23/11/2023
- Criador: Tanus Szabo (tanus.szabo@cnpem.br)

---
# "Instalação"

Para utilizar este software, você pode clonar este repositório diretamente ou usar o comando git para baixar os arquivos:
``` bash
git clone https://github.com/tanusszabo/PySolidGUI
```
Depois de obter os arquivos do repositório, acesse a pasta onde os arquivos foram baixados e execute o script principal, main.py, usando o seguinte comando:
```bash
python3 main.py
```

## Dependências

Certifique-se de ter os pacotes Python necessários instalados, são eles:
- ```PyQt5``` (para GUI)
- ```pandas``` (análise e manipulação de dados)
- ```matplotlib``` (visualização de dados)
- ```numpy``` (só pra usar o logaritmo, pode alterar se quiser)
- ```geopandas``` (análise geoespacial)

 Você pode instalá-los usando o seguinte comando:

```bash
pip3 install PyQt5 pandas matplotlib numpy geopandas
```

---
# Tutorial
O PySolidGUI utiliza parâmetros de dias e coordenadas terrestres para calcular o deslocamento terrestre devido ao efeito de maré, retornando as vertentes latitudinal, longitudinal e radial do deslocamento em metros.

Para realizar os cálculos, basta definir um dia ou conjunto de dias e as coordenadas terrestres.

## Configuração dos Dias

Para configurar os dias de início e fim para o cálculo de maré, você pode utilizar o próprio calendário ou as caixas de texto abaixo.

### Calendário:

- Clique para definir um dia inicial único.
- Segure Shift e clique para definir um conjunto de dias.

### Caixas de texto:

- Você pode definir os dias inicial ou final escrevendo a data no formato **dia/mes/ano**.

## Configuração das Coordenadas

Para configurar as coordenadas para o cálculo da maré, você pode utilizar o mapa interativo ou as caixas de texto abaixo.

### Mapa:

- Clique no mapa para definir a latitude e longitude.
- Alguns aceleradores pelo mundo foram destacados e podem ser observados passando o mouse sobre eles.
- Para mover o mapa, clique e segure com o botão esquerdo do mouse e arraste. Use o scroll/rolagem do mouse para dar zoom. Clique com o botão direito para retornar o mapa à posição original.

### Caixas de Texto:

- Você pode definir a latitude e longitude escrevendo na caixa de texto. Os valores são em graus, o separador decimal é um ponto ( **.** ), a latitude varia de -90 até 90, e a longitude de -180 até 180.

## Gráfico

Selecione um dia ou um conjunto de dias e as coordenadas desejadas para o gráfico. Clique no botão **Plot** e o cálculo será feito, mostrando o gráfico em alguns instantes.

Quanto maior o número de dias, mais demorado será o cálculo.

Você pode mostrar ou ocultar cada uma das vertentes de deslocamento terrestre (radial, latitudinal e longitudinal) nas caixas de seleção acima do gráfico.

## Salvar

Para salvar o gráfico ou os dados do gráfico, utilize o botão **Salvar** no menu acima.

### Salvar dados

Clique em **Salvar dados** para abrir uma janela e definir o local e nome do arquivo para salvar os dados. O arquivo conterá as primeiras três linhas com os parâmetros de latitude, longitude e dias utilizados nos cálculos. As linhas seguintes terão os valores do gráfico, com cada linha representando um ponto e separado em:

    dia e hora, tempo em segundos do início do cálculo, vertente latitudinal (north), vertente longitudinal (east), vertente radial (radial).

### Salvar imagem

Clique em **Salvar imagem** para abrir uma janela e definir o local e nome do arquivo para salvar o gráfico.

---

### Tenha um ótimo dia!
