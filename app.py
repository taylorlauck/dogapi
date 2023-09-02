from flask import Flask, request, render_template, url_for
import requests 
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///capstone1"
app.config['SECRET_KEY'] = "PEEEPEEPOOPOO"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_ECHO'] = True
debug = DebugToolbarExtension(app)

connect_db(app)

def get_dogs():
    url = "https://dog.ceo/api/breeds/list/all"
    response = requests.get(url)
    data = response.json()
    all_dogs = []
    
    for key, item in data['message'].items():
        if len(item) == 0:
            all_dogs.append(key)
        else:
            for i in item:
                all_dogs.append(i + " " + key)
    
    return all_dogs


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('home.html', name=name , breeds=get_dogs()) # Render the home template with the 'name' variable
        
    else:

     return render_template('enter_name.html')

@app.route("/home/<name>", methods=['GET', 'POST'])
def home_with_name(name):
    if request.method == 'POST':
        dog_breed = request.form.get('dog_breed')
        
        # Fetch a random image from the specified breed collection
        response = requests.get(f'https://dog.ceo/api/breed/{dog_breed}/images/random/10')  # Fetch 10 images
        data = response.json()
        image_urls = data['message']
        
        return render_template('result.html', name=name, dog_breed=dog_breed, image_urls=image_urls)
        
    else:
        # Fetch the list of dog breeds
        breeds_url = "https://dog.ceo/api/breeds/list/all"
        breeds_response = requests.get(breeds_url)
        breeds_data = breeds_response.json()
        breeds = breeds_data['message']
        
        return render_template('home.html', name=name, breeds=breeds)


if __name__ == '__main__':
    app.run(debug=True)
