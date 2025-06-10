var snakesAndLadders = function(board) {
    const boardSize = board.length;
    const hasVisited = new Array(boardSize * boardSize + 1).fill(false);
    const positionsToCheck = [[1, 0]];
    hasVisited[1] = true;

    while (positionsToCheck.length > 0) {
        const [currentSquare, moveCount] = positionsToCheck.shift();
        for (let dice = 1; dice <= 6; dice++) {
            let nextSquare = currentSquare + dice;
            if (nextSquare > boardSize * boardSize) continue;
            const [row, col] = convertToCoordinates(nextSquare, boardSize);
            if (board[row][col] !== -1) {
                nextSquare = board[row][col];
            }
            if (!hasVisited[nextSquare]) {
                if (nextSquare === boardSize * boardSize) {
                    return moveCount + 1;
                }
                hasVisited[nextSquare] = true;
                positionsToCheck.push([nextSquare, moveCount + 1]);
            }
        }
    }
    return -1;
};

function convertToCoordinates(squareNumber, boardSize) {
    const rowFromBottom = Math.floor((squareNumber - 1) / boardSize);
    let col = (squareNumber - 1) % boardSize;
    if (rowFromBottom % 2 === 1) {
        col = boardSize - 1 - col;    
        }
    const actualRow = boardSize - 1 - rowFromBottom;
    return [actualRow, col];
}