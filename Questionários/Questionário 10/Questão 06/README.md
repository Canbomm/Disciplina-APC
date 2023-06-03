A aula de Algoritmos ensinou a manipular diversos arquivos e mostrou como funcionam as suas respectivas permissões. Durante a aula, o professor da disciplina comentou que, para qualquer arquivo que um programa tenha permissão para leitura, ele irá conseguir abrir e ler o seu conteúdo. Como curiosidade, ele comentou que se o seu programa está executando em um outro computador ou servidor remoto, a leitura de arquivos iria acontecer da mesma forma, desde que o programa tenha as devidas permissões de leitura. E olha, ISSO É EXATAMENTE O QUE O MOODLE FAZ! Você submete um código para o servidor, ele compila (ou interpreta), executa e exibe os resultados. Como desafio, o professor propôs a seguinte atividade: Será que você consegue ler informações sigilosas do servidor, como por exemplo senhas?

Ao pesquisar a respeito, você descobriu que o moodle executa em um servidor linux, mas infelizmente, por padrão, as senhas de todos os usuários ficam em um arquivo que não há permissão para leitura de usuários comuns. Esse arquivo é o shadow, que fica no seguinte caminho: /etc/shadow

![Exemplo de diretório da shadow](https://i.imgur.com/hXLUafA.png "Exemplo de diretório da shadow")

Porém, em sistemas linux há um arquivo que contém a lista de todos os usuários cadastrados no sistema e esse arquivo é chamado de passwd. Esse arquivo também encontra-se no diretório etc (onde ficam os arquivos de configuração do sistema) e a permissões dele são:

![Exemplo de diretório da passwd](https://i.imgur.com/R8ZE8D3.png "Exemplo de diretório da passwd")

-rw-r--r-- indicam que, o dono do arquivo (root) pode ler e escrever, quem faz parte do grupo root pode somente ler o arquivo, e outros usuários podem somente ler o arquivo. Então, como qualquer usuário tem permissão de leitura desse arquivo, é possível descobrir quais são os usuários cadastrados em um sistema. Além disso, o passwd é um arquivo onde cada linha representa o cadastro de um usuário e cada linha possui o seguinte padrão:

![Exemplo do dono do arquivo](https://i.imgur.com/mGt0A85.png "Exemplo do dono do arquivo")

Essa linha possui sete campos separados por dois pontos (:), e cada uma dessas informações indica o seguinte:

1. O primeiro campo é o nome do usuário, aquele escolhido quando é realizado o seu cadastro no sistema.
2. Aqui vai a informação de senha do usuário. Caso contenha um 'x', indica que a senha encontra-se em outro arquivo (/etc/shadow).
3. Identificador de usuário, o número que o sistema operacional utiliza para propósitos internos.
4. O quarto campo é o campo de identificador do grupo ao qual o usuário incialmente pertence.
5. Campo Gecos. É um comentário que descreve a pessoa ou a conta. Tipicamente, é um conjunto de valores separados por vírgulas, incluindo o nome completo do usuário e detalhes para contato.
6. O sexto campo é o caminho para o diretório home do usuário.
7. O sétimo campo é o programa de shell que será iniciado toda vez que o usuário logar no sistema.

Juntando todas as informações apresentadas pelo professor e aqui, você ficou curioso se seria possível vazar a lista de usuários do servidor onde o Moodle executa os programas dos alunos. Assim o seu desafio é ler o arquivo /etc/passwd, receber um índice e imprimir qual o nome do usuário referente a aquela linha indicada.
