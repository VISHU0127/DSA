// class Solution {
// public:
//     int maxProfit(vector<int>& prices) {
//       int bestbuy = prices[0];
//       int mp = 0;
//         for(int i = 1; i < prices.size(); i++){
//             if(prices[i] > bestbuy){
//                   mp = max(mp, prices[i] - bestbuy);
//             }
//             bestbuy = min(bestbuy, prices[i]);
//         }
//       return mp;
//     }
// };
// class Solution {
// public:
//     int singleNumber(vector<int>& nums) {
//         int ans = 0;
//         for(int val : nums){
//           ans ^= val;
//         }
//         return ans;
//     }
// };

class Solution {
public:
    int maxArea(vector<int>& height) {
        int mw = 0; 
        int l = 0;
        int r = height.size() - 1;
        while(l < r){
          int w = r - l;
          int h = min(height[l], height[r]);
          int water = w * h;
          mw = max(mw, water);
          height[l] < height[r]? l++ : r--;
        }
        return mw;
    }
};