DOXYGEN_CONFIG = ../config_file
DESTDIR = ../install
INSFLAGS = -m 0755

.Phony: all install start clean test doc run profile pack

all: start run

start:
		pip3 install -r requirements.txt
		pip3 freeze
clean:
	mkdir /foo



install: main.py matlib.py calculator.py ui_calculator.py requirements.txt
		mkdir -p $(DESTDIR)/usr/local/bin 2>/dev/null
		mkdir -p $(DESTDIR)/usr/share/calc 2>/dev/null
		install $(INSFLAGS) main.py $(DESTDIR)/usr/share/calc
		chmod +x $(DESTDIR)/usr/share/calc/main.py
		install $(INSFLAGS) matlib.py $(DESTDIR)/usr/share/calc
		install $(INSFLAGS) calculator.py $(DESTDIR)/usr/share/calc
		install $(INSFLAGS) ui_calculator.py $(DESTDIR)/usr/share/calc
		ln -sf $(DESTDIR)/usr/share/calc/main.py $(DESTDIR)/usr/local/bin/test-calculator
		mkdir -p $(DESTDIR)/tmp 2>/dev/null
		install $(INSFLAGS) requirements.txt $(DESTDIR)/tmp/
		chmod +x $(DESTDIR)/DEBIAN/postinst
		dpkg-deb --build $(DESTDIR) $(DESTDIR)/calculator.deb



