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
\newcommand{\azimuth}{30}
\newcommand{\polar}{60}
'''

postscript = r'''
\begin{document}
\begin{frame}
\centering
\tdplotsetmaincoords{\polar}{\azimuth}

\begin{tikzpicture}[tdplot_main_coords,scale=0.333]

\clip[tdplot_screen_coords,scale=3] (-3.5,-2.5) rectangle (3.5,2.5);
\draw[white,tdplot_screen_coords,scale=3] (-3.5,-2.5) rectangle (3.5,2.5);

\pgfmathsetmacro\viewdirX{\sphereX{-\azimuth}{90 - \polar}} % Adjusting Z component
\pgfmathsetmacro\viewdirY{\sphereY{-\azimuth}{90 - \polar}} % Adjusting Z component
\pgfmathsetmacro\viewdirZ{\sphereZ{-\azimuth}{90 - \polar}} % Adjusting Z component
\tdplotsetrotatedcoords{\VT}{\VT}{\VT}

\begin{scope}[shift={(0,0,-5)}]
\foreach \Vt in {0,10,...,720}{
\draw[ultra thin,variable=\Vtt,domain=90:360,tdplot_rotated_coords] plot ({\sphereX{\Vt}{\Vtt}+4*cos(\Vt)},{\sphereY{\Vt}{\Vtt}+4*sin(\Vt)},{\sphereZ{\Vt}{\Vtt}+5*\Vt/360});
}





\foreach \Vt in {90,100,...,360}{
\draw[ultra thin,variable=\Vtt,domain=0:720,samples=80,tdplot_rotated_coords] plot ({4*cos(\Vtt)+cos(\Vt)*cos(\Vtt)},{4*sin(\Vtt)+cos(\Vt)*sin(\Vtt)},{5*\Vtt/360+sin(\Vt)});
}


\foreach \Vt in {10,20,...,720}{
\pgfmathsetmacro\lastix{\sphereX{\Vt-10}{90}+4*cos(\Vt-10)}
\pgfmathsetmacro\lastiy{\sphereY{\Vt-10}{90}+4*sin(\Vt-10)}
\pgfmathsetmacro\lastiz{\sphereZ{\Vt-10}{90}+5*(\Vt-10)/360}
\tdplottransformrotmain{\lastix}{\lastiy}{\lastiz}
\pgfmathsetmacro\lastix{\tdplotresx}
\pgfmathsetmacro\lastiy{\tdplotresy}
\pgfmathsetmacro\lastiz{\tdplotresz}

\foreach \Vtt[
    remember=\Vxth as \lastx (initially \lastix),
    remember=\Vyth as \lasty (initially \lastiy),
    remember=\Vzth as \lastz (initially \lastiz),
] in {90,100,...,350}{
% one
\pgfmathsetmacro\Vxo{\sphereX{\Vt}{\Vtt}+4*cos(\Vt)}
\pgfmathsetmacro\Vyo{\sphereY{\Vt}{\Vtt}+4*sin(\Vt)}
\pgfmathsetmacro\Vzo{\sphereZ{\Vt}{\Vtt}+5*\Vt/360}
\tdplottransformrotmain{\Vxo}{\Vyo}{\Vzo}
\pgfmathsetmacro\Vxo{\tdplotresx}
\pgfmathsetmacro\Vyo{\tdplotresy}
\pgfmathsetmacro\Vzo{\tdplotresz}

\pgfmathsetmacro\Vxt{\sphereX{\Vt}{\Vtt+10}+4*cos(\Vt)}
\pgfmathsetmacro\Vyt{\sphereY{\Vt}{\Vtt+10}+4*sin(\Vt)}
\pgfmathsetmacro\Vzt{\sphereZ{\Vt}{\Vtt+10}+5*\Vt/360}
\tdplottransformrotmain{\Vxt}{\Vyt}{\Vzt}
\pgfmathsetmacro\Vxt{\tdplotresx}
\pgfmathsetmacro\Vyt{\tdplotresy}
\pgfmathsetmacro\Vzt{\tdplotresz}

\pgfmathsetmacro\Vxth{\sphereX{\Vt-10}{\Vtt+10}+4*cos(\Vt-10)}
\pgfmathsetmacro\Vyth{\sphereY{\Vt-10}{\Vtt+10}+4*sin(\Vt-10)}
\pgfmathsetmacro\Vzth{\sphereZ{\Vt-10}{\Vtt+10}+5*(\Vt-10)/360}
\tdplottransformrotmain{\Vxth}{\Vyth}{\Vzth}
\pgfmathsetmacro\Vxth{\tdplotresx}
\pgfmathsetmacro\Vyth{\tdplotresy}
\pgfmathsetmacro\Vzth{\tdplotresz}

\pgfmathsetmacro\currentDotProduct{\lastx*\viewdirX + \lasty*\viewdirY + \lastz*\viewdirZ} % Dot product with the viewer direction
\ifdim\currentDotProduct pt > 0 pt
% these are the little rectangles
\draw[fill,white] (\lastx,\lasty,\lastz) -- ({\Vxo},{\Vyo},{\Vzo}) -- ({\Vxt},{\Vyt},{\Vzt}) -- ({\Vxth},{\Vyth},{\Vzth});
\draw[fill,opacity=0.5] (\lastx,\lasty,\lastz) -- ({\Vxo},{\Vyo},{\Vzo}) -- ({\Vxt},{\Vyt},{\Vzt}) -- ({\Vxth},{\Vyth},{\Vzth});
\fi
%\pgfmathsetmacro\lastx{\Vxth}
%\pgfmathsetmacro\lasty{\Vyth}
%\pgfmathsetmacro\lastz{\Vzth}
%\global\let\lastx\lastx
%\global\let\lasty\lasty
%\global\let\lastz\lastz

}
\draw[red,thick,tdplot_rotated_coords] ({4*cos(\Vt-10)},{4*sin(\Vt-10)},{5*(\Vt-10)/360}) -- ({4*cos(\Vt)},{4*sin(\Vt)},{5*\Vt/360});
}
\end{scope}

\end{tikzpicture}
\end{frame}
\end{document}
'''

def main():
    """
    Purpose:
        Makes an animation of the rectangular dot product
    Parameters:
        No parameters.
    Return:
        Void.
    """
    animatetex.before_loop()
    for angle in np.linspace(0,60,numiter):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(preamble)
            f.write(r'\newcommand{\VT}{' +f'{-angle}' +'}')
            f.write(postscript)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()