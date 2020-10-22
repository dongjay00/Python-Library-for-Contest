from filecmp import cmp
print(cmp('result.txt', 'output.txt'))  # 만들어진 결과물과 정답 파일 비교