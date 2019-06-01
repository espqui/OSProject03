
int main(void)
{
    set_device("/dev/ttyardu0");

    move(5,5);
    pick();
    drop();
    
    
    return 0;
}