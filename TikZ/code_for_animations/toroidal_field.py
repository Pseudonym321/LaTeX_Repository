
import numpy as np
import Animation_Modules.animatetex as animatetex
numiter = 24
start= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty
\usepackage{tikz,tikz-3dplot}
\usetikzlibrary{spath3}
%%% COMMANDS %%%
\newcommand{\Clat}[1]{(1/cos(#1))}
\newcommand{\Rlat}[1]{(sqrt((1/(cos(#1))^2)-abs(cos(#1))))}
\newcommand{\Clon}[1]{(-sin(#1)/cos(#1))}
\newcommand{\Rlon}[1]{(1/cos(#1))}
'''
end = r'''
\begin{document}
\centering
\tdplotsetmaincoords{60}{\Vazi}
\begin{tikzpicture}[tdplot_main_coords]
%%% AXES %%%
%\draw[-latex] (-3,0,0) -- (3,0,0) node[pos=1]{$x$};
%\draw[-latex] (0,-3,0) -- (0,3,0) node[pos=1]{$y$};
%\draw[-latex] (0,0,-3) -- (0,0,3) node[pos=1]{$z$};



\draw[tdplot_screen_coords,white] (-5,-4) rectangle (5,4.5);
\clip[tdplot_screen_coords] (-5,-4) rectangle (5,4);



%%% 60 TORUS %%%
\foreach \Vt in {0,30,60,87,93,120,150,180}{
%%% LONGITUDE %%%
\foreach \Vtheta in {0,10,...,350}{
\tdplotsetrotatedcoords{\Vtheta+90}{0}{0}
\draw[tdplot_rotated_coords,domain=0:360,smooth,variable=\Vp,very thin] plot (0,{\Rlat{\Vt}*sin(\Vp)+\Clat{\Vt}},{\Rlat{\Vt}*cos(\Vp)});
}
%%% LATITUDE %%%
\foreach \Vtheta in {0,10,...,350}{
\draw[domain=0:360,smooth,variable=\Vp,very thin] plot ({\Rlon{\Vt}+cos(\Vtheta)*\Rlat{\Vt})*sin(\Vp)},{\Rlon{\Vt}+cos(\Vtheta)*\Rlat{\Vt})*cos(\Vp)},{\Rlat{\Vt}*sin(\Vtheta)});
}

%\def \Vn {7}
%\def \Vq {40}
%\draw[domain=0:360,samples=1000,red,smooth,variable=\Vp] plot ({((1/(cos(\Vt)))+(sqrt((1/((cos(\Vt))^2))-cos(\Vt))*cos(\Vn*\Vp)))*cos(\Vq*\Vp)},{((1/(cos(\Vt)))+(sqrt((1/((cos(\Vt))^2))-cos(\Vt))*cos(\Vn*\Vp)))*sin(\Vq*\Vp)},0{sqrt((1/((cos(\Vt))^2))-cos(\Vt))*sin(\Vn*\Vp)});

%%% 60 SPHERE %%%
%%% LATITUDE %%%
\foreach \Vtheta in {0,10,...,350}{
\tdplotsetrotatedcoords{\Vtheta}{0}{0}
\draw[tdplot_rotated_coords,variable=\Vp,smooth,domain=0:360,very thin] plot ({\Rlon{\Vt}*cos(\Vp)},{0},{\Rlon{\Vt}*sin(\Vp)+\Clon{\Vt}});
}
%%% LONGITUDE %%%
\foreach \Vtheta in {0,10,...,350}{
\draw[variable=\Vp,smooth,domain=0:360,very thin] plot ({sin(\Vtheta)*\Rlon{\Vt}*cos(\Vp)},{sin(\Vtheta)*\Rlon{\Vt}*sin(\Vp)},{\Clon{\Vt}+\Rlon{\Vt}*cos(\Vtheta)});
}
}

\end{tikzpicture}


\end{document}
'''

def main():
    animatetex.before_loop()
    for angle in np.linspace(0,360,numiter):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(start)
            f.write(r'\newcommand{\Vazi}{' +f'{angle}' +'}')
            f.write(end)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()