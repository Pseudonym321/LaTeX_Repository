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
'''

postscript = r'''
\begin{document}
    \begin{frame}
        \centering
        \tdplotsetmaincoords{60}{\varT}
        \begin{tikzpicture}[
        line join=bevel,tdplot_main_coords,
        scale=2,fill opacity=.5]
            \tdplotsetpolarplotrange{0}{360}{0}{360}
            \tdplotsphericalsurfaceplot[parametricfill]{72}{36}%
            {1+(1/5)*sin(6*\tdplottheta)*sin(5*\tdplotphi)}%
            {black}%
            {\tdplotphi}%
            {\path[color=black,thick,->] (0,0,0)
            -- (1,0,0) node[anchor=north east]{};}%
            {\path[color=black,thick,->] (0,0,0)
            -- (0,1,0) node[anchor=north west]{};}%
            {\path[color=black,thick,->] (0,0,0)
            -- (0,0,1) node[anchor=south]{};}%
        \end{tikzpicture}
    \end{frame}
\end{document}
'''

def main():
    """
    Purpose:
        This function animates a spinning bumpy sphere.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    animatetex.before_loop()
    for theta in np.linspace(0,48,numiter):
        with open(animatetex.TeX_file, 'w') as TeX:
            TeX.write(preamble)
            TeX.write(r'\newcommand{\varT}{' +f'{theta}' +'}')
            TeX.write(postscript)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()