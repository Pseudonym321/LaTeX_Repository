import numpy as np
import Animation_Modules.animatetex as animatetex
# Credit for formulae: https://www.researchgate.net/publication/376028984_Visualizing_atomic_orbitals_of_an_electron_by_Latex

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
        \begin{tabular}{cc}
            \tdplotsetmaincoords{60}{110+\Vt}
            \begin{tikzpicture}[scale=1.75,line join=bevel,tdplot_main_coords,%
            fill opacity=.5]
                \tdplotsetpolarplotrange{0}{360}{0}{360}
                \tdplotsphericalsurfaceplot[parametricfill]{72}{36}%
                {sqrt(7)/(4*sqrt(pi))*(5*(cos(\tdplottheta))^3-3*cos(\tdplottheta))}{black}{\tdplotphi}%
                {\path[color=black,thick,->] (0,0,0)
                -- (1,0,0) node[anchor=north east]{};}%
                {\path[color=black,thick,->] (0,0,0)
                -- (0,1,0) node[anchor=north west]{};}%
                {\path[color=black,thick,->] (0,0,0)
                -- (0,0,1) node[anchor=south]{};}%

                \draw[white,tdplot_screen_coords] (0,0) circle({sqrt(110)/(4*sqrt(pi))});
            \end{tikzpicture}
            &
            \tdplotsetmaincoords{60}{110-\Vt}
            \begin{tikzpicture}[scale=1.75,line join=bevel,tdplot_main_coords,%
            fill opacity=.5]
                \tdplotsetpolarplotrange{0}{360}{0}{360}
                \tdplotsphericalsurfaceplot[parametricfill]{72}{36}%
                {sqrt(105)/(4*sqrt(pi))*(sin(\tdplottheta))^2*cos(\tdplottheta)*sin(2*\tdplotphi)}{black}{\tdplotphi}%
                {\path[color=black,thick,->] (0,0,0)
                -- (1,0,0) node[anchor=north east]{};}%
                {\path[color=black,thick,->] (0,0,0)
                -- (0,1,0) node[anchor=north west]{};}%
                {\path[color=black,thick,->] (0,0,0)
                -- (0,0,1) node[anchor=south]{};}%

                \draw[white,tdplot_screen_coords] 
                (0,0) circle({sqrt(110)/(4*sqrt(pi))});
            \end{tikzpicture}\\
            \tdplotsetmaincoords{60}{110-\Vt}
            \begin{tikzpicture}[scale=1.75,line join=bevel,tdplot_main_coords,%
            fill opacity=.5]
                \tdplotsetpolarplotrange{0}{360}{0}{360}
                \tdplotsphericalsurfaceplot[parametricfill]{72}{36}%
                {sqrt(15)/(4*sqrt(pi))*(sin(\tdplottheta))^2*cos(2*\tdplotphi)}
                {black}{\tdplotphi}%
                {\path[color=black,thick,->] (0,0,0)
                -- (1,0,0) node[anchor=north east]{};}%
                {\path[color=black,thick,->] (0,0,0)
                -- (0,1,0) node[anchor=north west]{};}%
                {\path[color=black,thick,->] (0,0,0)
                -- (0,0,1) node[anchor=south]{};}%

                \draw[white,tdplot_screen_coords] 
                (0,0) circle({sqrt(110)/(4*sqrt(pi))});
            \end{tikzpicture}
            &
            \tdplotsetmaincoords{60}{110+\Vt}
            \begin{tikzpicture}[scale=1.75,line join=bevel,tdplot_main_coords,%
            fill opacity=.5]
                \tdplotsetpolarplotrange{0}{360}{0}{360}
                \tdplotsphericalsurfaceplot[parametricfill]{72}{36}%
                {sqrt(35)/(4*sqrt(2*pi))*(sin(\tdplottheta))^3*cos(3*\tdplotphi)}
                {black}{\tdplotphi}%
                {\path[color=black,thick,->] (0,0,0)
                -- (1,0,0) node[anchor=north east]{};}%
                {\path[color=black,thick,->] (0,0,0)
                -- (0,1,0) node[anchor=north west]{};}%
                {\path[color=black,thick,->] (0,0,0)
                -- (0,0,1) node[anchor=south]{};}%

                \draw[white,tdplot_screen_coords] 
                (0,0) circle({sqrt(110)/(4*sqrt(pi))});
            \end{tikzpicture}
        \end{tabular}
    \end{frame}
\end{document}
'''

def main():
    """
    Purpose:
        Makes an animation of four spinning atomic orbitals.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    animatetex.before_loop()
    for angle in np.linspace(0,360,numiter):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(preamble)
            f.write(r'\newcommand{\Vt}{' +f'{angle}' +'}')
            f.write(postscript)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()