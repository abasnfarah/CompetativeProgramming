#include "/Users/abasfarah/workspaces/competativeProgramming/stdc++.h"

using namespace std;

int maximumDifference(vector<int> &nums){
    // solution comes here
    int n = (int) nums.size();
    int currMin = nums[0];
    int globalMax = -1;
    for(int i = 1; i < n; i++){
        if(nums[i] < currMin){
            currMin = nums[i];
        }

        int localMax = nums[i] - currMin;

        if(localMax != 0){
            globalMax = max(globalMax, localMax);
        }
    }
    return globalMax;
}

int main() {
    ios_base::sync_with_stdio(0);

    //vector<int> nums = {7, 1, 5, 4};
    //vector<int> nums = {9, 4, 3, 2};
    vector<int> nums = {1, 5, 2, 10};
    
    //vector<int> nums = {999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15};

    int output = maximumDifference(nums);
    printf("output: %d\n", output);
    
    return 0;
}

