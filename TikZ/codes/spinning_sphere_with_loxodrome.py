"""
File name: bumpy_sphere.py
Author: Jasper Nice
Purpose:
    This file produces a spinning "bumpy sphere." This sphere is defined
    in spherical coordinates, where the radii oscilate over different 
    theta and phi values - producing a wavy sphere. This particular
    example is taken from Stewart's Calculus.
Credit:
    There was a member in the TeX.SE community who first showed me 
    tikz-3dplot when I was initially trying to draw this.
"""

import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

preamble= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty

\usepackage{tikz}
\usepackage{tikz-3dplot}

\newcommand{\sphereX}[2]{cos(#1)*cos(#2)}
\newcommand{\sphereY}[2]{cos(#1)*sin(#2)}
\newcommand{\sphereZ}[2]{sin(#1)}

\newcommand{\loxodromeX}[1]{cos(#1)/sqrt((cos(#1))^2+(sin(#1))^2+((#1)/360)^2)}
\newcommand{\loxodromeY}[1]{sin(#1)/sqrt((cos(#1))^2+(sin(#1))^2+((#1)/360)^2)}
\newcommand{\loxodromeZ}[1]{(#1)/360/sqrt((cos(#1))^2+(sin(#1))^2+((#1)/360)^2)}

\newcommand{\elevation}{30}
%\newcommand{\azimuth}{130}
'''

postscript = r'''
% https://tex.stackexchange.com/a/729510/319072
\pgfmathsetmacro{\CameraX}{sin(\azimuth)*cos(\elevation)}
\pgfmathsetmacro{\CameraY}{-cos(\azimuth)*cos(\elevation)}
\pgfmathsetmacro{\CameraZ}{sin(\elevation)}

\begin{document}
    \begin{frame}
        \centering
        \tdplotsetmaincoords{90-\elevation}{\azimuth}
        \begin{tikzpicture}[tdplot_main_coords,scale=2]

            \clip[tdplot_screen_coords,scale=0.5] 
            (-\textwidth/2,-\textheight/2) 
            rectangle 
            (\textwidth/2,\textheight/2);
            \draw[white,tdplot_screen_coords,scale=0.5] 
            (-\textwidth/2,-\textheight/2) 
            rectangle 
            (\textwidth/2,\textheight/2);

            \foreach \latitude in {-90,-80,...,90}{
                \foreach \longitude in {0,10,...,360}{

                    \pgfmathsetmacro\dotproduct{(\CameraX)*(\sphereX{\latitude}{\longitude}) + (\CameraY)*(\sphereY{\latitude}{\longitude}) + (\CameraZ)*(\sphereZ{\latitude}{\longitude})}

                    \ifdim\dotproduct pt > 0pt
                    \draw[thin] 
                    (
                        {\sphereX{\latitude}{\longitude}},
                        {\sphereY{\latitude}{\longitude}},
                        {\sphereZ{\latitude}{\longitude}}
                    ) 
                    -- 
                    (
                        {\sphereX{\latitude}{\longitude+10}},
                        {\sphereY{\latitude}{\longitude+10}},
                        {\sphereZ{\latitude}{\longitude+10}}
                    );

                    \fi
                }
            }

            \foreach \longitude in {0,10,...,360}{
                \foreach \latitude in {-90,-80,...,90}{

                    \pgfmathsetmacro\dotproduct{(\CameraX)*(\sphereX{\latitude}{\longitude}) + (\CameraY)*(\sphereY{\latitude}{\longitude}) + (\CameraZ)*(\sphereZ{\latitude}{\longitude})}

                    \ifdim\dotproduct pt > 0pt
                        \draw[thin]
                        (
                            {\sphereX{\latitude}{\longitude}},
                            {\sphereY{\latitude}{\longitude}},
                            {\sphereZ{\latitude}{\longitude}}
                        ) 
                        -- 
                        (
                            {\sphereX{\latitude+10}{\longitude}},
                            {\sphereY{\latitude+10}{\longitude}},
                            {\sphereZ{\latitude+10}{\longitude}}
                        );
                    \fi
                }
            }

            \foreach \Vt in {-1800,-1790,...,1800}{
                \pgfmathsetmacro\dotproduct{(\CameraX)*(\loxodromeX{\Vt}) + (\CameraY)*(\loxodromeY{\Vt}) + (\CameraZ)*(\loxodromeZ{\Vt})}

                \ifdim\dotproduct pt > 0pt
                    \draw[red] 
                    (
                        {\loxodromeX{\Vt}},
                        {\loxodromeY{\Vt}},
                        {\loxodromeZ{\Vt}}
                    ) 
                    -- 
                    (
                        {\loxodromeX{\Vt+10}},
                        {\loxodromeY{\Vt+10}},
                        {\loxodromeZ{\Vt+10}}
                    );
                \fi
            }

            \draw[tdplot_screen_coords] circle[radius=1];
        \end{tikzpicture}
    \end{frame}
\end{document}
'''

def main():
    """
    Purpose:
        This function animates a spinning sphere with a loxodrome.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    animatetex.before_loop()
    for theta in np.linspace(130,130+24,numiter//2):
        with open(animatetex.TeX_file, 'w') as TeX:
            TeX.write(preamble)
            TeX.write(r'\newcommand{\azimuth}{' +f'{theta}' +'}')
            TeX.write(postscript)
        animatetex.during_loop()
    for theta in np.linspace(130+24,130,numiter//2):
        with open(animatetex.TeX_file, 'w') as TeX:
            TeX.write(preamble)
            TeX.write(r'\newcommand{\azimuth}{' +f'{theta}' +'}')
            TeX.write(postscript)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()