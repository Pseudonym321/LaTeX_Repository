
import numpy as np
import Animation_Modules.animatetex as animatetex

numiter = 24

start= r'''
\documentclass{beamer}
\beamertemplatenavigationsymbolsempty

% packages
\usepackage{tikz,tikz-3dplot}

% commands
\newcommand{\sphereX}[2]{
% Purpose: Gives the 'x' coordinate on a sphere, for a given 
% polar-azimuthal coordinate.
% Parameters:
% #1  - azimuthal angle
% #2  - polar angle
cos(#2)*cos(#1)
}

\newcommand{\sphereY}[2]{
% Purpose: Gives the 'y' coordinate on a sphere, for a given 
% polar-azimuthal coordinate.
% Parameters:
% #1  - azimuthal angle
% #2  - polar angle
cos(#2)*sin(#1)
}

\newcommand{\sphereZ}[2]{
% Purpose: Gives the 'z' coordinate on a sphere, for a given 
% polar-azimuthal coordinate. [Note: the azimuthal angle is redundant.]
% Parameters:
% #1  - azimuthal angle
% #2  - polar angle
sin(#2)
}

\newcommand{\SPX}[2]{
% Purpose: Gives the 'x' coordinate of the stereographic projection of a 
% point on a sphere.
% Parameters:
% #1  - the x value of a point on the sphere
% #2  - the z value of that point
#1/(1-#2)
}

\newcommand{\SPY}[2]{
% Purpose: Gives the 'y' coordinate of the stereographic projection of a 
% point on a sphere.
% Parameters:
% #1  - the x value of a point on the sphere
% #2  - the z value of that point
#1/(1-#2)
}

\newcommand{\polar}{
% The polar viewing angle
60
}
\newcommand{\azimuth}{
% the azimuthal viewing angle
45
}
'''

end = r'''
\begin{document}
    \tdplotsetmaincoords{\polar}{\azimuth}
    \begin{tikzpicture}[tdplot_main_coords]

        % this sets the Euler-angles for the rotated reference frame
        % (i.e. ZYZ angles).
        \tdplotsetrotatedcoords{\varT}{\varT}{\varT}

        % This clips and draws a frame for us to view the picture 
        % through.
        \clip[tdplot_screen_coords] 
        (-\textwidth/2,-\textheight/2) 
        rectangle (\textwidth/2,\textheight/2);
        \draw[white,ultra thin,tdplot_screen_coords] 
        (-\textwidth/2,-\textheight/2) 
        rectangle (\textwidth/2,\textheight/2);

        % This plots an elliptic Mobius transformation, based on the 
        % chosen Euler-angles of rotation
        \foreach \polarAngle in {-90,-70,...,90}{
            
            % This obtains the rotated coordinates for the initial 
            % point under our specified rotation frame.
            \tdplottransformrotmain
            {\sphereX{0}{\polarAngle}}
            {\sphereY{0}{\polarAngle}}
            {\sphereZ{0}{\polarAngle}}

            % When taking the stereographic projection of points on 
            % a sphere, points near the north pole are projected off
            % to infinity. So, we omit those points to keep the
            % dimensions manageable. This initialized the initial point
            % of our plot.
            \ifdim \tdplotresz pt<0.999pt
                \pgfmathsetmacro\lastx{\SPX{\tdplotresx}{\tdplotresz}}
                \pgfmathsetmacro\lasty{\SPY{\tdplotresy}{\tdplotresz}}
            \fi

            % we initialize the opacity at 1, only to be set to 0 
            % for lines which diverge to infinity (to prevent them 
            % from connecting improperly).
            \gdef\opacity{1}
            \foreach \varT in {0,10,...,360} {

                % This obtains the rotated coordinates for each 
                % intermittant point under our specified rotation frame.
                \tdplottransformrotmain
                {\sphereX{\varT}{\polarAngle}}
                {\sphereY{\varT}{\polarAngle}}
                {\sphereZ{\varT}{\polarAngle}}

                % Once again, we check for closeness to the north pole
                % before performing stereographic projection.
                \ifdim \tdplotresz pt<0.99pt

                    % These set the next points along our trajectory.
                    % We draw from the first point, to the second, and
                    % finally replace the first with the second before
                    % finding the third. We carry on this procedure 
                    % until the path is drawn.
                    \pgfmathsetmacro\Vx{\SPX{\tdplotresx}{\tdplotresz}}
                    \pgfmathsetmacro\Vy{\SPY{\tdplotresy}{\tdplotresz}}

                    % This is the part which actually draws the path 
                    % segment. It is a small piece of code, which 
                    % requires a lot of groundwork to find.
                    \draw[opacity=\opacity,ultra thin] 
                    (\lastx,\lasty) -- (\Vx,\Vy);

                    % We reset the opacity for the next loop.
                    \gdef\opacity{1}

                    % We redefine the initial points as the terminal 
                    % points, so we can update the terminal point with 
                    % the next one.
                    \pgfmathsetmacro\lastx{\Vx}
                    \pgfmathsetmacro\lasty{\Vy}
                    \global\let\lastx\lastx
                    \global\let\lasty\lasty
                \else
                    \gdef\opacity{0}
                \fi
            } % end inner for loop
        } % end outer for loop





        \fill[white] ({cos(\azimuth)},{sin(\azimuth)}) 
        arc [start angle=\azimuth, end angle={\azimuth-180}, radius=1] 
        -- cycle;
        \fill[tdplot_screen_coords,white] ({cos(0)},{sin(0)}) 
        arc [start angle=0, end angle=180, radius=1] -- cycle;

        % outer circle
        \draw[tdplot_screen_coords,ultra thin] ({cos(0)},{sin(0)}) 
        arc[start angle=0,end angle=180,radius=1];
        \draw[ultra thin] ({cos(0+\azimuth)},{sin(0+\azimuth)}) 
        arc[start angle=0+\azimuth,end angle=-180+\azimuth,radius=1];


        % latitudinal lines
        \foreach \Vnn in {-90,-70,...,90}{
        \tdplottransformrotmain
        {\sphereX{0}{\Vnn}}
        {\sphereY{0}{\Vnn}}
        {\sphereZ{0}{\Vnn}}
        \pgfmathsetmacro\lastx{\tdplotresx}
        \pgfmathsetmacro\lasty{\tdplotresy}
        \pgfmathsetmacro\lastz{\tdplotresz}
        \foreach \Vn in {10,20,...,360}{
        \tdplottransformrotmain{\sphereX{\Vn}{\Vnn}}{\sphereY{\Vn}{\Vnn}}{\sphereZ{\Vn}{\Vnn}}
        \pgfmathsetmacro\Vx{\tdplotresx}
        \pgfmathsetmacro\Vy{\tdplotresy}
        \pgfmathsetmacro\Vz{\tdplotresz}
        % Viewing direction components
                \pgfmathsetmacro\viewdirX{\sphereX{-\azimuth}{90 - \polar}} % Adjusting Z component
                \pgfmathsetmacro\viewdirY{\sphereY{-\azimuth}{90 - \polar}} % Adjusting Z component
                \pgfmathsetmacro\viewdirZ{\sphereZ{-\azimuth}{90 - \polar}} % Adjusting Z component

                \pgfmathsetmacro\currentDotProduct{\lastx*\viewdirX + \lasty*\viewdirY + \lastz*\viewdirZ} % Dot product with the viewer direction

                % Check if the dot product is positive
                \ifdim\currentDotProduct pt > 0 pt
                \ifdim\lastz pt>0pt
                \ifdim\Vz pt>0pt
                    \draw[ultra thin] (\lastx,\lasty,\lastz) -- (\Vx,\Vy,\Vz);
                \fi\fi\fi
        \pgfmathsetmacro\lastx{\Vx}
        \pgfmathsetmacro\lasty{\Vy}
        \pgfmathsetmacro\lastz{\Vz}
        \global\let\lastx\lastx
        \global\let\lasty\lasty
        \global\let\lastz\lastz
        } % end inner for loop
        } % end outer for loop

    \end{tikzpicture}
\end{document}
'''

def main():
    """
    Purpose:
        Makes an animation of the parallelogram dot product.
    Parameters:
        No parameters.
    Return:
        Void.
    """
    animatetex.before_loop()
    for angle in np.linspace(0,90,numiter):
        with open(animatetex.TeX_file, 'w') as f:
            f.write(start)
            f.write("\n" + r"\newcommand{\varT}{" + f"{angle}" + "}")
            f.write(end)
        animatetex.during_loop()
    animatetex.after_loop()

if __name__ == "__main__":
    main()