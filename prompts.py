"""
M?dulo de prompts para generaci?n de im?genes de modelos con remeras.
Mantiene consistencia en: modelo, prenda, iluminaci?n y fondo.
"""

from typing import Optional

# ?? Prompt base (siempre presente) ?????????????????????????????????????????????
BASE_PROMPT = (
    "fashion photography, model wearing the t-shirt from the mockup, "
    "studio photo, pure white background, soft natural studio lighting, "
    "professional fashion shoot, high resolution, sharp focus, "
    "the exact same t-shirt design and print as in the reference image, "
    "same colors same graphic same placement on shirt, "
    "full body or upper body shot, Instagram-ready photo, "
    "clean aesthetic, commercial product photography"
)

# ?? Prompts negativos ??????????????????????????????????????????????????????????
NEGATIVE_PROMPT = (
    "deformed body, extra limbs, disfigured, blurry, out of focus, "
    "different shirt design, different print, logo changed, altered graphic, "
    "dark background, colorful background, outdoor background, "
    "harsh shadows, overexposed, underexposed, watermark, text overlay, "
    "cartoon, illustration, painting, drawing, anime, 3d render"
)

# ?? Opciones de g?nero ?????????????????????????????????????????????????????????
GENDER_PROMPTS = {
    "mujer": "young woman, female model, feminine look",
    "hombre": "young man, male model, masculine look",
    "unisex": "androgynous model, unisex style",
    # aliases
    "femenino": "young woman, female model, feminine look",
    "masculino": "young man, male model, masculine look",
    "female": "young woman, female model, feminine look",
    "male": "young man, male model, masculine look",
    "woman": "young woman, female model, feminine look",
    "man": "young man, male model, masculine look",
}

# ?? Opciones de estilo ?????????????????????????????????????????????????????????
STYLE_PROMPTS = {
    "casual": "casual relaxed pose, everyday look, natural expression",
    "urbano": "urban streetwear style, edgy pose, confident look",
    "deportivo": "athletic sporty pose, dynamic stance, energetic",
    "elegante": "elegant pose, sophisticated look, refined style",
    "streetwear": "streetwear fashion, urban style, cool attitude",
    # aliases
    "sport": "athletic sporty pose, dynamic stance, energetic",
    "urban": "urban streetwear style, edgy pose, confident look",
}

# ?? Opciones de ambiente ???????????????????????????????????????????????????????
ENVIRONMENT_PROMPTS = {
    "interior": "indoor studio, clean white studio backdrop, controlled lighting",
    "exterior": "outdoor natural light, white seamless background, airy feel",
    "estudio": "professional photography studio, seamless white backdrop, softbox lighting",
    # default = studio
    "studio": "professional photography studio, seamless white backdrop, softbox lighting",
}

# ?? Opciones de iluminaci?n espec?fica ????????????????????????????????????????
LIGHTING_PROMPTS = {
    "suave": "soft diffused lighting, even illumination, no harsh shadows",
    "dramatica": "dramatic side lighting, strong contrast, editorial feel",
    "natural": "natural daylight look, soft shadows, warm tone",
    "brillante": "bright high-key lighting, crisp clean look, Instagram bright",
}

DEFAULT_GENDER = GENDER_PROMPTS["unisex"]
DEFAULT_STYLE = STYLE_PROMPTS["casual"]
DEFAULT_ENVIRONMENT = ENVIRONMENT_PROMPTS["estudio"]
DEFAULT_LIGHTING = LIGHTING_PROMPTS["suave"]


def parse_caption(caption: str) -> dict:
    """
    Parsea el caption del usuario y extrae par?metros de customizaci?n.
    Ejemplo: "mujer urbano exterior" ? {gender, style, environment}
    """
    words = caption.lower().split()
    result = {
        "gender": DEFAULT_GENDER,
        "style": DEFAULT_STYLE,
        "environment": DEFAULT_ENVIRONMENT,
        "lighting": DEFAULT_LIGHTING,
    }

    for word in words:
        if word in GENDER_PROMPTS:
            result["gender"] = GENDER_PROMPTS[word]
        elif word in STYLE_PROMPTS:
            result["style"] = STYLE_PROMPTS[word]
        elif word in ENVIRONMENT_PROMPTS:
            result["environment"] = ENVIRONMENT_PROMPTS[word]
        elif word in LIGHTING_PROMPTS:
            result["lighting"] = LIGHTING_PROMPTS[word]

    return result


def build_prompt(caption: str = "") -> str:
    """
    Construye el prompt completo para la generaci?n de imagen.
    Mantiene fidelidad al dise?o de la remera del mockup + estilo foto Instagram/web.
    
    Args:
        caption: Texto opcional del usuario (ej: "mujer urbano exterior")
    
    Returns:
        Prompt completo para enviar a la API
    """
    params = parse_caption(caption)

    prompt = (
        f"{params['gender']}, "
        f"{params['style']}, "
        f"{BASE_PROMPT}, "
        f"{params['environment']}, "
        f"{params['lighting']}, "
        "photorealistic, 8k quality, Canon EOS R5 style photo"
    )

    return prompt


def get_negative_prompt() -> str:
    """Retorna el prompt negativo est?ndar."""
    return NEGATIVE_PROMPT


# ?? Preview para debug ?????????????????????????????????????????????????????????
if __name__ == "__main__":
    test_cases = [
        "",
        "mujer",
        "hombre urbano",
        "mujer casual exterior",
        "unisex deportivo brillante",
    ]
    for case in test_cases:
        print(f"\nCaption: '{case}'")
        print(f"Prompt: {build_prompt(case)[:120]}...")
