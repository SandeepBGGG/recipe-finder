"""Recipe Finder web interface; original matching logic lives in recipes.py."""
from flask import Flask, render_template, request
from recipes import RECIPES, compare

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 32 * 1024

@app.route('/', methods=['GET', 'POST'])
def index():
    query = request.form.get('ingredients', '') if request.method == 'POST' else ''
    ingredients = [part.strip() for part in query.split(',') if part.strip()]
    error = None
    results = None
    if request.method == 'POST':
        if not ingredients:
            error = 'Enter at least one ingredient to begin.'
        elif len(query) > 5000:
            error = 'Please keep your ingredient list under 5,000 characters.'
        else:
            results = []
            for match in compare(ingredients):
                # Do not send locked instructions to the browser.
                result = dict(match)
                if result['missing']:
                    result.pop('instructions', None)
                results.append(result)
    return render_template('index.html', query=query, results=results, error=error,
                           recipe_count=len(RECIPES),
                           ready=sum(not r['missing'] for r in results or []))

@app.errorhandler(413)
def too_large(error):
    return 'Ingredient list too large. Return to the homepage and use a shorter list.', 413

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
