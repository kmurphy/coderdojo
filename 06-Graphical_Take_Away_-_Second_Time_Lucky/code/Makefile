PY_TO_OUT.py = 

PY_TO_PDF.py = Events.py


PY_TO_OUT.out = ${subst .py,.out, ${PY_TO_OUT.py}}
PY_TO_PDF.pdf = ${subst .py,.pdf, ${PY_TO_PDF.py}}

%.out: %.py
	python $< > $@

%.pdf: %.py
	python get_screenshot.py $<

default: ${PY_TO_OUT.out} ${PY_TO_PDF.pdf}
