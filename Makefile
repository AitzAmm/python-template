PYTHON = python
SRC_DIR = src
OUT_DIR = out

all: $(OUT_DIR)/mytool

$(OUT_DIR)/mytool:
	$(PYTHON) -m py_compile $(SRC_DIR)/*.py
	mkdir -p $(OUT_DIR)
	mv $(SRC_DIR)/*.pyc $(OUT_DIR)/

clean:
	rm -rf $(OUT_DIR)
