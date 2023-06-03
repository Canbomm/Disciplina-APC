Padrões existem para (teoricamente) facilitar a vida das pessoas. No entanto para que isso aconteça é necessário que eles sejam adotados por muitas pessoas. Um dos padrões que é muito adotado é o Celsius, para temperatura. Porém alguns poucos países ainda usam Fahrenheit. A conversão de um para o outro é bem simples, mas chata de se fazer de cabeça. Veja abaixo.

```
Fahrenheit = (Celsius * 1.8)/32
Celsius = 0.5555556 * (Fahrenheit - 32)
```

Sua tarefa nessa questão vai ser criar uma função converter que recebe dois argumentos: um número do tipo float, que representa a temperatura, e uma string s, que pode ser 'F' ou 'C', representando o padrão dessa temperatura. Você deve converter a temperatura para o outro padrão.