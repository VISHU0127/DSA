class Solution {
public:
    int minimizedMaximum(int n, vector<int>& arr) {
        int st = 1; int end = *max_element(arr.begin(), arr.end());
        while(st < end){
            int mid = st + (end - st)/2;
            long long x = 0;
            for(int y : arr){
                x += (y + mid - 1)/mid;
            }
            if(x <= n) end = mid;
            else st = mid + 1;
        }
        return st;
    }
};
