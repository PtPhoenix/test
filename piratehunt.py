def get_coordinate(treasure, coordinate):
    print(Azara[treasure])
Azara = {
    "Amethyst Octopus": "1F",
    "Angry Monkey Figurine": "5B",
    "Antique Glass Fishnet Float": "3D",
    "Brass Spyglass": "4B",
    "Carved Wooden Elephant": "8C",
    "Crystal Crab": "6A",
    "Glass Starfish": "6D",
    "Model Ship in Large Bottle": "8A",
    "Pirate Flag": "7F",
    "Robot Parrot": "1C",
    "Scrimshawed Whale Tooth": "2A",
    "Silver Seahorse": "4E",
    "Vintage Pirate Hat": "7E"
}
get_coordinate("Amethyst Octopus", "1F")

def convert_coordinate(coordinate):
    result = tuple(coordinate)
    print(result)

convert_coordinate("1F")
