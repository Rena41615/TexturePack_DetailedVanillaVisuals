# TexturePack: Detailed Vanilla Visuals 🔮

Un paquete de texturas para **Minecraft Java Edition** diseñado para quienes buscan conservar la estética clásica del juego, pero con un toque extra de profundidad. 

Este proyecto añade una textura sutil y rugosa a los bloques, dejando pequeños matices de relieve y color sin alterar la esencia ni la paleta original de Minecraft. Es ideal para una experiencia de supervivencia más detallada, suave a la vista y sin contrastes agresivos.

## Características
- **Resolución HD:** Escalado de 16x16 a **128x128px**.
- **Estilo "Vanilla HDR":** Suaviza y detalla el mundo manteniendo el aspecto clásico.
- **Generación Procedimental:** Las texturas no fueron pintadas a mano una por una. Se utilizó un script automatizado en **Python** (`generador_texturas.py`) que aplica un algoritmo de superposición y opacidad con una textura base de piedra, logrando un relieve uniforme en todos los bloques del juego.
- **Versión Soportada:** Probado de forma estable en Minecraft 26.3 (Pack Format 34).

## Cómo Instalar
1. Ve a la sección de descargas o haz clic en el botón verde **"Code"** -> **"Download ZIP"** en este repositorio.
2. Extrae el contenido si es necesario (asegúrate de que el archivo `pack.mcmeta` esté en la carpeta principal).
3. Presiona `Windows + R`, escribe `%appdata%\.minecraft\resourcepacks` y presiona Enter.
4. Arrastra la carpeta del paquete de texturas a esa ubicación.
5. Abre Minecraft, ve a **Opciones > Paquetes de recursos**, mueve el pack al lado derecho y dale a "Aceptar". *(Si te aparece una advertencia de incompatibilidad, simplemente dale a "Sí", el paquete cargará sin problemas).*

## Sobre el Código Fuente
Si te interesa el lado técnico, el archivo `generador_texturas.py` incluido en este repositorio es el responsable de la magia. Utiliza la librería **Pillow** (PIL) para iterar sobre todos los bloques originales de Minecraft, aplicar el multiplicador de opacidad (0.35) con el relieve base, y exportar la versión en 128x128 lista para el motor del juego.
