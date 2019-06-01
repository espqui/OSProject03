CFLAGS = -L. -lfinger.so
CC = gcc
all: libfinger.so
	
libfinger.so: finger.c
	${CC} -shared -o libfinger.so -fPIC finger.c

main: main.c finger.c libfinger.so
	${CC} ${CFLAGS} -o $@ $^