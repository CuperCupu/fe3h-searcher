import os

from flask import Flask, request, render_template, Response, Markup

from data.characters import Character
from data.items import Item
from .database import Database

db = Database(os.environ.get('DATA_SOURCE', 'data.json'))

directory = os.path.split(__file__)[0]

results_shown = 5

app = Flask(
    'Fire Emblem 3 Houses',
    static_url_path='/static',
    template_folder=os.path.join(directory, 'web/templates'),
    static_folder=os.path.join(directory, 'web/static'),
)


@app.route('/api/search')
def search():
    if 'query' in request.args:
        query = request.args['query']
        if not query:
            return Response(status=400)
        result = db.search(request.args['query'])
        if result:
            i = result[0][1]
            return {'type': i.__class__.__name__, **i.to_native()}
        else:
            return Response(status=404)
    return Response(status=400)


@app.route('/')
def home():
    results = []
    if 'query' in request.args:
        query = request.args['query']
    else:
        query = 'rhea'
    if query:
        search_result = db.search(request.args['query'])
        if search_result:
            for i in range(min(results_shown, len(search_result))):
                results.append(search_result[i][1])
        rendered = []
        for result in results:
            if isinstance(result, Character):
                rendered.append(Markup(render_template('character.html', character=result)))
            elif isinstance(result, Item):
                rendered.append(Markup(render_template('item.html', item=result)))
        results = rendered
    return render_template('home.html', query=query, results=results)


def main():
    app.jinja_env.cache = None
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.run(host='0.0.0.0', port='9090')
