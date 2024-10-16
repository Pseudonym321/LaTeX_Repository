import numpy as np
import matplotlib.pyplot as plt
import subprocess

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
contour_levels = np.linspace(0.1, 2.9, 30)

# Initialize a list to store contour coordinates
contour_coordinates = []

# Define a distance threshold
distance_threshold = 0.1

# Plot contours and collect coordinates
for level in contour_levels:
    contours = plt.contour(X, Y, Z, levels=[level], colors='black')
    for collection in contours.collections:
        for path in collection.get_paths():
            vertices = path.vertices
            # Check for distance and add disconnected segments
            disconnected_segment = []
            last_point = None
            for point in vertices:
                if last_point is not None:
                    distance = np.linalg.norm(point - last_point)
                    if distance > distance_threshold:
                        # If the distance exceeds the threshold, store the current segment
                        if disconnected_segment:
                            contour_coordinates.append(np.array(disconnected_segment))
                            disconnected_segment = []
                disconnected_segment.append(point)
                last_point = point
            # Add the last segment if it exists
            if disconnected_segment:
                contour_coordinates.append(np.array(disconnected_segment))

# Generate TikZ code
tikz_code = "\\begin{tikzpicture}\n"
for i, coords in enumerate(contour_coordinates):
    tikz_code += "\\draw[black]"
    for x, y in coords:
        tikz_code += f"({x:.2f},{y:.2f}) --"
    tikz_code = tikz_code[:-2] + f" -- cycle;\n"  # Close the contour
tikz_code += "\\end{tikzpicture}"

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

# Save to a .tex file
with open('contours.tex', 'w') as f:
    f.write(preamble)
    f.write(tikz_code)
    f.write(postscript)

# Compile the TikZ file with LuaLaTeX
subprocess.run(['lualatex', 'contours.tex'], check=True)

# Print message
print("TikZ file 'contours.tex' has been created and compiled.")
