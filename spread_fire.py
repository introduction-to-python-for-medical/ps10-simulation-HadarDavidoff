import copy

def spread_fire(grid):
    grid_size = len(grid)
    update_grid = copy.deepcopy(grid)  # יצירת עותק של הרשת לשם עדכון

    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i][j] == 1:  # אם יש עץ בתא הנוכחי
                # בדיקת שכנים ישירות
                if (i > 0 and grid[i-1][j] == 2) or \
                   (i < grid_size - 1 and grid[i+1][j] == 2) or \
                   (j > 0 and grid[i][j-1] == 2) or \
                   (j < grid_size - 1 and grid[i][j+1] == 2):
                    update_grid[i][j] = 2  # הצתת התא אם אחד השכנים בוער

    return update_grid
