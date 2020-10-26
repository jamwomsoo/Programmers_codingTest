def solution(board, moves):
    answer = 0
    s = []
    for i in moves:
        num = 0

        while board[num][i - 1] == 0:
            if num >= len(board) - 1:
                break
            num = num + 1
        if (board[num][i - 1] == 0):
            continue
        if not s:  # 스택에 아무 값도 없을 때
            s.append(board[num][i - 1])
        else:  # 스택에 무슨 값이 있을 때
            if s[len(s) - 1] == board[num][i - 1]:  # 최상단 값이랑 들어오는 값이 같으면
                s.pop()  # 스택의 맨위의 값 제거
                answer = answer + 2
            else:
                s.append(board[num][i - 1])
        board[num][i - 1] = 0

    return answer


solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
         [1, 5, 3, 5, 1, 2, 1, 4])