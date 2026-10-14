from PIL import Image
import os

def aplicar_overlay_vanilla(ruta_bloque, ruta_textura_base, ruta_salida, escala=8, opacidad_textura=0.35):
    # 1. Cargar el bloque original y escalarlo (Nearest Neighbor para no perder el pixel art)
    img_bloque = Image.open(ruta_bloque).convert("RGBA")
    nuevo_tamano = (img_bloque.width * escala, img_bloque.height * escala)
    img_escalada = img_bloque.resize(nuevo_tamano, Image.Resampling.NEAREST)
    
    # 2. Cargar la textura realista y ajustarla al nuevo tamaño
    img_textura = Image.open(ruta_textura_base).convert("L")
    img_textura = img_textura.resize(nuevo_tamano, Image.Resampling.LANCZOS)
    
    pixeles_bloque = img_escalada.load()
    pixeles_textura = img_textura.load()
    
    # 3. Fusionar las imágenes matemáticamente
    for y in range(img_escalada.height):
        for x in range(img_escalada.width):
            r, g, b, a = pixeles_bloque[x, y]
            
            # Ignorar transparencia (hojas, cristales)
            if a == 0:
                continue
                
            valor_textura = pixeles_textura[x, y] / 255.0
            
            # Aplicar la textura usando multiplicación suave
            ajuste_r = int(r * (1 - opacidad_textura) + (r * valor_textura) * opacidad_textura)
            ajuste_g = int(g * (1 - opacidad_textura) + (g * valor_textura) * opacidad_textura)
            ajuste_b = int(b * (1 - opacidad_textura) + (b * valor_textura) * opacidad_textura)
            
            # Limitar colores entre 0 y 255
            nuevo_r = max(0, min(255, ajuste_r))
            nuevo_g = max(0, min(255, ajuste_g))
            nuevo_b = max(0, min(255, ajuste_b))
            
            pixeles_bloque[x, y] = (nuevo_r, nuevo_g, nuevo_b, a)
            
    img_escalada.save(ruta_salida)

def procesar_carpeta(carpeta_entrada, carpeta_salida, textura_base):
    # Crea la ruta de destino si no existe
    os.makedirs(carpeta_salida, exist_ok=True)
    
    archivos = os.listdir(carpeta_entrada)
    print(f"Empezando a procesar {len(archivos)} archivos...")
    
    for archivo in archivos:
        # Solo procesar imágenes .png para ignorar los .mcmeta
        if archivo.endswith(".png"):
            ruta_entrada = os.path.join(carpeta_entrada, archivo)
            ruta_salida = os.path.join(carpeta_salida, archivo)
            
            try:
                aplicar_overlay_vanilla(
                    ruta_bloque=ruta_entrada, 
                    ruta_textura_base=textura_base, 
                    ruta_salida=ruta_salida, 
                    escala=8, 
                    opacidad_textura=0.35
                )
            except Exception as e:
                print(f"Omitiendo {archivo} (Error: {e})")
                
    print("¡Todos los bloques han sido procesados y guardados en HD!")

# --- EJECUCIÓN ---
carpeta_originales = "bloques_vanilla"
carpeta_destino = "assets/minecraft/textures/block"
textura = "textura_base_stn.jpg"

procesar_carpeta(carpeta_originales, carpeta_destino, textura)