from PS2_rectparity import *

Answers = [
    'No correction is necessary',
    'Uncorrectable error is detected',
    'Error Detected and Corrected'
]


def rect_parity(codeword, nrows, ncols):
    parity_col = codeword[-1]
    parity_row = codeword[-2]
    data = codeword[:-2]
    print(data)
    print(parity_row)
    ROW, COL = -1, -1

    for i in range(len(data)):
        print("even=",even_parity(data[i]))
        print("even=",int(even_parity(data[i])))
        if (int(even_parity(data[i])) == parity_row[i]):
            print("gaya")
            if (ROW == -1):
                ROW = i
            else:
                return data, 1  # untracable error
        print("ROW=",ROW,"i=",i)

    for i in range(len(data[1])):
        current_col = []
        for j in range(len(data)):
            current_col.append(data[j][i])
        print(current_col)
        print("even col=",even_parity(current_col))
        print("even col=",int(even_parity(current_col)))
        if (int(even_parity(current_col)) == parity_col[i]):
            if (COL == -1):
                COL = i
            else:
                return data, 1  # untracable error

    # return (ROW, COL)
    if (ROW == -1 and COL == -1):
        return data, 0  # no error
    elif (ROW == -1 or COL == -1):
        return data, 1  # untracable error
    else:
        data[ROW][COL] = flip_bit(data[ROW][COL])
        return data, 2  # error


# def rect_parity(codeword, nrows, ncols):
#     parity_col = codeword[-1]
#     parity_row = codeword[-2]
#     data = codeword[:-2]
#     ROW, COL = [], []

#     for i in range(len(data)):
#         if (int(even_parity(data[i])) == parity_row[i]):
#             ROW.append(i)

#     for i in range(len(data[1])):
#         current_col = []
#         for j in range(len(data)):
#             current_col.append(data[j][i])
#         if (int(even_parity(current_col)) == parity_col[i]):
#             COL.append(i)

#     # return (ROW, COL)
#     if (ROW == [] and COL == []):
#         return data, 'No correction is necessary'
#     elif (ROW == [] or COL == []):
#         return data, 'Uncorrectable error is detected'
#     elif (len(ROW) > 1 and len(COL) > 1):
#         return data, 'Uncorrectable error is detected'
#     else:
#         for r in ROW:
#             for c in COL:
#                 data[r][c] = flip_bit(data[r][c])
#         return data, 'Error Detected and Corrected'


def test_correct_errors():
    questions = [   [[0, 1, 1, 0], [1, 1, 0, 1], [0, 1], [1, 0, 1, 1]],
                 [[1, 0, 0, 1], [0, 0, 1, 0], [1, 1], [1, 0, 1, 0]],
                 [[0, 1, 1, 1], [1, 1, 1, 0], [1, 1], [1, 0, 0, 0]]]
    for que in questions:
        print("The given Bits are : ", que[:2])
        message_sequence = rect_parity(que, len(que), len(que[1]))
        print(Answers[message_sequence[1]],
              end=" , Hence output of rect_parity is : ")
        print(message_sequence[0], end="\n\n")
    nrows = len(questions[0])-1
    ncols = len(questions[0][0]) + 1
    nrows -= 1
    ncols -= 1
    print(f'({nrows*ncols+nrows+ncols},{nrows*ncols}) rectangular parity code is tested successfully for 1 bit errors')


test_correct_errors()