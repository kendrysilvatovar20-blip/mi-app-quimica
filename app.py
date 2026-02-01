import os
from flask import Flask, render_template_string, request
import google.generativeai as genai

app = Flask(__name__)

# Configuración con llave directa y Gemini 1.5 Flash
api_key = "AIzaSyAffDqnRJ7HQYkZYUGGOHPyrJUc3tPQZ0"
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/', methods=['GET', 'POST'])
def inicio():
    texto_respuesta = ""
    if request.method == 'POST':
        duda = request.form.get('pregunta')
        if duda:
            try:
                res = model.generate_content("Responde como tutor de química: " + duda)
                texto_respuesta = res.text
            except Exception as e:
                texto_respuesta = "Error de conexión con la IA. Revisa tu LLAVE_API."

    # He corregido la 'r' por 'texto_respuesta' para que coincida con el HTML
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Tutor de Química</title>
            <meta charset="utf-8">
        </head>
        <body style="font-family: Arial; text-align: center; padding: 50px;">
            <h1>Tutor de Química con IA</h1>
            <form action="/" method="post">
                <input type="text" name="pregunta" placeholder="Escribe tu duda de química..." style="width: 300px; padding: 10px;" required>
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
    ''', r=texto_respuesta)

if __name__ == "__main__":
    # Render necesita el puerto dinámico para no dar "Internal Server Error"
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)












