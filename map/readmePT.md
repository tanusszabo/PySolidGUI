# MapCoordinates

## Visão Geral


Este script em Python, mapplot.py, implementa uma visualização de mapa interativo simples usando `GeoPandas` e `Matplotlib`. O script permite que os usuários ampliem/reduzam e movam pelo mapa, além de interagir com pontos de dados específicos.

## Dependências

Certifique-se de ter os pacotes Python necessários instalados. Você pode instalá-los usando o seguinte comando:

```bash
`pip install geopandas matplotlib`
```

## Uso

Para usar o script, execute-o como módulo principal:

```bash
python mapplot.py
```

Isso inicializará um mapa com configurações padrão e o exibirá interativamente. Você pode ampliar usando a roda de rolagem e mover clicando e arrastando. Além disso, o clique com o botão direito redefine a visualização, e o clique com o botão esquerdo coloca um marcador vermelho na localização clicada.

Também é possível de utilizá-lo como módulo, como no exemplo abaixo:

```python
from mapplot import MapCoordinates
zp = MapCoordinates()
zp.init_plot()
zp.show_plot()
```

## Configuração

O script é projetado para funcionar com um shapefile de mapa mundial, e o arquivo de mapa padrão é definido como [mapfiles/ne\_110m\_admin\_0\_countries\_lakes.dbf](map/mapfiles/ne_110m_admin_0_countries_lakes.dbf). Você pode alterar o arquivo de mapa modificando o parâmetro mapfile no método `init_plot`.

Os shapefiles de mapa foram adquiridos em [https://www.naturalearthdata.com](https://www.naturalearthdata.com/downloads/110m-cultural-vectors/).

O script também inclui pontos de dados predefinidos de instalações de aceleradores. Você pode personalizar esses dados no dicionário `acel_data`. Cada par chave-valor representa o nome da instalação e suas coordenadas de longitude e latitude correspondentes.

## Funcionalidades

### Ampliação

O script suporta ampliação e redução do mapa usando a roda de rolagem. Rode para cima para ampliar e para baixo para reduzir.

### Movimentação

Mova o mapa clicando e arrastando. A visualização atual pode ser redefinida para os limites iniciais clicando com o botão direito no mapa.

### Colocação de Marcadores

Clique com o botão esquerdo no mapa para colocar um marcador vermelho na localização clicada. O marcador representa um ponto selecionado pelo usuário no mapa.

### Informações ao Passar o Mouse

Ao passar o mouse sobre pontos de dados predefinidos (marcadores pretos), são exibidas informações sobre a instalação, incluindo seu nome, latitude e longitude.

## Notas

Certifique-se de que o arquivo de mapa exista no local especificado ou forneça o caminho correto.

Ajuste o dicionário `acel_data` conforme necessário para seus pontos de dados específicos.

O script usa `GeoPandas` para a plotagem do mapa e `Matplotlib` para a visualização interativa.

Sinta-se à vontade para explorar e modificar o script para atender ao seu caso de uso específico. Se encontrar algum problema ou tiver sugestões de melhorias, por favor, me avise!

Aproveite a exploração do mapa interativo!