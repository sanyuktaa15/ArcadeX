from flask import Flask, render_template
import subprocess
import os

app = Flask(__name__, static_folder='.', template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run/<game>')
def run_game(game):
    base_path = os.getcwd()
    
    game_paths = {
        "rain-dodge": os.path.join(base_path, "raindodge", "rain_dodge.py"),
        "space-invaders": os.path.join(base_path, "spaceinvaders", "space_invaders.py"),
        "galaxy-fighters": os.path.join(base_path, "galaxyfighters", "galaxy_fighters.py"),
        "car-racing": os.path.join(base_path, "carracing", "car_racing.py")
    }

    if game in game_paths:
        subprocess.Popen(["python", game_paths[game]])
        return f"<h2>Running {game}...</h2>"
    else:
        return "<h2>Game not found!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
