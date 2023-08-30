from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension 
import requests 
from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///capstone1"
app.config['SECRET_KEY'] = "PEEEPEEPOOPOO"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        dog_breed = request.form.get('dog_breed')
        
        # Fetch a random image from the specified breed collection
        response = requests.get(f'https://dog.ceo/api/breed/{dog_breed}/images/random/10')  # Fetch 3 images
        data = response.json()
        image_urls = data['message']
        
        return render_template('result.html', dog_breed=dog_breed, image_urls=image_urls)
        
    else:
        # Fetch the list of dog breeds
        breeds_url = "https://dog.ceo/api/breeds/list/all"
        breeds_response = requests.get(breeds_url)
        breeds_data = breeds_response.json()
        breeds = breeds_data['message']
        
        return render_template('home.html', breeds=breeds)


if __name__ == '__main__':
      app.run(debug=True)

