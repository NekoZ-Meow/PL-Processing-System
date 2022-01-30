PYTHON	= python
PYDOC	= pydoc
PYCS	= $(shell find . -name "*.pyc")
PYCACHE	= $(shell find . -name "__pycache__")
MODULE	= main
TARGET	= $(MODULE).py
PACKAGE	= hiyo
PKGPATH	= $(shell echo $(PACKAGE) | sed -e 's/\./\//g')
PKGTDIR	= $(shell echo $(PACKAGE) | cut -d '.' -f1)
WORKDIR	= ./
TEST_SOURCE_DIR = test_txt/
TEST_VM_DIR = test_tree/
PYLINT	= pylint
LINTRCF	= pylintrc.txt
LINTRST	= pylintresult.txt
APP = Hiyo.app
INSTDIR = $(APP)/Contents/Resources/Python/
ARGS	=

PARSER_DIR = $(WORKDIR)/parser/
PARSER_INST_DIR = $(PACKAGE)/parser/


all:clean
	(cd $(PARSER_DIR); make all)
	mkdir -p $(PARSER_INST_DIR)
	(cp $(PARSER_DIR)tree  $(PARSER_INST_DIR))

clean:
	(cd $(PARSER_DIR); make clean)
	@for each in ${PYCS} ; do echo "rm -f $${each}" ; rm -f $${each} ; done
	@for each in ${PYCACHE} ; do echo "rm -f $${each}" ; rm -rf $${each} ; done
	@if [ -e $(LINTRST) ] ; then echo "rm -f $(LINTRST)" ; rm -f $(LINTRST) ; fi
	@if [ -e MANIFEST ] ; then echo "rm -f MANIFEST" ; rm -f MANIFEST ; fi
	@find . -name ".DS_Store" -exec rm {} ";" -exec echo rm -f {} ";"

test: all
	$(PYTHON) $(TARGET) ${ARGS}

test-files:all
	@for each in $(TEST_SOURCE_DIR)*.txt;do echo "------$$each------"; $(PYTHON) $(TARGET) $$each;done

install:all
	@if [ ! -e $(INSTDIR) ] ; then echo "mkdir $(INSTDIR)" ; mkdir $(INSTDIR) ; fi
	cp -p -r $(TARGET) $(PKGTDIR) $(INSTDIR)
	xattr -cr $(APP)

lint:
	@if [ ! -e $(LINTRCF) ] ; then $(PYLINT) --generate-rcfile > $(LINTRCF) 2> /dev/null ; fi
	$(PYLINT) --rcfile=$(LINTRCF) --extension-pkg-whitelist=lark-parser ./$(TARGET) `find ./$(PKGPATH) -name "*.py" -not -name "__init__.py"` > $(LINTRST) ; less $(LINTRST)

doc:
	$(PYDOC) ./$(TARGET) ./$(PKGPATH)/$(MODULE)

pydoc:
	(sleep 3 ; open http://localhost:9999/$(PACKAGE).html) & $(PYDOC) -p 9999

# 
# pip is the PyPA recommended tool for installing Python packages.
# 
pip:
	@if [ -z `which pip` ]; \
	then \
		(cd $(WORKDIR); curl -O https://bootstrap.pypa.io/get-pip.py); \
		(cd $(WORKDIR); sudo -H python get-pip.py); \
		(cd $(WORKDIR); rm -r get-pip.py); \
	else \
		(cd $(WORKDIR); sudo -H pip install -U pip); \
	fi

# 
# Pylint is a tool that checks for errors in Python code,
# tries to enforce a coding standard and looks for code smells.
# 
pylint:
	@if [ -z `pip list --format=freeze | grep pylint` ]; \
	then \
		(cd $(WORKDIR); sudo -H pip install pylint); \
	else \
		(cd $(WORKDIR); sudo -H pip install pylint -U); \
	fi

# 
# 構文解析を行うためのライブラリLarkをインストールする
# 
lark:
	@if [ -z `pip list --format=freeze | grep lark-parser=` ]; \
	then \
		(cd $(WORKDIR); sudo -H pip install sip); \
		(cd $(WORKDIR); sudo -H pip install lark-parser); \
	else \
		(cd $(WORKDIR); sudo -H pip install sip -U); \
		(cd $(WORKDIR); sudo -H pip install lark-parser -U); \
	fi

# 
# List of the required packages
# 
list: pip
	@(pip list --format=freeze | grep ^pip)
	@(pip list --format=freeze | grep ^pylint)
	@(pip list --format=freeze | grep ^sip)
	@(pip list --format=freeze | grep ^lark-parser)

prepare: pip pylint lark
