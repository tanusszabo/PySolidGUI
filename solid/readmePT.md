# PySolid
O PySolid é uma biblioteca em Python que fornece uma interface para realizar cálculos de deslocamento terrestre devido ao efeito de maré com base no código Solid, criado por Dennis Milbert. O código original em Fortran foi adaptado e incorporado nesta biblioteca, permitindo a integração fácil com Python.

## Instalação
Antes de usar o PySolid, é necessário instalar as bibliotecas numpy e pandas:

```bash
pip install numpy pandas
```

## Como Usar
A seguir, um exemplo básico de como utilizar o PySolid para calcular o deslocamento terrestre e gerar um gráfico.

```python
from pysolid import PySolid
import matplotlib.pyplot as plt

# Criar uma instância do PySolid
ps = PySolid()

# Configurar as coordenadas (latitude e longitude)
ps.set_coordinates(-22.80719940, -47.05231470)

# Configurar o intervalo de tempo (data inicial, formato da data, dias de cálculo)
ps.set_time_range('02/03/2028', date_format='%d/%m/%Y', days=7)

# Realizar o cálculo de deslocamento terrestre
ps.tide_calculation()

# Salvar os DataFrame em um arquivo csv 
ps.df_solid.to_csv("output.csv")

# Exibir o gráfico
ax = ps.df_solid.plot(x="date time", y=["north", "east", "radial"])
plt.legend(loc='best')
plt.show()
```

Certifique-se de ajustar as coordenadas e o intervalo de tempo conforme necessário para sua aplicação.

## Resultados
O método ```tide_calculation()``` retorna um DataFrame pandas contendo as seguintes colunas:

- ```date time```: Data e hora no formato "dd/mm/aaaa hh:mm:ss".
- ```seconds```: Tempo em segundos desde o início do cálculo.
- ```north```: Deslocamento terrestre na direção norte.
- ```east```: Deslocamento terrestre na direção leste.
- ```radial```: Deslocamento terrestre na direção radial.

Você pode usar esses resultados para análises adicionais ou salvar em um arquivo para referência futura.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests) para melhorar o PySolid.

## Contato
Para mais informações ou dúvidas, entre em contato com o criador Tanus Szabo (tanus.szabo@cnpem.br).

Tenha um ótimo dia!