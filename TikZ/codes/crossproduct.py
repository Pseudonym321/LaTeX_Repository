
import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

start = r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty

\usepackage{physics}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,angles}
\usepackage{tikz-3dplot}

\newcommand{\lengthVOne}{0.75}
\newcommand{\lengthVTwo}{1.75}
'''

end = r'''
\begin{document}
    \centering
    \tdplotsetmaincoords{45}{45}
    \begin{tikzpicture}[tdplot_main_coords]

        \clip[tdplot_screen_coords] (-\textwidth/2,-\textheight/2) rectangle (\textwidth/2,\textheight/2);
        \draw[white,tdplot_screen_coords] (-\textwidth/2,-\textheight/2) rectangle (\textwidth/2,\textheight/2);

        \coordinate (O) at (0,0);
        \coordinate (V1) at (0:\lengthVOne);
        \coordinate (V2) at (\varT:\lengthVTwo);
        \path[draw,white] (-5,-5) -- (5,5);

        \draw[] (\lengthVOne,0) arc [start angle=360, end angle=180, radius=\lengthVOne] -- (\lengthVOne,0) -- cycle;
        \draw[dotted] (-\lengthVOne,0) arc [start angle=180, end angle=0, radius=\lengthVOne];

        \draw[] (0,0) -- (270:\lengthVTwo) arc [start angle=270, end angle=\varT, radius=\lengthVTwo];

        %%% VECTORS %%%
        \draw[-Triangle] (0,0) -- (V2) node[pos=1,above] {$\va{q}$};
        \draw[-Triangle] (0,0) -- (V1) node[pos=1,right] {$\va{p}$};

        %%% GEOMETRY %%%
        \fill[red,opacity=0.2] (0,0) -- ++(\varT:\lengthVOne) -- ++(0,-\lengthVTwo) -- ++(\varT+180:\lengthVOne);
        \draw[] (0,0) -- ++(\varT:\lengthVOne) -- ++(0,-\lengthVTwo) -- ++(\varT+180:\lengthVOne) -- cycle;

        \fill[blue,opacity=0.2] (0,0) -- ++(\varT:\lengthVTwo) -- ++(\lengthVOne,0) -- ++(\varT+180:\lengthVTwo);
        \draw[] (0,0) -- ++(\varT:\lengthVTwo) -- ++(\lengthVOne,0) -- ++(\varT+180:\lengthVTwo) -- cycle;
        \draw[blue,-Triangle] (0,0,0) -- (0,0,{\lengthVOne*\lengthVTwo*sin(\varT)}) node[left]{$\va{p}\cross\va{q}$};
    \end{tikzpicture}
\end{document}
'''

end2 = r"""
\begin{document}
    \centering
    \tdplotsetmaincoords{45}{45}
    \begin{tikzpicture}[tdplot_main_coords]

        \clip[tdplot_screen_coords] (-\textwidth/2,-\textheight/2) rectangle (\textwidth/2,\textheight/2);
        \draw[white,tdplot_screen_coords] (-\textwidth/2,-\textheight/2) rectangle (\textwidth/2,\textheight/2);

        \coordinate (O) at (0,0);
        \coordinate (V1) at (0:\lengthVOne);
        \coordinate (V2) at (\varT:\lengthVTwo);
        \path[draw,white] (-5,-5) -- (5,5);

        \draw[] (\lengthVOne,0) arc [start angle=0, end angle=180, radius=\lengthVOne] -- (\lengthVOne,0) -- cycle;
        \draw[dotted] (-\lengthVOne,0) arc [start angle=180, end angle=360, radius=\lengthVOne];

        \draw[] (0,0) -- (90:\lengthVTwo) arc [start angle=90, end angle=\varT, radius=\lengthVTwo];

        %%% VECTORS %%%
        \draw[-Triangle] (0,0) -- (V2) node[pos=1,above] {$\va{q}$};
        \draw[-Triangle] (0,0) -- (V1) node[pos=1,right] {$\va{p}$};

        %%% GEOMETRY %%%
        \fill[red,opacity=0.2] (0,0) -- ++(\varT:\lengthVOne) -- ++(0,\lengthVTwo) -- ++(\varT+180:\lengthVOne);
        \draw[] (0,0) -- ++(\varT:\lengthVOne) -- ++(0,\lengthVTwo) -- ++(\varT+180:\lengthVOne) -- cycle;

        \fill[blue,opacity=0.2] (0,0) -- ++(\varT:\lengthVTwo) -- ++(\lengthVOne,0) -- ++(\varT+180:\lengthVTwo);
        \draw[] (0,0) -- ++(\varT:\lengthVTwo) -- ++(\lengthVOne,0) -- ++(\varT+180:\lengthVTwo) -- cycle;
        \draw[blue,-Triangle] (0,0,0) -- (0,0,{\lengthVOne*\lengthVTwo*sin(\varT)}) node[left]{$\va{p}\cross\va{q}$};

    \end{tikzpicture}
\end{document}
"""

def main():
    """
    Purpose:
        Makes an animation of the cross and dot products.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    animatetex.before_loop()
    for angle in np.linspace(0,360,numiter):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(start)
            f.write(r'\newcommand{\varT}{' + f'{angle}' + r'}')
            if angle <= 180:  
                f.write(end2)
            else:
                f.write(end)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()