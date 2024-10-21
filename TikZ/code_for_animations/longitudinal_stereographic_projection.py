
import numpy as np
import Animation_Modules.animatetex as animatetex
numiter = 24
start= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty

%tikzpicture
\usepackage{tikz}
\usepackage{tkz-euclide}
\usetikzlibrary{arrows.meta}
'''
end = r'''
\begin{document}
    \begin{frame}
        \centering
        \begin{tikzpicture}

            %%% GEOMETRY %%%
            \draw[] (0,0) circle [radius=1];
            \draw[] (\varT+180:1) -- (\varT:1);
            \draw[] (\varT+180:1) -- (0,1);
            \fill[] ({(-cos(\varT))/(sin(\varT)+1)},0) circle [radius=0.05];
            \fill[] ({(cos(\varT))/(1-sin(\varT))},0) circle [radius=0.05];
            \draw[] (0,1) -- ({(cos(\varT))/(1-sin(\varT))},0);
            \draw[densely dotted,thin] ({(cos(\varT))/(1-sin(\varT))},0) -- ({(cos(\varT))/(1-sin(\varT))},-1.3);
            \draw[densely dotted,thin] ({(-cos(\varT))/(sin(\varT)+1)},0) -- ({(-cos(\varT))/(sin(\varT)+1)},-1.3);
            \draw[|-|] ({(-cos(\varT))/(sin(\varT)+1)},-1.3) -- ({(cos(\varT))/(1-sin(\varT))},-1.3);
            \draw[] (0,1) -- ({cos(\varT)},{sin(\varT)});
            \draw[] (0,1) -- ({-cos(\varT)/(1+sin(\varT)},0);
            
            %%% AXES %%%
            \draw[-latex,thick] (0,0) -- (0,2);
            \draw[-latex,thick] (-2,0) -- (3,0);

            %%% NODES %%%
            \fill[] (0,0) circle [radius=0.05];
            \fill[] (0,1) circle [radius=0.05];
            \fill[] (\varT+180:1) circle [radius=0.05];
            \fill[] (\varT:1) circle [radius=0.05];
            \draw[red,|-Latex] ({tan(\varT)},-1.5) -- ({tan(\varT)},0);
        \end{tikzpicture}
    \end{frame}
\end{document}
'''

def main():
    animatetex.before_loop()
    for angle in np.linspace(-30,50,numiter//2):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(start)
            f.write(r'\newcommand{\varT}{' +f'{angle}' +'}')
            f.write(end)
        animatetex.during_loop()
    for angle in np.linspace(50,-30,numiter//2):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(start)
            f.write(r'\newcommand{\varT}{' +f'{angle}' +'}')
            f.write(end)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()