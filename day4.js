var minimizedMaximum = function(n, quantities) {
    let low = 1;
    let high = Math.max(...quantities);
    let result = 0;
    
    while(low <= high) {
        const mid = Math.floor((low + high)/2);
        let stores = 0;
        
        for(let q of quantities) {
            stores += Math.ceil(q/mid);
        }
        
        if(stores <= n) {
            result = mid;
            high = mid - 1;
        }
        else {
            low = mid + 1;
        }
    }
    return result;
};

console.log(minimizedMaximum(6, [11,6]))