#include <stdio.h>
#include <stdlib.h>
#include "arithmatic.h"
 
void connect()
{
    printf("Connected to C extension...\n");
}
 
//return random value in range of 0-50
int randNum()
{
    int nRand = rand() % 100; 
    return nRand;
}
 
//add two number and return value
int addNum(int a, int b)
{
    int nAdd = a + b;
    return nAdd;
}
