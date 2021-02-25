class Street:
    def __init__(self, raw_values):
        self.start = int(raw_values[0])
        self.stop = int(raw_values[1])
        self.name = raw_values[2]
        self.length = int(raw_values[3])
        self.passes = 0


class Cars:
    def __init__(self, raw_values):
        self.path_length = int(raw_values[0])
        self.streets = raw_values[1:]


class Inters:
    def __init__(self, idd):
        self.id = idd
        self.in_streets = []
        self.out_streets = []


class Simulation:
    def __init__(self, raw_values):
        self.duration = int(raw_values[0])
        self.inters_num = int(raw_values[1])
        self.streets_num = int(raw_values[2])
        self.cars_num = int(raw_values[3])
        self.bonus_points = int(raw_values[4])
        self.streets = []

        self.inters = {}
        for i in range(self.inters_num):
            self.inters[i] = Inters(i)
        self.cars = []

    def init_inters(self):
        for street in self.streets:
            self.inters[street.start].out_streets.append(street)
            self.inters[street.stop].in_streets.append(street)

