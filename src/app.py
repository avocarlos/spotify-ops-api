from flask import Flask, render_template
from flask_graphql import GraphQLView

from schema import schema

app = Flask(__name__)

# To be removed
@app.route('/')
def home():
    return render_template('home.html')

graphql_view = GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True
)

app.add_url_rule('/graphql', view_func = graphql_view)
