from flask import Blueprint, request, render_template, Markup, Response

from data.characters import Character
from data.items import Item
from .database import db
from . import directory

results_shown = 5

gifts = Blueprint(
    'gifts',
    __name__
)


@gifts.route('/api/search')
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


@gifts.route('/')
def home():
    results = []
    if 'query' in request.args:
        query = request.args['query']
    else:
        query = 'rhea'
    if query:
        search_result = db.search(query)
        if search_result:
            for i in range(min(results_shown, len(search_result))):
                results.append(search_result[i][1])
        rendered = []
        for result in results:
            if isinstance(result, Character):
                rendered.append(Markup(render_template('gifts/character.html', character=result)))
            elif isinstance(result, Item):
                rendered.append(Markup(render_template('gifts/item.html', item=result)))
        results = rendered
    return render_template('gifts/index.html', query=query, results=results)
