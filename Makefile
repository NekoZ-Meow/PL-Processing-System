HIYO_DIR = hiyo/
HIYO = hiyo.py
PARSER_DIR = ./parser/
VM_DIR = ./vm/
HIYO_VM = hiyo_vm
SOURCE_DIR = test_txt/

PARSER = tree
PYTHON = python3


all:clean
	(cd $(PARSER_DIR); make all)
	(cd $(VM_DIR); make all)
	cp -f $(PARSER_DIR)$(PARSER) ./$(HIYO_DIR)
	cp -rf $(VM_DIR)$(HIYO_VM) ./$(HIYO_DIR)

test:all
	$(PYTHON) $(HIYO_DIR)$(HIYO)

test-files:all
	$(PYTHON) $(HIYO_DIR)$(HIYO) $(SOURCE_DIR)*.txt

install:all
	
clean:
	rm -rf $(HIYO_DIR)$(HIYO_VM)
	rm -rf $(HIYO_DIR)__pycache__
	rm -f $(HIYO_DIR)$(PARSER)
	rm -f $(HIYO_DIR).DS_Store
	(cd $(PARSER_DIR); make clean)
	(cd $(VM_DIR); make clean)
