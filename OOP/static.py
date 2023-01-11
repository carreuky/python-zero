
#static does not act on class or instance ( no cls or self)
#organie code better

class Physics:
    # Write your code here

        @staticmethod
        def calculate_net_force(mass, acceleration):
            if mass < 0 or acceleration < 0:
                return 0.0
            return mass * acceleration

        @staticmethod
        def calculate_acceleration(mass, net_force):
            if mass <= 0 or net_force < 0:
                return 0.0
            return net_force / mass

        @staticmethod
        def calculate_mass(net_force, acceleration):
            if acceleration <= 0 or net_force < 0:
                return 0.0

            return acceleration / net_force

print(Physics.calculate_acceleration(2,4))