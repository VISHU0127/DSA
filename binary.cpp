#include <iostream>
#include <vector>
using namespace std;

//iterative binary search function
int binarySearch(vector<int> arr, int target){ // Function to perform binary search on a sorted array
      int start = 0, end = arr.size() - 1; // Initialize start and end indices
      while(start <= end){ // Continue searching while the start index is less than or equal to the end index
            int mid = (start + end) / 2;
            if(target > arr[mid]){
                  start = mid + 1;
            }
            else if (target < arr[mid]){
                  end = mid - 1;
            }
            else {
                  return mid;
            }
      }                             
      return -1; // Return -1 if the target is not found
};

//Example usage of the binary search function
int main(){ 
      vector<int> arr1 = {1, 3, 5, 7, 9, 11, 13};
      int target1 = 4;
      cout << "Index of " << target1 << " in arr1: " << binarySearch(arr1, target1) << endl;

      vector<int> arr2 = {0, 2, 4, 6, 8, 10, 12}; 
      int target2 = 0;
      cout << "Index of" << target2 << " in arr2: " << binarySearch(arr2, target2) << endl;
}

