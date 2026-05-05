TEX=main.tex
PREVIEW_TEX=main_double_column_preview.tex
PDF=main.pdf

.PHONY: all preview clean distclean sync-bib

all:
	latexmk -pdf -pdflatex="pdflatex %O %S" $(TEX)

preview:
	latexmk -pdf -pdflatex="pdflatex %O %S" $(PREVIEW_TEX)

sync-bib:
	cp ../../03_references/references.bib references.bib

clean:
	latexmk -c $(TEX)
	latexmk -c $(PREVIEW_TEX)

distclean:
	latexmk -C $(TEX)
	latexmk -C $(PREVIEW_TEX)
