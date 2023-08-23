"""
The function is not returning the correct values. Can you figure out why?

Example (Input --> Output ):

3 --> "Earth"""

#Solution
def get_planet_name(id):
    switch_id = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus",
        8: "Neptune",
        }
    return switch_id.get(id, "Error")