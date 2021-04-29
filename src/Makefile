DOXYGEN_CONFIG = ../src/Doxyfile
PYTHON = python3

.PHONY: all start pack clean test doc run profile

#prelozi projekt i s profilingem
all: start run profile

start:
	pip3 install -r requirements.txt
	pip3 freeze

#zabali projekt
pack: doc
	mkdir -p ../../xabike00_xdrlam00_xauero00/install
	mkdir -p ../../xabike00_xdrlam00_xauero00/repo
	cp -a ../doc ../../xabike00_xdrlam00_xauero00
	cp -a calcutron_1.0_amd64.deb ../../xabike00_xdrlam00_xauero00/install
	cp -a ../../calc/. ../../xabike00_xdrlam00_xauero00/repo
	rm -rf ../../xabike00_xdrlam00_xauero00/repo/doc
	rm -rf ../../xabike00_xdrlam00_xauero00/repo/src/calcutron_1.0_amd64.deb
	cd ../../. && zip -r xabike00_xdrlam00_xauero00.zip xabike00_xdrlam00_xauero00

#smaze soubory, co nemaji byt odevzdany
clean:
#	rm -rf calcutron_1.0_amd64.deb
	rm -rf ../doc

#spusti testy mat. knihovny
test:
	$(PYTHON) tests.py

#spusti generovani dokumentace
doc:
	rm -rf ../doc
	mkdir ../doc
	doxygen $(DOXYGEN_CONFIG)
	mv ../html/ ../doc
	rm -rf ../latex/

#spusti program
run:
	$(PYTHON) calcutron.py

#spusti preklad profilingu
profile:
	$(PYTHON) profiling.py



