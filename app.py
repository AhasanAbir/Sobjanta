# app.py

from flask import Flask, render_template, request
from sobjanta_search import search  # Import the search function

# Initialize Flask app
app = Flask(__name__)

# Define the route for the homepage
@app.route('/', methods=['GET', 'POST'])
def home():
    search_results = []
    if request.method == 'POST':
        query = request.form['query']  # Get the search query from the form
        search_results = search(query)  # Call the search function
    return render_template('index.html', results=search_results, query=query)

if __name__ == '__main__':
    app.run(debug=True)
