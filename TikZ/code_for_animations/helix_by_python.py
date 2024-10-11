import math
import subprocess
import numpy as np

def signed_distance(point, plane_point, normal_vector):
    return np.dot(point - plane_point, normal_vector) / np.linalg.norm(normal_vector)

def sort_rectangles(rectangles, plane_point, normal_vector):
    # Calculate the center of each rectangle for sorting
    distances = []
    for rect in rectangles:
        # Average the coordinates of the rectangle vertices
        center = np.mean(rect, axis=0)
        distance = signed_distance(center, plane_point, normal_vector)
        distances.append((distance, rect))
    # Sort rectangles based on their signed distances
    return [rect for _, rect in sorted(distances)]

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

list_of_rectangles = []

for Vt in range(10, 720 + 1, 10):
    current_lastx = sphereX(90, Vt - 10) + 4 * math.cos(math.radians(Vt - 10))
    current_lasty = sphereY(90, Vt - 10) + 4 * math.sin(math.radians(Vt - 10))
    current_lastz = sphereZ(90, Vt - 10) + 5 * (Vt - 10) / 360

    for Vtt in range(90, 350 + 1, 10):
        Vxo = sphereX(Vtt, Vt) + 4 * math.cos(math.radians(Vt))
        Vyo = sphereY(Vtt, Vt) + 4 * math.sin(math.radians(Vt))
        Vzo = sphereZ(Vtt, Vt) + 5 * Vt / 360

        Vxt = sphereX(Vtt + 10, Vt) + 4 * math.cos(math.radians(Vt))
        Vyt = sphereY(Vtt + 10, Vt) + 4 * math.sin(math.radians(Vt))
        Vzt = sphereZ(Vtt + 10, Vt) + 5 * Vt / 360

        Vxth = sphereX(Vtt + 10, Vt - 10) + 4 * math.cos(math.radians(Vt - 10))
        Vyth = sphereY(Vtt + 10, Vt - 10) + 4 * math.sin(math.radians(Vt - 10))
        Vzth = sphereZ(Vtt + 10, Vt - 10) + 5 * (Vt - 10) / 360

        list_of_rectangles.append([
            (current_lastx, current_lasty, current_lastz),
            (Vxo, Vyo, Vzo),
            (Vxt, Vyt, Vzt),
            (Vxth, Vyth, Vzth)
        ])

        current_lastx = Vxth
        current_lasty = Vyth
        current_lastz = Vzth

# Sort rectangles based on their depth
plane_point = np.array([0, 0, 0])  # Define a plane point (can be adjusted)
sorted_rectangles = sort_rectangles(list_of_rectangles, plane_point, the_normal_vector)

# Write to TeX file
with open("TeX_file.tex", "w") as TeX:
    start = r"""
\documentclass[tikz, border=1cm]{standalone}
\usepackage{tikz-3dplot}
\begin{document}
\tdplotsetmaincoords{60}{30}
\begin{tikzpicture}[tdplot_main_coords]
"""
    end = r"""
\end{tikzpicture}
\end{document}
"""
    TeX.write(start)
    for rect in sorted_rectangles:
        # Generate the TeX command for each rectangle
        command = f"""
        \\fill[white] ({rect[0][0]},{rect[0][1]},{rect[0][2]}) -- ({rect[1][0]},{rect[1][1]},{rect[1][2]}) -- ({rect[2][0]},{rect[2][1]},{rect[2][2]}) -- ({rect[3][0]},{rect[3][1]},{rect[3][2]}) -- cycle;
        \\fill[opacity=0.5] ({rect[0][0]},{rect[0][1]},{rect[0][2]}) -- ({rect[1][0]},{rect[1][1]},{rect[1][2]}) -- ({rect[2][0]},{rect[2][1]},{rect[2][2]}) -- ({rect[3][0]},{rect[3][1]},{rect[3][2]}) -- cycle;
        """
        TeX.write(command)
    TeX.write(end)

subprocess.run(['lualatex', "TeX_file.tex"])
