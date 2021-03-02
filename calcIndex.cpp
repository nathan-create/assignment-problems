# include <iostream>
# include <cassert>

int calcTerms(int index){
    int fib_zero = 0;
    int fib_one = 1;
    int sum = 0;
    int terms = [index];

    if (index == 0){
         terms[0] = fib_zero;
    }
    if (index == 1){
        terms[1] = fib_one;
    }
    for (int i = 0; i < index-1; i++){
        sum = fib_one + fib_zero;
        fib_zero = fib_one;
        fib_one = sum;
        terms[i+2] = sum;
    }
    return terms;
}
int calcIndex(int x){
    terms = calcTerms(x);
    for (int i = 0; i<x;i++){
        if terms[i] > x{
            return i;
        }
    }
}

int main()
{
    std::cout << "Testing...\n";

    assert(calcIndex(8)==7);
    assert(calcIndex(100000)==26);

    std::cout << "Success!";

    return 0;
}