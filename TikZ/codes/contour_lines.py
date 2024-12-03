import numpy as np
import matplotlib.pyplot as plt
import Animation_Modules.animatetex as animatetex


animatetex.before_loop()
for Vi in range(0,12):
    polar_angle = 60
    azimuthal_angle = 130
    highlight_level = Vi  # Change this value to select which contour level to draw in red (0-based index)
    num_samples = 10  # Change this value to set the number of samples for the red line and rectangles

    # Define the function
    def my_function(x, y):
        return (np.exp(-((x - 2 * np.cos(0))**2 + (y - 2 * np.sin(0))**2)) +
                2 * np.exp(-((x - 2 * np.cos(120 * np.pi / 180))**2 + (y - 2 * np.sin(120 * np.pi / 180))**2)) +
                3 * np.exp(-((x - 2 * np.cos(240 * np.pi / 180))**2 + (y - 2 * np.sin(240 * np.pi / 180))**2)))

    # Create a grid of points
    x_vals = np.linspace(-5, 5, 1000)
    y_vals = np.linspace(-5, 5, 1000)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Evaluate the function on the grid
    Z = my_function(X, Y)

    # Set contour levels
    contour_levels = np.linspace(0.1, 2.9, 12)

    # Initialize a list to store contour coordinates
    contour_coordinates = []
    highlight_contours = []

    # Define a distance threshold
    distance_threshold = 0.1

    # Plot contours and collect coordinates
    for level_index, level in enumerate(contour_levels):
        contours = plt.contour(X, Y, Z, levels=[level], colors='black')
        for collection in contours.collections:
            for path in collection.get_paths():
                vertices = path.vertices
                if len(vertices) > 1:
                    filtered_coords = [vertices[0]]
                    for i in range(1, len(vertices)):
                        distance = np.linalg.norm(vertices[i] - vertices[i-1])
                        if distance <= distance_threshold:
                            filtered_coords.append(vertices[i])
                        else:
                            if len(filtered_coords) > 1:
                                contour_coordinates.append(np.array(filtered_coords))
                                if level_index == highlight_level:
                                    highlight_contours.append(np.array(filtered_coords))
                            filtered_coords = [vertices[i]]
                    if len(filtered_coords) > 1:
                        contour_coordinates.append(np.array(filtered_coords))
                        if level_index == highlight_level:
                            highlight_contours.append(np.array(filtered_coords))

    # Generate TikZ code for contours
    tikz_code = """\\begin{tikzpicture}[tdplot_main_coords,scale=0.5]
    \\clip[tdplot_screen_coords,scale=2] (-3.5,-2.5) rectangle (3.5,2.5);
    \\draw[white,tdplot_screen_coords,scale=2] (-3.5,-2.5) rectangle (3.5,2.5); 
    """
    for coords in contour_coordinates:
        tikz_code += "\\draw[black]"
        for x, y in coords:
            tikz_code += f"({x:.2f},{y:.2f}) -- "
        tikz_code = tikz_code[:-3] + ";\n"  # Close the contour

    # Draw the selected contour level in red and add rectangles
    for highlight_contour in highlight_contours:
        highlight_contour = highlight_contour[::num_samples]  # Reduce the number of samples
        tikz_code += "\\draw[red, thick]\n"
        for i in range(len(highlight_contour) - 1):
            x1, y1 = highlight_contour[i]
            x2, y2 = highlight_contour[i + 1]
            tikz_code += f"({x1:.2f},{y1:.2f}) -- "
        tikz_code = tikz_code[:-3] + ";\n"  # Close the red contour line

        # Draw rectangles for each line segment, extending from the base to the height of the function
        for i in range(len(highlight_contour) - 1):
            x1, y1 = highlight_contour[i]
            x2, y2 = highlight_contour[i + 1]
            z1 = my_function(x1, y1)
            z2 = my_function(x2, y2)
            tikz_code += f"""
            \\fill[opacity=0.3,red] ({x1:.2f},{y1:.2f},0) -- ({x2:.2f},{y2:.2f},0) -- ({x2:.2f},{y2:.2f},{z2:.2f}) -- ({x1:.2f},{y1:.2f},{z1:.2f}) -- cycle;
            \\draw[red] ({x1:.2f},{y1:.2f},0) -- ({x2:.2f},{y2:.2f},0) -- ({x2:.2f},{y2:.2f},{z2:.2f}) -- ({x1:.2f},{y1:.2f},{z1:.2f}) -- cycle;
            """

    # Generate TikZ code for triangular mesh grid
    x_vals = np.linspace(-5, 5, 20)
    y_vals = np.linspace(-5, 5, 20)

    for i in range(len(x_vals) - 1):
        for j in range(len(y_vals) - 1):
            V1 = (x_vals[i], y_vals[j], my_function(x_vals[i], y_vals[j]))
            V2 = (x_vals[i+1], y_vals[j], my_function(x_vals[i+1], y_vals[j]))
            V3 = (x_vals[i], y_vals[j+1], my_function(x_vals[i], y_vals[j+1]))
            V4 = (x_vals[i+1], y_vals[j+1], my_function(x_vals[i+1], y_vals[j+1]))

            # First triangle
            tikz_code += f"""\\fill[opacity=0.2] ({V1[0]},{V1[1]},{V1[2]}) -- ({V2[0]},{V2[1]},{V2[2]}) -- ({V3[0]},{V3[1]},{V3[2]}) -- cycle;
            \\draw ({V1[0]},{V1[1]},{V1[2]}) -- ({V2[0]},{V2[1]},{V2[2]}) -- ({V3[0]},{V3[1]},{V3[2]}) -- cycle;
            """

            # Second triangle
            tikz_code += f"""\\fill[opacity=0.2] ({V2[0]},{V2[1]},{V2[2]}) -- ({V3[0]},{V3[1]},{V3[2]}) -- ({V4[0]},{V4[1]},{V4[2]}) -- cycle;
            \\draw ({V2[0]},{V2[1]},{V2[2]}) -- ({V3[0]},{V3[1]},{V3[2]}) -- ({V4[0]},{V4[1]},{V4[2]}) -- cycle;
            """

    tikz_code += "\\end{tikzpicture}"

    preamble = f"""
    \\documentclass{{beamer}}
    \\beamertemplatenavigationsymbolsempty
    \\usepackage{{tikz,tikz-3dplot}}
    \\begin{{document}}
    \\begin{{frame}}
    \\centering
    \\tdplotsetmaincoords{{{polar_angle}}}{{{azimuthal_angle}}}
    """

    postscript = f"""
    \\end{{frame}}
    \\end{{document}}
    """

    # Save to a .tex file
    with open('TeX_File.tex', 'w') as f:
        f.write(preamble)
        f.write(tikz_code)
        f.write(postscript)

    animatetex.during_loop()

animatetex.after_loop()