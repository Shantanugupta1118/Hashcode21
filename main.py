from pathlib import Path
from data_model import Street, Cars, Simulation, Inters
from ioo import read_input, write_result


#def process(sim):
#    streets = {}
#    for car in sim.cars:
#        for strt in car.streets:
#            if strt not in streets:
#                streets[strt] = 0;
#
#            streets[strt] += 1






sim = read_input(Path('in/a.txt'))
write_result(Path('out/a_out.txt'), sim)

sim = read_input(Path('in/b.txt'))
write_result(Path('out/b_out.txt'), sim)

sim = read_input(Path('in/c.txt'))
write_result(Path('out/c_out.txt'), sim)

sim = read_input(Path('in/d.txt'))
write_result(Path('out/d_out.txt'), sim)

sim = read_input(Path('in/e.txt'))
write_result(Path('out/e_out.txt'), sim)

sim = read_input(Path('in/f.txt'))
write_result(Path('out/f_out.txt'), sim)
