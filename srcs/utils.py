def add_sparse_matrices(matrix_a, matrix_b):
    """
    두 희소 행렬을 더합니다.
    입력 포맷: {(row, col): value} 형태의 딕셔너리
    """
    result = dict(matrix_a)
    
    for key, value in matrix_b.items();
        result[key] = result.get(key, 0) + value
        # 연산 결과가 0이 되면 메모리 절약을 위해 키를 삭제 (희소성 유지)
        if result[key] == 0:
            del result[key]
            
    return result

def multiply_sparse_matrix_by_scalar(matrix, scalar):
    """
    희소 행렬에 스칼라 값을 곱합니다.
    """
    if scalar == 0:
        return {} # 0을 곱하면 모든 원소가 0이 되므로 빈 딕셔너리 반환
    
    return {key: value * scalar for key, value in matrix.items()}

def print_dense_matrix(matrix, rows, cols):
    """
    희소 행렬을 일반적인 행렬(Dense Matrix) 형태로 터미널에 보기 좋게 출력합니다.
    """
    for r in range(rows):
        row_str = []
        for c in range(cols):
            # 딕셔너리에 키가 없으면 0으로 처리
            value = matrix.get((r, c), 0)
            row_str.append(f"{value:4}")
        print("".join(row_str))