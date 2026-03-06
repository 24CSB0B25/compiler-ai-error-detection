int main() {
    int a = 10;
    float b = 20.5;
    system("ls");  // malicious function
    if (a < b) {
        a = a + 1;
    }
    return 0;
}

/*
#include<stdio.h>

int main()
{
    char name[10];
    gets(name);
    return 0;
}
*/
