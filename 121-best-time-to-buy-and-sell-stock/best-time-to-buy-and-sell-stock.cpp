#include <vector>
using namespace std;
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxprofit = 0;
        int minprice = prices[0];
        int profit = 0;

        for (int i = 1; i < prices.size(); i++) {
            
            if (minprice > prices[i]) {
                minprice = prices[i];
            }

            profit = prices[i] - minprice;

            if (maxprofit <= profit) {
                maxprofit = profit;
            }
        }

        return maxprofit;
    }
};