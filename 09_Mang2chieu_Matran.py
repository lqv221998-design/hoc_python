# Ma trận trong python (matrix) 
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Truy cập từng phần tử trong ma trận
print(matrix[2])    # Kết quả: in ra hàng cuối cùng [7, 8, 9]
print(matrix[1][0]) # Kết quả: 4

# Vòng lặp for lấy ra danh sách các hàng:
for row in matrix:
    print(row)      # Kết quả tạo ra danh sách các hàng  [1, 2, 3]
                                                        #[4, 5, 6]
                                                        #[7, 8, 9]
    print(type(row)) # Kết quả: list

# Vòng lặp lấy ra từng phần tử có trong ma trận:
for row in matrix:
    for column in row:
        print(column)
        print(type(column))