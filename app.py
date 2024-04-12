""" Application vraiment extrèmement simpliste qui devrait être très améliorée mais qui va me permettre de tester la containerization et le déploiement sur Azure. 

A ajouter :
- drop down pour les variables catégorielles, 
- valeur par défaut adaptée (pas 0 mais la moyenne par exemple)
- bouton de reset pour refairer une prédiction
- UI de l'interface.
"""


from flask import Flask, request, render_template, jsonify
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    # Default values for form, initialized to zero or appropriate category
    default_data = {
        'num_critic_for_reviews': 0, 'duration': 0, 'gross': 0, 'num_voted_users': 0,
        'cast_total_fb_likes': 0, 'num_user_for_reviews': 0, 'budget': 0,
        'title_year': 0, 'Action': 0, 'Adventure': 0, 'Animation': 0,
        'Biography': 0, 'Comedy': 0, 'Crime': 0, 'Documentary': 0, 'Drama': 0,
        'Family': 0, 'Fantasy': 0, 'Film-Noir': 0, 'Game-Show': 0, 'History': 0,
        'Horror': 0, 'Music': 0, 'Musical': 0, 'Mystery': 0, 'News': 0,
        'Reality-TV': 0, 'Romance': 0, 'Sci-Fi': 0, 'Short': 0, 'Sport': 0,
        'Thriller': 0, 'War': 0, 'Western': 0, 'Europe': 0, 'North America': 0,
        'Other countries': 0, 'English': 0, 'Other language': 0
    }
    return render_template('index.html', data=default_data)


@app.route('/predict', methods=['POST'])
def predict():
    data = {key: float(request.form.get(key, 0)) for key in request.form}
    features = list(data.values())
    prediction = model.predict([features])
    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text=f'Predicted IMDB Score: {output}', data=data)


@app.route('/api/predict', methods=['POST'])
def api_predict():
    data = request.get_json()
    features = [float(data.get(key, 0)) for key in data]
    prediction = model.predict([features])
    output = round(prediction[0], 2)
    return jsonify({'prediction': output})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
