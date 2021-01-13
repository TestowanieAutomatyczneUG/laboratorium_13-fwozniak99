class Planets:
    def game(self, x, planet):
        if planet == "Ziemia":
            age = 31557600
        elif planet == "Merkury":
            age = 31557600*0.2408467
        elif planet == "Wenus":
            age = 31557600 * 0.61519726
        elif planet == "Mars":
            age = 31557600 * 1.8808158
        elif planet == "Jowisz":
            age = 31557600 * 11.862615
        elif planet == "Saturn":
            age = 31557600 * 29.447498
        elif planet == "Uran":
            age = 31557600 * 84.016846
        elif planet == "Neptun":
            age = 31557600 * 164.79132
        else:
            raise Exception("Error in Planets")

        return round(x/age, 2)
