TEX=main.tex
PDF=main.pdf

.PHONY: all clean distclean sync-bib

all:
	latexmk -pdf -pdflatex="pdflatex %O %S" $(TEX)

sync-bib:
	cp ../../03_references/references.bib references.bib

clean:
	latexmk -c $(TEX)

distclean:
	latexmk -C $(TEX)
