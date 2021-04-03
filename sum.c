#include "sum.h"

static int _sum = 0;

int sum(int x)
{
    _sum += x;

    return _sum;
}