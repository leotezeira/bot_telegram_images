# 👕 TShirt Mockup Bot

Bot de Telegram que convierte mockups de remeras en fotos de modelos listas para Instagram y webs. Usa la **API gratuita de Hugging Face** para generación de imágenes.

-----

## ✨ Qué hace

- Recibís una foto de tu mockup (remera con diseño)
- El bot genera una imagen de modelo usando esa remera
- Fondo blanco limpio, iluminación de estudio, listo para subir a Instagram o web
- Mantiene el diseño/gráfico de la remera original

-----

## 🚀 Setup rápido

### 1. Clonar el repo

```bash
git clone https://github.com/TU_USUARIO/tshirt-mockup-bot.git
cd tshirt-mockup-bot
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar tokens

```bash
cp .env.example .env
```

Editá `.env` con tus tokens:

```env
TELEGRAM_TOKEN=tu_token_aqui
HF_TOKEN=tu_token_aqui
```

### 4. Correr el bot

```bash
python bot.py
```

-----

## 🔑 Cómo conseguir los tokens

### Telegram (`TELEGRAM_TOKEN`)

1. Abrí Telegram y buscá **@BotFather**
1. Enviá `/newbot`
1. Seguí los pasos y copiá el token que te da

### Hugging Face (`HF_TOKEN`) — GRATIS

1. Creá cuenta en [huggingface.co](https://huggingface.co/join) (gratis)
1. Andá a **Settings → Access Tokens**
1. Creá un token nuevo de tipo **“Read”**
1. Copiá el token al `.env`

> ⚡ El plan gratuito tiene un límite de requests por hora. Si se agota, el bot te avisa y podés volver a intentar más tarde.

-----

## 📱 Cómo usar el bot

1. Iniciá una conversación con tu bot en Telegram
1. Enviá `/start` para ver instrucciones
1. **Mandá una foto** de tu mockup (remera con diseño)
1. Opcional: agregá un **caption** para personalizar:

|Parámetro  |Opciones                                             |
|-----------|-----------------------------------------------------|
|Género     |`mujer` `hombre` `unisex`                            |
|Estilo     |`casual` `urbano` `deportivo` `elegante` `streetwear`|
|Ambiente   |`interior` `exterior` `estudio`                      |
|Iluminación|`suave` `dramatica` `natural` `brillante`            |

**Ejemplos de caption:**

- `mujer casual`
- `hombre urbano exterior`
- `mujer elegante brillante`

-----

## 🗂️ Estructura del proyecto

```
tshirt-mockup-bot/
├── bot.py              # Bot principal de Telegram
├── prompts.py          # Construcción de prompts para IA
├── requirements.txt    # Dependencias Python
├── .env.example        # Template de variables de entorno
├── .gitignore          # Archivos ignorados por git
└── README.md           # Esta documentación
```

-----

## 🔧 Modelos de IA utilizados

El bot intenta los modelos en este orden (todos gratuitos en Hugging Face):

1. `stabilityai/stable-diffusion-xl-base-1.0` — Mayor calidad
1. `runwayml/stable-diffusion-v1-5` — Fallback
1. `CompVis/stable-diffusion-v1-4` — Último recurso

Si un modelo está cargando o no disponible, pasa automáticamente al siguiente.

-----

## ⚠️ Límites de la API gratuita

- Hugging Face Free tier: ~100-500 requests/día (varía según el modelo)
- Si llegás al límite, el bot te avisa con un mensaje claro
- Para más requests, podés upgradear en [huggingface.co/pricing](https://huggingface.co/pricing)

-----

## 🛠️ Deploy en servidor (opcional)

Para que el bot corra 24/7 podés usar:

**Railway / Render (gratuito con límites):**

- Subí el repo a GitHub
- Conectalo a [railway.app](https://railway.app) o [render.com](https://render.com)
- Configurá las variables de entorno (`TELEGRAM_TOKEN` y `HF_TOKEN`)
- Deploy automático

**VPS propio:**

```bash
# Con tmux o screen
tmux new -s bot
python bot.py
# Ctrl+B, D para detach
```

-----

## 📄 Licencia

MIT — libre para uso personal y comercial.