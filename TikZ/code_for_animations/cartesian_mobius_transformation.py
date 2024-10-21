"""
File name: cartesian_mobius_transformation.py
Author: Jasper Nice
Purpose:
    This file produces a sphere and a plane. The plane is initially 
    mapped onto the sphere, then the sphere is rotated. What we see is 
    the inverse mapping of that rotated map back onto the plane. We use
    stereographic projection to perform the mapping. All together, the
    concept is called a Mobius transformation of the cartesian grid.
Credit:
    I became aware of this concept from a professor who was interested 
    in my development.
"""

import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

start= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty

% packages
\usepackage{tikz}
\usepackage{tikz-3dplot}

% commands
\newcommand{\sphereX}[2]{
% Purpose: Gives the 'x' coordinate on a sphere, for a given 
% polar-azimuthal coordinate.
% Parameters:
% #1  - azimuthal angle
% #2  - polar angle
cos(#2)*cos(#1)
}

\newcommand{\sphereY}[2]{
% Purpose: Gives the 'y' coordinate on a sphere, for a given 
% polar-azimuthal coordinate.
% Parameters:
% #1  - azimuthal angle
% #2  - polar angle
cos(#2)*sin(#1)
}

\newcommand{\sphereZ}[2]{
% Purpose: Gives the 'z' coordinate on a sphere, for a given 
% polar-azimuthal coordinate. [Note: the azimuthal angle is redundant.]
% Parameters:
% #1  - azimuthal angle
% #2  - polar angle
sin(#2)
}

\newcommand{\SPX}[2]{
% Purpose: Gives the 'x' coordinate of the stereographic projection of a 
% point on a sphere.
% Parameters:
% #1  - the x value of a point on the sphere
% #2  - the z value of that point
#1/(1-#2)
}

\newcommand{\SPY}[2]{
% Purpose: Gives the 'y' coordinate of the stereographic projection of a 
% point on a sphere.
% Parameters:
% #1  - the x value of a point on the sphere
% #2  - the z value of that point
#1/(1-#2)
}

\newcommand{\ISPX}[2]{
% Purpose: Given a point on the plane, gives the 'x' coordinate of its 
% inverse stereographic projection.
% Parameters:
% #1  - the x value
% #2  - the y value
2*(#1)/(1+(#1)^2+(#2)^2)
}

\newcommand{\ISPY}[2]{
% Purpose: Given a point on the plane, gives the 'y' coordinate of its 
% inverse stereographic projection.
% Parameters:
% #1  - the x value
% #2  - the y value
2*(#2)/(1+(#1)^2+(#2)^2)
}

\newcommand{\ISPZ}[2]{
% Purpose: Given a point on the plane, gives the 'z' coordinate of its 
% inverse stereographic projection.
% Parameters:
% #1  - the x value
% #2  - the y value
(-1+(#1)^2+(#2)^2)/(1+(#1)^2+(#2)^2)
}
'''

end = r'''
\begin{document}
    \begin{frame}
        \centering

        % sets the viewing angle
        \tdplotsetmaincoords{60}{45}
        \begin{tikzpicture}[tdplot_main_coords]

            % Clips a screen rectangle, and sets up struts around it
            \clip[tdplot_screen_coords] 
            (-3.5,-2.5) rectangle (3.5,2.5);
            \draw[white,tdplot_screen_coords] 
            (-3.5,-2.5) rectangle (3.5,2.5);

            % Sets the Euler-angle rotation of the rotated coordinate 
            % system
            \tdplotsetrotatedcoords{\VT}{\VT}{\VT}

            \foreach \Vn in {-3,-2,...,3}{
            \draw[tdplot_rotated_coords,smooth,variable=\Vt,domain=-10:10,samples=100] plot ({\ISPX{\Vn}{\Vt}},{\ISPY{\Vn}{\Vt}},{\ISPZ{\Vn}{\Vt}});
            \draw[tdplot_rotated_coords,smooth,variable=\Vt,domain=-10:10,samples=100] plot ({\ISPX{\Vt}{\Vn}},{\ISPY{\Vt}{\Vn}},{\ISPZ{\Vt}{\Vn}});


            \gdef\opacity{1}
            \tdplottransformrotmain{\ISPX{\Vn}{-10}}{\ISPY{\Vn}{-10}}{\ISPZ{\Vn}{-10}}
            \ifdim\tdplotresz pt<0.999pt
            \pgfmathsetmacro\lastx{\SPX{\tdplotresx}{\tdplotresz}}
            \pgfmathsetmacro\lasty{\SPY{\tdplotresy}{\tdplotresz}}
            \fi
            \foreach \Vnn in {-3,-2,...,3}{
            \typeout\Vn
            \typeout\Vnn
            \tdplottransformrotmain{\ISPX{\Vn}{\Vnn}}{\ISPY{\Vn}{\Vnn}}{\ISPZ{\Vn}{\Vnn}}
            \ifdim \tdplotresz pt<0.999pt
            \pgfmathsetmacro\Vx{\SPX{\tdplotresx}{\tdplotresz}}
            \pgfmathsetmacro\Vy{\SPY{\tdplotresy}{\tdplotresz}}
            \draw[opacity=\opacity] (\lastx,\lasty) -- (\Vx,\Vy);
            \gdef\opacity{1}
            \pgfmathsetmacro\lastx{\Vx}
            \pgfmathsetmacro\lasty{\Vy}
            \global\let\lastx\lastx
            \global\let\lasty\lasty
            \else
            \gdef\opacity{0}
            \fi
            }}








            \foreach \Vn in {-3,-2,...,3}{
            %\draw[tdplot_rotated_coords,smooth,variable=\Vt,domain=-10:10,samples=100] plot ({\ISPX{\Vn}{\Vt}},{\ISPY{\Vn}{\Vt}},{\ISPZ{\Vn}{\Vt}});
            %\draw[tdplot_rotated_coords,smooth,variable=\Vt,domain=-10:10,samples=100] plot ({\ISPX{\Vt}{\Vn}},{\ISPY{\Vt}{\Vn}},{\ISPZ{\Vt}{\Vn}});


            \gdef\opacity{1}
            \tdplottransformrotmain{\ISPX{-10}{\Vn}}{\ISPY{-10}{\Vn}}{\ISPZ{-10}{\Vn}}
            \ifdim\tdplotresz pt<0.999pt
            \pgfmathsetmacro\lastx{\SPX{\tdplotresx}{\tdplotresz}}
            \pgfmathsetmacro\lasty{\SPY{\tdplotresy}{\tdplotresz}}
            \fi
            \foreach \Vnn in {-3,-2,...,3}{
            \typeout\Vn
            \typeout\Vnn
            \tdplottransformrotmain{\ISPX{\Vnn}{\Vn}}{\ISPY{\Vnn}{\Vn}}{\ISPZ{\Vnn}{\Vn}}
            \ifdim \tdplotresz pt<0.999pt
            \pgfmathsetmacro\Vx{\SPX{\tdplotresx}{\tdplotresz}}
            \pgfmathsetmacro\Vy{\SPY{\tdplotresy}{\tdplotresz}}
            \draw[opacity=\opacity] (\lastx,\lasty) -- (\Vx,\Vy);
            \gdef\opacity{1}
            \pgfmathsetmacro\lastx{\Vx}
            \pgfmathsetmacro\lasty{\Vy}
            \global\let\lastx\lastx
            \global\let\lasty\lasty
            \else
            \gdef\opacity{0}
            \fi
            }}
        \end{tikzpicture}
    \end{frame}
\end{document}
'''

def main():
  """
    Purpose:
        Makes an animation of the cross product of a fixed vector and another one which
        follows the trajectory of a loxodrome.
    Parameters:
        No parameters.
    Return:
        Void.
    """
  animatetex.before_loop()
  for angle in np.linspace(0,40,numiter):
      with open(animatetex.TeX_file, 'w') as f:
          f.write(start)
          f.write(r'\newcommand{\VT}{' +f'{angle}' +'}\n')
          f.write(end)
      animatetex.during_loop()
  animatetex.after_loop()

if __name__ == "__main__":
    main()