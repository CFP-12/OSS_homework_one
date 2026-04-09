from utils import load_sparse_matrix_from_md, add_sparse_matrices, print_dense_matrix

def main():
    print("=== [FINAL] 희소 행렬 연산 표준 시스템 ===")
    
    # 파일 로드
    file_path = input("마크다운 행렬 파일 경로를 입력하세요 (예: docs/matrix.md): ")
    matrix_a = load_sparse_matrix_from_md(file_path)
    
    if not matrix_a:
        print("행렬 데이터가 비어있거나 파일을 읽을 수 없습니다.")
        return

    # 연산 테스트를 위한 임의의 행렬 B 생성
    matrix_b = {(0, 0): 10, (2, 2): -8}
    
    rows, cols = 3, 3 # 기본 크기 설정
    
    print("\n[로드된 행렬 A (From Markdown)]")
    print_dense_matrix(matrix_a, rows, cols)
    
    print("\n[더할 행렬 B (고정값)]")
    print_dense_matrix(matrix_b, rows, cols)
    
    print("\n[A + B 결과]")
    result = add_sparse_matrices(matrix_a, matrix_b)
    print_dense_matrix(result, rows, cols)

if __name__ == "__main__":
    main()