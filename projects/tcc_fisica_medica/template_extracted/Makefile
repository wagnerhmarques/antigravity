LATEXMK ?= latexmk
SHELL := /bin/sh


all: TCC

TCC:
	$(LATEXMK) main.tex


clean:
	$(LATEXMK) -C main.tex || true

