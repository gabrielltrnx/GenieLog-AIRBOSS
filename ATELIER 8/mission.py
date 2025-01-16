# mission.py
from drone import Tello

class Mission:
    def __init__(self):
        self.drone = Tello()

    def start_mission(self):
        if self.drone.connect() == "Simulation: Connected to Tello drone":
            print("Mission started")
            self.drone.takeoff()
            # Ajouter ici d'autres étapes de la mission comme la détection, le suivi, etc.
        else:
            print("Failed to start mission")

    def end_mission(self):
        print("Ending mission")
        self.drone.land()
        self.drone.disconnect()

    def get_status(self):
        if self.drone.is_connected:
            if self.drone.is_flying:
                return "Drone: En vol"
            else:
                return "Drone: Au sol"
        else:
            return "Drone: Non connecté"

    def get_telemetry(self):
        if self.drone.is_flying:
            data = {
                'hauteur': 100,    # en mètres
                'distance': 500,   # en mètres
                'vitesse': 20,     # en m/s
                'duree': '00:15:00',
                'autonomie': 75    # en pourcentage
            }
        else:
            data = {
                'hauteur': 0,      # en mètres
                'distance': 0,     # en mètres
                'vitesse': 0,      # en m/s
                'duree': '00:00:00',
                'autonomie': 0     # en pourcentage
            }

    