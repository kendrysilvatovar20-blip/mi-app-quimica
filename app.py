import os
from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configuración segura de la IA
llave = os.environ.get("LLAVE_API")
genai.configure(api_key=llave)
model = genai.GenerativeModel('gemini-1.5-flash')

# Esta es la página principal que verá tu profesor
@app.route('/')
def inicio():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>Tutor de Quimica</title></head>
    <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>Tutor de Química con IA</h1>
        <form action="/preguntar" method="post">
            <input type="text" name="pregunta" placeholder="Escribe tu duda de quimica..." style="width: 300px; padding: 10px;">
            <button type="submit" style="padding: 10px;">Preguntar</button>
        </form>
        {% if respuesta %}
            <div style="margin-top: 30px; border: 1px solid #ccc; padding: 20px;">
                <h3>Respuesta:</h3>
                <p>{{ respuesta }}</p>
            </div>
        {% endif %}
    </body>
    </html>
    '''

@app.route('/preguntar', methods=['POST'])
def preguntar():
    pregunta = request.form['pregunta']
    respuesta = model.generate_content("Eres un tutor de química. Responde esto: " + pregunta)
    return inicio().replace('{% if respuesta %}', f'<div style="margin-top: 30px; border: 1px solid #ccc; padding: 20px;"><h3>Respuesta:</h3><p>{respuesta.text}</p></div>')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
