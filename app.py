from flask import Flask, render_template, jsonify
from mission import Mission

app = Flask(__name__)

# Créer une instance de la mission
mission = Mission()

@app.route("/")
def hello_word():
    return render_template('index.html')

@app.route("/takeoff")
def takeoff():
    message = mission.drone.takeoff()  # Utilise la simulation
    return message

@app.route("/land")
def land():
    message = mission.drone.land()  # Utilise la simulation
    return message

@app.route("/start_mission")
def start_mission():
    mission.drone.connect()  # Connecte le drone sans le faire décoller
    return "Drone connectée et prêt pour la mission."

@app.route("/end_mission")
def end_mission():
    mission.end_mission()  # Utilise la simulation
    return "Mission terminée"

@app.route("/status")
def status():
    # Appel de la méthode get_status dans mission.py pour obtenir le statut du drone
    return mission.get_status()

@app.route("/telemetry")
def telemetry():
    # Appel de la méthode get_telemetry dans mission.py pour obtenir les données de télémétrie
    data = mission.get_telemetry()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
