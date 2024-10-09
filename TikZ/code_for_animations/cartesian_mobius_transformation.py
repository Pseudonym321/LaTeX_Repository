
import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

start= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty
\usepackage{tikz}
\usepackage{tikz-3dplot}
\newcommand{\sphereX}[2]{cos(#2)*cos(#1)}
\newcommand{\sphereY}[2]{cos(#2)*sin(#1)}
\newcommand{\sphereZ}[2]{sin(#2)}
\newcommand{\SPX}[2]{#1/(1-#2)}
\newcommand{\SPY}[2]{#1/(1-#2)}
\newcommand{\ISPX}[2]{2*(#1)/(1+(#1)^2+(#2)^2)}
\newcommand{\ISPY}[2]{2*(#2)/(1+(#1)^2+(#2)^2)}
\newcommand{\ISPZ}[2]{(-1+(#1)^2+(#2)^2)/(1+(#1)^2+(#2)^2)}
'''
end = r'''

\begin{document}
\begin{frame}
\centering
\tdplotsetmaincoords{60}{45}
\begin{tikzpicture}[tdplot_main_coords,scale=0.5]
\clip[tdplot_screen_coords,scale=2] (-3.5,-2.5) rectangle (3.5,2.5);
\draw[white,tdplot_screen_coords,scale=2] (-3.5,-2.5) rectangle (3.5,2.5);
\tdplotsetrotatedcoords{\VT}{\VT}{\VT}

\foreach \Vn in {-10,-9.6,...,10}{
\draw[tdplot_rotated_coords,smooth,variable=\Vt,domain=-10:10,samples=100] plot ({\ISPX{\Vn}{\Vt}},{\ISPY{\Vn}{\Vt}},{\ISPZ{\Vn}{\Vt}});
\draw[tdplot_rotated_coords,smooth,variable=\Vt,domain=-10:10,samples=100] plot ({\ISPX{\Vt}{\Vn}},{\ISPY{\Vt}{\Vn}},{\ISPZ{\Vt}{\Vn}});

\pgfextra{
\gdef\opacity{1}
\tdplottransformrotmain{\ISPX{\Vn}{-10}}{\ISPY{\Vn}{-10}}{\ISPZ{\Vn}{-10}}
\ifdim\tdplotresz pt<0.999pt
\pgfmathsetmacro\lastx{\SPX{\tdplotresx}{\tdplotresz}}
\pgfmathsetmacro\lasty{\SPY{\tdplotresy}{\tdplotresz}}
\fi
\foreach \Vnn in {-10,-9.8,...,10}{
\typeout\Vn
\typeout\Vnn
\tdplottransformrotmain{\ISPX{\Vn}{\Vnn}}{\ISPY{\Vn}{\Vnn}}{\ISPZ{\Vn}{\Vnn}}
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
}}}








\foreach \Vn in {-10,-9.6,...,10}{
%\draw[tdplot_rotated_coords,smooth,variable=\Vt,domain=-10:10,samples=100] plot ({\ISPX{\Vn}{\Vt}},{\ISPY{\Vn}{\Vt}},{\ISPZ{\Vn}{\Vt}});
%\draw[tdplot_rotated_coords,smooth,variable=\Vt,domain=-10:10,samples=100] plot ({\ISPX{\Vt}{\Vn}},{\ISPY{\Vt}{\Vn}},{\ISPZ{\Vt}{\Vn}});

\pgfextra{
\gdef\opacity{1}
\tdplottransformrotmain{\ISPX{-10}{\Vn}}{\ISPY{-10}{\Vn}}{\ISPZ{-10}{\Vn}}
\ifdim\tdplotresz pt<0.999pt
\pgfmathsetmacro\lastx{\SPX{\tdplotresx}{\tdplotresz}}
\pgfmathsetmacro\lasty{\SPY{\tdplotresy}{\tdplotresz}}
\fi
\foreach \Vnn in {-10,-9.8,...,10}{
\typeout\Vn
\typeout\Vnn
\tdplottransformrotmain{\ISPX{\Vnn}{\Vn}}{\ISPY{\Vnn}{\Vn}}{\ISPZ{\Vnn}{\Vn}}
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
}}}
\end{tikzpicture}
\end{frame}
\end{document}
'''

def main():
  """
    Purpose:
        Makes an animation of the cross product of a fixed vector and another one which
        follows the trajectory of a loxodrome.
    Parameters:
        No parameters.
    Return:
        Void.
    """
  animatetex.before_loop()
  for angle in np.linspace(0,40,numiter):
      with open(animatetex.TeX_file, 'w') as f:
          f.write(start)
          f.write(r'\newcommand{\VT}{' +f'{angle}' +'}\n')
          f.write(end)
      animatetex.during_loop()
  animatetex.after_loop()

if __name__ == "__main__":
    main()