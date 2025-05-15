var decodeString = function(s) {
    if(!s.length) return -1;
    let stack = []  
    for (let char of s) {
        if (char !== ']') {
            stack.push(char);
        } else {
            let temp = '';
            while (stack[stack.length - 1] !== '[') {
                temp = stack.pop() + temp;
            }
            stack.pop();
            let k = '';
            while (stack.length && !isNaN(stack[stack.length - 1])) {
                k = stack.pop() + k;
            }
            stack.push(temp.repeat(parseInt(k)));
        }
    }
    return stack.join('');

};