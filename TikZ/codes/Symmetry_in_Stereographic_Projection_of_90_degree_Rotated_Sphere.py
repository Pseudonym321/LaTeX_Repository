
import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

preamble= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty

\usepackage{tikz,tikz-3dplot}

\newcommand{\sphereX}[2]{
% #1  - azimuthal angle
% #2  - polar angle
cos(#2)*cos(#1)
}

\newcommand{\sphereY}[2]{
% #1  - azimuthal angle
% #2  - polar angle
cos(#2)*sin(#1)
}

\newcommand{\sphereZ}[2]{
% #1  - azimuthal angle
% #2  - polar angle
sin(#2)
}

\newcommand{\torusRadius}[1]{
% #1  - projection angle
(-sin(#1)/cos(#1))
}

\newcommand{\torusCenter}[1]{
% #1  - projection angle
(1/cos(#1))
}
'''

postscript = r'''
\begin{document}
    \tdplotsetmaincoords{60}{130}
    \begin{tikzpicture}[tdplot_main_coords]

        % This clips, and adds struts to a rectangle that is the size of a Beamer frame.
        \clip[tdplot_screen_coords] 
        (-12.8/2,-9.6/2) 
        rectangle (12.8/2,9.6/2);
        \draw[opacity=0,very thin,tdplot_screen_coords] 
        (-12.8/2,-9.6/2) 
        rectangle (12.8/2,9.6/2);

        % For every azimuthal angle, we draw the corresponding line of longitude on the torus. 
        % The lines of longitude vary in their polar angles.
        \foreach \azimuthalAngle in {0,10,...,350}{
            \draw[variable=\polarAngle,domain=0:360,smooth] 
            plot 
            (
                {\torusRadius{\variableTheta}*\sphereX{\azimuthalAngle}{\polarAngle}+\torusCenter{\variableTheta}*cos(\azimuthalAngle)},
                {\torusRadius{\variableTheta}*\sphereY{\azimuthalAngle}{\polarAngle}+\torusCenter{\variableTheta}*sin(\azimuthalAngle)},
                {\torusRadius{\variableTheta}*\sphereZ{\azimuthalAngle}{\polarAngle}}
            );
        }

        % Similarly, for every polar angle on the torus, we draw the corresponding line of latitude.
        % Latitudinal lines vary in their azimuthal angle. 
        % Note that the paths on the tori have the same equation, and we just vary a different parameter.
        \foreach \polarAngle in {0,10,...,350}{
            \draw[variable=\azimuthalAngle,domain=0:360,smooth] 
            plot 
            (
                {\torusRadius{\variableTheta}*\sphereX{\azimuthalAngle}{\polarAngle}+\torusCenter{\variableTheta}*cos(\azimuthalAngle)},
                {\torusRadius{\variableTheta}*\sphereY{\azimuthalAngle}{\polarAngle}+\torusCenter{\variableTheta}*sin(\azimuthalAngle)},
                {\torusRadius{\variableTheta}*\sphereZ{\azimuthalAngle}{\polarAngle}}
            );
        }

        % We follow a similar strategy for the sphere.
        % Here we draw the lines of longitude (which vary in their polar angles)
        % Note that the radius of the sphere is the same as for the longitudinal lines on the torus.
        \foreach \azimuthalAngle in {0,10,...,350}{
            \draw[variable=\polarAngle,domain=0:360,smooth] 
            plot 
            (
                {\torusCenter{\variableTheta}*\sphereX{\azimuthalAngle}{\polarAngle}},
                {\torusCenter{\variableTheta}*\sphereY{\azimuthalAngle}{\polarAngle}},
                {\torusRadius{\variableTheta}+\torusCenter{\variableTheta}*\sphereZ{\azimuthalAngle}{\polarAngle}}
            );
        }

        % And for the latitudinal lines, we vary the azimuthal angle in the same formula.
        \foreach \polarAngle in {0,10,...,350}{
            \draw[variable=\azimuthalAngle,domain=0:360,smooth] 
            plot 
            (
                {\torusCenter{\variableTheta}*\sphereX{\azimuthalAngle}{\polarAngle}},
                {\torusCenter{\variableTheta}*\sphereY{\azimuthalAngle}{\polarAngle}},
                {\torusRadius{\variableTheta}+\torusCenter{\variableTheta}*\sphereZ{\azimuthalAngle}{\polarAngle}}
            );
        }
        
    \end{tikzpicture}
\end{document}
'''

def main():
    """
    Purpose:
        Symmetry_in_Stereographic_Projection_of_90_degree_Rotated_Sphere.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    animatetex.before_loop()
    for theta in np.linspace(0,180,numiter):
        with open(animatetex.TeX_file, 'w') as TeX:
            TeX.write(preamble)
            TeX.write(r'\newcommand{\variableTheta}{' +f'{theta}' +'}')
            TeX.write(postscript)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()