# Tutorial PySolidGUI

Este é um tutorial de como utiliza a interface gráfica PySolidGUI, baseada no programa Solid de Dennis Milbert [https://geodesyworld.github.io/SOFTS/solid.htm](https://geodesyworld.github.io/SOFTS/solid.htm).

O PySolidGUI utiliza parâmetros de dias e coordenadas terrestres para fazer o cálculo do deslocamento terrestre, devido ao efeito de maré. Esse cálculo retorna as vertentes latitudinal, longitudinal e radial do deslocamento em metros.

Para realizar os cálculos, basta definir um dia ou conjunto de dias e as coordenadas terrestres.

----
## Configuração dos Dias
Para configurar os dias de início e fim para o cálculo de maré, você pode utilizar o próprio calendário ou nas caixas de texto abaixo.

### Calendário:
Apenas clicando você define um dia inicial único.

Segurando Shift e clicando você define conjunto de dias.
### Caixas de texto:
Você pode definir os dias inicial ou finai escrevendo a data em um formato **dia/mes/ano**.

----
## Configuração das Coordenadas
Para configurar as coordenadas para o cálculo da maré, você pode utilizar o mapa interativo, ou as caixas de texto abaixo.
### Mapa:
Clicando no mapa você irá definir a latitude e longitude de onde clicou. Alguns aceleradores pelo mundo foram destacados e podem ser observados passando com o mouse em cima.

Se quiser movimentar o mapa, clicando e segurando com o botão esquerdo do mouse você arrasta a posição do mapa. Com o scroll/rolagem do mouse você pode dar zoom. Clicando com o botão direito você retorna o mapa para a posição original.
### Caixas de Texto:
Você pode definir a latitude e longitude escrevendo elas na caixa de texto. Os valores são em graus, o separador decimal é um ponto ( **.** ), não uma vírgula ( **,** ), a latitude recebe valores de -90 até 90, e a longitude de -180 até 180.

----
## Gráfico
Selecionado um dia ou um conjunto de dias, e as coordenadas que você gostaria de fazer o gráfico, basta clicar no botão **Plot** que você o cálculo será feito e o gráfico aparecerá em alguns instantes.

Quanto maior o número de dias, mais o cálculo irá a demorar.

Cada uma das vertentes de deslocamento terrestre, radial, latitudinal e longitudinal, podem ser mostradas ou escondidas nas caixas de seleção acima do gráfico.

----
## Salvar
Para salvar o gráfico ou os dados do gráfico, utilize o botão **Salvar** no menu acima.
### Salvar dados
Clicando em **Salvar dados**, abrirá uma janela para definir o local e nome de salvamento dos dados.

O arquivo salvo terá nas primeiras 3 linhas os parâmetros de latitude, longitude e dias utilizado para os cálculos, e as linhas seguintes terão os valores do gráfico em que cada linha determina um ponto, separado em:

    dia e hora, tempo em segundos do início do cálculo, vertente latitudinal (north), vertente longitudinal (east), vertente radial (radial). 
### Salvar imagem
Clicando em **Salvar imagem**, abrirá uma janela para definir o local e nome de salvamento do gráfico.


Para mais informações sobre o programa, consulte a informações no menu **Ajuda > Sobre**, ou contate o criador Tanus Szabo (tanus.szabo@cnpem.br).