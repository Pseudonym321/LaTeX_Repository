import math
import subprocess
import numpy as np

def signed_distance(point, plane_point, normal_vector):
    return np.dot(point - plane_point, normal_vector) / np.linalg.norm(normal_vector)

def sort_shapes(shapes, plane_point, normal_vector):
    distances = []
    for shape in shapes:
        if shape['type'] == 'rectangle':
            # Average the coordinates of the rectangle vertices
            center = np.mean(shape['vertices'], axis=0)
        elif shape['type'] == 'line':
            # Average the coordinates of the line endpoints
            center = np.mean(shape['endpoints'], axis=0)
        distance = signed_distance(center, plane_point, normal_vector)
        distances.append((distance, shape))
    return [shape for _, shape in sorted(distances)]

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

shapes = []

for Vt in range(10, 720 + 1, 10):
    current_lastx = sphereX(90, Vt - 10) + 4 * math.cos(math.radians(Vt - 10))
    current_lasty = sphereY(90, Vt - 10) + 4 * math.sin(math.radians(Vt - 10))
    current_lastz = sphereZ(90, Vt - 10) + 5 * (Vt - 10) / 360

    line_lastx = 4 * math.cos(math.radians(Vt - 10))
    line_lasty = 4 * math.sin(math.radians(Vt - 10))
    line_lastz = 5 * (Vt - 10) / 360

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

        line_nextx = 4 * math.cos(math.radians(Vt))
        line_nexty = 4 * math.sin(math.radians(Vt))
        line_nextz = 5 * Vt / 360

        # Add rectangle to shapes
        shapes.append({
            'type': 'rectangle',
            'vertices': [
                (current_lastx, current_lasty, current_lastz),
                (Vxo, Vyo, Vzo),
                (Vxt, Vyt, Vzt),
                (Vxth, Vyth, Vzth)
            ]
        })

        # Add line to shapes
        shapes.append({
            'type': 'line',
            'endpoints': [
                (line_lastx, line_lasty, line_lastz),
                (line_nextx, line_nexty, line_nextz)
            ]
        })

        current_lastx = Vxth
        current_lasty = Vyth
        current_lastz = Vzth

        line_lastx = line_nextx
        line_lasty = line_nexty
        line_lastz = line_nextz

# Sort shapes based on their depth
plane_point = np.array([0, 0, 0])  # Define a plane point (can be adjusted)
sorted_shapes = sort_shapes(shapes, plane_point, the_normal_vector)

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
    for shape in sorted_shapes:
        if shape['type'] == 'rectangle':
            rect = shape['vertices']
            command = f"""
            \\fill[white] ({rect[0][0]},{rect[0][1]},{rect[0][2]}) -- ({rect[1][0]},{rect[1][1]},{rect[1][2]}) -- ({rect[2][0]},{rect[2][1]},{rect[2][2]}) -- ({rect[3][0]},{rect[3][1]},{rect[3][2]}) -- cycle;
            \\fill[opacity=0.5] ({rect[0][0]},{rect[0][1]},{rect[0][2]}) -- ({rect[1][0]},{rect[1][1]},{rect[1][2]}) -- ({rect[2][0]},{rect[2][1]},{rect[2][2]}) -- ({rect[3][0]},{rect[3][1]},{rect[3][2]}) -- cycle;
            \\draw ({rect[0][0]},{rect[0][1]},{rect[0][2]}) -- ({rect[1][0]},{rect[1][1]},{rect[1][2]}) -- ({rect[2][0]},{rect[2][1]},{rect[2][2]}) -- ({rect[3][0]},{rect[3][1]},{rect[3][2]}) -- cycle;
            """
            TeX.write(command)
        elif shape['type'] == 'line':
            line = shape['endpoints']
            command = f"""
            \\draw[thick,red] ({line[0][0]},{line[0][1]},{line[0][2]}) -- ({line[1][0]},{line[1][1]},{line[1][2]});
            """
            TeX.write(command)
    TeX.write(end)

subprocess.run(['lualatex', "TeX_file.tex"])
