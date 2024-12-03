
import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

preamble= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty
\usepackage{tikz,tikz-3dplot}
\usepackage{pgfmath-xfp}
\newcommand{\sphereX}[2]{cos(#2)*cos(#1)}
\newcommand{\sphereY}[2]{cos(#2)*sin(#1)}
\newcommand{\sphereZ}[2]{sin(#2)}

\newcommand{\polar}{60}
\newcommand{\azimuth}{45}
\newcommand{\SPX}[2]{#1/(1-#2)}
\newcommand{\SPY}[2]{#1/(1-#2)}

\newcommand{\loxodromeX}[1]{cos(#1)/sqrt((cos(#1))^2+(sin(#1))^2+(#1/360)^2)}
\newcommand{\loxodromeY}[1]{sin(#1)/sqrt((cos(#1))^2+(sin(#1))^2+(#1/360)^2)}
\newcommand{\loxodromeZ}[1]{#1/360/sqrt((cos(#1))^2+(sin(#1))^2+(#1/360)^2)}
'''

postscript = r'''
\begin{document}
\begin{frame}
\centering
\tdplotsetmaincoords{\polar}{\azimuth}
\begin{tikzpicture}[tdplot_main_coords]
\tdplotsetrotatedcoords{\VT}{\VT}{\VT}
\clip[tdplot_screen_coords] (-3.5,-2.5) rectangle (3.5,2.5);
\draw[white,tdplot_screen_coords] (-3.5,-2.5) rectangle (3.5,2.5);







% latitude
\pgfextra{\foreach \Vn in {0,10,...,350}{

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
\draw[opacity=\opacity,ultra thin] (\lastx,\lasty) -- (\Vx,\Vy);
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

%longitude
\pgfextra{\foreach \Vn in {0,10,...,350}{

\tdplottransformrotmain{\sphereX{\Vn}{0}}{\sphereY{\Vn}{0}}{\sphereZ{\Vn}{0}}
\ifdim \tdplotresz pt<0.999pt
\pgfmathsetmacro\lastx{\SPX{\tdplotresx}{\tdplotresz}}
\pgfmathsetmacro\lasty{\SPY{\tdplotresy}{\tdplotresz}}
\fi
\gdef\opacity{1}
\foreach \Vt in {0,5,...,355} {
\tdplottransformrotmain{\sphereX{\Vn}{\Vt}}{\sphereY{\Vn}{\Vt}}{\sphereZ{\Vn}{\Vt}}
\ifdim \tdplotresz pt<0.999pt
\pgfmathsetmacro\Vx{\SPX{\tdplotresx}{\tdplotresz}}
\pgfmathsetmacro\Vy{\SPY{\tdplotresy}{\tdplotresz}}
\draw[opacity=\opacity,ultra thin] (\lastx,\lasty) -- (\Vx,\Vy);
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




% loxodrome
\pgfextra{
\tdplottransformrotmain{\loxodromeX{-1800}}{\loxodromeY{-1800}}{\loxodromeZ{-1800}}
\ifdim \tdplotresz pt<0.999pt
\pgfmathsetmacro\lastx{\SPX{\tdplotresx}{\tdplotresz}}
\pgfmathsetmacro\lasty{\SPY{\tdplotresy}{\tdplotresz}}
\fi

\gdef\opacity{1}
\foreach \Vt in {-1800,-1790,...,1800}{
\tdplottransformrotmain{\loxodromeX{\Vt}}{\loxodromeY{\Vt}}{\loxodromeZ{\Vt}}
\ifdim \tdplotresz pt<0.999pt
\pgfmathsetmacro\Vx{\SPX{\tdplotresx}{\tdplotresz}}
\pgfmathsetmacro\Vy{\SPY{\tdplotresy}{\tdplotresz}}
\draw[opacity=\opacity,very thin,red] (\lastx,\lasty) -- (\Vx,\Vy);
\gdef\opacity{1}
\pgfmathsetmacro\lastx{\Vx}
\pgfmathsetmacro\lasty{\Vy}
\global\let\lastx\lastx
\global\let\lasty\lasty
\else
\gdef\opacity{0}
\fi
}% end foreach
}





















\fill[white] ({cos(\azimuth)},{sin(\azimuth)}) arc [start angle=\azimuth, end angle={\azimuth-180}, radius=1] -- cycle;
\fill[tdplot_screen_coords,white] ({cos(0)},{sin(0)}) arc [start angle=0, end angle=180, radius=1] -- cycle;



\draw[tdplot_screen_coords,ultra thin] ({cos(0)},{sin(0)}) arc[start angle=0,end angle=180,radius=1]; % outer circle

\pgfextra{
% longitudinal lines
\foreach \Vnn in {0,10,...,350}{
\tdplottransformrotmain{\sphereX{\Vnn}{0}}{\sphereY{\Vnn}{0}}{\sphereZ{\Vnn}{0}}
\pgfmathsetmacro\lastx{\tdplotresx}
\pgfmathsetmacro\lasty{\tdplotresy}
\pgfmathsetmacro\lastz{\tdplotresz}
\foreach \Vn in {5,10,...,360}{
\tdplottransformrotmain{\sphereX{\Vnn}{\Vn}}{\sphereY{\Vnn}{\Vn}}{\sphereZ{\Vnn}{\Vn}}
\pgfmathsetmacro\Vx{\tdplotresx}
\pgfmathsetmacro\Vy{\tdplotresy}
\pgfmathsetmacro\Vz{\tdplotresz}
 % Viewing direction components
        \pgfmathsetmacro\viewdirX{\sphereX{-\azimuth}{90 - \polar}} % Adjusting Z component
        \pgfmathsetmacro\viewdirY{\sphereY{-\azimuth}{90 - \polar}} % Adjusting Z component
        \pgfmathsetmacro\viewdirZ{\sphereZ{-\azimuth}{90 - \polar}} % Adjusting Z component

        \pgfmathsetmacro\currentDotProduct{\lastx*\viewdirX + \lasty*\viewdirY + \lastz*\viewdirZ} % Dot product with the viewer direction

        % Check if the dot product is positive
        \ifdim\currentDotProduct pt > -0.3 pt
        \ifdim\lastz pt>-0.049pt
        \ifdim\Vz pt>-0.049pt
            \draw[ultra thin] (\lastx,\lasty,\lastz) -- (\Vx,\Vy,\Vz);
        \fi\fi\fi
\pgfmathsetmacro\lastx{\Vx}
\pgfmathsetmacro\lasty{\Vy}
\pgfmathsetmacro\lastz{\Vz}
\global\let\lastx\lastx
\global\let\lasty\lasty
\global\let\lastz\lastz






} % end inner for loop
} % end outer for loop


% latitudinal lines
\foreach \Vnn in {0,10,...,350}{
\tdplottransformrotmain{\sphereX{0}{\Vnn}}{\sphereY{0}{\Vnn}}{\sphereZ{0}{\Vnn}}
\pgfmathsetmacro\lastx{\tdplotresx}
\pgfmathsetmacro\lasty{\tdplotresy}
\pgfmathsetmacro\lastz{\tdplotresz}
\foreach \Vn in {5,10,...,360}{
\tdplottransformrotmain{\sphereX{\Vn}{\Vnn}}{\sphereY{\Vn}{\Vnn}}{\sphereZ{\Vn}{\Vnn}}
\pgfmathsetmacro\Vx{\tdplotresx}
\pgfmathsetmacro\Vy{\tdplotresy}
\pgfmathsetmacro\Vz{\tdplotresz}
 % Viewing direction components
        \pgfmathsetmacro\viewdirX{\sphereX{-\azimuth}{90 - \polar}} % Adjusting Z component
        \pgfmathsetmacro\viewdirY{\sphereY{-\azimuth}{90 - \polar}} % Adjusting Z component
        \pgfmathsetmacro\viewdirZ{\sphereZ{-\azimuth}{90 - \polar}} % Adjusting Z component

        \pgfmathsetmacro\currentDotProduct{\lastx*\viewdirX + \lasty*\viewdirY + \lastz*\viewdirZ} % Dot product with the viewer direction

        % Check if the dot product is positive
        \ifdim\currentDotProduct pt > -0.3 pt
        \ifdim\lastz pt>-0.049pt
        \ifdim\Vz pt>-0.049pt
            \draw[ultra thin] (\lastx,\lasty,\lastz) -- (\Vx,\Vy,\Vz);
        \fi\fi\fi
\pgfmathsetmacro\lastx{\Vx}
\pgfmathsetmacro\lasty{\Vy}
\pgfmathsetmacro\lastz{\Vz}
\global\let\lastx\lastx
\global\let\lasty\lasty
\global\let\lastz\lastz
} % end inner for loop
} % end outer for loop



% loxodrome
\tdplottransformrotmain{\loxodromeX{-1800}}{\loxodromeY{-1800}}{\loxodromeZ{-1800}}
\pgfmathsetmacro\lastx{\tdplotresx}\pgfmathsetmacro\lasty{\tdplotresy}\pgfmathsetmacro\lastz{\tdplotresz}
\foreach \Vt in {-1800,-1790,...,1800}{
\tdplottransformrotmain{\loxodromeX{\Vt}}{\loxodromeY{\Vt}}{\loxodromeZ{\Vt}}
\pgfmathsetmacro\Vx{\tdplotresx}
\pgfmathsetmacro\Vy{\tdplotresy}
\pgfmathsetmacro\Vz{\tdplotresz}
 % Viewing direction components
        \pgfmathsetmacro\viewdirX{\sphereX{-\azimuth}{90 - \polar}} % Adjusting Z component
        \pgfmathsetmacro\viewdirY{\sphereY{-\azimuth}{90 - \polar}} % Adjusting Z component
        \pgfmathsetmacro\viewdirZ{\sphereZ{-\azimuth}{90 - \polar}} % Adjusting Z component

        \pgfmathsetmacro\currentDotProduct{\lastx*\viewdirX + \lasty*\viewdirY + \lastz*\viewdirZ} % Dot product with the viewer direction

        % Check if the dot product is positive
        \ifdim\currentDotProduct pt > -0.3 pt
        \ifdim\lastz pt>-0.049pt
        \ifdim\Vz pt>-0.049pt
\draw[very thin,red] (\lastx,\lasty,\lastz) -- (\Vx,\Vy,\Vz);
\fi\fi
\fi
\pgfmathsetmacro\lastx{\Vx}
\pgfmathsetmacro\lasty{\Vy}
\pgfmathsetmacro\lastz{\Vz}
\global\let\lastx\lastx
\global\let\lasty\lasty
\global\let\lastz\lastz
}% end foreach








} % end pgfextra
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
    for theta in np.linspace(0,60,numiter):
        with open(animatetex.TeX_file, 'w') as TeX:
            TeX.write(preamble)
            TeX.write(r'\newcommand{\VT}{' +f'{theta}' +'}')
            TeX.write(postscript)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()