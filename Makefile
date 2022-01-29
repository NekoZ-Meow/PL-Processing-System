HIYO_DIR = hiyo/
HIYO = hiyo.py
PARSER_DIR = ./parser/
VM_DIR = ./vm/
HIYO_VM = hiyo_vm
SOURCE_DIR = test_txt/

PARSER = tree
PYTHON = python3

PYLINT	= pylint
LINTRCF	= pylintrc.txt
LINTRST	= pylintresult.txt


all:clean
	(cd $(PARSER_DIR); make all)
	(cd $(VM_DIR); make all)
	cp -f $(PARSER_DIR)$(PARSER) ./$(HIYO_DIR)
	cp -rf $(VM_DIR)$(HIYO_VM) ./$(HIYO_DIR)

test:all
	$(PYTHON) $(HIYO_DIR)$(HIYO)

test-files:all
	@for each in $(SOURCE_DIR)*.txt;do echo "------$$each------"; $(PYTHON) $(HIYO_DIR)$(HIYO) $$each;done

install:all
	
clean:
	rm -rf $(HIYO_DIR)$(HIYO_VM)
	rm -rf $(HIYO_DIR)__pycache__
	rm -f $(HIYO_DIR)$(PARSER)
	rm -f $(HIYO_DIR).DS_Store
	@if [ -e $(LINTRST) ] ; then echo "rm -f $(LINTRST)" ; rm -f $(LINTRST) ; fi
	(cd $(PARSER_DIR); make clean)
	(cd $(VM_DIR); make clean)


lint:
	@if [ ! -e $(LINTRCF) ] ; then $(PYLINT) --generate-rcfile > $(LINTRCF) 2> /dev/null ; fi
	$(PYLINT) --rcfile=$(LINTRCF) --extension-pkg-whitelist=lark-parser `find ./$(HIYO_DIR) -name "*.py" -not -name "__init__.py"` > $(LINTRST) ; less $(LINTRST)

prepare:
	(cd $(VM_DIR); make prepare)
