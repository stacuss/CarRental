class GarageTester:
    @staticmethod
    def getExample():
        # Create a truck object (color is black, no trailer)
        truck = Truck("black", has_trailer=False)

        # Create a garage object
        garage = Garage()

        # Park the truck in the garage
        garage.setVehicle(truck)

        # Print the garage's description
        print(garage)
