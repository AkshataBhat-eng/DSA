var allPathsSourceTarget = function(graph) {
    lastNode = graph.length-1;
    result = [];

    function dfs(curr, path) {
        path.push(curr)
        if(curr === lastNode) {
            result.push([...path]);
        }
        else {
            for(const x of graph[curr]) {
                dfs(x, path)
            }
        }
        path.pop();
    }
    dfs(0, [])
    return result;
    
};

console.log(allPathsSourceTarget([[1,2],[3],[3],[]]))