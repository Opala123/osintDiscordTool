# OSINTDiscordTool
Ferramenta Open Source Intelligence para Discord. Com ela você pode **monitorar** quem entrou em uma chamada e quando, sem que seja necessário **permissão** alguma ou **cargo** algum! Imagine-mos a situação em que um investigador descobre que seu alvo usa Discord para se comunicar e cometer seus crimes, existe uma vasta quantidade de servidores, descubra quais chamadas ele frequenta e em quais servidores ele entrou em uma chamada.  Monitore vários ao mesmo tempo e tenha uma análise de resposta automática! 


# Qual propósito da aplicação? 


Monitorar logs de pessoas em chamadas de voz em qualquer servidor mesmo sem permissões de administração. É possível receber logs das pessoas que estiveram em chamadas nos servidores de análise, além de poder filtrar por tempo estimado em que essas pessoas permaneceram nas chamadas.

# Quando isso seria útil para mim? 


Em qualquer situação que seja necessário filtrar informações para descobrir quem frequenta chamadas de voz de servidores. Nós já vimos situações em que criminosos usaram o discord para dissipar suas atividades indesejadas: digamos que você sabe apenas o nome de alguma das contas que ele usa ou quer fazer uma busca triângular para descobrir cada vez mais o modo operante do sujeito investigado. Ou digamos que você conhece uma pessoa e quer saber se ela frequenta chamadas de voz mesmo que ela não aceite seu pedido de amizade. Agora você tem mais uma ferramenta a disposição use-a com responsabilidade!


# Como o código da ferramenta funciona? 

RESUMO:
A ferramenta usa uma tela construida com python + customtkinter, o código para colocar no console é feito em java script e é alterado pelo código python de acordo com o input do usuário. O código Java Script faz dowload filtrando por partes específicas da página html que quando filtradas em python dão as respostas que desejamos em um arquivo txt. Em suma é um webscraping que faz uma busca de informações separando somente as necessárias.    

# ** MANUAL DE COMO USAR A FERRAMENTA: **

![image](https://github.com/user-attachments/assets/7b1c25ea-e211-46fc-ad91-a43d25c2420f)



1 -  Instale as bibliotecas necessárias com pip install ( todas que você não tiver )


2 -  Execute o script.


3 -  No campo "Gerar javascript" coloque o tempo do delay em segundos (esse será o tempo que o código js vai esperar a cada requisição de dowload)


4 -  Clique em gerar e o script será copiado para sua área de transfererência


5 -  Use o discord no navegador e de preferência no google


6 -  Vá na página que você deseja analizar reduzar o zoom da página ao máximo (para carregar todo conteúdo possível html)


7 -  Pressione CONTROL+SHIFT+I para abrir o menu inspecionar


8 -  Na aba console digite:  allow pasting()          (Isso habilitará colar conteúdos)


9 -  Cole o script e veja que de acordo com o tempo configurado um pedaço do html da página é baixado 
     obs: (você pode deixar baixando para monitorar vários servidores ao mesmo tempo)

     
10 - Vá nas permissões da página e permita dowloads automáticos


11 - Em "PASTA ANÁLISE" coloque a pasta onde você tem salvo os arquivos html baixados.


12 - Em "RESULTADO ANÁLISE" coloque a pasta onde será salvo o arquivo txt com os resultados


13 - Agora clique em análise se tudo ocorrer bem receberás uma mensagem de sucesso


14 - Abra o arquivo txt gerado filtre pelo log necessário usando CONTROL+F 
