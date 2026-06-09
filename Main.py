from solid2 import *

def generate_gear(m, z, dist):
    blank = cylinder(r=m*(z+2)/2, h=10)
    tool = cube([10, 5, 12]) # À remplacer par la forme de dent

    # Logique de soustraction en Python
    for a in range(-20, 21):
        blank -= rotate(a)(translate([dist, 0, 0])(tool))

    blank.save_as_scad("gear.scad")

generate_gear(2,25, 30)

