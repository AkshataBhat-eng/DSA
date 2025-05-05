function maximizeProfit(prices) {
    if(!prices.length) return;

    let lowestPrice = prices[0];
    let lowestPriceDay = 0
    for(let i=0; i< prices.length; i++) {
        if(lowestPrice >= prices[i]) {
            lowestPrice = prices[i];    
            lowestPriceDay = i;
        }        
    }
    let highestPricesArray = prices.slice(lowestPriceDay);
    let highestPrice = highestPricesArray[0];
    if(highestPricesArray.length) {
        for(let i=0; i< highestPricesArray.length; i++) {
            if(highestPrice <= highestPricesArray[i]) highestPrice = highestPricesArray[i];
        }
        return highestPrice-lowestPrice;
    }
    else return 0


}

console.log(maximizeProfit([7,1,5,3,6,4]))
console.log(maximizeProfit([7,6,4,3,1]))
console.log(maximizeProfit([5,3,1,4,2,10,5,1,11]))