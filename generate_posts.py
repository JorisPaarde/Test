import json
import os
from datetime import datetime

def create_html_content(post):
    date_obj = datetime.strptime(post['date'], '%Y-%m-%d')
    formatted_date = date_obj.strftime('%-d %B %Y')  # Dutch date format

    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post['title']}</title>
    <link rel="stylesheet" href="../styles/main.css">
</head>
<body>
    <header>
        <nav>
            <a href="../index.html">← Terug naar home</a>
        </nav>
    </header>

    <main>
        <article>
            <h1>{post['title']}</h1>
            <time datetime="{post['date']}">{formatted_date}</time>

            <section class="article-content">
                {generate_content(post)}
            </section>
        </article>
    </main>

    <footer>
        <p>&copy; 2024 JP Web Creation. Alle rechten voorbehouden.</p>
    </footer>
</body>
</html>'''

def generate_content(post):
    # Dictionary met content templates voor elk artikel
    content_templates = {
        'css-grid-gids': '''
                <h2>Inleiding tot CSS Grid</h2>
                <p>CSS Grid heeft de manier waarop we layouts bouwen revolutionair veranderd. In deze gids duiken we diep in de mogelijkheden van CSS Grid en hoe je het effectief kunt gebruiken in je projecten.</p>

                <h2>Basis Concepten</h2>
                <p>Om CSS Grid goed te begrijpen, moet je eerst vertrouwd raken met de belangrijkste concepten:</p>
                <ul>
                    <li>Grid Container en Grid Items</li>
                    <li>Grid Lines en Grid Tracks</li>
                    <li>Grid Areas en Grid Cells</li>
                </ul>

                <h2>Praktische Voorbeelden</h2>
                <p>Laten we kijken naar enkele praktische voorbeelden van hoe professionele ontwikkelaars CSS Grid gebruiken:</p>
                <pre><code>
.grid-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}
                </code></pre>
        ''',
        'javascript-optimalisatie': '''
                <h2>JavaScript Performance Optimalisatie</h2>
                <p>Prestatie-optimalisatie is cruciaal voor moderne webapplicaties. In dit artikel behandelen we de belangrijkste technieken om je JavaScript code te optimaliseren.</p>

                <h2>Memory Management</h2>
                <p>Effectief geheugenbeheer is essentieel voor snelle JavaScript applicaties. We bespreken:</p>
                <ul>
                    <li>Memory Leaks voorkomen</li>
                    <li>Garbage Collection optimalisatie</li>
                    <li>Efficiënt gebruik van data structuren</li>
                </ul>

                <h2>Code Optimalisatie</h2>
                <p>Leer hoe je je code kunt optimaliseren voor betere prestaties:</p>
                <pre><code>
// Geoptimaliseerd
const cachedResults = new Map();

function getExpensiveResult(input) {
    if (cachedResults.has(input)) {
        return cachedResults.get(input);
    }
    // Bereken resultaat
    return result;
}
                </code></pre>
        ''',
        # Voeg hier templates toe voor andere artikelen
    }
    
    # Haal de template ID uit de URL
    template_id = post['url'].replace('.html', '').split('-', 3)[-1]
    
    # Return default content als er geen specifieke template is
    return content_templates.get(template_id, '''
                <h2>Inleiding</h2>
                <p>Dit artikel is momenteel in ontwikkeling. Kom binnenkort terug voor de volledige inhoud.</p>

                <h2>Wat kun je verwachten?</h2>
                <p>We zullen diep ingaan op het onderwerp en praktische voorbeelden delen.</p>

                <h2>Wordt vervolgd...</h2>
                <p>We werken hard aan het voltooien van dit artikel.</p>
    ''')

def main():
    # Lees het JSON-bestand
    with open('posts/posts.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Maak de posts directory als die nog niet bestaat
    os.makedirs('posts', exist_ok=True)
    
    # Genereer HTML-bestanden voor elke post
    for post in data['posts']:
        file_path = os.path.join('posts', post['url'])
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(create_html_content(post))
        print(f"Generated: {file_path}")

if __name__ == "__main__":
    main() 