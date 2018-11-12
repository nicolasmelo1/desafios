# Testando o Desafio
Siga os paços de inicialização e rode

Garanta que você está no diretório do projeto.
## Inicializando
Garanta que tenha python acima da versão 3 instalado em sua máquina e rode os seguintes comandos:


Antes de mais nada precisamos criar um `virtual environment`, para isso usamos:
#### Mac/Linux
```
$ python3 -m venv venv
```
```
$ source venv/bin/activate
```
#### Windows
```
> pip install virtualenv
```
```
> virtualenv venv
```
```
> venv\Scripts\activate
```
Depois instalamos as dependencias presentes no `requirements.txt` na `venv` que acabamos de criar:

```
pip install -r requirements.txt
```


## Rodando o Script
Tudo funciona através de um único arquivo, então tenha em mente os seguintes comandos

__Comandos__:
+ `--mine "<str>"` Use esse comando para descobrir o que está bombando nos subreddits de sua escolha, separados por `;` e entre `"`
+ `--set <int>` _Opcional_: Use esse comando para setar o número minimo de _upvotes_
+ `--telegram` _Opcional_: Ignora os demais comandos caso existam e inicializa o bot to telegram.

__Dica__:
 + Use `reddit_home` para descobrir o que está bombando na página principal do reddit
 + Se você não setar um número minimo de upvotes, o valor padrão é `5000`
### Terminal
Exemplo:
```
$ python3 main_crawlers.py --mine "cats;worldnews"
```
ou, para retornar as principais threads com pelo menos 3000 upvotes, use:
```
$ python3 main_crawlers.py --mine "cats;worldnews" --set 3000
```


P.S.: `reddit_home` refere-se a página inicial do reddit. 

Ou seja, `python3 main_crawlers.py --mine "reddit_home"` irá retornar as principais threads da página inicial do Reddit
### Telegram
Para Inicializar utilize o seguinte comando:
```
$ python3 main_crawlers.py --telegram
```
Você pode encontrar o bot procurando por `@mrcrawleybot` no telegram

__Comandos__:

+ `/start` - Inicializa o Bot.
+ `/help` - Ajuda.
+ `/config` - Mude o número minimo de votos para cada thread que você deseja visualizar.
+ `/nadaprafazer` - Encontre o que está bombando nos subreddits de sua escolha. 
Ex.: /nadaprafazer cats;dogs;worldnews

P.S.: `reddit_home` refere-se a página inicial do reddit. 

Ou seja, `/nadaprafazer reddit_home` irá retornar as principais threads da página inicial do Reddit


# Desafio 2: Crawlers

Parte do trabalho na IDwall inclui desenvolver *crawlers/scrapers* para coletar dados de websites.
Como nós nos divertimos trabalhando, às vezes trabalhamos para nos divertir!

O Reddit é quase como um fórum com milhares de categorias diferentes. Com a sua conta, você pode navegar por assuntos técnicos, ver fotos de gatinhos, discutir questões de filosofia, aprender alguns life hacks e ficar por dentro das notícias do mundo todo!

Subreddits são como fóruns dentro do Reddit e as postagens são chamadas *threads*.

Para quem gosta de gatos, há o subreddit ["/r/cats"](https://www.reddit.com/r/cats) com threads contendo fotos de gatos fofinhos.
Para *threads* sobre o Brasil, vale a pena visitar ["/r/brazil"](https://www.reddit.com/r/brazil) ou ainda ["/r/worldnews"](https://www.reddit.com/r/worldnews/).
Um dos maiores subreddits é o "/r/AskReddit".

Cada *thread* possui uma pontuação que, simplificando, aumenta com "up votes" (tipo um like) e é reduzida com "down votes".

Sua missão é encontrar e listar as *threads* que estão bombando no Reddit naquele momento!
Consideramos como bombando *threads* com 5000 pontos ou mais.

## Entrada
- Lista com nomes de subreddits separados por ponto-e-vírgula (`;`). Ex: "askreddit;worldnews;cats"

### Parte 1
Gerar e imprimir uma lista contendo número de upvotes, subreddit, título da thread, link para os comentários da thread, link da thread.
Essa parte pode ser um CLI simples, desde que a formatação da impressão fique legível.

### Parte 2
Construir um robô que nos envie essa lista via Telegram sempre que receber o comando `/NadaPraFazer [+ Lista de subrredits]` (ex.: `/NadaPraFazer programming;dogs;brazil`)

### Dicas
 - Use https://old.reddit.com/
 - Qualquer método para coletar os dados é válido. Caso não saiba por onde começar, procure por JSoup (Java), SeleniumHQ (Java), PhantomJS (Javascript) e Beautiful Soup (Python).
