
import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

preamble= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty
\usepackage{tikz,tikz-3dplot}
\newcommand{\sphereX}[2]{cos(#2)*cos(#1)}
\newcommand{\sphereY}[2]{cos(#2)*sin(#1)}
\newcommand{\sphereZ}[2]{sin(#2)}
\newcommand{\SPX}[2]{#1/(1-#2)}
\newcommand{\SPY}[2]{#1/(1-#2)}
'''

postscript = r'''
\begin{document}
\begin{frame}
\centering
\tdplotsetmaincoords{60}{45}
\begin{tikzpicture}[tdplot_main_coords,scale=0.5]

\clip[tdplot_screen_coords,scale=2] (-3.5,-2.5) rectangle (3.5,2.5);
\draw[white,tdplot_screen_coords,scale=2] (-3.5,-2.5) rectangle (3.5,2.5);

\tdplotsetrotatedcoords{\VT}{\VT}{\VT}




\pgfextra{\foreach \Vn in {0,10,...,350}{

\draw[variable=\Vt,domain=0:360,smooth,samples=100,tdplot_rotated_coords] ({\sphereX{0}{\Vn}},{\sphereY{0}{\Vn}},{\sphereZ{0}{\Vn}}) plot ({\sphereX{\Vt}{\Vn}},{\sphereY{\Vt}{\Vn}},{\sphereZ{\Vt}{\Vn}}) -- cycle;
    

\tdplottransformrotmain{\sphereX{0}{\Vn}}{\sphereY{0}{\Vn}}{\sphereZ{0}{\Vn}}
\ifdim \tdplotresz pt<0.999pt
\pgfmathsetmacro\lastx{\SPX{\tdplotresx}{\tdplotresz}}
\pgfmathsetmacro\lasty{\SPY{\tdplotresy}{\tdplotresz}}
\fi


\gdef\opacity{1}
\foreach \Vt in {0,5,...,355} {
\tdplottransformrotmain{\sphereX{\Vt}{\Vn}}{\sphereY{\Vt}{\Vn}}{\sphereZ{\Vt}{\Vn}}

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
}
}}


\end{tikzpicture}
\end{frame}
\end{document}
'''

def main():
    """
    Purpose:
        Makes a spinning loxodrome projection.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    animatetex.before_loop()
    for theta in np.linspace(0,90,numiter):
        with open(animatetex.TeX_file, 'w') as TeX:
            TeX.write(preamble)
            TeX.write(r'\newcommand{\VT}{' +f'{theta}' +'}')
            TeX.write(postscript)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()