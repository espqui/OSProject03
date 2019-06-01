CFLAGS = -L. -lfinger.so
CC = gcc
all: main libfinger.so
	
libfinger.so: 
	${CC} -fPIC -shared finger.h -o libfinger.so

main: main.c finger.h libfinger.so
	${CC} ${CFLAGS} -o $@ $^