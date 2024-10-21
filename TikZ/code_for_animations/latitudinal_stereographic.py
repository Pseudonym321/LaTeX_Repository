
import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24
start= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty

\usepackage{tikz}
\usetikzlibrary{arrows.meta}
'''

end = r'''
\begin{document}
    \begin{frame}
        \centering
        \begin{tikzpicture}
            %%% GEOMETRY %%%
            \draw[] (0,0) circle [radius=1];
            \draw[] (0,0) -- (\varT:1);

            %%% LINES %%%
            \draw[] (0,1) -- ({cos(\varT)},{sin(\varT)});
            \draw[] (0,1) -- ({cos(\varT)/(1-sin(\varT))},0);

            \fill[] ({cos(\varT)/(1-sin(\varT))},0) circle [radius=0.05];
            \draw[] ({cos(\varT)},{sin(\varT)}) -- ({cos(\varT)},{-sin(\varT)});
            \fill[] ({cos(\varT)},{-sin(\varT)}) circle [radius=0.05];

            \draw[] (0,1) -- ({cos(\varT)},{-sin(\varT)});
            \draw[] (0,1) -- ({cos(\varT)/(1+sin(\varT))},0);
            \fill[] ({cos(\varT)/(1+sin(\varT))},0) circle [radius=0.05];

            \draw[thin,densely dotted] ({cos(\varT)/(1-sin(\varT))},0) -- ({cos(\varT)/(1-sin(\varT))},-1.3);
            \draw[thin,densely dotted] ({cos(\varT)/(1+sin(\varT))},0) -- ({cos(\varT)/(1+sin(\varT))},-1.3);
            \draw[|-|] ({cos(\varT)/(1-sin(\varT))},-1.3) -- ({cos(\varT)/(1+sin(\varT))},-1.3);

            %%% AXES %%%
            \draw[-latex,thick] (0,0) -- (0,2);
            \draw[-latex,thick] (-1.5,0) -- (3,0);

            %%% NODES %%%
            \fill[] (0,0) circle [radius=0.05];
            \fill[] (0,1) circle [radius=0.05];
            %\fill[] (\varT+180:1) circle [radius=0.05];
            \fill[] (\varT:1) circle [radius=0.05];
            \draw[red,|-Latex] ({1/cos(\varT)},-1.5) -- ({1/cos(\varT)},0);

        \end{tikzpicture}
    \end{frame}
\end{document}
'''
def main():
    animatetex.before_loop()
    for angle in np.linspace(0,50,numiter//2):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(start)
            f.write(r'\newcommand{\varT}{' +f'{angle}' +'}')
            f.write(end)
        animatetex.during_loop()
    for angle in np.linspace(50,0,numiter//2):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(start)
            f.write(r'\newcommand{\varT}{' +f'{angle}' +'}')
            f.write(end)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()