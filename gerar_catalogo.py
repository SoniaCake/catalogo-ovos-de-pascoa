# gerar_catalogo.py
# Gera um catálogo virtual de ovos de páscoa em HTML
# Autor: Wemerson Lima

import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ARQUIVO_DADOS = os.path.join(BASE_DIR, "dados_ovos.json")
ARQUIVO_HTML = os.path.join(BASE_DIR, "index.html")
WHATSAPP_NUMERO = "5561981815975"

# Carrega os dados dos ovos
with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
    ovos = json.load(f)

# Início do HTML
html = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Catálogo de Ovos de Páscoa - Sonia Lima</title>

<style>
body {
    font-family: Arial, sans-serif;
    background: #f5f5f5;
    margin: 0;
}

header {
    background: #ffffff;
    padding: 30px;
    text-align: center;
}

header h1 {
    margin: 0;
}

.catalogo {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 20px;
    padding: 30px;
}

.card {
    background: #ffffff;
    border-radius: 10px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    overflow: hidden;
}

.card img {
    width: 100%;
    height: 220px;
    object-fit: cover;
}

.card .conteudo {
    padding: 20px;
}

.card h2 {
    margin-top: 0;
}

.detalhes {
    font-size: 14px;
    margin-top: 10px;
}

.botao {
    display: inline-block;
    margin-top: 15px;
    padding: 10px 15px;
    background: #25D366;
    color: #ffffff;
    text-decoration: none;
    border-radius: 5px;
    font-weight: bold;
}

.botao:hover {
    opacity: 0.9;
}

footer {
    text-align: center;
    padding: 20px;
    font-size: 13px;
}
</style>

</head>
<body>

<header>
<h1>Catálogo de Ovos de Páscoa</h1>
<p>Sonia Lima Confeitaria</p>
</header>

<section class="catalogo">
"""

# Geração dos cards
for ovo in ovos:

    mensagem = f"Olá, gostaria de encomendar o {ovo['nome']}."
    mensagem = mensagem.replace(" ", "%20")

    link_whatsapp = f"https://wa.me/{WHATSAPP_NUMERO}?text={mensagem}"

    html += f"""
    <div class="card">
        <img src="imagens/{ovo['imagem']}">
        <div class="conteudo">
            <h2>{ovo['nome']}</h2>
            <p>{ovo['descricao']}</p>
            <div class="detalhes">
                <strong>Recheios:</strong> {", ".join(ovo['recheios'])}
            </div>

            <a class="botao" href="{link_whatsapp}" target="_blank">
                Encomendar pelo WhatsApp
            </a>

        </div>
    </div>
    """

# Final do HTML
html += """
</section>

<footer>
<p>Catálogo Digital</p>
</footer>

</body>
</html>
"""

# Salva o HTML
with open(ARQUIVO_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("Catálogo gerado com sucesso!")