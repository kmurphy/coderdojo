TEX = ${wildcard *.tex}
PDF = ${subst .tex,.pdf,${TEX}}

default: ${PDF}

%.pdf: %.tex
	lualatex $<

clean:
	latex-clean