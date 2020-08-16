/*Given an array of integers, return a new array such that each element at index i of the new array is the product 
of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?*/

#include <vector>
#include <iostream>

using std::vector;

vector<long long> product_of_rest(vector<int> a){
    int s = a.size();

    vector<long long> inorder (s), reversed(s);
    inorder[0] = (long long) a[0];
    reversed[s-1] = (long long) a[s-1];

    for (int i=1; i<s; i++){
        inorder[i] = a[i] * inorder[i-1];
        reversed[s-i-1] = a[s-i-1] * reversed[s-i];
    }

    vector<long long> result;

    result.push_back(reversed[1]);

    for(int i=1; i<s-1; i++)
        result.push_back(inorder[i-1]*reversed[i+1]);

    result.push_back(inorder[inorder.size()-2]);

    return result;

}

int main(){

    vector<int> a = {1, 2, 3, 4, 5};
    vector<int> b = {3,2,1};

    vector<long long> res = product_of_rest(b);

    for (long long n: res)
        std::cout << n << " ";

}