# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player_name, player_bio, player_location):
        self.player_name = player_name
        self.player_bio = player_bio
        self.player_location = player_location
    def __str__(self):
        return f"{self.player_name}\n {self.player_bio}\n {self.player_location}"