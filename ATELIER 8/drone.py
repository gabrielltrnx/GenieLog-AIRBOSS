# drone.py
import time

class Tello:
    def __init__(self):
        self.is_connected = False
        self.is_flying = False  # Ajouter un attribut pour simuler l'état de vol

    def connect(self):
        """Simule la connexion au drone."""
        self.is_connected = True
        print("Simulation: Connexion au drone réussie")
        return "Simulation: Connected to Tello drone"

    def send_command(self, command):
        """Simule l'envoi de commandes au drone."""
        if self.is_connected:
            print(f"Simulation: Commande '{command}' envoyée")
            return f"Simulation: Commande '{command}' envoyée"
        else:
            return "Error: Not connected to the drone"

    def takeoff(self):
        """Simule le décollage du drone."""
        if self.is_connected:
            if not self.is_flying:
                self.is_flying = True
                print("Simulation: Le drone décolle")
                return "Simulation: Drone took off"
            else:
                return "Simulation: Le drone est déjà en vol"
        else:
            return "Error: Not connected to the drone"

    def land(self):
        """Simule l'atterrissage du drone."""
        if self.is_connected:
            if self.is_flying:
                self.is_flying = False
                print("Simulation: Le drone atterrit")
                return "Simulation: Drone landed"
            else:
                return "Simulation: Le drone est déjà au sol"
        else:
            return "Error: Not connected to the drone"

    def disconnect(self):
        """Simule la déconnexion du drone."""
        if self.is_connected:
            self.is_connected = False
            print("Simulation: Déconnexion du drone")
            return "Simulation: Disconnected from drone"
        else:
            return "Error: No connection to disconnect"
