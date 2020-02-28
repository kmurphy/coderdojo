MAIN := $(notdir $(PWD))
CODE := $(MAIN)_code

PASSWORD := $(shell cat ../../PASSWORD)
D:
	echo $(PASSWORD)

default: $(MAIN).pdf $(MAIN)_-_code.pdf

$(MAIN).pdf: $(MAIN).tex
	lualatex $<

code: $(MAIN)_-_code.pdf
$(MAIN)_-_code.pdf: $(MAIN)_-_code.tex
	lualatex $<
	#mv $@ tmp.pdf
	#qpdf --encrypt $(PASSWORD) $(PASSWORD) 256 -- tmp.pdf - > $@
	#@rm -f tmp.pdf
	

	
$(MAIN)_code.pdf: $(MAIN)_code.tex
	lualatex $<
