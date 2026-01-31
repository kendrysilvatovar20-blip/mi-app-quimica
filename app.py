import google.generativeai as genai

# Tu llave verificada
genai.configure(api_key="AIzaSyBv_CLxHTfnmENRBVjEGBL_MfD1X84LyM4")

def solucionador():
    print("\n🔍 BUSCANDO MODELO COMPATIBLE...")
    try:
        # Esto le pregunta a Google: "¿Qué modelo me dejas usar?"
        modelos_disponibles = [m.name for m in genai.list_models() 
                               if 'generateContent' in m.supported_generation_methods]
        
        if not modelos_disponibles:
            print("❌ No hay modelos disponibles para esta llave.")
            return

        # Usa el primero que encuentre
        model = genai.GenerativeModel(modelos_disponibles[0])
        print(f"✅ Conectado con éxito a: {modelos_disponibles[0]}")
        
        problema = input("\n¿Qué duda de química tienes?: ")
        response = model.generate_content(problema)
        print(f"\n📜 RESPUESTA:\n{response.text}")
        
    except Exception as e:
        print(f"\n❌ Error técnico: {e}")

if __name__ == "__main__":
    solucionador()