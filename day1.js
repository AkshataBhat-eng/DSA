/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if(!prices.length) return;

    let lowestPrice = prices[0];
    let profit = 0;
    for(let i=0; i< prices.length; i++) {
        if(prices[i] <= lowestPrice) lowestPrice = prices[i];

        if(prices[i] - lowestPrice > profit) profit = prices[i] - lowestPrice;
     
    }
    return profit;

};

console.log(maximizeProfit([2,1,2,1,0,0,1]))

// console.log(maximizeProfit([7,1,5,3,6,4]))
// console.log(maximizeProfit([7,6,4,3,1]))
// console.log(maximizeProfit([5,3,1,4,2,10,5,1,11]))