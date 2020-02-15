
% !TEX root =  /Users/kmurphy/projects/coderdojo/python/worksheets/02-Take_Away.tex

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{coderdojo}[2018/09/01 CoderDojo Python WorkSheets]

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax

\LoadClass[12pt]{article}

%: page setup

\usepackage[
    type={CC},
    modifier={by-nc-sa},
    version={3.0},
    imagewidth=2cm]{doclicense}

\usepackage[a4paper,margin=2cm]{geometry}
\usepackage{lastpage}

\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhead{\color{section!75!white}\@title\hfill \thepage/\pageref{LastPage}}
\fancyfoot{}
\fancypagestyle{first}{%
	\fancyhf{}
	\fancyfoot[L]{\footnotesize\smash{\begin{tabular}[b]{@{}p{\linewidth}@{}}%
		\hline\\[-12pt]
		CoderDojo, Tramore, Waterford. (\url{kmurphy@wit.ie})\\[-18pt]\doclicenseThis\\{}\end{tabular}}
}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
}
\renewcommand{\headrulewidth}{0pt}

\usepackage{xpatch}
\xpretocmd\headrule{\color{section}}{}{\PatchFailed}
\parindent 0pt

%: graphics 

\usepackage[svgnames]{xcolor}
\usepackage{graphicx}
\graphicspath{{.},{pic/}, {code/}}
\chead{\raisebox{-12pt}[0pt][0pt]{\includegraphics[decodearray={0.94 1 0.33 1 0.17 1},trim=20 25 20 20,width=24pt]{coderdojo_logo.jpg}}}
\usepackage{tikz}
\usetikzlibrary{decorations}
\usetikzlibrary{shapes.symbols, shadows}

%: colours

\definecolor{deepblue}{rgb}{0,0,0.5}
\definecolor{deepred}{rgb}{0.6,0,0}
\definecolor{deepgreen}{rgb}{0,0.5,0}
\definecolor{myOrange}{RGB}{241,85,44}
\definecolor{myGray}{RGB}{106,100,100}


\definecolor{section}{RGB}{241,85,44}
\definecolor{todo}{rgb}{0,0,0.4}
\definecolor{comment}{rgb}{0.2,0,0.2}

%: fonts

\usepackage{relsize}
\usepackage{amsmath}
\usepackage[T1]{fontenc}
\usepackage{textcomp}
\usepackage{unicode-math}
\setmathfont{Asana-Math.otf}
\setmainfont{Optima Regular}[
	BoldFont=Optima Bold,
	ItalicFont=Optima Italic,
	BoldItalicFont=Optima Bold Italic]
\usepackage{pifont}

\def\tickYes{\textcolor{green}{\ding{52}}}
\def\tickNo{\textcolor{red}{\ding{54}}}
\usepackage{fontawesome}

\newfontfamily{\sectionFont}{XKCD Regular}
\DeclareTextFontCommand{\textSectionFont}{\sectionFont}

\newfontfamily{\historyFont}{Bradley Hand Bold}
\DeclareTextFontCommand{\textHistoryFont}{\historyFont}

\newfontfamily{\textfixFont}[Scale=0.55]{Arial}


% symbols
\newcommand{\todoSymbol}{{\textcolor{todo}{\larger[2]\faEdit}}}
\newcommand{\pointSymbol}{\color{section!70!black}\larger[2]\ding{43}}
\newcommand{\commentSymbol}{{\textcolor{comment}{\larger[1]\faCommentingO}}}

%@ boxes
\usepackage[listings]{tcolorbox}
\tcbuselibrary{most}

\newtcolorbox{boxTitle}{enhanced,
	width=12cm, halign=center,valign=center,
	colback=title!5!white, colframe=title!75!black,
	fonttitle=\bfseries,
	fontupper=\LARGE\bfseries,
	drop lifted shadow=title!50!black,
	attach boxed title to top center={yshift=-3mm},title={\@worksheet},
	boxed title style={colback=title!5!white},coltitle=black}

\NewTColorBox[auto counter]{exercise}{+O{}}{% 
	enhanced,colframe=green!20!black,colback=yellow!10!white,coltitle=green!40!black, fonttitle=\bfseries,
	underlay={\begin{tcbclipinterior}
       \shade[inner color=green!30!white,outer color=yellow!10!white]
         (interior.north west) circle (2cm);
       \draw[help lines,step=5mm,yellow!80!black,shift={(interior.north west)}]
         (interior.south west) grid (interior.north east);
\end{tcbclipinterior}}, 
attach boxed title to top right={yshift=-2mm}, 
boxed title style={colback=title!5!white},title={Take Away Game}, 
savelowerto=solutions/exercise-\thetcbcounter.tex, record={\string\solution{\thetcbcounter}{solutions/exercise-\thetcbcounter.tex}}, #1
}

% tcolorbox page 160
\usepackage{varwidth}
\newtcolorbox{asideBox}[2][]{enhanced,
before skip=2mm,after skip=2mm, colback=black!5,colframe=black!50,boxrule=0.2mm,
attach boxed title to top left={xshift=1cm,yshift*=1mm-\tcboxedtitleheight}, varwidth boxed title*=-3cm,
boxed title style={frame code={
            \path[fill=tcbcol@back!30!black]
              ([yshift=-1mm,xshift=-1mm]frame.north west)
                arc[start angle=0,end angle=180,radius=1mm]
              ([yshift=-1mm,xshift=1mm]frame.north east)
                arc[start angle=180,end angle=0,radius=1mm];
            \path[left color=tcbcol@back!60!black,right color=tcbcol@back!60!black,
              middle color=tcbcol@back!80!black]
              ([xshift=-2mm]frame.north west) -- ([xshift=2mm]frame.north east)
              [rounded corners=1mm]-- ([xshift=1mm,yshift=-1mm]frame.north east)
              -- (frame.south east) -- (frame.south west)
              -- ([xshift=-1mm,yshift=-1mm]frame.north west)
              [sharp corners]-- cycle;
            },interior engine=empty,
          },
          fonttitle=\bfseries,
          title={#2},#1}

          
% make title
\newcommand\worksheet[2]{\gdef\@worksheet{#1}\title{#2}}

\definecolor{title}{named}{Blue}

\renewcommand{\maketitle}{%
%
\enlargethispage{-1cm}
\thispagestyle{first}

%
\begin{center}
\begin{boxTitle}
\@title
\end{boxTitle}
\end{center}
\medskip}

% sectioning
\usepackage{titlesec}
\renewcommand\section{\@startsection {section}{1}{\z@}%
    {-3.5ex \@plus -0.1ex \@minus -.2ex}%
    {1.2ex \@plus.01ex}%
    {\sffamily\Large\bfseries\color{section}}}
\renewcommand\subsection{\@startsection {subsection}{2}{\z@}%
    {-3.5ex \@plus -0.1ex \@minus -.2ex}%
    {1.2ex \@plus.01ex}%
    {\sffamily\large\bfseries\color{section}}}
\renewcommand\subsubsection{\@startsection {subsubsection}{3}{\z@}%
    {-3.5ex \@plus -0.1ex \@minus -.2ex}%
    {1.2ex \@plus.01ex}%
    {\sffamily\bfseries\color{section}}}
        
    
% code
\DeclareFixedFont{\ttb}{T1}{txtt}{bx}{n}{12} % for bold
\DeclareFixedFont{\ttm}{T1}{txtt}{m}{n}{12}  % for normal

\usepackage{wit-code-2012}

% Python style for highlighting
\newcommand\pythonstyle{\lstset{
language=Python,
basicstyle=\ttm,
otherkeywords={self},             % Add keywords here
keywordstyle=\ttb\color{deepblue},
emph={MyClass,__init__},          % Custom highlighting
emphstyle=\ttb\color{deepred},    % Custom highlighting style
stringstyle=\color{deepgreen},
showstringspaces=false            % 
}}\pythonstyle

\lstnewenvironment{python}[1][]
{
\pythonstyle
\lstset{#1}
}
{}

% Python for external files
\newcommand\pythonexternal[2][]{{
\pythonstyle
\lstinputlisting[#1]{#2}}}

% Python for inline
\renewcommand\code[1]{{\pythonstyle\lstinline!#1!}}

\newtcbinputlisting{\codeonly}[5]{
    enhanced,
    listing file={#4/#5},
    listing only,
    width=1\linewidth,
	%border
    colback=blue!5,
    colframe=blue!25!black,
	drop lifted shadow,
	% title
	fonttitle=\bfseries,coltitle=red!50!black,
	  attach boxed title to top center={xshift=-3.2mm,yshift=-0.50mm},
	 boxed title style={skin=enhancedfirst jigsaw,
	    size=small,arc=1mm,bottom=-1mm,
	    interior style={fill=none,
	      top color=blue!30!white,
	      bottom color=blue!5}
	},
	% code
	left=0pt,top=0pt,bottom=0pt,
    listing options={
      inputencoding=utf8,
      firstline=#2,lastline=#3,firstnumber=#2
  },#1
}
  
\newtcbinputlisting{\codeandoutput}[6]{
    enhanced,
	listing file={#4/#5},
    listing and comment,
    sidebyside,
	% width
    width=1\linewidth,
    lefthand width=.6\textwidth,
    comment={#6},
	%border
    colback=blue!5,
    colframe=blue!25!black,
	drop lifted shadow,
	% title
	fonttitle=\bfseries,coltitle=red!50!black,
	  attach boxed title to top center={xshift=-3.2mm,yshift=-0.50mm},
	 boxed title style={skin=enhancedfirst jigsaw,
	    size=small,arc=1mm,bottom=-1mm,
	    interior style={fill=none,
	      top color=blue!30!white,
	      bottom color=blue!5}
	},
	% code
	left=0pt,top=0pt,bottom=0pt,
    listing options={
      inputencoding=utf8,
      firstline=#2,lastline=#3,firstnumber=#2
  },#1
}




% 
\newcommand\WeAreDone{
\begin{center}
\begin{tikzpicture}
	\node[draw=red,starburst,fill=yellow!10,line width=2pt,drop shadow] {We are Done !};
\end{tikzpicture}
\end{center}}

% referencing
\usepackage{hyperref}
\AtBeginDocument{
\hypersetup{%
	pdfsubject={Tramore CoderDojo - Python Worksheets - Autumn 2018},
	pdftitle={\@worksheet\ - \@title},
	pdfauthor={Kieran Murphy ({kmurphywit.ie)}},
	pdfkeywords={Python, coderdojo}
}}

\usepackage[margin=10pt,font=small,labelfont=bf,labelsep=endash]{caption}

