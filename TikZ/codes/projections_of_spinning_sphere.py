
# Credit: I used code from https://tex.stackexchange.com/a/726815/319072 
# to overcome a barrier with the projections.

import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

start= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty
\usepackage{tikz,tikz-3dplot}
\usetikzlibrary{hobby,arrows.meta}
\newif\ifdrawAxes
\pgfqkeys{/drawaxes}{show axes/.is if=drawAxes}
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
    \ifdrawAxes
      \draw[-Classical TikZ Rightarrow] (0,0) -- (#2,0);
      \draw[-Classical TikZ Rightarrow] (0,0) -- (0,#3);
      \draw[-Classical TikZ Rightarrow] (0,0) -- (0,0,#4);
    \fi
  }

'''

end = r'''
\begin{document}
  \begin{frame}
    \centering
    \tdplotsetmaincoords{60}{120}
    \begin{tikzpicture}[tdplot_main_coords]

      \tdplotsetrotatedcoords{2*\Vn}{1*\Vn}{3*\Vn}
      \coordinate (Shift) at (2,2,2);
      \tdplotsetrotatedcoordsorigin{(Shift)}

      \xyzGrid[show axes]{4}{4}{4}

      \foreach \Vi in {-90,-70,...,90}{
        \draw[tdplot_rotated_coords]
          (
            {0.5*cos(\Vi)*cos(0)},
            {0.5*cos(\Vi)*sin(0)},
            {0.5*sin(\Vi)}
          )
        foreach \t in {20,40,...,340}{ 
        -- 
          (
            {0.5*cos(\Vi)*cos(\t)},
            {0.5*cos(\Vi)*sin(\t)},
            {0.5*sin(\Vi)}
          )
        } 
        -- cycle;
        \draw[tdplot_rotated_coords]
          (
            {0.5*cos(0)*cos(\Vi)},
            {0.5*cos(0)*sin(\Vi)},
            {0.5*sin(0)}
          )
        foreach \t in {20,40,...,340}{ 
        -- 
          (
            {0.5*cos(\t)*cos(\Vi)},
            {0.5*cos(\t)*sin(\Vi)},
            {0.5*sin(\t)}
          )
        } 
        -- cycle;
      }


      \foreach \Vi in {-90,-60,...,90}{
        \draw[shift={(0,2,2)}]
        \pgfextra{
          \tdplottransformrotmain
          {0.5*cos(\Vi)*cos(0)}
          {0.5*cos(\Vi)*sin(0)}
          {0.5*sin(\Vi)}
        } 
        
        (0,\tdplotresy,\tdplotresz)
        foreach \t in {20,40,...,340}{ 
          \pgfextra{
            \tdplottransformrotmain
            {0.5*cos(\Vi)*cos(\t)}
            {0.5*cos(\Vi)*sin(\t)}
            {0.5*sin(\Vi)}
          } 
          -- 
          (0,\tdplotresy,\tdplotresz)
        } 
        -- cycle;
        \draw[shift={(0,2,2)}]
        \pgfextra{
        \tdplottransformrotmain
        {0.5*cos(0)*cos(\Vi)}
        {0.5*cos(0)*sin(\Vi)}
        {0.5*sin(0)}} 
        (0,\tdplotresy,\tdplotresz)
        foreach \t in {20,40,...,340}{ 
          \pgfextra{
            \tdplottransformrotmain
            {0.5*cos(\t)*cos(\Vi)}
            {0.5*cos(\t)*sin(\Vi)}
            {0.5*sin(\t)}
          } 
          -- 
          (0,\tdplotresy,\tdplotresz)
        } 
        -- cycle;
      }

      \foreach \Vi in {-90,-60,...,90}{
        \draw[shift={(2,0,2)}]
        \pgfextra{
          \tdplottransformrotmain
          {0.5*cos(\Vi)*cos(0)}
          {0.5*cos(\Vi)*sin(0)}
          {0.5*sin(\Vi)}
        } 
        (\tdplotresx,0,\tdplotresz)
        foreach \t in {20,40,...,340}{ 
          \pgfextra{
            \tdplottransformrotmain
            {0.5*cos(\Vi)*cos(\t)}
            {0.5*cos(\Vi)*sin(\t)}
            {0.5*sin(\Vi)}
          } 
          -- 
          (\tdplotresx,0,\tdplotresz)
        } -- cycle;
        \draw[shift={(2,0,2)}]
        \pgfextra{
          \tdplottransformrotmain
          {0.5*cos(0)*cos(\Vi)}
          {0.5*cos(0)*sin(\Vi)}
          {0.5*sin(0)}
        } 
        (\tdplotresx,0,\tdplotresz)
        foreach \t in {20,40,...,340}{ 
          \pgfextra{
            \tdplottransformrotmain
            {0.5*cos(\t)*cos(\Vi)}
            {0.5*cos(\t)*sin(\Vi)}
            {0.5*sin(\t)}
          } 
          -- 
          (\tdplotresx,0,\tdplotresz)
        } -- cycle;
      }

      \foreach \Vi in {-90,-60,...,90}{
        \draw[shift={(2,2,0)}]
        \pgfextra{
          \tdplottransformrotmain
          {0.5*cos(\Vi)*cos(0)}
          {0.5*cos(\Vi)*sin(0)}
          {0.5*sin(\Vi)}
        } 
        (\tdplotresx,\tdplotresy,0)
        foreach \t in {20,40,...,340}{ 
        \pgfextra{
          \tdplottransformrotmain
          {0.5*cos(\Vi)*cos(\t)}
          {0.5*cos(\Vi)*sin(\t)}
          {0.5*sin(\Vi)}
        } 
        -- 
        (\tdplotresx,\tdplotresy,0)
        } 
        -- cycle;
        \draw[shift={(2,2,0)}]
        \pgfextra{
          \tdplottransformrotmain
          {0.5*cos(0)*cos(\Vi)}
          {0.5*cos(0)*sin(\Vi)}
          {0.5*sin(0)}
        } 
        (\tdplotresx,\tdplotresy,0)
        foreach \t in {20,40,...,340}{ 
          \pgfextra{
            \tdplottransformrotmain
            {0.5*cos(\t)*cos(\Vi)}
            {0.5*cos(\t)*sin(\Vi)}
            {0.5*sin(\t)}
          } 
          -- 
          (\tdplotresx,\tdplotresy,0)
        } -- cycle;
      }

    \end{tikzpicture}
  \end{frame}
\end{document}
'''


def main():
    animatetex.before_loop()
    for angle in np.linspace(15,180,numiter):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(start)
            f.write(r'\def \Vn {' + f'{angle}' + '}')
            f.write(end)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()