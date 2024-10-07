import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

preamble= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty
\usepackage{tikz,tkz-euclide}
\usetikzlibrary{decorations.markings}
'''

postscript = r'''
\begin{document}
\begin{frame}
\centering
\begin{tikzpicture}[scale=0.7]
\draw[
decoration={markings,
mark=at position \Vt with {\fill (0,0) coordinate (DeliberatelyLongName0) circle[radius=0.062];},
mark=at position \Vt with {\draw[->] (0,0) -- (1,0) coordinate(DeliberatelyLongName1);},
mark=at position \Vt with {\draw[->] (0,0) -- (0,1) coordinate(DeliberatelyLongName2);},
},
postaction={decorate}
]%%% END
(0,0) arc[start angle=90, end angle=0, radius=5];
\draw pic[draw,-,angle eccentricity=1.4, angle radius=0.3cm]{right angle=DeliberatelyLongName1--DeliberatelyLongName0--DeliberatelyLongName2};
\draw[white] (-2,-2) rectangle (8,8);
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
    for angle in np.linspace(0,0.8,numiter//2):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(preamble)
            f.write(r'\newcommand{\Vt}{' +f'{angle}' +'}')
            f.write(postscript)
        animatetex.during_loop()
    for angle in np.linspace(0.8,0,numiter//2):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(preamble)
            f.write(r'\newcommand{\Vt}{' +f'{angle}' +'}')
            f.write(postscript)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()