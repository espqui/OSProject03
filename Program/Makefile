all :
	$(MAKE) -C driver
	$(MAKE) -C library
	
.PHONY: install
install:
	sudo rmmod cdc-acm
	sudo insmod driver/arduino.ko
	sudo chmod 777 /dev/ardu0
	
.PHONY: clean
clean:
	sudo rmmod arduino


.PHONY: run
run:
	python3 GUI/connectionPC.py
