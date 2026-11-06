class NumMatrix {
private:
    
    vector<vector<int>> sums;

public:
    NumMatrix(vector<vector<int>>& matrix)
    : sums(matrix.size() + 1, vector<int>(matrix[0].size() + 1, 0)) {
        int m = matrix.size();
        int n = matrix[0].size();

        sums[0][0] = 0;
        sums[1][1] = matrix[0][0];

        for (int i = 1; i < m; i++) {
            sums[i + 1][0] = 0;
            sums[i + 1][1] = sums[i][1] + matrix[i][0];
        }

        for (int j = 1; j < n; j++) {
            sums[0][j + 1] = 0;
            sums[1][j + 1] = sums[1][j] + matrix[0][j];
        }

        for (int i = 2; i < m + 1; i++) {
            for (int j = 2; j < n + 1; j++) {
                sums[i][j] = sums[i][j - 1] + sums[i - 1][j] - sums[i - 1][j - 1] + matrix[i - 1][j - 1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        int A = sums[row1][col1];
        int B = sums[row1][col2 + 1];
        int C = sums[row2 + 1][col1];
        int D = sums[row2 + 1][col2 + 1];
        return D - B - C + A;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */