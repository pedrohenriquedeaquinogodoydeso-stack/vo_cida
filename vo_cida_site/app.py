from flask import Flask, render_template

app = Flask(__name__)

produtos = {
    "quiches": [
        "Quiche de Frango Cremoso com Milho",
        "Quiche de Frango Cremoso",
        "Quiche de Frango com Catupiry",
        "Quiche de Palmito",
        "Quiche de Carne de Panela",
        "Quiche de Calabresa",
        "Quiche de Alho-Poró"
    ],

    "paes": [
        "Pão de Fubá",
        "Pão Tradicional",
        "Recheado de Calabresa",
        "Recheado de Frango"
    ],

    "cucas": [
        "Coco",
        "Morango",
        "Doce de Leite",
        "Uva"
    ],

    "doces": [
        "Bolos no pote",
        "Tortinha na travessa",
        "Sobremesas artesanais"
    ]
}


@app.route("/")
def home():
    return render_template("index.html", produtos=produtos)


if __name__ == "__main__":
    app.run(debug=True)