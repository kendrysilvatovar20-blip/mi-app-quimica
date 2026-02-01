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
        # Usamos 'preguntay' para que coincida con el formulario
        duda = request.form.get('preguntay')
        if duda:
            try:
                # Conexión con el modelo Flash
                res = model.generate_content("Responde como tutor de química: " + duda)
                texto_respuesta = res.text
            except Exception as e:
                texto_respuesta = "Error de conexión con la IA. Verifica los módulos."

    # Diseño completo con TODO en color gris (gray)
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Tutor de Química</title>
            <meta charset="utf-8">
        </head>
        <body style="font-family: Arial; text-align: center; padding: 50px; color: gray;">
            <h1 style="color: gray;">Tutor de Química con IA</h1>
            <form method="post">
                <input type="text" name="preguntay" placeholder="Escribe tu duda aquí..." style="width: 300px; padding: 10px;">
                <button type="submit" style="padding: 10px 20px;">Preguntar</button>
            </form>
            <div style="margin-top: 30px; white-space: pre-wrap; text-align: left; display: inline-block; max-width: 80%; color: gray;">
                <h3 style="color: gray;">Respuesta:</h3>
                <div style="color: gray;">{{ respuesta }}</div>
            </div>
        </body>
        </html>
    ''', respuesta=texto_respuesta)

if __name__ == '__main__':
    # Corregido: puerto 10000 para que abra normal en local y Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)










