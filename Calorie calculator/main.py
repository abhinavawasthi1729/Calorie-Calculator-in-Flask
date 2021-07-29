from flask.views import MethodView
from flask import Flask, render_template, request
from calorie import Calorie

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')
    
class CalorieFormPage(MethodView):
    def get(self):
        return render_template('calorie_form_page.html')
    
    def post(self):
        weight = request.form.get('weight')
        height = request.form.get('height')
        age = request.form.get('age')
        city = request.form.get('city')

        
        calorie = Calorie(float(weight), float(height), float(age))
        temperature = calorie.temperature(city)
        # temperature = 300

        value = calorie.calculate(float(temperature))
        result = True
        return render_template('calorie_form_page.html',result=result, value=value)

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calorie', view_func=CalorieFormPage.as_view('calorie_form_page'))
app.run(debug=True)