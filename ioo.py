#!/usr/env/python

from pathlib import Path
from data_model import Street, Cars, Simulation, Inters


def read_input(input_path):
    with open(input_path, 'r') as file:
        line = file.readline()
        values = line.split()

        sim = Simulation(values)

        for i in range(sim.streets_num):
            line = file.readline()
            line = line.split()
            sim.streets.append(Street(line))


        for i in range(sim.cars_num):
            line = file.readline()
            line = line.split()
            sim.cars.append(Cars(line))

        sim.init_inters()

    return sim


def write_result(output_path, sim):
    with open(output_path, "w") as file:
        file.write("{}\n".format(sim.inters_num))

        for _, inters in sim.inters.items():
            file.write("{}\n".format(inters.id))
            file.write("{}\n".format(len(inters.in_streets)))
            for street in inters.in_streets:
                file.write("{} {}\n".format(street.name, 1))
