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
