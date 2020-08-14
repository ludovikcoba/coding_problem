/*
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

*/

#include <vector>
#include <unordered_set>
#include <iostream>

using std::vector;
using std::unordered_set;
using std::cout;

bool find_k_as_sum(int k, vector<int> vec){
    unordered_set<int> scanned_nr;

    for (int i: vec){

        if(scanned_nr.count(k-i)>0){
            return true;
        }else
        {
            if(scanned_nr.count(i) == 0) scanned_nr.insert(i);
        }
    
    }

    return false;

}

int main(){
    vector<int> a = {10, 15, 3, 7};

    cout << find_k_as_sum(17, a) << std::endl;
    cout << find_k_as_sum(16, a) << std::endl;

}