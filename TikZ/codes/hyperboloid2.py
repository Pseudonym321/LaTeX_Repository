import math
import numpy as np
import subprocess
import Animation_Modules.animatetex as animatetex
animatetex.before_loop()
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

viewdirX = sphereX(90 - polar_angle, -azimuthal_angle)
viewdirY = sphereY(90 - polar_angle, -azimuthal_angle)
viewdirZ = sphereZ(90 - polar_angle, -azimuthal_angle)

the_normal_vector = np.array([viewdirX, viewdirY, viewdirZ])






for parameter in np.linspace(-2,2,12):
    def hyperbola(radius: float) -> float:
        return math.sqrt(radius**2 - (parameter) + 0.00001)

    def calculate_center(rectangle):
        return np.mean(rectangle, axis=0)

    rectangles = []
    if parameter > 0:
        # Generate rectangles
        for radius in np.arange(math.sqrt(parameter),10, 0.2):
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
    else:
        # Generate rectangles
        for radius in np.arange(0,10, 0.2):
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
    \\documentclass{{beamer}}
    \\beamertemplatenavigationsymbolsempty
    \\usepackage{{tikz,tikz-3dplot}}
    \\begin{{document}}
    \\begin{{frame}}
    \\centering
    \\tdplotsetmaincoords{{{polar_angle}}}{{{azimuthal_angle}}}
    \\begin{{tikzpicture}}[tdplot_main_coords,scale=0.333]
    \\clip[tdplot_screen_coords,scale=3] (-3.5,-2.5) rectangle (3.5,2.5);
    \\draw[white,tdplot_screen_coords,scale=3] (-3.5,-2.5) rectangle (3.5,2.5);
    """

    postscript = f"""
    \\end{{tikzpicture}}
    \\end{{frame}}
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

    animatetex.during_loop()

for parameter in np.linspace(2,-2,12):
    def hyperbola(radius: float) -> float:
        return math.sqrt(radius**2 - (parameter) + 0.00001)

    def calculate_center(rectangle):
        return np.mean(rectangle, axis=0)

    rectangles = []
    if parameter > 0:
        # Generate rectangles
        for radius in np.arange(math.sqrt(parameter),10, 0.2):
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
    else:
        # Generate rectangles
        for radius in np.arange(0,10, 0.2):
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
    \\documentclass{{beamer}}
    \\beamertemplatenavigationsymbolsempty
    \\usepackage{{tikz,tikz-3dplot}}
    \\begin{{document}}
    \\begin{{frame}}
    \\centering
    \\tdplotsetmaincoords{{{polar_angle}}}{{{azimuthal_angle}}}
    \\begin{{tikzpicture}}[tdplot_main_coords,scale=0.333]
    \\clip[tdplot_screen_coords,scale=3] (-3.5,-2.5) rectangle (3.5,2.5);
    \\draw[white,tdplot_screen_coords,scale=3] (-3.5,-2.5) rectangle (3.5,2.5);
    """

    postscript = f"""
    \\end{{tikzpicture}}
    \\end{{frame}}
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

    animatetex.during_loop()



animatetex.after_loop()
