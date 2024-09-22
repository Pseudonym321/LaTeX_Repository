
import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

preamble= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty
\usepackage{tikz}
\usetikzlibrary{spath3}
\usepackage{tikz-3dplot}

\usetikzlibrary{arrows.meta,decorations.pathreplacing}
\usetikzlibrary{calc}

\newcommand\xyzGrid[4][]
  {%
    % Draws a grid in the x-y plane.
    % #1  - optional axis
    % #2  - xmin
    % #3  - xmax
    % #4  - ymin
    % #5  - ymax
    \pgfqkeys{/drawaxes}{#1}%
    % xy small
    \foreach[parse=true] \Vx in {0.2,0.4,...,#2-0.2}{\draw[very thin,densely dotted] (\Vx,0) -- (\Vx,#3);}
    \foreach[parse=true] \Vy in {0.2,0.4,...,#3-0.2}{\draw[very thin,densely dotted] (0,\Vy) -- (#2,\Vy);}
    % xy big
    \foreach[parse=true] \Vx in {1,2,...,#2-1}{\draw[thin,densely dotted] (\Vx,0) -- (\Vx ,#3);}
    \foreach[parse=true] \Vy in {1,2,...,#3-1}{\draw[thin,densely dotted] (0,\Vy) -- (#2,\Vy);}
    % xz small
    \foreach[parse=true] \Vx in {0.2,0.4,...,#2-0.2}{\draw[very thin,densely dotted] (\Vx,0,0) -- (\Vx,0,#4);}
    \foreach[parse=true] \Vz in {0.2,0.4,...,#4-0.2}{\draw[very thin,densely dotted] (0,0,\Vz) -- (#2,0,\Vz);}
    % xz big
    \foreach[parse=true] \Vx in {1,2,...,#2-1}{\draw[thin,densely dotted] (\Vx,0,0) -- (\Vx,0,#4);}
    \foreach[parse=true] \Vz in {1,2,...,#2-1}{\draw[thin,densely dotted] (0,0,\Vz) -- (#2,0,\Vz);}
    % yz small
    \foreach[parse=true] \Vy in {0.2,0.4,...,#3-0.2}{\draw[very thin,densely dotted] (0,\Vy,0) -- (0,\Vy,#4);}
    \foreach[parse=true] \Vz in {0.2,0.4,...,#4-0.2}{\draw[very thin,densely dotted] (0,0,\Vz) -- (0,#3,\Vz);}
    % yz big
    \foreach[parse=true] \Vy in {1,2,...,#3-1}{\draw[thin,densely dotted] (0,\Vy,0) -- (0,\Vy,#4);}
    \foreach[parse=true] \Vz in {1,2,...,#4-1}{\draw[thin,densely dotted] (0,0,\Vz) -- (0,#3,\Vz);}
    %

      \draw[-Classical TikZ Rightarrow] (0,0) -- (#2,0);
      \draw[-Classical TikZ Rightarrow] (0,0) -- (0,#3);
      \draw[-Classical TikZ Rightarrow] (0,0) -- (0,0,#4);

  }
\begin{document}
\begin{frame}
\centering
\tdplotsetmaincoords{60}{120}
\begin{tikzpicture}[tdplot_main_coords,scale=0.5]
\xyzGrid[show axes]{10}{10}{10}


'''

postscript = r'''
\tdplotsetrotatedcoords{\VarTheta}{20}{0}


%same circle with points
\path[tdplot_rotated_coords,spath/save=name]
({0.5*cos(0)},{0.5*sin(0)},0)
foreach \t in {10,20,...,350}{
-- ({0.5*cos(\t)},{0.5*sin(\t)},0) -- ({0.5*cos(\t+10)},{0.5*sin(\t+10)},0)
};
\draw[,spath/use={name, transform={shift={(0.5*5,0.5*5,0.5*3)}}}];

%projection of these points on main xy plane
\path[tdplot_rotated_coords,spath/save=name]
 \pgfextra{\tdplottransformrotmain{0.5*cos(0)}{0.5*sin(0)}{0}} (\tdplotresx,\tdplotresy,0)
 foreach \t in {10,20,...,350}{ 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t)}{0.5*sin(\t)}{0}} -- (\tdplotresx,\tdplotresy,0) 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t+10)}{0.5*sin(\t+10)}{0}} -- (\tdplotresx,\tdplotresy,0)};
\draw[,spath/use={name, transform={shift={(0.5*5,0.5*5,0)}}}];

%projection of these points on main xz plane
\path[tdplot_rotated_coords,spath/save=name]
 \pgfextra{\tdplottransformrotmain{0.5*cos(0)}{0.5*sin(0)}{0}} (\tdplotresx,0,\tdplotresz)
 foreach \t in {10,20,...,350}{ 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t)}{0.5*sin(\t)}{0}} -- (\tdplotresx,0,\tdplotresz) 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t+10)}{0.5*sin(\t+10)}{0}} -- (\tdplotresx,0,\tdplotresz)};
\draw[,spath/use={name, transform={shift={(0.5*5,0,0.5*3)}}}];

%projection of these points on main yz plane
\path[tdplot_rotated_coords,spath/save=name]
 \pgfextra{\tdplottransformrotmain{0.5*cos(0)}{0.5*sin(0)}{0}} (0,\tdplotresy,\tdplotresz)
 foreach \t in {10,20,...,350}{ 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t)}{0.5*sin(\t)}{0}} -- (0,\tdplotresy,\tdplotresz)
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t+10)}{0.5*sin(\t+10)}{0}} -- (0,\tdplotresy,\tdplotresz)};
\draw[,spath/use={name, transform={shift={(0.5*0,0.5*5,0.5*3)}}}];



%same circle with points 2
\path[tdplot_rotated_coords,spath/save=name]
({0.5*cos(0)},{0.5*sin(0)},3)
foreach \t in {10,20,...,350}{
-- ({0.5*cos(\t)},{0.5*sin(\t)},3) -- ({0.5*cos(\t+10)},{0.5*sin(\t+10)},3)
};
\draw[,spath/use={name, transform={shift={(0.5*5,0.5*5,0.5*3)}}}];

%projection of these points on main xy plane
\path[tdplot_rotated_coords,spath/save=name]
 \pgfextra{\tdplottransformrotmain{0.5*cos(0)}{0.5*sin(0)}{3}} (\tdplotresx,\tdplotresy,0)
 foreach \t in {10,20,...,350}{ 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t)}{0.5*sin(\t)}{3}} -- (\tdplotresx,\tdplotresy,0) 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t+10)}{0.5*sin(\t+10)}{3}} -- (\tdplotresx,\tdplotresy,0)};
\draw[,spath/use={name, transform={shift={(0.5*5,0.5*5,0)}}}];

%projection of these points on main xz plane
\path[tdplot_rotated_coords,spath/save=name]
 \pgfextra{\tdplottransformrotmain{0.5*cos(0)}{0.5*sin(0)}{3}} (\tdplotresx,0,\tdplotresz)
 foreach \t in {10,20,...,350}{ 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t)}{0.5*sin(\t)}{3}} -- (\tdplotresx,0,\tdplotresz) 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t+10)}{0.5*sin(\t+10)}{3}} -- (\tdplotresx,0,\tdplotresz)};
\draw[,spath/use={name, transform={shift={(0.5*5,0,0.5*3)}}}];

%projection of these points on main yz plane
\path[tdplot_rotated_coords,spath/save=name]
 \pgfextra{\tdplottransformrotmain{0.5*cos(0)}{0.5*sin(0)}{3}} (0,\tdplotresy,\tdplotresz)
 foreach \t in {10,20,...,350}{ 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t)}{0.5*sin(\t)}{3}} -- (0,\tdplotresy,\tdplotresz)
 \pgfextra{\tdplottransformrotmain{0.5*cos(\t+10)}{0.5*sin(\t+10)}{3}} -- (0,\tdplotresy,\tdplotresz)};
\draw[,spath/use={name, transform={shift={(0,0.5*5,0.5*3)}}}];


%%% LINES 1 
\foreach \Vtheta in {0,10,...,350}{
% with points
\path[tdplot_rotated_coords,spath/save=name] 
({0.5*cos(\Vtheta)},{0.5*sin(\Vtheta)},{0}) -- ({0.5*cos(\Vtheta)},{0.5*sin(\Vtheta)},{3}) -- (0,0,4.5);
\draw[,spath/use={name, transform={shift={(0.5*5,0.5*5,0.5*3)}}}];

%projection of these points on main xy plane
\path[tdplot_rotated_coords,spath/save=name]
 \pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{0}} (\tdplotresx,\tdplotresy,0)
 foreach \t in {0}{ 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{0}} -- (\tdplotresx,\tdplotresy,0) 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{3}} -- (\tdplotresx,\tdplotresy,0)
 \pgfextra{\tdplottransformrotmain{0}{0}{4}} -- (\tdplotresx,\tdplotresy,0)};
\draw[,spath/use={name, transform={shift={(0.5*5,0.5*5,0)}}}];

%projection of these points on main xz plane
\path[tdplot_rotated_coords,spath/save=name]
 \pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{0}} (\tdplotresx,0,\tdplotresz)
 foreach \t in {0}{ 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{0}} -- (\tdplotresx,0,\tdplotresz) 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{3}} -- (\tdplotresx,0,\tdplotresz)
 \pgfextra{\tdplottransformrotmain{0}{0}{4}} -- (\tdplotresx,0,\tdplotresz)};
\draw[,spath/use={name, transform={shift={(0.5*5,0,0.5*3)}}}];

%projection of these points on main yz plane
\path[tdplot_rotated_coords,spath/save=name]
 \pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{0}} (0,\tdplotresy,\tdplotresz)
 foreach \t in {0}{ 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{0}} -- (0,\tdplotresy,\tdplotresz) 
 \pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{3}} -- (0,\tdplotresy,\tdplotresz)
 \pgfextra{\tdplottransformrotmain{0}{0}{4}} -- (0,\tdplotresy,\tdplotresz)};
\draw[,spath/use={name, transform={shift={(0,0.5*5,0.5*3)}}}];

}



\foreach \Vtheta in {0,60,...,300}{
% with points
\path[tdplot_rotated_coords,spath/save=name] 
({0.5*cos(\Vtheta)},{0.5*sin(\Vtheta)},{0}) -- ({cos(\Vtheta)},{sin(\Vtheta)},{0}) -- ({cos(\Vtheta)},{sin(\Vtheta)},{1}) -- ({0.5*cos(\Vtheta)},{0.5*sin(\Vtheta)},{1.5});
\draw[spath/use={name, transform={shift={(0.5*5,0.5*5,0.5*3)}}}];

% projection onto xy
\path[tdplot_rotated_coords,spath/save=name]
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{0}} (\tdplotresx,\tdplotresy,0)
 foreach \t in {0}{ 
\pgfextra{\tdplottransformrotmain{cos(\Vtheta)}{sin(\Vtheta)}{0}} -- (\tdplotresx,\tdplotresy,0) 
\pgfextra{\tdplottransformrotmain{cos(\Vtheta)}{sin(\Vtheta)}{1}} -- (\tdplotresx,\tdplotresy,0) 
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{1.5}} -- (\tdplotresx,\tdplotresy,0)};
\draw[,spath/use={name, transform={shift={(0.5*5,0.5*5,0)}}}];

% projection onto xz
\path[tdplot_rotated_coords,spath/save=name]
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{0}} (\tdplotresx,0,\tdplotresz)
 foreach \t in {0}{ 
\pgfextra{\tdplottransformrotmain{cos(\Vtheta)}{sin(\Vtheta)}{0}} -- (\tdplotresx,0,\tdplotresz)
\pgfextra{\tdplottransformrotmain{cos(\Vtheta)}{sin(\Vtheta)}{1}} -- (\tdplotresx,0,\tdplotresz) 
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{1.5}} -- (\tdplotresx,0,\tdplotresz)};
\draw[,spath/use={name, transform={shift={(0.5*5,0,0.5*3)}}}];

% projection onto yz
\path[tdplot_rotated_coords,spath/save=name]
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{0}} (0,\tdplotresy,\tdplotresz)
 foreach \t in {0}{ 
\pgfextra{\tdplottransformrotmain{cos(\Vtheta)}{sin(\Vtheta)}{0}} -- (0,\tdplotresy,\tdplotresz)
\pgfextra{\tdplottransformrotmain{cos(\Vtheta)}{sin(\Vtheta)}{1}} -- (0,\tdplotresy,\tdplotresz) 
\pgfextra{\tdplottransformrotmain{0.5*cos(\Vtheta)}{0.5*sin(\Vtheta)}{1.5}} -- (0,\tdplotresy,\tdplotresz)};
\draw[,spath/use={name, transform={shift={(0,0.5*5,0.5*3)}}}];
}

\end{tikzpicture}
\end{frame}
\end{document}
'''

def main():
    """
    Purpose:
        Makes a spinning bumpy sphere.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    animatetex.before_loop()
    for theta in np.linspace(80,360+80,numiter):
        with open(animatetex.TeX_file, 'w') as TeX:
            TeX.write(preamble)
            TeX.write(r'\newcommand{\VarTheta}{' +f'{theta}' +'}')
            TeX.write(postscript)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()