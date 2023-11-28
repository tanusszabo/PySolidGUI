# Sobre o programa

O PySolidGUI é uma interface gráfica baseada no código Solid, criado por Dennis Milbert [https://geodesyworld.github.io/SOFTS/solid.htm](https://geodesyworld.github.io/SOFTS/solid.htm), que permite realizar o cálculo do deslocamento terrestre, devido ao efeito de maré, em um determinado dia e coordenada terrestre.

A interface foi escrita em Python, utilizando a biblioteca PyQt5, enquanto o backend para os cálculos de deslocamento terrestre foi reproduzido em Fortran90, baseado no código original em Foretran de Dennis Milbert. 

O código original Solid foi alterado apenas em sintaxe para permitir sua utilização em comunicação com Python, através de subrotinas em Fortran90. Caso queira entender seu funcionamento, pode conferir no manual do Solid: [https://geodesyworld.github.io/SOFTS/solid.htm](https://geodesyworld.github.io/SOFTS/solid.htm).

Caso queira utilizar as rotinas em código, o arquivo **pysolid.py** pode ser utilizado como um módulo, que o tutorial/readme eu ainda vou escrever em algum momento.

Caso queira acompanhar atualizações, mesmo que não acredite que terão, pode acompanhar o projeto em: [https://github.com/tanusszabo/PySolidGUI](https://github.com/tanusszabo/PySolidGUI) e, para maiores informações, pode me contactar.

Tenha um ótimo dia!

----
- Versão 1.0
- Última atualização: 23/11/2023
- Criador: Tanus Szabo (tanus.szabo@cnpem.br)
