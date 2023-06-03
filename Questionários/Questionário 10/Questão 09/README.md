Você está interessado no menor preço para alguns equipamentos que estão em falta na sua empresa. Foi feita uma pesquisa de mercado em vários fornecedores diferentes, e você ficou responsável por dizer qual o melhor lugar para comprar cada item.

O resultado dessa pesquisa está em um arquivo do tipo csv (valores separados por vírgula - comma-separated values), formatado da seguinte maneira:

A primeira linha do arquivo é o cabeçalho. O primeiro campo do arquivo possui 2 números inteiros separados por espaço, n e m, que é a quantidade de fornecedores e a quantidade de itens a serem adquiridos, respectivamente. O resto da primeira linha é o nome dos n fornecedores.

As próximas m linhas do arquivo contém o nome do item no primeiro campo, seguido do preço desse item para cada um dos fornecedores.

Por exemplo, o arquivo pode ser:
```
4 3,CadeirasShop,MaterialParaEscritorio.com,Mercado da Esquina,Ármazem de usados
Cadeira,100.95,159.99,235.43,110.50
Mesa,330.00,220.55,440.39,115.34
Monitores,123.88,220.44,158.26,22.49
```

Dado o nome do arquivo, imprima o melhor fornecedor para cada item da lista.
