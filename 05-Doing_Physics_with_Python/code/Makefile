PY_TO_OUT.py = Basic.py Drop_1.py Drop_2.py \
	Throw_1.py Throw_2.py Throw_3.py

PY_TO_OUT.out = ${subst .py,.out, ${PY_TO_OUT.py}}

PY_TO_PDF.py = Throw_2.py Throw_3.py Throw_4.py

PY_TO_PDF.pdf = ${subst .py,.pdf, ${PY_TO_PDF.py}}

%.out: %.py
	python $< > $@

%.pdf: %.py
	python get_screenshot.py $<

default: ${PY_TO_OUT.out} ${PY_TO_PDF.pdf}

	
#	Square_Event.pdf 
 