from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/run/<game>')
def run_game(game):
    game_paths = {
        "car": "carracing/car_racing.py",
        "rain": "raindodge/rain_dodge.py",
        "galaxy": "galaxyfighters/galaxy_fighters.py",
        "space": "spaceinvaders/space_invaders.py"
    }

    if game in game_paths:
        subprocess.Popen(["python", game_paths[game]])
        return f"✅ Launched {game_paths[game]}"
    else:
        return "❌ Game not found", 404

if __name__ == '__main__':
    app.run(debug=True)
