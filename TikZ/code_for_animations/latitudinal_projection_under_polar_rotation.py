
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
\clip[tdplot_screen_coords,scale=1] (-3.5,-2.5) rectangle (3.5,2.5);
\draw[white,tdplot_screen_coords,scale=1] (-3.5,-2.5) rectangle (3.5,2.5);
\tdplotsetrotatedcoords{20+\Vn/2}{35+\Vn}{10}
\foreach \Vn in {0,10,...,350}{
    % latitude
    \draw[variable=\Vt,domain=0:360,smooth,samples=100,tdplot_rotated_coords]
    ({\sphereX{0}{\Vn}},{\sphereY{0}{\Vn}},{\sphereZ{0}{\Vn}}) plot ({\sphereX{\Vt}{\Vn}},{\sphereY{\Vt}{\Vn}},{\sphereZ{\Vt}{\Vn}}) -- cycle;
    % stereographic projection of latitude
    \draw
    \pgfextra{\tdplottransformrotmain{\sphereX{0}{\Vn}}{\sphereY{0}{\Vn}}{\sphereZ{0}{\Vn}}}
    \ifdim\tdplotresz pt<0.999pt % Exclude points too close to the north pole
    ({\SPX{\tdplotresx}{\tdplotresz}},{\SPX{\tdplotresy}{\tdplotresz}},0)
    \foreach \Vt in {-360,-355,...,360}{ 
        \pgfextra{\tdplottransformrotmain{\sphereX{\Vt}{\Vn}}{\sphereY{\Vt}{\Vn}}{\sphereZ{\Vt}{\Vn}}}
        \ifdim\tdplotresz pt<0.999pt % Exclude points too close to the north pole
        -- ({\SPX{\tdplotresx}{\tdplotresz}},{\SPX{\tdplotresy}{\tdplotresz}},0)
        \fi
    };
    \fi
}

\foreach \Vn in {0,10,...,350}{
    % latitude
    \draw[variable=\Vt,domain=0:360,smooth,samples=100,tdplot_rotated_coords]
    ({\sphereX{\Vn}{0}},{\sphereY{\Vn}{0}},{\sphereZ{0\Vn}{0}}) plot ({\sphereX{\Vn}{\Vt}},{\sphereY{\Vn}{\Vt}},{\sphereZ{\Vn}{\Vt}}) -- cycle;
    % stereographic projection of latitude
    \draw
    \pgfextra{\tdplottransformrotmain{\sphereX{\Vn}{0}}{\sphereY{\Vn}{0}}{\sphereZ{\Vn}{0}}}
    \ifdim\tdplotresz pt<0.999pt % Exclude points too close to the north pole
    ({\SPX{\tdplotresx}{\tdplotresz}},{\SPX{\tdplotresy}{\tdplotresz}},0)
    \foreach \Vt in {-360,-355,...,360}{ 
        \pgfextra{\tdplottransformrotmain{\sphereX{\Vn}{\Vt}}{\sphereY{\Vn}{\Vt}}{\sphereZ{\Vn}{\Vt}}}
        \ifdim\tdplotresz pt<0.999pt % Exclude points too close to the north pole
        -- ({\SPX{\tdplotresx}{\tdplotresz}},{\SPX{\tdplotresy}{\tdplotresz}},0)
        \fi
    };
    \fi
}
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
    for theta in np.linspace(0,50,numiter):
        with open(animatetex.TeX_file, 'w') as TeX:
            TeX.write(preamble)
            TeX.write(r'\newcommand{\Vn}{' +f'{theta}' +'}')
            TeX.write(postscript)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()