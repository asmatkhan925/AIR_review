TEX=main.tex
PREVIEW_TEX=main_double_column_preview.tex
PDF=main.pdf

.PHONY: all preview clean distclean sync-bib check submission-check

all:
	latexmk -pdf -pdflatex="pdflatex %O %S" $(TEX)

preview:
	latexmk -pdf -pdflatex="pdflatex %O %S" $(PREVIEW_TEX)

sync-bib:
	cp ../../03_references/references.bib references.bib

check:
	grep -n "TODO\\|TBD\\|??\\|undefined" main.tex || true

submission-check:
	test -f main.tex
	test -f sn-jnl.cls
	test -f references.bib
	test -f sn-basic.bst
	echo "Basic source files found. Check figures, compiled PDF, and flat submission packaging manually."

clean:
	latexmk -c $(TEX)
	latexmk -c $(PREVIEW_TEX)

distclean:
	latexmk -C $(TEX)
	latexmk -C $(PREVIEW_TEX)
