# O render template serve para conectar esse arquivo python com o arquivo html
from flask import Flask, render_template

# app é uma variável onde vai ficar a nossa aplicação
app = Flask(__name__)


# Essa linha está dando o nome da nossa rota
@app.route('/')

# Essa função tem que definir o que a nossa aplicação vai fazer nessa pagina
def ola():
    # O Return dará o retorno da função, ela tem que ser entendida pelo Python e pela Web, por isso usamos as aspas pro Python e a tag H1 pra Web
    return render_template('lista.html', titulo="Jogos")




#Isso faz a aplicação rodar
app.run()