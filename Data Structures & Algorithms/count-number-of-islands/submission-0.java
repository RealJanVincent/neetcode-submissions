class Solution {
    public int numIslands(char[][] grid) {
        int c = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    c++;
                    dfs(grid, i, j);
                }
            }
        }
        return c;
    }
    
    private void dfs(char[][] grid, int i, int j) {
        grid[i][j] = '0';
        int down = grid.length;
        int right = grid[0].length;
        int w = i - 1 >= 0 ? i - 1 : i;
        int x = i + 1 < down ? i + 1 : i;
        int y = j - 1 >= 0 ? j - 1 : j;
        int z = j + 1 < right ? j + 1 : j;

        if (grid[w][j] != '0') {
            dfs(grid, w, j);
        }
        if (grid[x][j] != '0') {
            dfs(grid, x, j);
        }
        if (grid[i][y] != '0') {
            dfs(grid, i, y);
        }
        if (grid[i][z] != '0') {
            dfs(grid, i, z);
        }
    }
}
