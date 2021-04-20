DOXYGEN_CONFIG = ../config_file

.Phony all start clean test doc run profile pack

all: start run

start:
      pip3 install -r requirements.txt
      pip3 freeze
clean:

test:
    python3 tests.py
doc:
    rm -rf ../doxygen_documentation
    mkdir ../doxygen_documentation
    doxygen $(DOXYGEN_CONFIG)
    mv ../html/ ../doxygen_documentation
    rm -rf ../latex/
run:
    python3 main.py
profile:
    python3 profiling.py
pack:

