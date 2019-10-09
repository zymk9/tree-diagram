#include <iostream>
using namespace std;
int a[10];
int main()
{
    int i = 3, j = 4;
    printf("%d", !(i++) - (--j) > (j--));
}