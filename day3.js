var rotate = function(matrix) {
    for(let i=0; i< matrix.length; i++) {
        for(let j=0; j<matrix[i].length; j++) {
            if(i>j) {
                let temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i]= temp;
            }   
            else continue;
        }
    }
    for(let i=0; i< matrix.length; i++){
        matrix[i].reverse();
    }
    console.log(matrix)
    
};