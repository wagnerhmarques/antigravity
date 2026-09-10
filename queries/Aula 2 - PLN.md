https://www.youtube.com/live/nXzUAubH8kg

> 📅 **Data:** 2026-08-29 | 🔗 **Conexões:** [[Inteligência Artificial (IA)|inteligencia-artificial]], [[Generalist Medical AI (GMAI) e Modelos de Fundação|generalist-medical-ai]], [[Índice de Detectabilidade|detectability-index]], [[Observadores de Modelo (Model Observers)|model-observers]], [[Estudo de Observadores 2AFC|2afc-observer-study]], [[Explainable AI (XAI)|explainable-ai-em-imagem-medica]] | 📺 **Vídeo:** [Um panorama da IA Generativa no Brasil e no Mundo: Presente e Futuro](https://www.youtube.com/watch?v=nXzUAubH8kg) | 👤 **Canal:** MBA IA Big Data

> 📅 **Data:** 2026-08-26 | 🔗 **Conexões:** [[Inteligência Artificial (IA)|inteligencia-artificial]], [[Generalist Medical AI (GMAI) e Modelos de Fundação|generalist-medical-ai]], [[Explainable AI (XAI)|explainable-ai-em-imagem-medica]]

## 1. Síntese Executiva & Tese Principal
A palestra ministrada pelo empresário e pesquisador **Rodrigo Nogueira** (fundador da *Maritaca AI*, Doutor pela NYU e cocriador do *Sabiá* e *Bertbal*) explora o panorama atual e futuro da inteligência artificial generativa (*Large Language Models* - LLMs) no Brasil e no cenário internacional. A tese central do autor sustenta que, embora o desenvolvimento de IA seja dominado por grandes corporações (*Big Techs*) por meio de leis de escala custosas e data centers massivos, existe uma viabilidade crítica e econômica na **especialização de domínio** (*domain-specific fine-tuning*). No entanto, o Brasil enfrenta um gargalo geopolítico e estrutural severo devido à ausência de infraestrutura computacional nacional de grande porte (clusters de milhares de GPUs), tornando urgente um salto estratégico análogo ao da industrialização de base para evitar a dependência tecnológica e a marginalização econômica.

## 2. Momentos-Chave & Roteiro do Vídeo
- **[00:00](https://www.youtube.com/watch?v=nXzUAubH8kg?t=0)** [Música] Abertura da transmissão híbrida no auditório do ICMC-USP.
- **[02:00](https://www.youtube.com/watch?v=nXzUAubH8kg?t=120)** Apresentação do palestrante Rodrigo Nogueira, histórico acadêmico na Unicamp e NYU, e introdução ao foco da *Maritaca AI*.
- **[04:44](https://www.youtube.com/watch?v=nXzUAubH8kg?t=284)** Definição da agenda: capacidades atuais dos LLMs, onde os bilhões de dólares são gastos, especialização de domínio e o futuro próximo.
- **[06:11](https://youtube.com/watch?v=nXzUAubH8kg?t=371)** Demonstração prática das capacidades do modelo *Sabiá 3* e análise sobre se os LLMs são meros bancos de dados sofisticados.
- **[11:01](https://youtube.com/watch?v=nXzUAubH8kg?t=661)** Discussão sobre robustez, generalização e avaliação em benchmarks de nível doutorado (*Google Proof Question Answering*).
- **[15:08](https://youtube.com/watch?v=nXzUAubH8kg?t=908)** Transição para agentes de IA autônomos no controle de computadores e avaliação em tarefas reais de programação no *Upwork*.
- **[20:32](https://youtube.com/watch?v=nXzUAubH8kg?t=1232)** Análise econômica detalhada: as leis de escala (*scaling laws*) e os custos massivos da fase de pré-treino (dados, eletricidade, arquiteturas *Transformer*).
- **[25:41](https://youtube.com/watch?v=nXzUAubH8kg?t=1541)** O gargalo nacional: a ausência de um cluster de 2.000+ GPUs no Brasil e a impossibilidade de treinar modelos de fronteira distribuídos via internet devido à latência de largura de banda.
- **[29:36](https://youtube.com/watch?v=nXzUAubH8kg?t=1776)** A aposta da especialização de domínio: estudo empírico demonstrando a eficiência computacional de modelos especializados (ex: jurídico e saúde).
- **[38:45](https://youtube.com/watch?v=nXzUAubH8kg?t=2325)** O cenário de longo prazo e riscos geopolíticos: a concentração de poder em oligopólios e o uso de modelos *open source* como ferramenta de *soft power*.
- **[47:35](https://youtube.com/watch?v=nXzUAubH8kg?t=2855)** Sessão de perguntas e respostas com o público acadêmico sobre modelos de negócio, computação híbrida e o papel da academia e engenharia de dados.

## 3. Análise Conceitual, Métodos & Modelagem

### A. Leis de Escala (*Scaling Laws*) e Eficiência Computacional
O progresso e o custo computacional dos LLMs obedecem a relações de escala empíricas. O investimento exponencial em poder computacional ($C$) e tokens de dados ($D$) resulta em ganhos log-lineares de desempenho e redução da perplexidade ($P$). Matematicamente, a perda $\mathcal{L}$ em função do número de parâmetros $N$ e dados $D$ expressa-se tipicamente como:

$$
\mathcal{L}(N, D) = \left( \frac{N_c}{N} \right)^{\alpha_N} + \left( \frac{D_c}{D} \right)^{\alpha_D}
$$

Onde $\alpha_N$ e $\alpha_D$ representam os expoentes de escala. O estudo apresentado por Rodrigo Nogueira demonstra que, ao restringir o treinamento a domínios específicos (curva de especialização), a eficiência computacional aumenta drasticamente (fator superior a $4\times$ em modelos de 14 bilhões de parâmetros), mitigando os requisitos de escala total necessários para atingir acurácia equivalente a modelos generalistas de uso corporativo fechado.

### B. Sincronização Distribuída em Clusters de Treinamento
O treinamento de modelos de linguagem baseados na arquitetura *Transformer* exige a atualização iterativa de gradientes via descida de gradiente estocástica em grande escala. Seja $\mathbf{W}$ o vetor de pesos da rede neural distribuído em $K$ aceleradores (GPUs/TPUs). A cada passo de lote, a sincronização global exige a operação de redução (*All-Reduce*):

$$
\mathbf{W}^{(t+1)} = \mathbf{W}^{(t)} - \eta \sum_{k=1}^{K}
abla \mathcal{L}_k(\mathbf{W}^{(t)})
$$

A largura de banda exigida entre nós de processamento invalida o treinamento distribuído via conexões de internet convencional de longa distância, justificando a necessidade física de data centers dedicados com interconexões de alta velocidade (InfiniBand de centenas de gigabits por segundo).

## 4. Conexões com o Acervo & Aplicações Práticas
- **Paralelo com a Física Médica e Tomografia Computadorizada:** Assim como demonstrado por Nogueira na necessidade de especialização de modelos para o contexto brasileiro (direito, saúde pública via SUS), a tomografia computadorizada exige adaptações específicas de algoritmos de reconstrução profunda ([[Deep Learning Image Reconstruction (DLR)|deep-learning-image-reconstruction]]) para lidar com artefatos e ruídos locais que redes generalistas treinadas em datasets estrangeiros não capturam adequadamente.
- **Avaliação Baseada em Tarefas:** A discussão sobre a saturação de benchmarks tradicionais e a discrepância com a percepção humana espelha perfeitamente a transição na física médica descrita no [[AAPM TG-233 - Avaliação de Desempenho em TC|aapm-tg233-ct-performance]], onde métricas puramente físicas falham, exigindo observadores de modelo baseados em tarefas ([[Índice de Detectabilidade|detectability-index]] e [[Estudo de Observadores 2AFC|2afc-observer-study]]).
- **Soberania Tecnológica e Infraestrutura:** A urgência de um cluster computacional nacional de IA discutida por Rodrigo Nogueira dialoga diretamente com os desafios de infraestrutura computacional enfrentados em projetos de pesquisa financiados pela FAPESP ([[Projeto Doutorado Direto FAPESP Wagner 2026|projeto-dd-fapesp-wagner-2026]]), onde o acesso a poder de processamento condiciona a capacidade de inovação e validação de observadores profundos.

---

<details>
<summary>📜 <b>Ver Transcrição Completa com Timestamps</b></summary>

- **[00:00](https://youtu.be/nXzUAubH8kg?t=0)** [Música]

- **[02:00](https://youtu.be/nXzUAubH8kg?t=120)** Eh, bom dia a todos. É uma alegria, né, estar aqui com vocês para mais um uma palestra dentro do nosso ciclo de palestras aqui da disciplina de tendências e mercado em inteligência artificial e big data do nosso MB em a e big data. Hoje, né, como todas as outras

- **[02:18](https://youtu.be/nXzUAubH8kg?t=138)** palestras, é uma palestra muito interessante. Eh, essa palestra vai tá sendo transmitida pelo canal do MCTV, né, do lá no YouTube, mas também pelo canal do MBA em Big Data. E é uma palestra híbrida. Então, tá, além dessa transmissão, a gente tá acompanhando aqui pelo auditório do ICMIC. Nessa palestra nós nosso

- **[02:43](https://youtu.be/nXzUAubH8kg?t=163)** convidado é o empresário Rodrigo Nogueira. O Rodrigo é fundador e diretor executivo da Maritaca AI. É uma startup brasileira focada em especializar modelos de linguagem para certos domínios e idiomas, garantindo que sejam eficientemente implementados e reflita o conhecimento único de diversos setores. Isso, né, Rodrigo? O Rodrigo é doutor em

- **[03:05](https://youtu.be/nXzUAubH8kg?t=185)** ciência de computação pela Universidade de Nova York e fez bacharelado e mestrado na Universidade Estadual de Campinas, a Unicamp, sendo um dos pioneiros no emprego de aprendizado profundo para recuperação de formações. Ele também é um dos cocriadores do Bertbal, que é um modelo de linguagem bem famoso aqui paraa língua portuguesa,

- **[03:25](https://youtu.be/nXzUAubH8kg?t=205)** que já tem mais de 50 milhões de downloads. Então é com muita alegria que eu convido, né, o Rodrigo para subir aqui à tribuna e nos agraciar aí com a sua palestra. Rodrigo, palavra tá com você. Obrigado. Tão me ouvindo bem? Mais ou menos agora tá melhor, né?

- **[03:49](https://youtu.be/nXzUAubH8kg?t=229)** Tá legal. Tá. Obrigado, pessoal, pelo convite. É, é um prazer estar aqui na USP. Eh, vou falar um pouco do o título aqui do do da apresentação. É um panorama de a generativa no Brasil e no mundo. E um dos objetivos aqui eh dessa palestra é que tem tem tendo todo mundo

- **[04:08](https://youtu.be/nXzUAubH8kg?t=248)** hoje tá sendo inundado por informações na na mídia, todo mundo fala sobre IA, né? tem uma ansiedade muito grande hoje que hoje no país e no mundo sobre o que vai acontecer, eh qual o impacto da IA, se de fato vai tirar trabalho, se de fato vai ser tudo isso que estão falando

- **[04:24](https://youtu.be/nXzUAubH8kg?t=264)** ou é só uma hype, estamos fazendo investimento desnecessário, né? E aqui o objetivo dessa palestra é dar uma visão que eu acredito que é um pouco particular em relação ao que eu escuto pelo menos na nas principais eh mídias e dos dos entendidos do assunto. Eh, mostrando alguns alguns potenciais

- **[04:44](https://youtu.be/nXzUAubH8kg?t=284)** problemas e oportunidades aqui, principalmente no Brasil, eh, no que se trata de A, né? Então, aqui tá o a agenda dos quatro tópicos que eu gostaria de falar. Primeiro é mostrar as capacidades as melhores e as atuais, né? Vou tentar fazer aqui o maior embasamento possível usando eh estudos

- **[05:02](https://youtu.be/nXzUAubH8kg?t=302)** científicos que mostram aí essas capacidades e o progresso que elas têm tido nos últimos anos, né? E quando eu digo IA aqui, entenda-se IA generativa, large language models, que que é a nossa área de especialização. E depois a gente vai falar onde a gente sempre fala em milhões, bilhões de reais que essas IAS

- **[05:20](https://youtu.be/nXzUAubH8kg?t=320)** e requerem para o seu desenvolvimento, né? E onde exatamente esse dinheiro é gasto, né? qual parte desse desenvolvimento que a gente, a maior parte dele é é gasto e depois a gente vai ver que isso é um problema ou como contornar esse problema, né? Uma das apostas que a Maritaca faz é essa

- **[05:37](https://youtu.be/nXzUAubH8kg?t=337)** especialização no domínio, né? Em vez da gente criar uma IA de propósito geral, vamos focar em alguns domínios específicos e vamos treinar IAS que que tentam resolver bem aqueles domínios, né? E por fim, vamos eh no último aqui, um possível futuro próximo, né? digo um possível futuro próximo, pois existem

- **[05:53](https://youtu.be/nXzUAubH8kg?t=353)** diversos futuros próximos. Eh, aqui seria a visão que eu tenho de de um futuro que tem o uma probabilidade, OK, de acontecer, mas se acontecer, o risco é alto. Por isso que eu acho que a gente precisa tomar ações eh o quanto antes aqui, principalmente a nível de país,

- **[06:11](https://youtu.be/nXzUAubH8kg?t=371)** né? Eh, então, mostrando um pouquinho do nosso, esse aqui é o Sabia 3, é o nosso melhor modelo eh feito pela Maritaca. a gente vai falar um pouquinho mais do que que como que ele é treinado mais pro final da apresentação, mas é um é um lar de lengua de model que ele foi treinado

- **[06:26](https://youtu.be/nXzUAubH8kg?t=386)** em dados relevantes para o Brasil, né? Entenda-se direito, medicina, finanças, o que que é relevante, isso é ditado pelos nossos classificadores, né? Inclusive, talvez na na sessão de perguntas a gente pode esclarecer um pouquinho mais como que como que esses classificadores atuam, mas enfim, o propósito dele é que seja uma IA útil

- **[06:42](https://youtu.be/nXzUAubH8kg?t=402)** para o Brasil, né? Esse útil é um pouco abstrato, eh, mas é ditado pelo uso dela ao longo do tempo. E aqui mostrando um pouquinho das capacidades a IA, eu fiz uma pergunta para ela. Isso aqui é é uma interface que a gente disponibiliza pro usuário, tá disponível em

- **[06:57](https://youtu.be/nXzUAubH8kg?t=417)** chatarita. E é uma interface parecida com os do chatbot que a gente tá acostumado, né? Então você pode fazer diversas perguntas. Uma delas aqui que eu fiz para pro nosso modelo SB3 é quem tem a maior densidade de potência em wats por eh por metro cúbico, o Sol, o

- **[07:15](https://youtu.be/nXzUAubH8kg?t=435)** humano ou uma GPU a 100. GPU a 100 é um dispositivo usado para treinar essas IA. E eu pedi aqui detalhe, explique seu racional, né, com números. E aqui o modelo vai gerando palavra por palavra, né, mais especificamente token a token, eh, dando a resposta pra gente. Então,

- **[07:30](https://youtu.be/nXzUAubH8kg?t=450)** ele ele sabe de cabeça, vamos dizer, através dos pesos dessa rede neural apenas qual que é o volume do Sol, que já é impressionante. Ele sabe a potência emitida pela eh pelo sol também, também de cabeça, e ele consegue fazer da calcular o a densidade de potência dividindo ali um pelo outro. E ele

- **[07:49](https://youtu.be/nXzUAubH8kg?t=469)** também faz isso de cabeça, né? são números grandes, tudo ele ele chega num num valor aproximado. Ele faz a mesma coisa pro humano, faz a mesma coisa paraa GPU e depois ele consegue rankear os três. Bom, chega à conclusão que a GPU ela tem mais densidade de potência

- **[08:03](https://youtu.be/nXzUAubH8kg?t=483)** do que o humano e por fim o Sol é o é o último colocado aqui, né? O que abrindo um parêntese só também já é muito incrível e que a gente ser humano foi capaz de criar um dispositivo ali que consome e emite mais energia do que o

- **[08:17](https://youtu.be/nXzUAubH8kg?t=497)** próprio humano e também que por sua vez emite mais do que o sol, né? E a gente volta nesse ponto aí do consumo de energia mais paraa frente ali na palestra. Daí olhando essa resposta assim, eh pode parecer que o sistema inteligente, uau, né? Ele fez aqui uma,

- **[08:32](https://youtu.be/nXzUAubH8kg?t=512)** ele, ele trouxe, é quase garantido que, pelo menos em uma busca rasa ali no Google, não existe nenhuma página que tem essas informações, as três em conjuntos, né? Mas obviamente que essa informação tá dispersa em diversos documentos e daí alguma pessoa pode argumentar: "Bom, a densidade de potência aqui e e o e o volume, essa

- **[08:52](https://youtu.be/nXzUAubH8kg?t=532)** rede neural simplesmente é um banco de dados sofisticado, um banco de dados diferente do que a gente tá acostumado. Ela é capaz de fazer essa interpolação, essa união da informação e apresentar pra gente ali de uma maneira concisa que daí e dá aquela impressão de uma inteligência. Uau, essa esse esse

- **[09:08](https://youtu.be/nXzUAubH8kg?t=548)** sistema aqui ele entende do que tá falando, né? Então você pode argumentar que, bom, eles são bons bancos de dados, um pouquinho diferente ou ou sofisticado se você quiser, né? Eh, mas devem a pergunta, eu eu fiz uma uma pergunta na sequência falando: "Agora, escreva essa resposta que você acabou de dar no

- **[09:27](https://youtu.be/nXzUAubH8kg?t=567)** formato de uma poesia e e daí ele vai, né, o o sabiá no cosmo vasto, sol reina com força imensa, luz que tce denidade de poder perde o humano que em se cresce". A GPU, arte de mente humana, em pequeno espaço, força imensa, 1 milhão de vezes mais que sol na tecnologia

- **[09:42](https://youtu.be/nXzUAubH8kg?t=582)** essência. E assim continua essa poesia. Eu não sou, eu, eu conseguiria responder a primeira pergunta. Essa segunda aqui com certeza não ficaria tão boa. Eh, mas esse daí você fala: "Uau, esse esse essa essa IA é realmente inteligente, ela consegue fazer alguma coisa ali que eu não consigo". Mas alguém pode

- **[09:59](https://youtu.be/nXzUAubH8kg?t=599)** argumentar: "Bom, esses são apenas bons reescritores, né?" Durante o treinamento desses modelos, eles viram ali uma tonelada de poesia. E você pode argumentar, bom, baseado poesia, para reescrever essa resposta na forma de poesia, basta um um rearranjo mecanístico das palavras. É uma substituição por eh eh GPU, arte de

- **[10:18](https://youtu.be/nXzUAubH8kg?t=618)** mente humana, fazer umas proximidades, enfim, é algo coisa, uma coisa mais mecânica que daí na superfície pode parecer inteligente pra gente no final. Então, bom, eh, você pode simplesmente argumentar, esses essas vias não estão fazendo nada muito de especial, elas só são bons bancos de dados, bons resescritores e que no final do dia elas

- **[10:37](https://youtu.be/nXzUAubH8kg?t=637)** enganam a gente ali mostrando que que eh colocam respostas num formato que a gente não tá acostumado a ver, pelo menos com as tecnologias anteriores, né? E eu acho que o cerne aqui, a pergunta mais principal que aprendizado de máquina, né, tenta responder eh ou desenvolver esses temas, é essas IAS,

- **[11:01](https://youtu.be/nXzUAubH8kg?t=661)** né, esses LLMs, eles conseguem resolver tarefas que não tão no seu dado de treinamento? Ou em outras palavras, elas conseguem, quando a gente escuta lá, generalizar, raciocinar, extrapolar. É isso que a gente a gente quer que essas IAS mostrem pra gente uma robustez que em outros que elas não vão quebrar

- **[11:20](https://youtu.be/nXzUAubH8kg?t=680)** quando ã os dados que chegam para ela ali em momento de inferência, em momento de teste sejam muito diferentes do que elas viram no eh no treino, né? Esse é o principal problema eh estudado em aprendizado de máquina. E a grande pergunta aqui, essas esses LLMs, dado que eles treinam praticamente tudo, eles

- **[11:36](https://youtu.be/nXzUAubH8kg?t=696)** são robustos à novas distribuições? Essa é uma pergunta ainda em aberto, mas que muita gente da comunidade o tempo todo eh criam métodos e datasets de avaliação que tentam mostrar essas limitações, essas IAS. E um em particular, um desses trabalhos em particular, eh, que que é hoje usado

- **[11:56](https://youtu.be/nXzUAubH8kg?t=716)** por por praticamente todo mundo que desenvolve essas de fronteira, né, os GPT4,5, O3, eh, Cloridropic, eles avaliam nesse benchmark é chamado de Google Proof Question Answering. E aqui é um benchmark construído com com perguntas de nível doutorado. Eh, são mais de 400 perguntas de múltipla escolha que foram escritas por

- **[12:17](https://youtu.be/nXzUAubH8kg?t=737)** especialistas em biologia, física e química. E uma dos das limitações quando eles foram construir esse benchmark é que humanos não especialistas no assunto com acesso à internet 30 minutos que eles poderiam navegar na internet e muito bem remunerados. Acho que eles estavam pagando cerca de $ não lembro de cabeça

- **[12:36](https://youtu.be/nXzUAubH8kg?t=756)** agora, mas era um bom valor em dólares por hora para resolver essas questões. Esses humanos não especialistas não conseguem acertar a resposta. Em outras palavras, é o Google Proof é a prova de Google. Você não consegue encontrar facilmente essas respostas com com o mecanismo de busca, né? E esses não especialistas aqui são

- **[12:52](https://youtu.be/nXzUAubH8kg?t=772)** pessoas com doutorado num assunto diferente do que tá sendo feita a pergunta, né? Então você pergunta de biologia, a pessoa tem um doutorado em física, então são pessoas ali que estão tão acostumadas a lidar com problemas difíceis, só que não daquele mesmo assunto. E aqui tá um exemplo de

- **[13:06](https://youtu.be/nXzUAubH8kg?t=786)** pergunta de física quântica desse desse benchmark. É um benchmark de múltipla escolha, né? Não consigo nem ler aqui para vocês a pergunta de eh tamanho. É, é o eh pelo menos a na forma parece que ela é complicada. E quando você olha aqui pros resultados nesse benchmark, desempenho aleatório 25%, né? São quatro

- **[13:25](https://youtu.be/nXzUAubH8kg?t=805)** múltipla escolha. E o humano não especialista com com acesso à internet ele consegue em torno de 30 a 35%. Então primeira etapa ali eles tá tá foi atingida, né? Ou seja, num o eles tiveram sucesso em que que humanos não especialistas não conseguissem uma pontuação alta. Daí um doutor, uma doutora no

- **[13:46](https://youtu.be/nXzUAubH8kg?t=826)** assunto com acesso à internet, ele consegue, eles, essas pessoas conseguem de 70 a 80% nesse benchmark. E os melhores modelos que a gente tem hoje é o Peni One e o e o Deepsic. É o modelo de raciocínio consegue também em torno de 70 80%. Então eles já tão ali, esses

- **[14:02](https://youtu.be/nXzUAubH8kg?t=842)** modelos, pelo menos esse benchmark de múltipla escolha, tão ali eh, próximo de um de uma pessoa com nível doutorado, né? Mas aqui a crítica principal é: "Putz, esse é esse é um benchmark de múltipla escolha, né? Será que esses modelos são de fato capazes de de gerar uma resposta ou até às vezes de criar

- **[14:18](https://youtu.be/nXzUAubH8kg?t=858)** essas alternativas?" E uma das razões de deles terem feito um ben marketing de múltipla escolha, que é muito difícil você avaliar hoje esses modelos quando eles geram muitos textos, né? Então é melhor escolher entre quatro alternativas, mas sempre fica aquela dúvida, né? Eles aqui tem, a gente tava

- **[14:33](https://youtu.be/nXzUAubH8kg?t=873)** conversando antes de vir aqui paraa palestra, tem esse descasamento, né, do que que os benchmarks hoje mostram pra gente do que a percepção humana com relação ao desempenho, essas esses modelos, né? Muitas pessoas ficam felizes com o uso deles, mas outros criticam, falam: "Ele ele errou coisas fundamentais aqui, né?

- **[14:48](https://youtu.be/nXzUAubH8kg?t=888)** Então, eh, o que que a gente pode fazer aqui para medir que seja algo além desses benchmarks de múltipla escolha, né, que hoje é praticamente um padrão, um padrão da indústria quando tá desenvolvendo esses essas IAS, né? Eh, a pergunta aqui, acho que principal é: "Bom, tudo bem, legal que ele que tem

- **[15:08](https://youtu.be/nXzUAubH8kg?t=908)** conhecimento nível doutor, eh, será que agora elas conseguem resolver tarefas do mundo real, né? E uma linha que as pessoas, que as empresas têm investido bastante e todo mundo tá discutindo são essas essas IA agentes, né, que tem o a capacidade hoje de assumir o controle do seu computador. Então você pensa aqui

- **[15:25](https://youtu.be/nXzUAubH8kg?t=925)** numa eh hoje você tem o humano interagindo no computador, ele tem visão e audição e ele emite comandos de voz e de controle al do mouse e do teclado para interagir com esse computador, né? Então você pensa que a pessoa tá participando de uma de uma reunião do

- **[15:40](https://youtu.be/nXzUAubH8kg?t=940)** Meet ou ou trabalhando em qualquer software ali do dia a dia. E hoje a gente tem IAS que são capazes eh de ter como entrada visão e audição e também são IAS capazes de de emitir esses controles pro teclado e pro mouse e também falar, né? Então em teoria nada

- **[15:56](https://youtu.be/nXzUAubH8kg?t=956)** impede que essas IA elas substituam ali o operador que tá na frente do computador. E essa é uma das apostas dessas grandes empresas, né, das dessas que estão na fronteira. Então você pode imaginar aqui você passando uma informação para Iá, uma tarefa de alto nível e definida por um humano, por

- **[16:12](https://youtu.be/nXzUAubH8kg?t=972)** exemplo, faça a próxima versão do produto XPTO com base nos feedbacks dos clientes atuais. Interaja com o time de vendas, engenharia, fornecedores para saber as limitações e oportunidades. Então você pode passar isso para IA e deixa ela interagindo ali para um para um um longo horizonte ali, tipo alguns

- **[16:29](https://youtu.be/nXzUAubH8kg?t=989)** meses com todas essas esses agentes aqui, né? Time de engenharia, fornecedores, etc. até de fazer o design do novo produto. Em teoria, isso é possível, mas eh será que de fato ela já elas já têm essas capacidades? E aqui a Opena, ela lançou recentemente, acho que pouco mais de um

- **[16:47](https://youtu.be/nXzUAubH8kg?t=1007)** mês, um artigo mostrando onde eles avaliaram eh as melhores IAs hoje em trabalhos freelancer reais de programação que são postados nesses sites Upwork, né? Então, lá no Upwork você tem alguma tarefa, você tem um app, você gostaria de colocar, por exemplo, um tocador de vídeo no seu app e você

- **[17:06](https://youtu.be/nXzUAubH8kg?t=1026)** não tá conseguindo, você vai lá no work, submete essa esse trabalho e as pessoas vão tentam resolver. Conforme vão, elas vão tendo mais dificuldade de resolver, automaticamente o valor dessa tarefa vai crescendo e então vão de tarefas desde simples, correção de bugs, 50 até tarefas mais complexas, que nem fazer

- **[17:23](https://youtu.be/nXzUAubH8kg?t=1043)** essas funcionalidades inteiras, né, que vão 32.000. E eles puseram a prova eh as melhores IAS, o O1, o Cloud 3,5, eh para resolver de um total de 1 milhão de dólares em tarefas do do site. Eh, e esses modelos, usando essas capacidades de agente, que que que que que é isso, né? De maneira

- **[17:42](https://youtu.be/nXzUAubH8kg?t=1062)** bem simples, é simplesmente interagindo com ferramentas. Você abre o terminal ali, emite comandos, recebe a resposta e tenta e tem acesso ao repositório e e decide daí quando que o modelo mesmo decide quando. Bom, a tarefa foi foi resolvida. Vou parar por aqui, né? E essas melhores elas conseguem hoje

- **[18:00](https://youtu.be/nXzUAubH8kg?t=1080)** ganhar um total de 400.000 desse 1 milhão que elas tentaram. E você pode imaginar que, bom, hoje essas grandes essas grandes empresas, elas estão deixando a gente usar essas IAS para ajudar a gente a resolver esse esse esses problemas, mas nada impede que no futuro, quando elas tiverem ali nos nos

- **[18:19](https://youtu.be/nXzUAubH8kg?t=1099)** 1 milhão, quase 100% das tarefas, elas simplesmente falar: "Quer saber? Vou aumentar o preço aqui. Não vai ser mais dólar por 1 milhão de tokens, vai ser $ e eu vou agora todo o lucro vai ser meu, vocês não podem mais submeter pro Upwork, né? Eh, essa essa é uma coisa

- **[18:34](https://youtu.be/nXzUAubH8kg?t=1114)** que eu que a gente vai voltar mais aqui nessa palestra para discutir o impacto, o poder que hoje essas empresas estão tendo, né? E mas uma crítica aqui, a gente pode falar, bom, tá tá em 400.000, 1000, mas eu escutei falar lá na mídia que eh 40% só desse desse dinheiro tá

- **[18:50](https://youtu.be/nXzUAubH8kg?t=1130)** sendo destinado ali, tá sendo tirado ali do site do OPWK, mas eu já escutei que acabaram-se os dados, né? Não tem mais dados humanos para treinar essas IAS, a gente tá tendo que gerar dados sintéticos. Tem uma série de incertezas ali. Será que de fato a gente vai já não

- **[19:04](https://youtu.be/nXzUAubH8kg?t=1144)** já não saturou? Já vamos esquecer um pouco dessa hype, vamos parar por aí. E aqui aqui a minha visão é que parece que não, tudo bem, é um pouco meio eh, como se diz? eh uma pessoa que tem uma empresa de A falando que não saturou ainda, né? Pode

- **[19:18](https://youtu.be/nXzUAubH8kg?t=1158)** continuar investindo, né? Eh, mas o que a gente vê no progresso nos últimos anos, eh, é que esse progresso tem se tornado constante, né? Então aqui eu mostro isso, voltando naquele benchmark do Google Proof Qway, eh o GPT 3,5 quando foi lançado há 2 anos e meio atrás de 2022, ele mal atingiu o nível

- **[19:37](https://youtu.be/nXzUAubH8kg?t=1177)** de um humano não especialista. E aquilo já foi suficiente ali para fazer um um alarde no mundo, né? Depois GPT4 conseguiu 41%, o O1 consegue 70% e hoje o melhor modelo da Google, o Gemini 2,5 consegue 84%, que é o mesmo nível desses especialistas, né? Então o que a gente

- **[19:54](https://youtu.be/nXzUAubH8kg?t=1194)** tem observado nesses últimos 3 anos, essa essa essa curva contínua aqui, né? Tem tem ainda essa incerteza de que se eh a gente vai conseguir romper essa barreira ainda, né? Uma vez agora que os dados de fato esgotaram ou ou de fato a gente estagnou, né? Mas assim, o os

- **[20:12](https://youtu.be/nXzUAubH8kg?t=1212)** últimos anos não indicam isso, né? Essa é o é a principal mensagem. Agora, desse esse todo esse investimento que a gente fala desses desses milhões bilhões de dólares gastados para desenvolver IA, né? Onde onde que ele é gasto, né? essa essa segunda parte aqui da da palestra, o

- **[20:32](https://youtu.be/nXzUAubH8kg?t=1232)** existem existe uma uma um conceito bastante que tá se popularizando cada vez mais, que são essas leis de escala das IAS. E basicamente ela aqui é uma versão bem caricata da coisa, num prática ela é um pouquinho mais complicada esses eixos X e Y, mas aqui eu quis retratar uma versão simplista

- **[20:51](https://youtu.be/nXzUAubH8kg?t=1251)** para para facilitar o entendimento, né? Então, o que que basicamente diz as leis de escala? Que quando você faz um investimento, eh, você aumenta o seu investimento exponencialmente em computação, em dados de treinamento para treinar essas IAS, você tem um ganho linear em tarefas que você consegue resolver, né? Então, por exemplo, se

- **[21:10](https://youtu.be/nXzUAubH8kg?t=1270)** você decide investir R$ 10 milhões deais para treinar uma IA, você consegue resolver, por exemplo, 20% de algumas tarefas que você tem interesse. Se você aumenta em 10 vezes esse investimento, agora você consegue 40%, se 1 bilhão, 60% e assim por diante. Então, basicamente eh o que tá dizendo esse

- **[21:27](https://youtu.be/nXzUAubH8kg?t=1287)** gráfico aqui é uma versão uma versão bastante não não eh uma versão bastante pessimista da coisa, né? Você precisa desse investimento exponencial aqui para ter esse ganho linear. Mas uma coisa que a gente nota o tempo todo é que dá para empurrar essa curva para cima e mais pra

- **[21:43](https://youtu.be/nXzUAubH8kg?t=1303)** esquerda, né, com com melhorias em hardware, então GPUs, TPUs estão sendo lançadas, produzidas a todo momento, que daí fazem que o seu treino fique mais eficiente. Eh, melhorias da curadoria de dados. Toda hora a gente tá descobrindo novas formas de como coletar dados de treinamento e gerar dados sintéticos que

- **[21:59](https://youtu.be/nXzUAubH8kg?t=1319)** deixa o treino mais menos custoso. Ou seja, você treina com menos dados, mais dados e mais qualidade, portanto, você gasta menos. e algoritmos também, né? Se você olha o paper do deep seek, é um é um é um belíssimo trabalho de engenharia lá, né? Eles detalham bastante como é que foi

- **[22:13](https://youtu.be/nXzUAubH8kg?t=1333)** feito o treinamento, como que eles conseguiram economizar. Então, de na prática, o que eles estão fazendo é puxando. E essa curva tá continuamente sendo puxada, né? Não é só o deepic, que é um um breakthrough, mas dentro das empresas, a comunidade científica todo o tempo tá publicando artigos que aos

- **[22:27](https://youtu.be/nXzUAubH8kg?t=1347)** pouquinhos vai puxando essa curva. E daí o efeito que isso tem eh psicologicamente no investimento é de uma realimentação positiva. Então, por exemplo, se você hoje você fala pro seu investidor, me dá R$ 100 milhões aqui deais para eu fazer um modelo, eu consigo resolver 40% das tarefas. Agora

- **[22:43](https://youtu.be/nXzUAubH8kg?t=1363)** você descobriu algumas técnicas novas que você conseguiu aumentar para 50% o nível de tarefas, eh, a quantidade de tarefas serem resolvidas com esses mesmos 100 milhões. Você agora você chega e fala pro pro investidor, lembra aqueles 100 milhões que eu falei? consegui resolver agora 10% mais. Você não quer me dar 1 bilhão, então esse

- **[23:00](https://youtu.be/nXzUAubH8kg?t=1380)** essa é um é um ciclo ali que a gente tem notado hoje no eh eh no mundo, né, de investimento, essa essa corrida ali pelo ouro para gastar mais dinheiro para treinar essas IA. E eh mas esses esses milhões bilhões que a gente tá falando, onde exatamente ele é gasto, né? O o treino dessas IAS,

- **[23:20](https://youtu.be/nXzUAubH8kg?t=1400)** ele ele consiste de múltiplos estágios. Então, tem a fase de pré-treino, tem a fase aqui do, isso aqui é uma, é um exemplo que eu tirei do artigo do DEPS, que tem a fase de deixar com que o modelo entenda mais o contexto, né, contextos maiores que chegam, por

- **[23:33](https://youtu.be/nXzUAubH8kg?t=1413)** exemplo, a 1000 páginas de documento. E daí tem a parte do pós-treino, que hoje também tem sido uma grande uma área que teve bastante progresso, mas todas essas áreas em em em custo de treinamento, o pré-treino é onde a gente gasta mais dinheiro. 90% desse dinheiro vai nessa

- **[23:49](https://youtu.be/nXzUAubH8kg?t=1429)** fase de pré-treino, né? E o que que o que que é exatamente esse pré-treino aqui? Eu tento detalhar de uma forma também meio caricata os ingredientes para se treinar um modelo como depsic V3, que é esses modelos de fronteira ali que tem desempenho próximo ao GPT4. Então a gente coleta muitos dados,

- **[24:07](https://youtu.be/nXzUAubH8kg?t=1447)** então textos ali da Wikipedia, livros, notícias, código. Eh, a gente faz autossupervisão. O que que é autossupervisão aqui? É simplesmente d palavras anteriores, tentar prever a próxima. E é isso que é é a função objetiva do modelo. E esses modelos são treinados em 10 trilhões de palavras. Eh, isso aqui é equivalente a um humano

- **[24:25](https://youtu.be/nXzUAubH8kg?t=1465)** lendo sem parar por 50.000 anos. Então, uma quantidade muito maior do que qualquer um de nós aqui nessa sala vai ler. E eles precisam de muita computação. Então você eh tem um cluster com 2.000 GPUs que roda ali, faz o treinamento por dois meses. A eletricidade consumida é equivalente a

- **[24:43](https://youtu.be/nXzUAubH8kg?t=1483)** 400 brasileiros em um ano. É bastante coisa, mas se você vê talvez o modelo final ali não é tão assim absurdo. E daí tem a arquitetura do Transformer. Hoje a arquitetura tem tido eh grandes grandes avanços e principalmente do o Deep que já tinha usado e arquiteturas que já

- **[25:03](https://youtu.be/nXzUAubH8kg?t=1503)** eram conhecidas no passado, ele conseguiu fazer algumas algumas melhorias no nela que deixam o treino ainda mais eficiente. Mas desses três ingredientes aqui, o a coleta de dados, por exemplo, é uma que a Maritaca a gente especializa em fazer, né? Coleta dados, faz dados sintéticos, eh compra dados. Isso é uma coisa assim que tanto

- **[25:23](https://youtu.be/nXzUAubH8kg?t=1523)** a academia quanto a indústria eu acho que não é não é tanto um gargalo. A gente consegue fazer isso bem e estamos estamos tendo progresso. Arquitetura de modelos, o tempo todo você vai nessas grandes conferências como Neurips, tem 1000 artigos sendo publicados cada ano, eh fazendo, eh, propostas de melhoria

- **[25:41](https://youtu.be/nXzUAubH8kg?t=1541)** para deixar esses treinos mais eficientes e outros algoritmos de treinamento, né? Eh, agora o gargalo aqui do ponto de vista país tá nesse cluster. Esse cluster com 2000 GPUs ele custa pelo menos 500 milhões deais. A gente não tem nenhum hoje no país. Então, por exemplo, os nossos treinos a gente faz todo lá

- **[25:58](https://youtu.be/nXzUAubH8kg?t=1558)** fora, em especial nos Estados Unidos. E isso, a gente vai voltar a discutir esse assunto, para mim é um dos principais fatores hoje que impede o progresso de A no país, pelo menos o progresso de IA generativa, né? Vamos discutir um pouquinho mais o que o que que tem de

- **[26:12](https://youtu.be/nXzUAubH8kg?t=1572)** especial esse cluster, né? Não dá para usar qualquer cluster. Eu tenho aqui um cluster da USP, tem da Unicamp, tem FBA. Vamos unir esses todos esses clusters aqui e formar um um mega treinamento com essa computação compartilhada. Esse seria uma excelente solução. Eh, se não fosse o problema hoje do treinamento

- **[26:28](https://youtu.be/nXzUAubH8kg?t=1588)** dessas IA. Hoje elas precisam de milhares de TPUs ou GPUs, eh, que são que é esse hardware especializado para treino de A. Se você não tiver milhares, se tiver só uma centena, esse treino aqui vai demorar em vez de de alguns meses, vai demorar alguns anos. Então, impraticável. Eh, mas voltando naquela

- **[26:47](https://youtu.be/nXzUAubH8kg?t=1607)** ideia, né? Bom, mas eu eu consigo juntar 2.000 GPUs aqui no Brasil todo e interconectar com elas via internet. O problema hoje que o da forma que é feito o treino desses modelos em larga escala é que essas GPUs, essas TPUs, elas precisam estar altamente interconectadas para uma largura de de banda alta,

- **[27:04](https://youtu.be/nXzUAubH8kg?t=1624)** porque todo tempo no treino, a cada a cada 500 exemplos que você vê, por exemplo, você precisa sincronizar os pesos da rede neural que estão distribuídos. Se você faz isso via internet, demora uma eternidade, você fica mais tempo ali perdendo, sincronizando esses pesos do que eh propriamente usando hardware

- **[27:19](https://youtu.be/nXzUAubH8kg?t=1639)** especializado e de novamente o treino vai demorar os anos que que a gente não quer, né? Então, o hardware hoje é um é um hardware bastante específico e eles tendem todos a concentrar no único data center de propósito especializado e a gente gasta ali uma boa fração eh desse

- **[27:35](https://youtu.be/nXzUAubH8kg?t=1655)** hardware com o equipamento de rede, não com as GPUs propriamente. Eh, isso tem feito com que daí eh isso tem movido o mundo, né? governos tem dedicado orçamento que poderiam estar sendo construídos ali para hospitais e saneamento básico, t sido usados para construir data centers para treinar essas IAS, né? Então a Alemanha planeja

- **[27:56](https://youtu.be/nXzUAubH8kg?t=1676)** investir R9 bilhões deais para construção de data centers. Brasil tem o PBIA, que acho que tem R bilhões de reais. Nem tudo vai ser uma par, acho que não lembro agora de cabeça, mas uma boa parte vai ser dedicada pra construção de um de um grande cluster. Eh, Antropic tá falando que treinos de

- **[28:14](https://youtu.be/nXzUAubH8kg?t=1694)** IAS vão custar cerca de 10 bilhões de dólares nos próximos anos. A a a Open AI hoje ela tem planos de construir, como você não consegue enxergar com tanta energia assim nesses data centers, hoje ela tem planos de construir data centers que estão dispersos em múltiplas localidades, que daí ela pega energia de

- **[28:32](https://youtu.be/nXzUAubH8kg?t=1712)** diferentes fontes. E a gente tá falando de uma energia de equivalente a 1 GW. 1 GW é 10% da energia produzida em Taipu. Então é um mundo que tá se movendo ali simplesmente para treinar essas IAS. Eh, e as pessoas estão apostando grandes somas nessa nessa nessa nessa

- **[28:49](https://youtu.be/nXzUAubH8kg?t=1729)** estratégia, né? Eh, como que a gente resolve esse problema, né? Hoje, que nem a gente já chegou a discutir, a gente consegue fazer melhorias nas arquiteturas e treinamentos. Pode ser que alguma algum laboratório ali, eh, pense em um jeito de fazer, por exemplo, esse treino assíncrono distribuído, por

- **[29:07](https://youtu.be/nXzUAubH8kg?t=1747)** exemplo, já mitigaria muito hoje o gasto computacional que a gente tem. Eh, dados de treinamento de maior qualidade. Isí o tempo todo a gente tá investindo em como a gente, eu digo como comunidade, como como fazer o maior proveito de cada token, de cada palavra que é alimentada

- **[29:21](https://youtu.be/nXzUAubH8kg?t=1761)** para esse modelo. E aqui chega daí na especialização do domínio, que é a aposta da maritaca, né? A gente acredita que essa é uma das uma das estratégias que a gente tem para não precisar gastar tanto dinheiro assim no treino dessas IAS. E vamos discutir um pouquinho mais

- **[29:36](https://youtu.be/nXzUAubH8kg?t=1776)** eh de como que isso é feito, né? Então, a inspiração aqui para especializar no domínio é que as profissões elas naturalmente tendem a especialização, né? Ou citando aqui um exemplo no direito, a gente tem o direito trabalhista, tem direito internacional, direito empresarial. Os advogados se especializam nessas áreas e

- **[29:53](https://youtu.be/nXzUAubH8kg?t=1793)** eu acho que mais importante hoje a gente não conhece nenhum eh eh chefe do Supremo, que também é um excelente neurocirurgião, né? As pessoas têm que dedicar energia ali para resolver bem um determinado problema, eh, porque porque o tempo é finito, né? e vai ter um concorrente ali que vai est fazendo o

- **[30:09](https://youtu.be/nXzUAubH8kg?t=1809)** mesmo, só que ele vai estar 100% do tempo dedicando naquela área e especialista. Então, a gente tira inspiração aqui das profissões e a gente tem essa hipótese da especialização. Eh, então, voltando naquelas naquelas le curva da leis de escala, essa curva laranja aqui, imagina que esse é um modelo treinado em dados

- **[30:29](https://youtu.be/nXzUAubH8kg?t=1829)** gerais ou ou generalistas, né? São dados ali coletados da web que não tem nenhuma profissão em mente ali. Ele, esse modelo, tem o propósito de ser um modelo geral que vai resolver tantas tarefas jurídicas, médicas, financeiras, etc. A nossa hipótese aqui que é possível a gente eh quando a gente faz um

- **[30:46](https://youtu.be/nXzUAubH8kg?t=1846)** treinamento em dados do domínio mostrado nessa curva verde, a gente vai conseguir atingir o mesmo nível de de tarefas sendo resolvidas no domínio que a gente se importa, gastando menos eh computação, menos dados, menos eh modelos de tamanho menor. Então esse trein essa hipótese que dá para dá para

- **[31:04](https://youtu.be/nXzUAubH8kg?t=1864)** inclinar um pouco mais essa reta. E uma das perguntas é por que que essa reta aqui é inclinada, né? não é não é deslocada simplesmente que nem no exemplo anterior. Isso aqui a gente eh empiricamente através de um estudo, a gente descobriu que de fato ela ela ela

- **[31:20](https://youtu.be/nXzUAubH8kg?t=1880)** tem essa inclinação. Aqui eu queria eh parar um tempinho explicando um pouco esse artigo que eu acho que é muito interessante que mostra eh é um é um exemplo claro que a gente partiu de uma hipótese e depois no final dos estudos a gente chegou numa outra conclusão, né?

- **[31:34](https://youtu.be/nXzUAubH8kg?t=1894)** Então, o Roseval aqui, o Ramon, que são o Roseval foi o líder aqui desse desse estudo. Eh, a gente o que que a gente fez aqui? Então, no eixo, nesse primeiro gráfico, no eixo X, a gente tem a computação gasta no treino desses modelos em flops, né, em front point

- **[31:52](https://youtu.be/nXzUAubH8kg?t=1912)** operations. E entenda-se isso como dados que foram vistos durante o treinamento, eh, o tempo que a sua máquina ficou ligada, né? Essa é uma proxy para pra computação. E daí no eixo Y a gente tem a perplexidade. Perplexidade entenda-se como o erro desse modelo em um benchmark que a gente se importa. No caso aqui,

- **[32:11](https://youtu.be/nXzUAubH8kg?t=1931)** por exemplo, provas da OAB, a gente queria treinar um modelo especializado no jurídico, eh, no jurídico brasileiro. Então, a gente treinou dois modelos. O primeiro é o da curva eh da laranja, o mais cima ali. Eh, cada pontinho desse é um modelo de tamanho diferente, é um LLM. E a gente treinou ele em dados

- **[32:30](https://youtu.be/nXzUAubH8kg?t=1950)** gerais, ou seja, pegamos os dados da web, tivemos alguns classificadores que colocam dados de qualidade, mas a gente não fez nenhuma curadoria específica pro domínio jurídico. Tem dado de tudo que você imaginar lá. E daí na curva e e daí se a gente mediu o erro, dá para ver conforme

- **[32:46](https://youtu.be/nXzUAubH8kg?t=1966)** aumenta o tamanho do modelo, aumenta o gasto em computação, vai diminuindo o erro desse modelo generalista. E a curva em azul daí é o modelo treinado em domínio específico, treinado no jurídico. Então a gente tem classificadores que tentam detectar se aquele documento vai ser útil ou não pro

- **[33:01](https://youtu.be/nXzUAubH8kg?t=1981)** aprendizado jurídico. E a gente treinou esses modelos somente nesses dados jurídicos, né? E daí a curva aqui, como a gente já esperava, esse modelo especializado, eh, ele ele ele aprende mais do que generalista, mas a nossa hipótese inicial é que essas duas curvas elas iam convergir conforme a gente

- **[33:19](https://youtu.be/nXzUAubH8kg?t=1999)** aumentasse a computação. Em outras palavras, como como a gente tem um modelo muito muito grande, tanto faz você tá dando dado para ele médico, jurídico, tudo assim, meio que para bom entendedor, meio a palavra basta, né? Você faz um pequeno treino ali, ele já consegue resolver bem essas tarefas. Mas

- **[33:32](https://youtu.be/nXzUAubH8kg?t=2012)** para nossa surpresa, essas curvas elas estão divergente, né? O que mostra que modelos especialistas eles na verdade têm um, eles são computacionalmente mais eficientes do que os modelos generalistas. Se você, se tudo que você quer é resolver bem uma tarefa em um único domínio. Isso, esse gráfico aqui,

- **[33:49](https://youtu.be/nXzUAubH8kg?t=2029)** ele é meio que eh a mensagem desse gráfico da esquerda, ele pode ele ele ele é traduzido aqui pro gráfico da direita, que mostra a eficiência computacional ao treinar esses modelos, né? Então, eh, se a gente pegar esse último ponto ali do gráfico da direita, é um modelo de 14 bilhões de parâmetros.

- **[34:08](https://youtu.be/nXzUAubH8kg?t=2048)** E no eixo Y é uma métrica que a gente mede com quanto deficiência computacional que a gente teve no treinamento desse modelo especialista com relação ao generalista. Então, esse número, o modelo de 14B, ele consegue quatro e alguma coisa nessa métrica. Quer dizer que ao treinar o modelo

- **[34:26](https://youtu.be/nXzUAubH8kg?t=2066)** especialista de 14 bilhões de parâmetros, ele gastou quatro e alguma coisa vezes menos computação para chegar no mesmo desempenho de um modelo de mesmo tamanho generalista, né? Então, quanto o fato dessa reta tá tá inclinada para cima, quer dizer que quanto mais a gente aumenta o tamanho do modelo, mais

- **[34:44](https://youtu.be/nXzUAubH8kg?t=2084)** eficiente, menos computação proporcionalmente a gente gasta para ter um bom resultado no no nos benchmarks, nas tarefas que a gente quer. E isso não é só eh não é só apenas um estudo que foi conduzido em uma pequena escala, a gente também aplica isso nos produtos, né? É, é um dos

- **[35:02](https://youtu.be/nXzUAubH8kg?t=2102)** orgulhos que eu tenho da empresa é que a gente a gente é bem inde nesse aspecto de vamos fazer estudos, vamos desenvolver produto, mas tem que ter um embasamento, eh, tem que ter tem que ter indicações, pelo menos no no laboratório, de que o que a gente tá

- **[35:15](https://youtu.be/nXzUAubH8kg?t=2115)** fazendo aqui, desses desses dessa boa quantidade de dinheiro que a gente tá gastando, que vai dar certo ali, né? E aqui é o modelo que a gente aqui tá uma curva de treinamento do do nosso melhor modelo Sabia A3. a gente parte de um modelo open source que que ele é mais ou

- **[35:29](https://youtu.be/nXzUAubH8kg?t=2129)** menos aqui no eixo Y a gente tá medindo o desempenho desse modelo em 64 exames brasileiros, né? Então entende, Enem, ENAD, USP, vestibular da USP, da Unicamp, OAB, Revalida, o que você imaginar, né? Eh, esse modelo open source que a gente parte o treino, ele é um pouquinho melhor que o GPT3,5 nesses

- **[35:49](https://youtu.be/nXzUAubH8kg?t=2149)** exames. Daí, ao longo desse treino, a gente treina esse modelo, como já falei, em dados relevantes pro Brasil. E aqui no eixo X é a computação gasta, né? Mas computação entenda-se também como eh documentos que ele viu durante o treinamento. Eh, o esse modelo vai melhorando até chegar no nível do GPT4,

- **[36:05](https://youtu.be/nXzUAubH8kg?t=2165)** que era o nosso target, né, de de treinamento. E bom, muito feliz com essa curva, né? Tá, de fato, a nossa hipótese tá tá se mostrando verdadeira. Eh, o problema só de novo volta nesse nesse eixo X aqui que é escala logarítmica, né? Ou seja, de novo, a gente volta

- **[36:22](https://youtu.be/nXzUAubH8kg?t=2182)** nesse problema de ter eh necessidades exponenciais de dados em computação para ter um ganho linear nas tarefas que a gente se importa. E uma das coisas, uma das apostas nossas é que mais especialização ainda eh é uma maneira de contornar esse requisito exponencial ali de computação. Em outras palavras, se

- **[36:40](https://youtu.be/nXzUAubH8kg?t=2200)** você hoje treinou um modelo eh especializado no Brasil, vamos treinar um modelo especializado no Brasil jurídico, depois vamos treinar o modelo especializado no Brasil jurídico trabalhista e assim por diante. O que quer, que se isso for verdade, quer dizer que o futuro não vai ser apenas um único modelo eh generalista de grande

- **[36:56](https://youtu.be/nXzUAubH8kg?t=2216)** porte que vai servir todos nós, né? Vai ser um vai ser uma diversidade de modelos, cada um ali especializados, comunicando entre si. Essa esse pelo menos é a aposta que eu vejo pro eh pro futuro próximo, né? Isso não é não é só sai também um pouco do laboratório. Eu acho que isso é o

- **[37:15](https://youtu.be/nXzUAubH8kg?t=2235)** mais importante também numa empresa para a gente precisa entregar eh produtos que sejam úteis, que as pessoas estejam usando. Então o nosso Sab3, ele tem uma qualidade próxima ali do GPT4 em tarefas eh em português importantes pro Brasil, mas a gente consegue ofertar ele a quatro um preço quatro vezes menor do

- **[37:33](https://youtu.be/nXzUAubH8kg?t=2253)** que o GPT4 por causa dessa especialização, né? A OpenI não entrega o tamanho do modelo deles, mas imagino que é maior do que o nosso dado que eles cobram mais. Então a gente consegue treinar um modelo menor, eh, que tem o mesmo desempenho porque é especializado. Inclusive, tem outros outros estudos que

- **[37:48](https://youtu.be/nXzUAubH8kg?t=2268)** a gente fez que a gente mostra que o desempenho do nosso modelo em outros domínios é pior do que o do que o GPT4, bem pior. Então, cada vez que você especializa o modelo, naturalmente você perde qualidade em outros, né? Eh, e e um caso que eu tenho bastante

- **[38:03](https://youtu.be/nXzUAubH8kg?t=2283)** orgulho, a gente tem bastante orgulho, é da JUS Brasil, que tá usando hoje nossos modelos. A Jus Brasil é a maior legaltec do Brasil, eh, ela é uma das investidores da Maritaca e também a gente desenvolveu um modelo jurídico pro Brasil. Hoje, se você vai lá no site da

- **[38:17](https://youtu.be/nXzUAubH8kg?t=2297)** JUS Brasil e clica no tem lá o processo que você tá acompanhando, você clica um daqueles andamentos que é escrito em legaleza, né? super difícil de entender. Eh, é, é uma das nossas IAs que tá rodando ali por de trás, que que faz uma explicação pro Lego entender melhor o

- **[38:31](https://youtu.be/nXzUAubH8kg?t=2311)** processo e acompanhá-lo, né? Então, hoje a gente serve 25 milhões de brasileiros todos os meses através do site da JUS Brasil que estão usando essas IAs especializadas, né? Antes eles usavam modelos como por exemplo da Open AI e migraram pra gente. É um grande orgulho assim a gente ter pelo menos um desses

- **[38:45](https://youtu.be/nXzUAubH8kg?t=2325)** casos em que em massa eh agora tem uma empresa que tá usando uma tecnologia nacional, né? E por fim, aqui já chegando no final, eu queria discutir um pouco do de um possível futuro próximo, né? Tem tem muitas dúvidas o que que vai acontecer eh no mundo com com o Advento da Iá. E

- **[39:06](https://youtu.be/nXzUAubH8kg?t=2346)** aqui, como eu falei no começo da palestra, acho que tem eu tenho uma visão um pouquinho diferente, pelo menos do que eu escuto quando eu converso com as pessoas e é uma visão um pouco meio armagedona, da coisa, né? e que eu acho que é importante discutir, pode ser que

- **[39:18](https://youtu.be/nXzUAubH8kg?t=2358)** ela não aconteça, a gente acabou só perdendo um dinheiro ali, mas se acontecer, acho que o impacto vai ser grande. Então, para isso, tem esses cinco níveis, eh, paraa inteligência artificial geral, de acordo com a PNI, né? Eu sei que a inteligência artificial geral é um tema super polêmico, né? O

- **[39:35](https://youtu.be/nXzUAubH8kg?t=2375)** que que seria a inteligência geral? Mas pelo menos aqui acho que serve pra gente ter uma uma noção um pouco de progresso eh de onde estão essas IAS, né? Então, de acordo com o PNA, nível um de inteligência são esses chatbot, que você consegue conversar normalmente. Nível dois são esses e as capazes de fazer

- **[39:51](https://youtu.be/nXzUAubH8kg?t=2391)** raciocínio. Então você dá um problema complicado de matemática e física, ela consegue chegar na solução completa, na solução correta. Eh, nível três são esses agentes. A gente já tá começando, né, a ver eh bastante uso desses agentes, principalmente nas empresas. Então, IAS tem acesso a ferramentas, né, por exemplo, um banco de dados,

- **[40:10](https://youtu.be/nXzUAubH8kg?t=2410)** interface com com call center, que consegue aí tomar decisões e cumprir tarefas, né? Hoje a gente tem agentes bastante não confiáveis, né? Eles cometem erros a todo momento, mas a gente tá fazendo um bom progresso lá, né? Agora, eh, os níveis, o nível quatro, de acordo com o PNA, são IAS capazes de

- **[40:30](https://youtu.be/nXzUAubH8kg?t=2430)** produzir conhecimento. Essa, essa é a grande incógnita hoje, né? Será que dado que a gente já consumiu todo o conhecimento humano possível, será que agora, e essa I tá sendo ali próxima dos dos melhores humanos que temos hoje de em cada um das suas áreas especializadas, será que elas vão ser

- **[40:46](https://youtu.be/nXzUAubH8kg?t=2446)** capazes de fato conseguir produzir novo conhecimento, né? Será que ou elas só estão fazendo interpolação? Eh, essa é um próximo passo, ainda tá em aberto, a gente vai chegar lá. E daí por fim tem essas IAS que daí vão fazer o trabalho de organizações inteiras. Elas não vão

- **[41:00](https://youtu.be/nXzUAubH8kg?t=2460)** ser mais inteligentes ou intelectualmente mais capazes do que apenas um ser humano. Eh, mas vão ser o mesmo intelecto de uma organização inteira em termos de organizar, eh, por exemplo, eh, vender os seus produtos, eh, fazer pesquisa e etc., né? E o tudo bem, a gente não sabe se é

- **[41:20](https://youtu.be/nXzUAubH8kg?t=2480)** capaz ainda, se a gente é capaz ainda de chegar nesse nível quatro. Tem algumas mostras, por exemplo, você eh olha no artigo do Alpha F da Deep Mind, ele hoje é capaz de encontrar estruturas 3D da proteína e isso contribuiu pra nossa base de conhecimento universal. Eh, eh,

- **[41:36](https://youtu.be/nXzUAubH8kg?t=2496)** então ele, eu posso argumentar aqui que de uma maneira tímida a gente já tá conseguindo produzir novos conhecimentos, mas será que a gente vai de fato conseguir fazer grandes contribuições, né? Então, tá indo essa esse ponto em aberto, mas agora a parte mim que é mais importante de prestar

- **[41:50](https://youtu.be/nXzUAubH8kg?t=2510)** atenção é essa parte das organizações, né? Se de fato elas chegarem lá e elas vão conseguir fazer o trabalho de organizações inteiras, o argumento aqui é que a maior parte do capital intelectual de um país, ele vai ser produzido por essas IAS, ou pelo menos alguma parte desse capital

- **[42:05](https://youtu.be/nXzUAubH8kg?t=2525)** intelectual. E se todas essas IAS hoje elas são de fora, o valor agregado aqui dessas empresas brasileiras vai ser pequeno, né? Então imagina, voltando naquele ponto do do exemplo do site do Upwork, o que impede a OpenI daqui 10 anos, quando eles estiverem ali resolvendo 90% das tarefas, de

- **[42:22](https://youtu.be/nXzUAubH8kg?t=2542)** abruptamente aumentarem ali o custo do das IAS dele e falar: "Não, agora o lucro é todo meu". Eh, e de fato eles eles têm alguns alguns planos, por exemplo, de cobrar $.000 por uma ali, que eles dizem nível agentes, nível eh doutorado, né? se isso vai ser uma

- **[42:36](https://youtu.be/nXzUAubH8kg?t=2556)** realidade ou não, tá em aberto, eu reconheço. Mas se se de fato acontecer, o impacto vai ser muito grande. E aqui que da a gente chega nos pensamentos finais, né? Se se de fato isso for verdade e e a gente tá vendo mostras de que pelo menos não não tem nenhuma

- **[42:54](https://youtu.be/nXzUAubH8kg?t=2574)** barreira, eh existem desafios científicos a todo momento, mas não tem nenhuma barreira quando a gente olha paraos últimos 3 4 anos que essas não tão não estão tendo progresso, né? Então você olha pra programação, tivemos grandes avanços, biomedicina, você vê o Alpha Fold. E daí vem a pergunta pro

- **[43:08](https://youtu.be/nXzUAubH8kg?t=2588)** Brasil, né, pra gente se manter relevante, o que que a gente precisa fazer? Eh, na minha opinião, a gente precisa de um de uma infraestrutura computacional urgente para essa nova revolução industrial, né? Então, acho que a gente tá vivendo ali um exemplo bem próximo do que foi em 1940 na CSN,

- **[43:23](https://youtu.be/nXzUAubH8kg?t=2603)** quando o governo vai lá e fala: "Quer saber? Eu vou dedicar num país que era majoritariamente agrário, eu vou dedicar ali à construção de uma ciderúrgica para produzir aço e a gente vai começar a nossa industrialização. Eh, esse é um salto, né? Imagino que na devia ter muito

- **[43:36](https://youtu.be/nXzUAubH8kg?t=2616)** muitos críticos na época falando: "Não, o Brasil devia focar no agrário, vamos só eh vender café, que esse é o nosso forte, né?" Mas o governo foi lá e tomou esse essa o governo, né? A sociedade como um todo concordou em tomar esse esse passo para entrar nessa nova

- **[43:50](https://youtu.be/nXzUAubH8kg?t=2630)** revolução industrial e deu certo, né? Tem outros exemplos. Por exemplo, na África, eu fiquei sabendo recentemente que eh na década de 60, acho que foi Gana, tinha um surplus enorme de de alguma das plantações, eles tentaram fazer a revolução industrial e não conseguiram. E hoje é um país muito mais

- **[44:06](https://youtu.be/nXzUAubH8kg?t=2646)** pobre do que o Brasil, né? Então acho que é importante a gente olhar esses exemplos e dar esse salto com coragem para essa nova revolução industrial. Com isso, a academia ela vai também conseguir entender o comportamento da IAS. E eu acho que aqui é importante fez voltar de novo naquele ponto do cluster

- **[44:23](https://youtu.be/nXzUAubH8kg?t=2663)** especial que a gente precisa. Eh, eu queria usar a analogia aqui do telescópio, né? Hoje, se você tem 1 milhão de telescópios espalhados ali no país todo, você não consegue enxergar tão longe quanto o único James Web que que o pessoal, o Congresso resolveu investir dinheiro ali para para mirar

- **[44:41](https://youtu.be/nXzUAubH8kg?t=2681)** mais longe, né? E eu acho que hoje o problema que a gente tem é esse. A gente tem clusters pequenos ou ou melhor acesso a pouca computação. Os nossos estudos caseados, a gente acaba usando modelos pequenos, a gente chega em conclusões e erradas que talvez uma IA maior já tinha resolvido. Por exemplo,

- **[44:58](https://youtu.be/nXzUAubH8kg?t=2698)** você quer estudar algum algum tipo de baias que essa IA possa ter? Se você usa um um modelo de 7 bilhões de parâmetros, você vai chegar em conclusões diferentes que você tivesse usado um modelo que nem o depsic, porque os bias deles são diferentes desse modelo menor. E acho

- **[45:11](https://youtu.be/nXzUAubH8kg?t=2711)** que hoje a gente tá nesse ciclo de eh com esse problema de não ter acesso a essa essa essa grande computação. E uma vez que a gente tem um parque computacional desse, não só a academia ela vai entender melhor os impactos da da IA na sociedade. empresas também elas vão conseguir comercializar,

- **[45:27](https://youtu.be/nXzUAubH8kg?t=2727)** desenvolver e comercializar internamente também exportar, que é super importante, essas IAS de base. E caso contrário, caso a gente não tenha essas IAS, não tenha domínio dessa tecnologia, tanto na academia quanto no setor empresarial, o lucro todo vai para quem as as produz, né? que voltando de novo no argumento, o

- **[45:45](https://youtu.be/nXzUAubH8kg?t=2745)** que impede em algum momento dessas dessas empresas se consolidarem num num pequeno num oligopólio que falam que essa B vai ficar 100 vezes mais caro do que tá custando hoje, né? Então acho que esse é um perigo iminente e e eu queria terminar aqui a palestra com uma frase talvez até um

- **[46:02](https://youtu.be/nXzUAubH8kg?t=2762)** pouco depressiva, mas eu acho que é o momento da gente tomar ação, né? O Dario Modei era o CEO Antropic. Antropic para quem não conhece é uma das empresas líderes ali de desenvolvimento de IA. E ele publicou no começo desse ano um blog, eh, um blog poster, eh,

- **[46:18](https://youtu.be/nXzUAubH8kg?t=2778)** argumentando, defendendo que os Estados Unidos deveria banir a venda de chips paraa China. E a lógica dele, que eu acho que é muito interessante aqui, porque até bani os chips paraa China, até esperado que eles queiram fazer isso, mas a lógica dele é essas IAs elas já estão usando, já estão sendo úteis

- **[46:33](https://youtu.be/nXzUAubH8kg?t=2793)** hoje para desenvolver IAS futuras. Eh, na na Maritaca, por exemplo, cada hora que sai um modelo open source novo, a gente se beneficia, porque a gente pode usar esse modelo para fazer melhores curadorias e dados, eh, melhores modelos para partir do nosso pré-treino, open source, etc. Então, quem tem acesso a

- **[46:48](https://youtu.be/nXzUAubH8kg?t=2808)** melhores IAS consegue andar mais rápido. Se você, a lógica dele é, se você bane temporariamente essa, esse acesso da China aos chips, a China não vai conseguir avançar tão rápido. Isso vai dar uma liderança pros Estados Unidos seu aliados eh cada vez maior, que pode ser duradoura, que daí os Estados

- **[47:06](https://youtu.be/nXzUAubH8kg?t=2826)** Unidos, no futuro vai assumir essa liderança eh commanding and longing lead, ele usa no blog original dele. E eu acho que o mundo ele não precisa ser dividido entre comandantes e comandados, né? Deveria ter um espaço para para todos nós, só que a gente precisa fazer tomar essa atitude logo antes que a

- **[47:24](https://youtu.be/nXzUAubH8kg?t=2844)** gente não seja aqui da parte dos comandados, né? E é isso. Obrigado, pessoal. [Aplausos] Rodrigo, muito obrigado pela sua apresentação. Agora a gente vai passar pra etapa das perguntas. Vou começar com perguntas aqui do anfiteatro. Quem quiser fazer a primeira pergunta, levanta a mão. Rodrigo, muito obrigado pela sua

- **[47:55](https://youtu.be/nXzUAubH8kg?t=2875)** palestra aí, foi bem eh inspiradora aí com relação ao cenário atual da inteligência artificial. Eh, eu queria agradecer em nome do Departamento de Ciência de Computação. Eh, eu tô na chefia do departamento, vice-chefe aqui comigo também. Então, a gente recebeu essa sua visita com muita satisfação. Ah, eu queria

- **[48:16](https://youtu.be/nXzUAubH8kg?t=2896)** saber a de você sobre o modelo de negócio da IA. Acho que é algo aí que pega bastante, porque a gente, pelo menos até onde eu sei, você pode me corrigir, eh, o modelo de negócio não não tá se pagando, né? Tem muita gente enfiando dinheiro em I a não digo no

- **[48:34](https://youtu.be/nXzUAubH8kg?t=2914)** cenário nacional, mas no cenário internacional, ah, apostando no que isso vai acontecer, vai gerar no futuro, mas ainda não tá dando dinheiro para ninguém, não tá dando lucro para ninguém. Eh, e em paralelo tem muita gente assumindo que a IA vai ser uma commodity, né, granted, então a gente

- **[48:56](https://youtu.be/nXzUAubH8kg?t=2936)** vai ter essa comunidade no futuro, né? Então eu queria saber você como você acha que vai convergir essas essas esses dois fatos. Esses dois fatos. Ah, a gente vai ter essa comodidade mesmo, se comode mesmo, ela vai ser mais cara, né? Como é que você enxerga isso? É, eu

- **[49:13](https://youtu.be/nXzUAubH8kg?t=2953)** tenho duas duas eh partes da resposta, né? A primeira, de fato, hoje tem muito mais dinheiro sendo gasto em desenvolvimento dessas viadas, o que o Lucra tá trazendo. E acho que a aposta implícita ali que todo mundo tem é nesse futuro ali, né? o The Winner takes all,

- **[49:29](https://youtu.be/nXzUAubH8kg?t=2969)** né? Eu acho que o CEO da Google falou meio que isso. Você eh a gente vai se arrepender muito se a gente não investir bastante hoje, depois perder essa corrida e ver ali os bilhões que tem. Então, de fato, é um é um pensamento eh eh a na aposta de que de fato essa IA

- **[49:46](https://youtu.be/nXzUAubH8kg?t=2986)** vai ali tá permeando toda a sociedade, né? O quanto ao lucro, o que o que eu posso dizer é que hoje se parar a corrida, o lucro é bom. Eh, se você esses essas vendas por API, por exemplo, o Dip que ele publicou no site deles lá, o quanto

- **[50:01](https://youtu.be/nXzUAubH8kg?t=3001)** que eles conseguem de lucro pela API deles, era uma mar de 500, 600%, isso é verdade mesmo. É, não é não é tão não é tão fora o os números que eles colocaram, né? O problema é que tá nessa curva de crescente de investimento na tecnologia, então as empresas demandam

- **[50:16](https://youtu.be/nXzUAubH8kg?t=3016)** mais do que elas estão tendo de faturamento, né? E já na parte de virar commodity, e essa daí eu imagino que também já escutei o custo por token, né? O custo por prever cada palavra vai tender a zero. Isso é isso eu acredito que pode ser uma verdade. O a coisa é que a gente quer

- **[50:36](https://youtu.be/nXzUAubH8kg?t=3036)** cada vez mais esses tokens, né? Você pensa nesses modelos de raciocínio. Hoje antes eles geravam uma resposta curta pra gente com 500 palavras. Hoje você quer que eles fiquem lá, eh, buscando dados na web, tudo para gerar essa. Então, quanto mais quanto mais barato fica esse custo por token, eh, mais a

- **[50:52](https://youtu.be/nXzUAubH8kg?t=3052)** gente tá consumindo essas IAS, atividades antes, por exemplo, que você conseguia resolver com simples rejecs, eh, mas que tinha um pequeno erro, hoje as pessoas já vi pessoas mudando tudo para para irá, porque o custo benefício ali tá tudo no mesmo pipeline, integra e resolve, né? Eh, mas dito isso sobre a

- **[51:10](https://youtu.be/nXzUAubH8kg?t=3070)** commodity, eu eu tenho minhas dúvidas se dominar essa tecnologia vai se tornar uma commodity, né? Hoje tem, inclusive, já aproveitando e tocando no ponto dos modelos open source, que eu que eu não falei muito, os modelos open source eles são fantásticos, né? A gente se beneficia, a gente não existiria se não

- **[51:26](https://youtu.be/nXzUAubH8kg?t=3086)** fosse esses modelos open source, tanto para partir dos nossos treinos quanto também fazer curadoria de dados e uma série de outros ou avaliar modelos. Eh, o problema é que o open source hoje ele é um ele é um open source diferente do que a gente tá acostumado no nosso

- **[51:41](https://youtu.be/nXzUAubH8kg?t=3101)** imaginário do que que é o modelo open source. Por exemplo, no Linux quando você vai lá e e teve a comunidade open source, cada programador podia trabalhar durante o dia, chegar à noite e contribuir pro código fonte e as pessoas colocavam ali no repositório do Linux. Eh, hoje open source de A é bem

- **[51:58](https://youtu.be/nXzUAubH8kg?t=3118)** diferente. Quem que faz modelo open source de fronteira? São três empresas, Meta, Alibaba e o Dipsic. Talvez ali se quiser colocar algumas outras ali na jogada. Então o open source é feito por por Big Techs. Eh, infelizmente o indivíduo não consegue contribuir hoje. Se hoje eu tiver uma GPU e falar: "Quer

- **[52:17](https://youtu.be/nXzUAubH8kg?t=3137)** saber? Eu vou melhorar esse modelo". Você vai fazer um pequeno fine tuning lá que não é muito claro o relação com com esse essa tsunami que chega quando a a meta lança um novo modelo, né? Então, a gente tá na mão da benevolência dessas dessas big techs de lançarem o modelo

- **[52:32](https://youtu.be/nXzUAubH8kg?t=3152)** open source pra gente. Eu acho que esse que é o cenário mais perigoso no futuro, né? a qualquer momento, quando quando imagino que em em algum momento vai se vai ter um oligopólio de quem quem domina a tecnologia de de desenvolvimento as e oligopólio se eh de fato chegar eh o que

- **[52:55](https://youtu.be/nXzUAubH8kg?t=3175)** o que vai estimular essas empresas que fazem parte desse oligopólio de deixarem as ias open source. Esse é o eh pode ser que seque esses modelos open source da empresas, por exemplo, como a Maritaca, que hoje depende de open source, vai ficar com uma tecnologia defasada, a gente não vai conseguir competir eh eh

- **[53:13](https://youtu.be/nXzUAubH8kg?t=3193)** eh eh de igual para igual com as melhores e vai se sedimentar ainda mais o oligopólio, né? E do jeito que tá hoje, parece que sim, dado o capital necessário para investimento, eh, naturalmente estão convergindo por isso. Por isso que eu acho que países, né, países grandes como

- **[53:32](https://youtu.be/nXzUAubH8kg?t=3212)** Brasil, Índia, tudo, a gente precisa se unir como como governos para ou ou sociedade de uma forma geral e falar, vamos tentar combater isso, esse é o é o eu eu sei que todo isso tudo é abrir mão, por exemplo, de construir hospitais e e rede de esgoto, né? Mas enfim, eh,

- **[53:49](https://youtu.be/nXzUAubH8kg?t=3229)** são apostas ali que talvez fique pior no futuro se a gente não investir hoje nisso, né? É bom. Eh, primeiramente, muito obrigado pela palestra. Eu queria perguntar se você vê, tipo, o futuro das inteligências artificial caminhando junto com a engenharia de dados e a ciência de dados, porque se você pensar

- **[54:10](https://youtu.be/nXzUAubH8kg?t=3250)** no gargalo de dados que a gente tem hoje, cada vez mais vai ser necessário profissionais na área de engenharia de dados e ciência de dados, não só para treinar essas bases, não só para treinar essas novas inteligências artificiais ascendentes, mas como uma forma de tipo cooperação, né? Um proto uma

- **[54:27](https://youtu.be/nXzUAubH8kg?t=3267)** protosivência. Um depende do outro para tá funcionando. Eu queria a sua visão como especialista na área de como que vai ser esse futuro da engenharia de dados falando com a inteligência artificial, falando da ciência de dados. É hoje num futuro de de curto prazo, eu imagino que assim hoje hoje rola muito

- **[54:46](https://youtu.be/nXzUAubH8kg?t=3286)** mais cooperação do que do que essa competição entre as elas precisam de muita supervisão. O o meu maior medo é que isso não seja mais verdade num futuro daqui 5, 10 anos. Eh, é grandes coisas desse futuro não existir, né, de de fato, olha, essas sempre vão precisar de supervisão. Eh,

- **[55:06](https://youtu.be/nXzUAubH8kg?t=3306)** vai ter pessoas ali que vão precisar saber ser mais com grande profundidade, porque as IAS não são Deus, né? elas não sabem tudo. Eu eu acho que esse é um futuro provável, mas eh eu acho que a gente também não pode ser ingênuo de engêno a palavra, mas a gente tem que considerar o outro

- **[55:26](https://youtu.be/nXzUAubH8kg?t=3326)** futuro que talvez essas ias eh pode ser que você não precise mais saber ser mais mais, né? Daí você vai ter que se adaptar para uma nova coisa, uma nova uma nova forma de interação com essas IAS que vai ser bem diferente hoje, né? Eh, é como assim, ninguém sabe a

- **[55:40](https://youtu.be/nXzUAubH8kg?t=3340)** resposta, né? se se isso vai ser de fato acontecer ou não. Mas eu acho que o quanto antes a gente começar a pensar, discutir, eh, fazer design cursos, né, de treinar esses profissionais, tendo esse futuro em mente, não não fazer uma aposta 100%, né, não, IA vai, relaxa,

- **[55:55](https://youtu.be/nXzUAubH8kg?t=3355)** não precisa mais estudar a programação, que IA agora vai fazer toda a programação. Isso aí tem um, tem um risco de de não acontecer, mas enfim, ser um pouco mais diverso nas apostas hoje de ensino do que é o modelo. Mas uma coisa é certa, né? O modelo

- **[56:09](https://youtu.be/nXzUAubH8kg?t=3369)** tradicional hoje eu acredito que precisa mudar, né? Dado dado essa capacidade delas de que nem eh eu eh dava aula na Unicamp como como professor voluntário. Eh e e a e vocês devem ter milhares de casos assim também semelhantes, né? Você tem uma prova de seleção pros alunos,

- **[56:29](https://youtu.be/nXzUAubH8kg?t=3389)** daí você dá pro chatt, ele resolve todas as provas. E agora o que que eu vou fazer com com essa prova de seleção? E hoje hoje é o que acontece, né? a gente precisa reformular todos esses cursos para antes coisas básicas que a gente ensinava ficar na dúvida se deve ensinar

- **[56:42](https://youtu.be/nXzUAubH8kg?t=3402)** ou não, né? É, sou eu. Eh, sou Alexandre. Eh, eu vou perguntar mais sobre a questão da infraestrutura computacional. Eu tô como coordenador de infraestrutura computacional do centro de A, né, da USP BM FAPESP. E tem essa questão é latente há muito tempo, né, como que fazer conseguir esses recursos. Bem, você

- **[57:06](https://youtu.be/nXzUAubH8kg?t=3426)** colocou o problema, né, como fundamental, mas você tem alguma proposta, alguma ideia? O problema, né? Eu acho que imagino que você tenha ideias de como resolver isso. É, é, eu gostaria hoje, hoje uma das uma das frentes que a gente tá tentando levar é fazer um consórcio de empresas e

- **[57:24](https://youtu.be/nXzUAubH8kg?t=3444)** universidades para que tenha um cluster híbrido de uso híbrido, né? O grande desafio hoje, eu eu eu acredito talvez ingenuamente, eu tô começando a entender um pouco mais de como que funciona essa esfera política agora, mas o grande desafio, imagino que hoje tá mais na nas regras que já foram criadas, né? Por

- **[57:40](https://youtu.be/nXzUAubH8kg?t=3460)** exemplo, se você hoje quiser criar um cluster, tem uma empresa que quer investir x milhões, outra quer investir, a universidade também tem um dinheiro, vamos construir um cluster que vai ser compartilhado em todos esses, né? Hoje os regramos tanto dessas empresas quanto das suas universidades não permite que

- **[57:55](https://youtu.be/nXzUAubH8kg?t=3475)** esse cluster seja de propósito híbrido, né? Ou é só para pesquisa ou é só comercial, né? E e daí você tem um monstrão que daí você vai, por exemplo, ter que obrigar a USP a usar sozinho toda essa capacidade computacional, sendo que ela poderia estar compartilhando com uma empresa que de

- **[58:11](https://youtu.be/nXzUAubH8kg?t=3491)** bom grado eh gostaria de pagar pro uso dessa computação, né? Então hoje acho que é um entrave quase que político, porque juntar pelo menos a minha experiência conversando com as empresas e com as com as universidades, cada um tem um pouquinho de dinheiro. E a gente não tá falando de muito dinheiro, por

- **[58:26](https://youtu.be/nXzUAubH8kg?t=3506)** exemplo, para construir hoje um cluster mínimo para fazer um um fine tuning, né, um pequeno treino do deep seek, você precisa de R$ 60 milhões de reais. Não é tão difícil conseguir R 60 milhões de de reais com 10 players. O problema são os regramentos hoje dessas instituições e

- **[58:43](https://youtu.be/nXzUAubH8kg?t=3523)** empresas. Ninguém quer compartilhar nada, né? E acho que esse é o principal entráve. Dinheiro não acho que é tanto problema. Eh, Rodrigo, eu vou alternar algumas perguntas agora pro público que tá nos assistindo online pelo canal do MBA e do ICMC, tá? Eh, a primeira pergunta eh é do Lucas Nóbrega. A

- **[59:04](https://youtu.be/nXzUAubH8kg?t=3544)** pergunta dele é: "Qual sua opinião sobre a melhor forma do Brasil regular a inteligência artificial? o quanto isso influencia ou vai influenciar na capacidade de novas tecnologias brasileiras de IA? Eh, esse esse é um tópico, infelizmente eu não tenho tanto conhecimento, mas algumas visões só. Eh, o principal hoje, se você ir para

- **[59:28](https://youtu.be/nXzUAubH8kg?t=3568)** ultrulação, empresas pequenas como a gente são mortas no sentido de você cria 100 regras para conseguir colocar a sua IA em uso. Eh, grandes empresas conseguem eh implementar essas regras com muito mais velocidade do que a gente. Então é bem possível ali que, por exemplo, para você servir a Soiá num

- **[59:48](https://youtu.be/nXzUAubH8kg?t=3588)** tribunal tal, precisa ter 10 certificados tudo para passar. Isso aí são tipos de de regulamentações que que que desfavorecem empresas pequenas, né? Mas agora nível sociedade, pensando um pouquinho mais longo prazo, eu acho que é super importante ter essas regulamentações asias, né? Hoje teve se você vai, por exemplo, usa umas viagas

- **[01:00:09](https://youtu.be/nXzUAubH8kg?t=3609)** que nem do Grock lá do do Twitter, é a coisa medonha que ela que ela é capaz de fazer, que ela pode gerar. Tem vários exemplos, né? Se imagina uma daqui três, 5 anos muito mais capaz de de inventar fake news, etc. Então, acho que a recomendação tem que ser super forte.

- **[01:00:25](https://youtu.be/nXzUAubH8kg?t=3625)** Eh, ainda reconheço que ainda tá cedo pra gente ter uma regulamentação certeira, precisa ser revisada várias vezes, mas eh temos que fazer, né, assim, com certeza vai ser que nem a aviação, precisa ter ali um órgão fiscalizador, né? Eh, uma outra pergunta também por quem nos acompanha online do Everton Sherman.

- **[01:00:47](https://youtu.be/nXzUAubH8kg?t=3647)** Em um mundo onde exista LLMs abertas, o quanto realmente é crítico termos uma eh para uma nação ter LLM própria, já que a gente teria acesso às abertas? E eu eu acho que isso volta no no argumento da de hoje, a gente depende da benevolência dessas big tech em fazerem as open

- **[01:01:05](https://youtu.be/nXzUAubH8kg?t=3665)** source pra gente, né? De fato, se hoje o mundo parar, né? não tiver mais progresso em todas as empresas parem de desenvolvimento, os open sources que tem hoje são bons, a gente já consegue usar bastante. Eh, o problema, volta naquele assunto, o o se de fato o oligopólio se

- **[01:01:23](https://youtu.be/nXzUAubH8kg?t=3683)** formar, para que que uma para que que essas empresas do oligopólio vão continuar entregando a tecnologia deles, né? Eles vão vão segurar para si. E é triste de ver, mas por exemplo, exemplos como eh institutos que hoje tentam treinar suas open source, eu cito, por exemplo, o Allen Ai, eles têm

- **[01:01:42](https://youtu.be/nXzUAubH8kg?t=3702)** um grande parque computacional lá em em em Washington. Eles Washington não disci o estado, eles têm um grande parque computacional para treinar esses modelos, só que os modelos deles não são tão bons quanto os melhores open source das das bigtechs, né? Então a gente vê esse essa defasagem de open source de

- **[01:02:01](https://youtu.be/nXzUAubH8kg?t=3721)** instituição eh com relação ao open source de bigtech. Então você não vê nenhum open source de Stanford que que treinou do zero, apesar deles terem um parque computacional decente. E então a gente tá na mão desses bigtechs. Logo, eu acho que a gente precisa não não dá para apenas viver esperando que a cada

- **[01:02:20](https://youtu.be/nXzUAubH8kg?t=3740)** novo mês alguma empresa generosamente vai colocar o open source no mundo, que para mim a propósito é uma forma de soft power, né? você quer ali ganhar. Ninguém conhecia o Deepsic antes. Se o Depsic tivesse feito uma IA Close Source, talvez a gente não teria falando dele agora, não. Mas ele resolveu fazer o

- **[01:02:34](https://youtu.be/nXzUAubH8kg?t=3754)** peso, os códigos, os pesos do modelo abertos e eh publicar um artigo técnico mostrando a proeza deles, né? Então, o mundo inteiro. Hoje o o dono de psique, ele consegue uma audiência com qualquer presidente de qualquer país por causa dessa dessa pro técnica, né? Mas para mim isso é só uma forma de soft power.

- **[01:02:51](https://youtu.be/nXzUAubH8kg?t=3771)** Eh, o que impede ele daqui 10 anos de querer fazer a mesma coisa, né? Eh, bom dia, Rodrigo. Eh, obrigado pela palestra. Eu queria perguntar, sair um pouco desse nível eh político, geopolítico ali, né, de Estados Unidos, China, Brasil, como que a gente se posiciona, dar um passo atrás

- **[01:03:11](https://youtu.be/nXzUAubH8kg?t=3791)** e para um lado mais abstrato dessa questão que você tava falando sobre eh inteligência artificial eh geral. E a minha dúvida é até que ponto os problemas que a gente se depara hoje ou que a gente imagina hoje, projeta hoje, eh, em termos dessa fronteira, do que que a IA pode se tornar, eh,

- **[01:03:30](https://youtu.be/nXzUAubH8kg?t=3810)** tecnologicamente, é um problema, eh, que a gente consegue resolver dentro da academia, ou seja, um problema técnico da computação. Eh, ou e até que ponto ele é um problema político que a gente vai ter que agir a respeito da da regulação e etc? Eh, minha preocupação é o seguinte, eh, até que

- **[01:03:50](https://youtu.be/nXzUAubH8kg?t=3830)** ponto a gente consegue ter soluções eh técnicas para problemas, como, por exemplo, desalinhamento ou falta de controle que a gente projeta hoje sendo problemas possíveis desse cenário de Armagedon que você se referiu, né? Sim. Eh, o que que que você enxerga disso? Qual que é o papel, por exemplo, de a

- **[01:04:08](https://youtu.be/nXzUAubH8kg?t=3848)** gente que tá hoje num mestrado, num doutorado? Eh, e acho que num slide seu você até coloca, né, de tipo que a gente tem que pensar mais como é que esses modelos funcionam, como é que eles de fato reproduzem inteligência, né? Eh, o que que é o limite do que a gente consegue

- **[01:04:23](https://youtu.be/nXzUAubH8kg?t=3863)** agir na academia e o que que a gente age politicamente? Eu acho que a academia tem muitas oportunidades que nem deveriam ser tarefas das empresas, né? Hoje, por exemplo, essa questão de alignment é hoje toda delegada pras empresas, você interage com o chatbot, ela tem uma pequena carinha ali do

- **[01:04:39](https://youtu.be/nXzUAubH8kg?t=3879)** Silicon Valley, do Vale do Silício, dos criadores ali de eh da daquelas morais da da moral que é que é que é colocada ali naqueles modelos, né? E eu acho que o potencial da academia para isso, principalmente na questão de alignment, eh, a academia ela tem que ter uma, ela

- **[01:04:58](https://youtu.be/nXzUAubH8kg?t=3898)** tem que ter a, como se diz, a frente desse tipo de problema, né? Porque fica tudo publicado. A gente usa modelos open source, pesos abertos, dizem como é que o alinhamento é feito, dizem onde falha. Porque a maritaca pode publicar ali um estudo falando: "Olha, aqui tá as

- **[01:05:13](https://youtu.be/nXzUAubH8kg?t=3913)** limitações do meu modelo, Antrópico pode fazer o mesmo, mas quem que vai acreditar que a gente não não tá escondendo um monte de outras limitações que a gente fez, né?" Então, acho que o papel da academia de de validar essas IAS, inclusive de criar métodos, hoje hoje um problema que a gente tem muito

- **[01:05:27](https://youtu.be/nXzUAubH8kg?t=3927)** grande, eh, que eu mencionei um pouco na palestra, é o é o é o essa percepção, né? A gente tem benchmarks que hoje estão saturados, a gente chama os melhores especialistas do assunto, criam perguntas e e a consegue responder bem. Só que a percepção humana quando interage com esses chatbots é que esse

- **[01:05:46](https://youtu.be/nXzUAubH8kg?t=3946)** esse negócio não é tão bom, né? todo esse desalinhamento. Hoje a gente não sabe por eu acho que é é um trabalho da academia eh conseguir entender primeiramente. E se a gente não tá falando de trabalhos de de especialista, se a gente tá falando de uma IA que é

- **[01:06:03](https://youtu.be/nXzUAubH8kg?t=3963)** nível alguém que tem doutorado em física quântica, eh como a gente a gente que não tem esse nível de conhecimento consegue garantir que essas IAS elas de fato estão dando as respostas corretas pra gente? Não tem nenhum erro ali, né? Eh, hoje não não existe acho que nenhuma

- **[01:06:19](https://youtu.be/nXzUAubH8kg?t=3979)** forma, nenhum consenso, tanto na academia quanto na indústria, de como avaliar essas IA. E esse é um esse é um dos problemas. Eh, tem também um problema de impacto da sociedade. Eh, hoje a gente pensa muito nessas IAS como iterações de curto prazo, né? Você manda um documento grande, faz algumas

- **[01:06:37](https://youtu.be/nXzUAubH8kg?t=3997)** perguntas e tarefa feita, mas e num futuro próximo, talvez elas vão estar começando muito mais tempo interagindo com o seu computador. Como é que você garante que nenhum dos passos ali dela, como é que você faz essa supervisão para que nenhum dos passos dela lá, de fato, ela não usou sua conta bancária e fez

- **[01:06:52](https://youtu.be/nXzUAubH8kg?t=4012)** alguma coisa errada? Não, não que ela seja, não que ela tenha esse nenhum ímpeto ali interno de querer ter umas discussões nessa nessa linha de que as IAS elas têm alguma alguma vontade, não nessa linha, mas mais na linha de de fato a sua tarefa foi não foi 100%

- **[01:07:08](https://youtu.be/nXzUAubH8kg?t=4028)** especificada para IA. Ela simplesmente adotou um trajeto ali que uma trajetória que vai te prejudicar no futuro, mas ela só tá cumprindo a tarefa, né? Como que você garante isso? Eh, eu imagino que é um trabalho da academia e o impacto social, com certeza, né? Eh, elas vão

- **[01:07:26](https://youtu.be/nXzUAubH8kg?t=4046)** est, querendo ou não, elas vão estar ali decidindo quem recebe crédito, quem não recebe crédito, quem que vai paraa prisão, quem que não vai paraa prisão. Não, não que não vai ter sempre um juiz ali, talvez dando a assinatura final, mas se ele usa a IA para gerar 80% dos

- **[01:07:43](https://youtu.be/nXzUAubH8kg?t=4063)** argumentos dele ou para inspecionar, vai ter um pequeno bias ali que a IA vai estar introduzindo, né? E acho que a academia da isso é super importante de de garantir que tá refletindo de fato o conhecimento, as morais que a gente tem ou ou ainda, né? O pode ser que essa IA

- **[01:07:58](https://youtu.be/nXzUAubH8kg?t=4078)** seja perfeita, mas é perfeita talvez para lá fora, né? E aqui dentro do Brasil tem um monte de particularidades, né? Tava Thiago até deu um exemplo ontem interessante da da medicina, né? Você tem uma IA que é usada, por exemplo, para para receitar remédios. Se essa I tá num hospital ali em São Francisco,

- **[01:08:17](https://youtu.be/nXzUAubH8kg?t=4097)** ela vai querer, talvez, ela talvez vai ser treinada para receitar o remédio mais caro que vai tratar a melhor doença, mas você tá no SUS, você tem ali uma série de problemas, talvez o mais caro não resolva. Então, como treinar essas IAS que se adaptem? Eh, isso acho

- **[01:08:30](https://youtu.be/nXzUAubH8kg?t=4110)** que é um são problemas que a academia pode atacar muito, né? Ô, Rodrigo, bom dia. Eh, obrigado pela palestra. Eu sou Marco da Itera. Eh, eu queria entender um pouquinho, voltar um pouquinho no modelo de negócio da Maritaca para entender como vocês vão conseguir escapar desse jogo de gato e rato aí

- **[01:08:47](https://youtu.be/nXzUAubH8kg?t=4127)** entre muito dinheiro e a construção de um modelo especializado ao nível que vai ficar interno por algum momento. Eu queria entender como vocês vão triangular, né? Então, hoje você tem eh APIs já disponíveis a um custo baixo. Uhum. Que gera um grande bite. Então, provavelmente hoje vocês estão ganhando

- **[01:09:08](https://youtu.be/nXzUAubH8kg?t=4148)** dinheiro com a construção de APIs, por exemplo, para pro Jus Brasil. Eh, e também que esse custo tende a baixar. Então, eu quero entender ali como que você vai escapar desse momento como empresa, tá? Eu queria abordar a Maritaca aí, por favor. É, nesse assim, sendo 100% honesto, esse momento é um

- **[01:09:25](https://youtu.be/nXzUAubH8kg?t=4165)** salto de fé dos investidores, né? Você tá nessa corrida grande e a gente espera que o investimento em tecnologia daqui 20 anos não vai ser desse volume que a gente tá precisando hoje. A gente não só maritaca como empresas, né? De fato, de fato é uma é um é um risco assim

- **[01:09:42](https://youtu.be/nXzUAubH8kg?t=4182)** que é é um salto de fé. Não tem nenhuma conta. Acho que hoje você chega ali para e nenhuma empresa que trabalha, que faz essas vias de conta, eu duvido que elas tm alguma conta. tive 100 bilhões de faturamento e só preciso de de 10 bilhões de investimento. Hoje esses

- **[01:09:56](https://youtu.be/nXzUAubH8kg?t=4196)** números estão todos eh descasados, mas as pessoas estão apostando, porque eu tô apostando porque acham que que o impacto vai ser muito maior. Mas mas eu concordo com você 100%, assim, é é um logicamente eh a gente consegue ter lucro hoje se parar o desenvolvimento, mas a hora que

- **[01:10:13](https://youtu.be/nXzUAubH8kg?t=4213)** você consegue coloca o desenvolvimento na jogada é sempre prejuízo. E todas as empresas ali tão estão nessa aposta, né? Não, não tem, não tem resposta simples ali, né? Saldo de fé. Você tá conseguindo esse salto de fé no Brasil ou fora? A Jus Brasil, por exemplo, é uma das

- **[01:10:29](https://youtu.be/nXzUAubH8kg?t=4229)** pessoas, uma empresa ali que se não fossem eles, eh a gente não teria assim dado esse tamanho de investimento. Outro também, eu falo mal de Big Tex tudo, mas o Google, por exemplo, na criação da Maritaca, eles deram acesso pra gente no cluster deles, era 1 milhão de dólares,

- **[01:10:46](https://youtu.be/nXzUAubH8kg?t=4246)** 4 meses de uso. E foi foi porque eu tinha uma conexão com a academia. Eu falei: "Ó, já publiquei vários modelos em português, tô criando uma startup, nem tinha startup ainda, vocês me dão acesso a esse cluster." Daí um e-mail só falando assim, OK? Eu falei: "Bom, temos

- **[01:11:01](https://youtu.be/nXzUAubH8kg?t=4261)** uma empresa, né?" Então esse salto de fé começou com Google e depois com alguns outros investidores aqui no no Brasil, né? Isso que é essa essa é a parte tensa que eu vejo, né? Ninguém quer investir numa empresa que vai desenvolver e nacionais fala: "Você vai perder para

- **[01:11:16](https://youtu.be/nXzUAubH8kg?t=4276)** Open AI, né? Para que que eu vou investir aqui no Brasil, né? Mas você pode falar uma ordem? Infelizmente não. Eu até gost até por pela Marital que a gente poderia falar, mas pelos investidores é esse é segredo, né? É. Opa. Eh, bom dia. Obrigado, Rodrigo, pela palestra. Foi muito interessante.

- **[01:11:36](https://youtu.be/nXzUAubH8kg?t=4296)** Eh, meu nome é Danilo, eu sou da startup Sigalei. A gente atua muito do lado assim do Jus Brasil, ele atua junto com formação jurídica, né? A gente já atua formações regulatórias e legislativas, né? tudo que deveria ser resolvido antes de virar processo, né? Deveria resolver, a gente ataca nessa área. Então, a gente

- **[01:11:53](https://youtu.be/nXzUAubH8kg?t=4313)** tá muito muito interessado nesses modelos, né? Porque a gente tá sempre pensando na camada de aplicação, mas já que a gente tá aqui na academia, eu queria pedir licença pra gente falar um pouco de futurologia, né? Eh, hoje os modelos de linguagem, né? Modelos de geração de linguagem, né? geração de imagem,

- **[01:12:13](https://youtu.be/nXzUAubH8kg?t=4333)** geração de áudio. A gente percebe testando nosso aqui, que ele é um modelo de ida só, né? Uhum. Ele é um modelo que ele tem os pesos dele, que é o conhecimento do mundo dele, né? Que tem lá a camada de atenção e toda a inovação que ele que ele traz, né? Mas ele é um

- **[01:12:29](https://youtu.be/nXzUAubH8kg?t=4349)** modelo de ida. O que que ele sabe de nós? O contexto, a janela de contexto, né? É a única coisa de informação. É a aquela coisa, né? Aquela armadura gigante, aquele espacinho de de visão, né? Bem curto, né? Então, é a única coisa de interação e a gente percebe que

- **[01:12:44](https://youtu.be/nXzUAubH8kg?t=4364)** essa arquitetura que você pode ser muito bom no modelo específico ou muito eh geral também tem suas limitações, porque ele sempre de novo, é um modelo de ida, né? aquela aquela experiência, pô, ontem você respondeu certo para mim, hoje você respondeu errado. Se fosse qualquer estagiário mais mais com menos conhecimento possível,

- **[01:13:03](https://youtu.be/nXzUAubH8kg?t=4383)** né, ele aprenderia com tempo. Ou seja, essa arquitetura, ao meu ver, ele tem uma aplicação enorme. E o que eu fico me perguntando, a gente tá desenvolvendo muita aplicação em cima dele, né? E a gente fica dependendo das dos provedores de modelo, por exemplo, pra gente poder adaptar o máximo possível, eventualmente

- **[01:13:20](https://youtu.be/nXzUAubH8kg?t=4400)** fazer um fine tuning, mas é isso, né? sai algo, tem um investimento grande do modelo básico, a gente faz o fine tune e aplica, né? Uma coisa mais estática. E a gente pesquisando, a gente sempre todo dia tem paper, né? Pá, pá, e tem o o a proposta do modelo de do mundo, né? Word

- **[01:13:37](https://youtu.be/nXzUAubH8kg?t=4417)** models, que é um modelo que é como você contratar o eh adotar um modelo de LLM para você, né? Tipo, ele vai cria uma instância para você, você vai interagindo com ele e ele vai ajustando os pesos dele. Vai o que a gente chama de aprender de fato, né? Sim. Eh, e

- **[01:13:52](https://youtu.be/nXzUAubH8kg?t=4432)** esse, na minha percepção, é o que de fato pode chegar, né, na AGI e qualquer outra coisa mais eh interessante. Aí a questão é como negócio aqui, né, eu fico pensando qual que é a nossa janela de oportunidade com esses modelos só de ida assim, sabe? Quanto, quão longe a gente

- **[01:14:09](https://youtu.be/nXzUAubH8kg?t=4449)** tá desses modelos de world models que realmente conseguem aprender? Porque na hora que ele chegar, ele vai jogar tudo pro lixo, né? Tipo, ah, que que você acha sobre isso? Eh, eu eu eu também aposto que que esses modelos que vão interagir longo prazo resolvendo nossas tarefas é o vão ser o futuro, né? Por

- **[01:14:28](https://youtu.be/nXzUAubH8kg?t=4468)** exemplo, aquela coisa, aquela questão do descasamento hoje que a gente tem com benchmarks com a experiência humana, né? Que eu acho que reflete um pouco, talvez que o que você falou que a gente não passa todo o contexto de o que a gente tá trabalhando hoje por modelo, né? A

- **[01:14:41](https://youtu.be/nXzUAubH8kg?t=4481)** gente tem que especificar um prompt, né? uma pergunta, talvez tem um histórico da conversa, mas não é a mesma coisa com que ele se tivesse acesso aos últimos 5 anos seu de de conversas de e-mail e tudo mais. Então eu imagino que os os melhores modelos são esses modelos ali

- **[01:14:56](https://youtu.be/nXzUAubH8kg?t=4496)** de iterações de longo prazo com a gente, né? Vão ter uma janela de contexto, seja lá como vai ser isso, eh, de de anos que que vai tá constantemente sendo sendo refinado, né? e que acho que um um artigo que eu li recentemente do do Richard Sutton, Richard Sutton é o é um

- **[01:15:13](https://youtu.be/nXzUAubH8kg?t=4513)** dos pais ali do não pais, mas um dos grandes nomes do do aprendizado por reforço. E ele com o David Silver da Deep M escreveram um artigo que é chama a era da experiência, alguma coisa assim. E o argumento deles é que a gente esgotou já os dados humanos, ou seja, a

- **[01:15:27](https://youtu.be/nXzUAubH8kg?t=4527)** gente já esgotou em imitar o que que o humano, o comportamento do humano na web. Claro que a gente faz curadoria, tudo para não pegar os piores comportamentos, né? Mas a próxima era agora vai ser a era da experiência desses agentes, né? Eles vão estar interagindo e eles vão estar

- **[01:15:43](https://youtu.be/nXzUAubH8kg?t=4543)** coletando eh respostas do do ambiente e vão estar se melhorando com isso, vão est com base nas decisões que eles fizeram, né? Então, é é o é o é o clássico aprendizado por reforço, mas o argumento dele é que agora a gente vai sair um pouco dessa era de simulação que

- **[01:15:57](https://youtu.be/nXzUAubH8kg?t=4557)** foi aprendizado por reforço de uns 10 anos atrás, mas vai começar a deixar esses agentes tomarem ações cada vez mais longo prazo. Mas mas eu eu eu concordo com você. Eu acho que o futuro vai ser um vai ser esse esse cenário e não esse cenário hoje que é entra 1

- **[01:16:12](https://youtu.be/nXzUAubH8kg?t=4572)** milhão de token só e faz a predição para mim, né? uma questão. Nesse caso, por exemplo, o modelo ele é treinado, tem bilhões de parâmetros, né? Uma coisa que eu fico curioso pensar, ah, desculpa, obrigado. É, então eu fico pensando, beleza, um modelo tem bilhão de panorâmetros, né?

- **[01:16:29](https://youtu.be/nXzUAubH8kg?t=4589)** Para você rodar um modelo, você tem que ter uma GPU. Eh, teoricamente, nessa questão que a gente tá falando de futurologia, a gente tá falando de ele ajustar os pesos dele, né? Reajustar os pesos dele. Uma coisa que eu fico pensando é isso, né? Como que é igual a

- **[01:16:42](https://youtu.be/nXzUAubH8kg?t=4602)** gente dorme, ajusta nossos pesos na mente, né? e acorda mais inteligente no dia seguinte. Será que eh eu fico pensando sobre essa capacidade e essa limitação de como que você vai retreinar um modelo gigante em minutos, né? Sim. E e eu acho que daí você também, voltando naqueles pontos do do que atacar hoje,

- **[01:17:02](https://youtu.be/nXzUAubH8kg?t=4622)** né, nesse universo tudo aí e o que que eu vou fazer pesquisa, né, esses são os problemas em abertos hoje, né? Inclusive, eu eu cooriento um aluno de doutorado que o tema dele é exatamente esse, como que você faz um adiciona conhecimento no modelo continuamente, de maneira eficiente. Hoje a gente,

- **[01:17:19](https://youtu.be/nXzUAubH8kg?t=4639)** paradoxalmente, a gente consegue treinar em bilhões de tokens e ter sucesso, mas a gente não consegue treinar em 10 páginas de documento e ter sucesso. Então, surgiu, supor, mudou uma nova legislação, saiu uma jurisprudência nova, eh, você quer que o modelo tenha isso nos pesos dele, você consegue meio

- **[01:17:35](https://youtu.be/nXzUAubH8kg?t=4655)** que ele decorar aquele documento, só que daí você destrói uma série de outras tarefas. Então, hoje é tudo uma arte, né, essa essa ingestão de conhecimento. Por isso que acho que hoje não existe nenhum modelo hoje, pelo menos comercial, acadêmico também acho que não, que tem esse aprendizado contínuo,

- **[01:17:51](https://youtu.be/nXzUAubH8kg?t=4671)** né, que eh porque hoje não não é é um problema que não é resolvido. E inclusive até um tema de pesquisa, acho que que é super interessante, né? E também tem a questão da eficiência, que nem você falou, são bilhões de parâmetros. Você pode usar técnicas ali que nem o Lora, por exemplo, para para

- **[01:18:03](https://youtu.be/nXzUAubH8kg?t=4683)** conseguir fazer um treino menor, mas no longo prazo você vai acabar destruindo ou não, degradando ou não o conhecimento, né? Tudo tudo em aberto. Eh, Rodrigo, uma pergunta do que veio de do do pessoal assistindo online, fazer ra sobre modelos genéricos não seria mais barato do que treinar os modelos

- **[01:18:21](https://youtu.be/nXzUAubH8kg?t=4701)** especialistas? Aí vou só mudar um pouquinho, né? Se você usar um modelo eh uma LLM muito grande, boa, né? E será que qual que é o tradeoff do que que compensa ou não? Na sua opinião? A a gente tem grandes discussões. A Maritaca, eu sou eu sou do time que não

- **[01:18:35](https://youtu.be/nXzUAubH8kg?t=4715)** tem que fazer o treino especialista. Tem, tem várias pessoas na Maritá que falam: "Vamos, vamos focar um pouco em reg, né? Eu sou o cara do contra aqui, então minha resposta é super viezada". Eh, um dos problemas que eu vejo no reg, aliás, o meu meu tema de doutorado foi

- **[01:18:51](https://youtu.be/nXzUAubH8kg?t=4731)** em sistemas de busca, né? information retrieval. E uma das coisas que eu que eu notei durante o o doutorado é que era muito difícil você conseguir sistema recuperação de informação. É fácil você conseguir eh buscar conhecimentos que tão eh únicos ali específicos em trechos e documentos, né? Então você quer saber

- **[01:19:11](https://youtu.be/nXzUAubH8kg?t=4751)** ali a altura da torre fel. É muito fácil hoje um sistema de busca trazer acuradamente aquela informação para você. O problema fica sendo quando quando essa informação tá dispersa em diversos documentos e você quer unir aquele conhecimento. Eh, eu, por exemplo, um dos casos é o é o Google

- **[01:19:27](https://youtu.be/nXzUAubH8kg?t=4767)** Proof lá. Foi é um benchmark exatamente feito assim. Não, não existe nenhum documento que fala tudo isso. Você precisa fazer essa ponte entre vários. É possível de fazer usar o regte? Não vejo problema algum. você pode fazer várias buscas e eh e e coletar esses documentos e depois

- **[01:19:46](https://youtu.be/nXzUAubH8kg?t=4786)** soltar a resposta final pro usuário, né? Bem como os agentes hoje são utilizados. Mas o argumento que eu que eu que eu vejo contra relação a isso e também confesso que hoje o Hag ele é ele é muito mais eficiente do que essas partes de de fazer esse treinamento contínuo on

- **[01:20:01](https://youtu.be/nXzUAubH8kg?t=4801)** the fly. Eh, mas é que me parece muito contrainttuitivo você chegar num médico ali especialista, sei lá, um médico torrino, ô, tô com uma, eh, enfim, tô tô com uma dor aqui. E daí ele fala: "Pera aí, só um segundinho, eu vou pesquisar aqui em 100 artigos científicos e vou

- **[01:20:18](https://youtu.be/nXzUAubH8kg?t=4818)** aprender sobre o assunto on the fly". Para mim parece muito mais natural que esse médico já tem ali nos pesos dele, eh, tanto o médico artificial quanto natural, eh, já tenho nos pesos dele o conhecimento sobre esse assunto e use o mecanismo de busca como uma ferramenta ali auxiliar para tirar eventuais

- **[01:20:34](https://youtu.be/nXzUAubH8kg?t=4834)** dúvidas, né? Mas eu eu acredito que o futuro vai ser vai ser híbrido. Você vai ter com certeza a busca vai existir lá. essas ferramentas vão estar lá o tempo todo para para auxiliar, assim como os médicos, os advogados, eles usam busca o tempo todo. Eh, mas a questão de ter já

- **[01:20:49](https://youtu.be/nXzUAubH8kg?t=4849)** esse conhecimento impregnado e e mais importante ter essas informações que estavam dispersas de alguma forma unidas hoje no peso da rede neural, eu acho que é fundamental. Mas eu confesso que hoje não é assim. Hoje o Hag ele é um é uma técnica ali que se você usa já resolve

- **[01:21:05](https://youtu.be/nXzUAubH8kg?t=4865)** bastante seus problemas. Eu tô falando mais num um futuro de longo prazo. Eh, Rodrigo, a minha pergunta acho que vai só um pouco eh repetitiva depois dessa, que ela vai na mesma linha, mas falando de usar IA generativa como uma fonte de conhecimento factual, eh você citou o Hag como uma maneira de gerar um

- **[01:21:24](https://youtu.be/nXzUAubH8kg?t=4884)** conhecimento, bom, que não é uma alucinação. E hoje em dia a gente tem muita gente assim que tá acostumado a usar e a Generativa GPT como uma ferramenta de busca, como uma ferramenta de conhecimento. E como você citou, apesar de bem benchmark, na vida real alucina bastante, erra. E eu queria

- **[01:21:41](https://youtu.be/nXzUAubH8kg?t=4901)** expandir um pouco mais essa relação entre busca e LLM. Hoje em dia a gente vê conferência de busca no Sigil, no Neurips, que tem cada vez mais intersecção entre essas duas áreas. Acho que até uma área que você trabalhou anteriormente, né? Você usa ll para expandir termo de querer? Você usa busca

- **[01:21:58](https://youtu.be/nXzUAubH8kg?t=4918)** para gerar informação factual com rádio, você já tem gente usando LLM como máquina de busca, como recomendador. Mas hoje em dia, ou melhor no futuro, como que você vê a relação dessas duas áreas? Como como você citou agora? Uma relação de simbiose, uma apoia a outra ou você

- **[01:22:14](https://youtu.be/nXzUAubH8kg?t=4934)** vê que eventualmente uma LM vai substituir uma uma máquina de busca, um information retrivo ou ou são coisas totalmente separadas? É, essa é uma boa pergunta de novo, que a resposta é um pouco meio super vizada. Eh, o um dos problemas que eu vejo na busca é que

- **[01:22:32](https://youtu.be/nXzUAubH8kg?t=4952)** você precisa resolver rapidamente, percorrer rapidamente uma um banco de dados enorme. Para isso, você não consegue gastar muita computação, né? você consegue mover essa computação, por exemplo, pro estágio de indexação, você consegue mover essa computação pro estágio de ranqueamento, mas como a gente tá falando ali de milhares de

- **[01:22:50](https://youtu.be/nXzUAubH8kg?t=4970)** documentos ou ou milhões toda hora, você tá sempre limitado por essa computação. Então, o meu entendimento é que esses LLMs hoje eles são um sistema de busca mais eficiente para buscar esses conhecimentos mais contínuos do que do que o do que o do que o sistema de busca

- **[01:23:10](https://youtu.be/nXzUAubH8kg?t=4990)** mais clássico, né? mesmo o clássico que usa LLM ou que usa redes neurais, ele ele ainda tem essa limitação. E daí por causa disso, eu imagino que o futuro vai ser o LLM controlando o sistema de busca e não não como, por exemplo, o Hag anterior, que o Hag antes era o Hag

- **[01:23:25](https://youtu.be/nXzUAubH8kg?t=5005)** clássico, quando eles não tinham muita capacidade de argente. Você primeiro faz a busca, coloca qualquer contexto lá e torce para que o modelo vai vai trazer a resposta correta. Hoje eu vejo cada vez mais a gente tá tratando busca como uma ferramenta eh com erros também que permite uma interação que a gente

- **[01:23:41](https://youtu.be/nXzUAubH8kg?t=5021)** busque, né? Então assim, eu acho que busca vai continuar existindo. Essa pressão por ter por buscar documentos, milhões de documentos mais eficientemente vai tá lá e e técnicas vão surgir. Eh, mas eu vejo o papel do LLM cada vez mais aumentando conforme ele vai tendo já esse conhecimento nos pesos dele, né?

- **[01:24:00](https://youtu.be/nXzUAubH8kg?t=5040)** Aqui de novo voltando no argumento do é é bom que você já saiba de cabeça várias as coisas ali que no dia a dia você usa, né? E daí para todas aquelas que você não precisa de memorização, você o mecanismo de busca ele ele vai rápido, né? Olá, eh, eu sou o André, aluno de

- **[01:24:19](https://youtu.be/nXzUAubH8kg?t=5059)** graduação aqui e eu gostaria de saber eh quais que seriam os primeiros passos eh se eu preciso ter o quanto de conhecimento, né, como desenvolvedor para fundar a minha a minha própria empresa de LLM, né? E se e se for necessário, quais são os primeiros passos, né? É, não, excelente

- **[01:24:43](https://youtu.be/nXzUAubH8kg?t=5083)** pergunta. E eu fico feliz de você ter perguntado, eu tava até conversando com a minha esposa, ela ela é minha só fundadora também. Quando a gente começou com a maritaca, eh, a gente tinha dinheiro para fazer tipo 1% do treinamento do modelo, né? Eh, e fal vamos começar, daí veio o grant do

- **[01:25:00](https://youtu.be/nXzUAubH8kg?t=5100)** Google, etc., né? Então, nessa veia de empreendedorismo, eu acho que a conta, eu também escutei da da fundadora do do Magazine Luía, que ela juntou dinheiro suficiente para pagar o primeiro mês do aluguel da da loja que ela queria abrir e depois ela esperava, torcia para que os próximos meses e ela ia ter o

- **[01:25:18](https://youtu.be/nXzUAubH8kg?t=5118)** dinheiro, né? Então eu acho que preciso um pouco desse Isso. Tô primeiro falando na na na visão financeira, né? meio que eu a mensagem só se é que eu tenho direito de passar alguma mensagem numa empresa tão nova, mas eh vai eh faça esse risco que quando você começa a

- **[01:25:36](https://youtu.be/nXzUAubH8kg?t=5136)** fazer alguma coisa, outras pessoas vão lá e te ajudam, né? Mas a parte técnica, eu acho que tem muita coisa hoje que não é não exige tanto tanto conhecimento e e você vai aprender ao longo do tempo, né? e a área avança muito rápido. Eu não ficaria nem um pouco intimidado com com

- **[01:25:55](https://youtu.be/nXzUAubH8kg?t=5155)** essa com esse avanço, né? Porque você consegue hoje usar sistemas prontos, você consegue fazer uma pequena melhoria melhoria. E eu acho que o importante é que no longo prazo você continue investindo em alguma direção sem ficar tirando para todo lado, né? Porque quando você investe na sempre naquela direção aumenta a chance de você

- **[01:26:14](https://youtu.be/nXzUAubH8kg?t=5174)** fazer alguma coisa que ninguém mais fez. É a velha história do artesão ali, né? que que faz faz a coisa muito bem feita. Hoje hoje parando para pensar na Maritaca assim há 2 anos e meio quando a gente começou e para hoje a gente a gente aprendeu muito, né? A gente fazia

- **[01:26:27](https://youtu.be/nXzUAubH8kg?t=5187)** erros hoje que a gente olha ali no passado que é de dar risada, né? E acho que a gente tá hoje fazendo erros que daqui 5 anos a gente também vai dar risada. Mas enfim, eu acho que a resposta que é bem luz, eu sei, mas não é que eu poderia falar, não, você

- **[01:26:41](https://youtu.be/nXzUAubH8kg?t=5201)** precisa saber a álgebra linear, precisa saber computação distribuída, não sei o quê. A gente não sabe de quase nada disso perto do que a gente sabe hoje, né? E e tá dando certo. Então eu acho que assim, tem que ter um salto de fé ali. Não não precisa, acho que você se

- **[01:26:54](https://youtu.be/nXzUAubH8kg?t=5214)** preocupar muito em ter todo o arcabolso antes de começar, né? Eu acho que o a experiência vai dizendo para você ao longo do caminho, né? Bom, como estamos chegando no final, né, do nosso horário, eu vou fazer a última pergunta, eh, escolhendo aqui da do pessoal que tá assistindo online, aí

- **[01:27:11](https://youtu.be/nXzUAubH8kg?t=5231)** fica bem equilibrado. A Maritaca planeja expandir as capacidades de seus modelos, incorporando funcionalidades multimodais? Sim, planejamos isso também. É um, acho que a fonte de imagens e áudio tem conhecimento muito interessante ali, né? Eu acho que também faz sentido você ter um modelo multimodal especializado, né? Acho, eu cito, por exemplo, o caso do do

- **[01:27:34](https://youtu.be/nXzUAubH8kg?t=5254)** Imednet, né, que é um é um dataset bastante popular para treinar modelos de visão computacional. Ele foi todo ali, tem um viés muito grande. Já fizeram vários artigos publicados falando do viés, que aquelas imagens foram coletadas ali majoritariamente no norte. E daí quando você aplica aqui para essas

- **[01:27:50](https://youtu.be/nXzUAubH8kg?t=5270)** para reconhecer algumas imagens aqui do do nosso contexto, eh o desempenho desses modelos, desses modelos caem, né? Hoje, hoje não é mais realidade que hoje os grandes os grandes modelos de visão computacional são treinados numa quantidade muito maior de dados, mas eh eu acho que multimodal faz sentido. Eu

- **[01:28:06](https://youtu.be/nXzUAubH8kg?t=5286)** acho que faz sentido ter IAS ali que viram coisas ali que talvez as IAS de fora não viram, né? Muito bom, Rodrigo. Novamente nós agradecemos sua apresentação, o tempo aqui que passou com a gente e uma sala de palmas para [Aplausos] agradecer a as o restante das perguntas

- **[01:28:29](https://youtu.be/nXzUAubH8kg?t=5309)** que foram realizadas online, nós vamos compilar e enviar para você, tá, Rodrigo? Aí você escolhe algumas aí para responder e a gente repassa pro pro pessoal lá da turma de MB e ABgrata. Então, encerramos aqui a nossa palestra e a apresentação do Rodrigo. Bom para todo [Música] [Música]

- **[01:29:13](https://youtu.be/nXzUAubH8kg?t=5353)** mundo. Oh. เ
</details>
