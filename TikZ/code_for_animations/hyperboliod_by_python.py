import math
import numpy as np
import subprocess

polar_angle = 60
azimuthal_angle = 30

def signed_distance(point, plane_point, normal_vector):
    return np.dot(point - plane_point, normal_vector) / np.linalg.norm(normal_vector)

def sphereX(polar: float, azimuthal: float) -> float:
    return math.cos(math.radians(polar)) * math.cos(math.radians(azimuthal))

def sphereY(polar: float, azimuthal: float) -> float:
    return math.cos(math.radians(polar)) * math.sin(math.radians(azimuthal))

def sphereZ(polar: float, azimuthal: float) -> float:
    return math.sin(math.radians(polar))

viewdirX = sphereX(90 - 60, -30)
viewdirY = sphereY(90 - 60, -30)
viewdirZ = sphereZ(90 - 60, -30)

the_normal_vector = np.array([viewdirX, viewdirY, viewdirZ])

def hyperbola(radius: float) -> float:
    return math.sqrt(radius**2 - 1)

def calculate_center(rectangle):
    return np.mean(rectangle, axis=0)

rectangles = []

# Generate rectangles
for radius in np.arange(1, 5, 0.2):
    for angle in range(0, 360, 10):
        angle_rad = math.radians(angle)
        angle_next_rad = math.radians(angle + 10)

        r_coords = [
            (radius * math.cos(angle_rad), radius * math.sin(angle_rad), hyperbola(radius)),
            (radius * math.cos(angle_next_rad), radius * math.sin(angle_next_rad), hyperbola(radius)),
            ((radius + 0.2) * math.cos(angle_next_rad), (radius + 0.2) * math.sin(angle_next_rad), hyperbola(radius + 0.2)),
            ((radius + 0.2) * math.cos(angle_rad), (radius + 0.2) * math.sin(angle_rad), hyperbola(radius + 0.2))
        ]

        rectangles.append(r_coords)

        # Duplicate the rectangle with negative z-values
        r_coords_negative = [
            (x, y, -z) for (x, y, z) in r_coords
        ]
        
        rectangles.append(r_coords_negative)

# Sort rectangles based on depth with respect to the normal vector
plane_point = np.array([0, 0, 0])  # Define a plane point
rectangles.sort(key=lambda rect: signed_distance(calculate_center(rect), plane_point, the_normal_vector))

# Prepare TeX document
preamble = f"""
\\documentclass[tikz, border=1cm]{{standalone}}
\\usepackage{{tikz-3dplot}}
\\begin{{document}}
\\tdplotsetmaincoords{{{polar_angle}}}{{{azimuthal_angle}}}
\\begin{{tikzpicture}}[tdplot_main_coords]
"""

postscript = f"""
\\end{{tikzpicture}}
\\end{{document}}
"""

with open("TeX_File.tex", "w") as TeX:
    TeX.write(preamble)
    for rectangle in rectangles:
        drawn_rectangle = f"""
\\fill[white] ({rectangle[0][0]},{rectangle[0][1]},{rectangle[0][2]}) --
({rectangle[1][0]},{rectangle[1][1]},{rectangle[1][2]}) --
({rectangle[2][0]},{rectangle[2][1]},{rectangle[2][2]}) --
({rectangle[3][0]},{rectangle[3][1]},{rectangle[3][2]}) -- cycle;
\\fill[opacity=0.5] ({rectangle[0][0]},{rectangle[0][1]},{rectangle[0][2]}) --
({rectangle[1][0]},{rectangle[1][1]},{rectangle[1][2]}) --
({rectangle[2][0]},{rectangle[2][1]},{rectangle[2][2]}) --
({rectangle[3][0]},{rectangle[3][1]},{rectangle[3][2]}) -- cycle;
\\draw ({rectangle[0][0]},{rectangle[0][1]},{rectangle[0][2]}) --
({rectangle[1][0]},{rectangle[1][1]},{rectangle[1][2]}) --
({rectangle[2][0]},{rectangle[2][1]},{rectangle[2][2]}) --
({rectangle[3][0]},{rectangle[3][1]},{rectangle[3][2]}) -- cycle;
"""
        TeX.write(drawn_rectangle)
    TeX.write(postscript)

subprocess.run(['lualatex', "TeX_File.tex"])
