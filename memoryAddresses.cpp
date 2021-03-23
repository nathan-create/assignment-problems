#include <iostream>

int main(){
    int array[] = {11,12,13,14};
    std::cout << "array has address " << &array << "\n";

    for(int i = 0;i < 4; i++){
        std::cout << "index " << i << "has value " << array[i] << "and address " << &array[i] << "\n";
    }
    return 0;
}