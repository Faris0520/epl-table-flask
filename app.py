from flask import Flask, render_template
import requests

request = requests
app = Flask(__name__)

@app.route('/')
def index():
    respon = request.get('https://football-standings-api.vercel.app/leagues/eng.1/standings?season=2024&sort=asc')
    data = respon.json()
    standings = data['data']['standings']
    return render_template('index.html', standings=standings)

if __name__ == '__main__':
    app.run(debug=True)