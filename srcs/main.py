from srcs.utils import add_sparse_matrices, multiply_sparse_matrix_by_scalar, print_dense_matrix

def main():
    print("=== 희소 행렬 연산 프로젝트 ===")
    
    # 3x3 크기의 희소 행렬 정의 (행, 열) -> 값
    matrix1 = {(0, 0): 5, (1, 2): 3, (2, 2): 8}
    matrix2 = {(0, 0): -2, (1, 2): 7, (2, 0): 4}
    
    rows, cols = 3, 3
    
    print("\n[행렬 A]")
    print_dense_matrix(matrix1, rows, cols)
    
    print("\n[행렬 B]")
    print_dense_matrix(matrix2, rows, cols)
    
    # 기능 1: 행렬 덧셈
    print("\n[A + B 결과]")
    added_matrix = add_sparse_matrices(matrix1, matrix2)
    print_dense_matrix(added_matrix, rows, cols)
    
    # 기능 2: 스칼라 곱
    scalar = 3
    print(f"\n[A * {scalar} (스칼라 곱) 결과]")
    scaled_matrix = multiply_sparse_matrix_by_scalar(matrix1, scalar)
    print_dense_matrix(scaled_matrix, rows, cols)

if __name__ == "__main__":
    main()