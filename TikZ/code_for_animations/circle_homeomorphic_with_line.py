
import numpy as np
import Animation_Modules.animatetex as animatetex
#i added this so i could save everything and make sure it was saved
radius=2.0
L=8.0
linspace_amount = 38
numiter = 24
# x_input is synonymous with "A" from the diagram

def x_input_function(x_input:float):
    """
    Purpose:
        Delivers the x coordinates of the inverse stereographic projection of the plane.
    Parameters:
        float - x_input: points on the real line
    Return:
        the x coordinates of the inverse stereographic projection of the points.
    """
    return (2*x_input*radius*np.abs((L**2)/(x_input**2+L**2))**(1/2))/np.abs(x_input**2+L**2)**(1/2)

def y_input_function_upper(x_input):
    """
    Purpose:
        Makes a spinning bumpy sphere.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    return (np.abs(radius**2-x_input**2)**(1/2)+L-radius)

def y_input_function_lower(x_input):
    """
    Purpose:
        Makes a spinning bumpy sphere.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    return (-np.abs(radius**2-x_input**2)**(1/2)+L-radius)

# https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python
import math

def rotate_x(x,y,theta): #rotate x,y around xo,yo by theta (rad)
    """
    Purpose:
        Makes a spinning bumpy sphere.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    xr=math.cos(theta)*(x-0)-math.sin(theta)*(y-(L-radius)) + 0
    return xr

def rotate_y(y,x,theta):
    """
    Purpose:
        Makes a spinning bumpy sphere.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    yr=math.sin(theta)*(x-0)+math.cos(theta)*(y-(L-radius))  + (L-radius)
    return yr

def rotate(angle):
    """
    Purpose:
        Makes a spinning bumpy sphere.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    global rotated_x_list,rotated_y_list
    rotated_x_list.clear()
    rotated_y_list.clear()
    for pos in range(len(x_input_list)):
        rotated_x_list.append(rotate_x(x_input_list[pos], y_input_list[pos],angle))
        rotated_y_list.append(rotate_y(y_input_list[pos], x_input_list[pos],angle))



start= r'''
\documentclass{beamer}
\usepackage{tikz}
\begin{document}
\vspace*{\fill}
\begin{center}
\begin{tikzpicture}[scale=0.5]
\clip[] (-10,-1) rectangle (10,9);
\draw[black,-latex,thick] (0,-1) -- (0,9); % y-axis
\draw[black,-latex,thick] (-10,0) -- (10,0); % x-axis
\draw[] (0,6) circle [radius=2];
'''

end = r'''
\end{tikzpicture}
\end{center}
\vspace*{\fill}
\end{document}
'''


def draw_path(x,y):
    """
    Purpose:
        Makes a spinning bumpy sphere.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    if np.abs((-L*x)/(y-L)) < 40:
        return r'''\draw[] (0,8) -- ({},0);
\fill[] ({},{}) circle [radius=0.08];
'''.format((-L*x)/(y-L),x,y)
    else:
        return r'''\draw[] (0,8) -- (0,0);
'''

def main():
    """
    Purpose:
        Makes a gif which demonstrates that a circle with a point removed is homeomorphic to the real line.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    global x_input_list, y_input_list, rotated_x_list, rotated_y_list
    x_input_list = [x_input_function(x_input) for x_input in np.linspace(-10,10,linspace_amount)]
    y_input_list = [y_input_function_upper(x_input) for x_input in x_input_list[:int(0.1*linspace_amount)]]
    y_input_list.extend([y_input_function_lower(x_input) for x_input in x_input_list[int(0.1*linspace_amount):int(0.9*linspace_amount)]])
    y_input_list.extend([y_input_function_upper(x_input) for x_input in x_input_list[int(0.9*linspace_amount):]])
    rotated_x_list = []
    rotated_y_list = []
    animatetex.before_loop()
    for i in range(0, numiter + 1):
        rotate((i*360/numiter)*np.pi/180)
        with open(animatetex.TeX_file, 'w') as f:
            f.write(start)
            for pos in range(len(x_input_list)):
                try:
                    f.write(draw_path(rotated_x_list[pos], rotated_y_list[pos]))
                except:
                    pass
            f.write(end)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()