# Name: Jasper
# Date: 2024
# Title: 
# Credit: https://tex.stackexchange.com/a/726815/319072

import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

start= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty
\usepackage{tikz}
\usetikzlibrary{spath3}
\usepackage{tikz-3dplot}
\begin{document}

'''

end = r'''
\begin{frame}
\centering
\tdplotsetmaincoords{60}{120}
\begin{tikzpicture}[tdplot_main_coords]


\tdplotsetrotatedcoords{0}{2*\Vn}{3*\Vn}

\foreach \Vt in {0,0.2,...,4}{
\draw[ultra thin] (\Vt,0,0) -- (\Vt,4,0);
\draw[ultra thin] (0,\Vt,0) -- (4,\Vt,0);

\draw[ultra thin] (\Vt,0,0) -- (\Vt,0,4);
\draw[ultra thin] (0,0,\Vt) -- (4,0,\Vt);

\draw[ultra thin] (0,\Vt,0) -- (0,\Vt,4);
\draw[ultra thin] (0,0,\Vt) -- (0,4,\Vt);

}
\foreach \Vi in {0,30,...,330}{

\path[tdplot_rotated_coords,spath/save=pathname]
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(0)}{0.5*cos(\Vi)*sin(0)}{0.5*sin(\Vi)}} (\tdplotresx,\tdplotresy,\tdplotresz)
 foreach \t in {30,60,...,330}{ 
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(\t)}{0.5*cos(\Vi)*sin(\t)}{0.5*sin(\Vi)}} -- (\tdplotresx,\tdplotresy,\tdplotresz) 
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(\t+30)}{0.5*cos(\Vi)*sin(\t+30)}{0.5*sin(\Vi)}} -- (\tdplotresx,\tdplotresy,\tdplotresz)};
\draw[spath/use={pathname,transform={shift={(2,2,2)}}}];

\path[tdplot_rotated_coords,spath/save=pathname]
\pgfextra{\tdplottransformrotmain{0.5*cos(0)*cos(\Vi)}{0.5*cos(0)*sin(\Vi)}{0.5*sin(0)}} (\tdplotresx,\tdplotresy,\tdplotresz)
 foreach \t in {30,60,...,330}{ 
\pgfextra{\tdplottransformrotmain{0.5*cos(\t)*cos(\Vi)}{0.5*cos(\t)*sin(\Vi)}{0.5*sin(\t)}} -- (\tdplotresx,\tdplotresy,\tdplotresz) 
\pgfextra{\tdplottransformrotmain{0.5*cos(\t+30)*cos(\Vi)}{0.5*cos(\t+30)*sin(\Vi)}{0.5*sin(\t)}} -- (\tdplotresx,\tdplotresy,\tdplotresz)};
\draw[spath/use={pathname,transform={shift={(2,2,2)}}}];
}


\foreach \Vi in {0,30,...,330}{

\path[tdplot_rotated_coords,spath/save=pathname]
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(0)}{0.5*cos(\Vi)*sin(0)}{0.5*sin(\Vi)}} (\tdplotresx,\tdplotresy,0)
 foreach \t in {30,60,...,330}{ 
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(\t)}{0.5*cos(\Vi)*sin(\t)}{0.5*sin(\Vi)}} -- (\tdplotresx,\tdplotresy,0) 
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(\t+30)}{0.5*cos(\Vi)*sin(\t+30)}{0.5*sin(\Vi)}} -- (\tdplotresx,\tdplotresy,0)};
\draw[spath/use={pathname,transform={shift={(2,2,0)}}}];

\path[tdplot_rotated_coords,spath/save=pathname]
\pgfextra{\tdplottransformrotmain{0.5*cos(0)*cos(\Vi)}{0.5*cos(0)*sin(\Vi)}{0.5*sin(0)}} (\tdplotresx,\tdplotresy,0)
 foreach \t in {30,60,...,330}{ 
\pgfextra{\tdplottransformrotmain{0.5*cos(\t)*cos(\Vi)}{0.5*cos(\t)*sin(\Vi)}{0.5*sin(\t)}} -- (\tdplotresx,\tdplotresy,0) 
\pgfextra{\tdplottransformrotmain{0.5*cos(\t+30)*cos(\Vi)}{0.5*cos(\t+30)*sin(\Vi)}{0.5*sin(\t)}} -- (\tdplotresx,\tdplotresy,0)};
\draw[spath/use={pathname,transform={shift={(2,2,0)}}}];
}

\foreach \Vi in {0,30,...,330}{

\path[tdplot_rotated_coords,spath/save=pathname]
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(0)}{0.5*cos(\Vi)*sin(0)}{0.5*sin(\Vi)}} (\tdplotresx,0,\tdplotresz)
 foreach \t in {30,60,...,330}{ 
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(\t)}{0.5*cos(\Vi)*sin(\t)}{0.5*sin(\Vi)}} -- (\tdplotresx,0,\tdplotresz) 
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(\t+30)}{0.5*cos(\Vi)*sin(\t+30)}{0.5*sin(\Vi)}} -- (\tdplotresx,0,\tdplotresz)};
\draw[spath/use={pathname,transform={shift={(2,0,2)}}}];

\path[tdplot_rotated_coords,spath/save=pathname]
\pgfextra{\tdplottransformrotmain{0.5*cos(0)*cos(\Vi)}{0.5*cos(0)*sin(\Vi)}{0.5*sin(0)}} (\tdplotresx,0,\tdplotresz)
 foreach \t in {30,60,...,330}{ 
\pgfextra{\tdplottransformrotmain{0.5*cos(\t)*cos(\Vi)}{0.5*cos(\t)*sin(\Vi)}{0.5*sin(\t)}} -- (\tdplotresx,0,\tdplotresz) 
\pgfextra{\tdplottransformrotmain{0.5*cos(\t+30)*cos(\Vi)}{0.5*cos(\t+30)*sin(\Vi)}{0.5*sin(\t)}} -- (\tdplotresx,0,\tdplotresz)};
\draw[spath/use={pathname,transform={shift={(2,0,2)}}}];
}

\foreach \Vi in {0,30,...,330}{

\path[tdplot_rotated_coords,spath/save=pathname]
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(0)}{0.5*cos(\Vi)*sin(0)}{0.5*sin(\Vi)}} (0,\tdplotresy,\tdplotresz)
 foreach \t in {30,60,...,330}{ 
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(\t)}{0.5*cos(\Vi)*sin(\t)}{0.5*sin(\Vi)}} -- (0,\tdplotresy,\tdplotresz) 
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vi)*cos(\t+30)}{0.5*cos(\Vi)*sin(\t+30)}{0.5*sin(\Vi)}} -- (0,\tdplotresy,\tdplotresz)};
\draw[spath/use={pathname,transform={shift={(0,2,2)}}}];

\path[tdplot_rotated_coords,spath/save=pathname]
\pgfextra{\tdplottransformrotmain{0.5*cos(0)*cos(\Vi)}{0.5*cos(0)*sin(\Vi)}{0.5*sin(0)}} (0,\tdplotresy,\tdplotresz)
 foreach \t in {30,60,...,330}{ 
\pgfextra{\tdplottransformrotmain{0.5*cos(\t)*cos(\Vi)}{0.5*cos(\t)*sin(\Vi)}{0.5*sin(\t)}} -- (0,\tdplotresy,\tdplotresz) 
\pgfextra{\tdplottransformrotmain{0.5*cos(\t+30)*cos(\Vi)}{0.5*cos(\t+30)*sin(\Vi)}{0.5*sin(\t)}} -- (0,\tdplotresy,\tdplotresz)};
\draw[spath/use={pathname,transform={shift={(0,2,2)}}}];
}

\end{tikzpicture}
\end{frame}
\end{document}
'''


def main():
    animatetex.before_loop()
    for angle in np.linspace(15,100,numiter):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(start)
            f.write(r'\def \Vn {' + f'{angle}' + '}')
            f.write(end)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()