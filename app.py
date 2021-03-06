from flask import Flask, jsonify
from flask import request, render_template
import pandas as pd
from io import StringIO
import os
from config import ordenarEntregas, includeSAL


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/romaneio', methods=['POST'])
def imprimeRomaneio(): 
        planilhaWishLocal = request.form['romaneio']
        if planilhaWishLocal[0:5] == 'Order':
            dados = StringIO(str(planilhaWishLocal))
            dataFrame = pd.read_csv(dados, sep="	")
            dataFrameOrdenado = ordenarEntregas(dataFrame)
            tamanhoDados = len(dataFrameOrdenado)
            return render_template('romaneio.html',df=dataFrameOrdenado,tamanho=tamanhoDados)
        else:
            addCabecalho = ('Order Sent Date	Order ID	Customer Name	Address	Phone	Product Name	SKU	Quantity	Package ID	Package Identifer\n'+planilhaWishLocal)
            dados = StringIO(str(addCabecalho))
            dataFrame = pd.read_csv(dados, sep="	")
            dataFrameOrdenado = ordenarEntregas(dataFrame)
            tamanhoDados = len(dataFrameOrdenado)
            return render_template('romaneio.html',df=dataFrameOrdenado,tamanho=tamanhoDados)


@app.route('/etiquetas', methods=['POST'])
def imprimeEtiqueta():
        planilhaWishLocal = request.form['etiquetas']
        if planilhaWishLocal[0:5] == 'Order':
            dados = StringIO(str(planilhaWishLocal))
            dataFrame = pd.read_csv(dados, sep="	")
            tamanhoDados = len(dataFrame)
            return render_template('etiquetas.html',df=dataFrame,tamanho=tamanhoDados)
        else:
            addCabecalho = ('Order Sent Date	Order ID	Customer Name	Address	Phone	Product Name	SKU	Quantity	Package ID	Package Identifer\n'+planilhaWishLocal)
            dados = StringIO(str(addCabecalho))
            dataFrame = pd.read_csv(dados, sep="	")
            tamanhoDados = len(dataFrame)
            return render_template('etiquetas.html',df=dataFrame,tamanho=tamanhoDados)




if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()