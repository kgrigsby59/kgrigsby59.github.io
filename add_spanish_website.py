#!/usr/bin/env python3
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
EN = ROOT / "index.html"
RU = ROOT / "ru" / "index.html"
ES_DIR = ROOT / "es"
ES = ES_DIR / "index.html"

for path in (EN, RU):
    if not path.exists():
        sys.exit(f"Missing required file: {path}")

english = EN.read_text(encoding="utf-8")
russian = RU.read_text(encoding="utf-8")

# Add Spanish SEO and navigation links to the English page.
if 'hreflang="es"' not in english:
    english = english.replace(
        '<link rel="alternate" hreflang="ru" href="https://www.quarterminder.com/ru/">',
        '<link rel="alternate" hreflang="ru" href="https://www.quarterminder.com/ru/">\n'
        '  <link rel="alternate" hreflang="es" href="https://www.quarterminder.com/es/">'
    )

if '<a href="es/" lang="es">Español</a>' not in english:
    english = english.replace(
        '<a href="ru/" lang="ru">Русский</a>',
        '<a href="ru/" lang="ru">Русский</a>\n'
        '      <a href="es/" lang="es">Español</a>'
    )

EN.write_text(english, encoding="utf-8")

# Add Spanish SEO and navigation links to the Russian page.
if 'hreflang="es"' not in russian:
    russian = russian.replace(
        '<link rel="alternate" hreflang="ru" href="https://www.quarterminder.com/ru/">',
        '<link rel="alternate" hreflang="ru" href="https://www.quarterminder.com/ru/">\n'
        '  <link rel="alternate" hreflang="es" href="https://www.quarterminder.com/es/">'
    )

if '<a href="../es/" lang="es">Español</a>' not in russian:
    russian = russian.replace(
        '<a href="../" lang="en">English</a>',
        '<a href="../" lang="en">English</a>\n'
        '      <a href="../es/" lang="es">Español</a>'
    )

RU.write_text(russian, encoding="utf-8")

# Build the Spanish page from the English page so layout and asset references stay identical.
spanish = english

replacements = {
    '<html lang="en">': '<html lang="es">',
    '<title>QuarterMinder - Track Your U.S. Quarter Collection</title>':
        '<title>QuarterMinder - Controla tu colección de monedas de 25 centavos de EE. UU.</title>',
    '<meta name="description" content="QuarterMinder for iPhone and iPad helps collectors track U.S. quarter programs, mint marks, notes, images, and collection progress.">':
        '<meta name="description" content="QuarterMinder para iPhone y iPad ayuda a organizar colecciones de monedas de 25 centavos de EE. UU., marcas de ceca, notas, imágenes y progreso.">',
    '<link rel="canonical" href="https://www.quarterminder.com/">':
        '<link rel="canonical" href="https://www.quarterminder.com/es/">',
    '<meta property="og:locale" content="en_US">':
        '<meta property="og:locale" content="es_US">',
    '<meta property="og:description" content="A focused iPhone and iPad app for tracking U.S. quarter collections.">':
        '<meta property="og:description" content="Una app para iPhone y iPad diseñada para organizar colecciones de monedas de 25 centavos de EE. UU.">',
    '<link rel="icon" type="image/x-icon" href="./favicon.ico">':
        '<link rel="icon" type="image/x-icon" href="../favicon.ico">',
    '<link rel="stylesheet" href="assets/styles.css">':
        '<link rel="stylesheet" href="../assets/styles.css">',
    'aria-label="Primary navigation"': 'aria-label="Navegación principal"',
    '<a class="brand" href="./" aria-label="QuarterMinder home">':
        '<a class="brand" href="./" aria-label="Página principal de QuarterMinder">',
    'src="assets/images/app-icon.jpg"': 'src="../assets/images/app-icon.jpg"',
    '<a href="#features">Features</a>': '<a href="#features">Funciones</a>',
    '<a href="#screenshots">Screenshots</a>': '<a href="#screenshots">Capturas</a>',
    '<a href="ru/" lang="ru">Русский</a>': '<a href="../ru/" lang="ru">Русский</a>',
    '<a href="es/" lang="es">Español</a>': '<a href="../" lang="en">English</a>',
    'src="static/templates/template4/images/badgeappstore.png"':
        'src="../static/templates/template4/images/badgeappstore.png"',
    'src="assets/images/iphone-collections.webp"':
        'src="../assets/images/iphone-collections.webp"',
    'src="assets/images/iphone-american-women.webp"':
        'src="../assets/images/iphone-american-women.webp"',
    'src="assets/images/iphone-detail.webp"':
        'src="../assets/images/iphone-detail.webp"',
    'src="assets/images/ipad-detail.webp"':
        'src="../assets/images/ipad-detail.webp"',
    'alt="QuarterMinder app icon"': 'alt="Ícono de la app QuarterMinder"',
    '<p class="kicker">For iPhone and iPad</p>':
        '<p class="kicker">Para iPhone y iPad</p>',
    'Keep track of your U.S. quarter collection with mint marks, notes, images, release details, and progress across every supported quarter program.':
        'Lleva el control de tu colección de monedas de 25 centavos de EE. UU. con marcas de ceca, notas, imágenes, detalles de emisión y progreso en cada programa compatible.',
    'aria-label="Download QuarterMinder on the App Store"':
        'aria-label="Descargar QuarterMinder en el App Store"',
    'alt="Download on the App Store"': 'alt="Descargar en el App Store"',
    'No account required. Your collection stays on your device.':
        'No necesitas una cuenta. Tu colección permanece en tu dispositivo.',
    'aria-label="QuarterMinder app preview"':
        'aria-label="Vista previa de la app QuarterMinder"',
    'alt="QuarterMinder collection tracking screen"':
        'alt="Pantalla de seguimiento de colecciones en QuarterMinder"',
    'alt="QuarterMinder quarter program screen"':
        'alt="Pantalla de un programa de monedas en QuarterMinder"',
    'alt="QuarterMinder quarter detail screen"':
        'alt="Pantalla de detalles de una moneda en QuarterMinder"',
    'Built for quarter collectors.':
        'Creada para coleccionistas de monedas de 25 centavos.',
    'QuarterMinder keeps the checklist practical: what you have, what you still need, and the details that make each coin easier to identify.':
        'QuarterMinder mantiene una lista práctica: lo que ya tienes, lo que todavía te falta y los detalles que facilitan identificar cada moneda.',
    'Track mint marks': 'Controla las marcas de ceca',
    'Follow Denver and Philadelphia mint progress separately so your collection status stays precise.':
        'Sigue por separado el progreso de las monedas de Denver y Filadelfia para mantener un estado preciso de tu colección.',
    'Multiple collections': 'Varias colecciones',
    'Create separate collections for different albums, family members, folders, or collecting goals.':
        'Crea colecciones separadas para distintos álbumes, familiares, carpetas u objetivos.',
    'Coin details': 'Detalles de cada moneda',
    'Use large coin images, release information, map links, and U.S. Mint links while you collect.':
        'Consulta imágenes grandes, información de emisión, enlaces a mapas y enlaces a la Casa de Moneda de EE. UU.',
    'Notes for each coin': 'Notas para cada moneda',
    'Add notes to individual coins for condition, source, album location, or anything else worth remembering.':
        'Añade notas sobre el estado, procedencia, ubicación en el álbum o cualquier otro detalle que quieras recordar.',
    'Share and export': 'Comparte y exporta',
    'Export collection information to Messages, Mail, Notes, and installed social media apps.':
        'Exporta la información de tu colección a Mensajes, Mail, Notas y las apps de redes sociales instaladas.',
    'Accessible by design': 'Accesible por diseño',
    'Dynamic Type support helps QuarterMinder stay readable with your preferred text size.':
        'La compatibilidad con Dynamic Type mantiene QuarterMinder legible con el tamaño de texto que prefieras.',
    'Current quarter programs.': 'Programas actuales.',
    'QuarterMinder is updated for the modern U.S. quarter series, including newer programs beyond the original State Quarters.':
        'QuarterMinder incluye las series modernas de monedas de 25 centavos de EE. UU., incluidos programas posteriores a la serie original de los estados.',
    'aria-label="Supported quarter programs"':
        'aria-label="Programas compatibles de monedas de 25 centavos"',
    'A quick, visual checklist.': 'Una lista rápida y visual.',
    'See collection progress at a glance, then open each quarter for larger images and more detail.':
        'Consulta el progreso de un vistazo y abre cada moneda para ver imágenes más grandes y más detalles.',
    '<p class="showcase-label">Collections</p>':
        '<p class="showcase-label">Colecciones</p>',
    'Know what you have and what you still need.':
        'Sabe lo que tienes y lo que todavía te falta.',
    'Separate collections make it easy to track albums, folders, family collections, or different collecting goals without mixing everything together.':
        'Las colecciones separadas facilitan el seguimiento de álbumes, carpetas, colecciones familiares u objetivos distintos sin mezclarlo todo.',
    'alt="QuarterMinder collections overview"':
        'alt="Vista general de colecciones en QuarterMinder"',
    '<p class="showcase-label">Programs</p>':
        '<p class="showcase-label">Programas</p>',
    'Move through each quarter series with less guesswork.':
        'Recorre cada serie con menos dudas.',
    'Browse supported U.S. quarter programs, track mint progress, and keep the checklist focused on the coins you actually collect.':
        'Explora los programas compatibles, controla el progreso por ceca y mantén la lista enfocada en las monedas que realmente coleccionas.',
    '<p class="showcase-label">Details</p>':
        '<p class="showcase-label">Detalles</p>',
    'Open a coin for the information that matters.':
        'Abre una moneda para ver la información importante.',
    'Each quarter can include larger artwork, release details, mint tracking, notes, and links for deeper reference.':
        'Cada moneda puede incluir imágenes ampliadas, detalles de emisión, seguimiento por ceca, notas y enlaces de referencia.',
    'Use the larger screen when you want more context.':
        'Usa la pantalla grande cuando quieras más contexto.',
    'On iPad, coin details have room for images, release information, notes, and reference links without feeling crowded.':
        'En el iPad hay espacio para imágenes, información de emisión, notas y enlaces de referencia sin que la pantalla se sienta saturada.',
    'alt="QuarterMinder detail screen on iPad"':
        'alt="Pantalla de detalles de QuarterMinder en el iPad"',
    'Ready for your next roll of quarters?':
        '¿Listo para tu próximo rollo de monedas?',
    'Download QuarterMinder from the App Store and keep your collection organized.':
        'Descarga QuarterMinder en el App Store y mantén tu colección organizada.',
    '>Support</a>': '>Soporte</a>',
}

for old, new in replacements.items():
    if old not in spanish:
        print(f"Warning: text not found for replacement: {old}")
    spanish = spanish.replace(old, new)

ES_DIR.mkdir(exist_ok=True)
ES.write_text(spanish, encoding="utf-8")

print("Updated:")
print(f"  {EN}")
print(f"  {RU}")
print(f"  {ES}")
print()
print("Next:")
print("  git add index.html ru/index.html es/index.html")
print('  git commit -m "Add Spanish QuarterMinder website"')
print("  git push")
