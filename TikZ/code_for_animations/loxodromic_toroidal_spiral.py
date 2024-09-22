import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 180

preamble= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty
\usepackage{tikz,tikz-3dplot}
\usetikzlibrary{spath3}
'''

postscript = r'''
\begin{document}
\centering
\tdplotsetmaincoords{0}{90}
\begin{tikzpicture}[tdplot_main_coords]
\draw[white,tdplot_main_coords] (-4.5,-3.5) rectangle (4.5,5);
\tdplotsetrotatedcoords{0}{0}{0}
\draw[tdplot_rotated_coords,domain=\Vn:360,smooth,very thin,samples=1000,variable=\Vt] plot ({1*sqrt(1-(\Vt/360)^2)*sin(40*\Vt)/(1-sqrt(1-(\Vt/360)^2)*cos(40*\Vt)))},{1*(\Vt/360)/(1-sqrt(1-(\Vt/360)^2)*cos(40*\Vt))*cos(10*\Vt)},{1*(\Vt/360)/(1-sqrt(1-(\Vt/360)^2)*cos(40*\Vt))*sin(10*\Vt)});
\end{tikzpicture}
\end{document}
'''

def main():
    """
    Purpose:
        Makes a stereographic projection of a loxodrome that follows the trajectory of a nested torus. 
    Parameters:
        No parameters.
    Return:
        Void.
    """
    animatetex.before_loop()
    for n in np.linspace(360,300,numiter):
        with open(animatetex.TeX_file, 'w') as TeX:
            TeX.write(preamble)
            TeX.write(r'\newcommand{\Vn}{' +f'{n}' +'}')
            TeX.write(postscript)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()