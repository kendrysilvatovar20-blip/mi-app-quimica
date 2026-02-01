import os
from flask import Flask, render_template_string, request
import google.generativeai as genai

app = Flask(__name__)

# Configuración de la IA
api_key = os.environ.get("LLAVE_API")
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
@app.route('/', methods=['GET', 'POST'])
def inicio():
    texto_ia = ""
    if request.method == 'POST':
        pregunta_usuario = request.form.get('pregunta')
        if pregunta_usuario:
            res = model.generate_content("Responde como tutor de química: " + pregunta_usuario)
            texto_ia = res.text

    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head><title>Tutor de Química</title><meta charset="UTF-8"></head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>Tutor de Química con IA</h1>
            <form action="/" method="post">
                <input type="text" name="pregunta" placeholder="Tu duda de química..." style="width: 300px; padding: 10px;" required>
                <button type="submit" style="padding: 10px;">Preguntar</button>
            </form>
            {% if r %}
                <div style="margin-top: 30px; border: 1px solid #ccc; padding: 20px; background-color: #f9f9f9; text-align: left; display: inline-block; max-width: 80%;">
                    <h3>Respuesta:</h3>
                    <p style="white-space: pre-wrap;">{{ r }}</p>
                </div>
            {% endif %}
        </body>
        </html>
    ''', r=texto_ia)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))










