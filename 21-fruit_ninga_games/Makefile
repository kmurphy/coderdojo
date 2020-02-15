MAIN := $(notdir $(PWD))
CODE := $(MAIN)_code

default: $(MAIN).pdf $(MAIN)_code.pdf

$(MAIN).pdf: $(MAIN).tex
	lualatex $<
	
code: $(MAIN)_code.pdf
$(MAIN)_code.pdf: $(MAIN)_code.tex
	lualatex $<
