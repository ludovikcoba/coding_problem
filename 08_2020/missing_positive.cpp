/*
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
*/


#include <iostream>
using std::cout;

int shift_negatives(int arr[], int s){
    int j=0;
    for (int i=0; i<s; i++){
        if(arr[i] <= 0){
            std::swap(arr[i], arr[j]);
            j++;
        }   
    }
    return j;
}

int find_missing(int arr[], int s){
    for(int i=0; i<s; i++)
        if(arr[abs(arr[i])-1] > 0 && abs(arr[i]) - 1<s)
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1];    

    for(int i=0; i<s; i++)
        if(arr[i]>0)
            return i+1;
    

    return s+1;

}

int missing(int arr[], int s){
    int shift = shift_negatives(arr, s);

    return find_missing(arr + shift, s-shift);
}

int main(){
    int arr[] = {1, 2, 0}; //{3, 4, -1, 1};
    int s = sizeof(arr)/sizeof(arr[0]);
    

    cout << missing(arr, s);



}