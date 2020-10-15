def even_parity(l):
    return l.count(1) % 2 == 0


def flip_bit(i):
    return [1, 0][i]


# # def rect_parity(codeword, nrows, ncols):
# #     parity_col = codeword[-1]
# #     parity_row = codeword[-2]
# #     data = codeword[:-2]
# #     ROW, COL = -1, -1

# #     for i in range(len(data)):
# #         if (int(even_parity(data[i])) == parity_row[i]):
# #             if(ROW == -1) :
# #                 ROW = i
# #             else :
# #                 return data

# #     for i in range(len(data[1])):
# #         current_col = []
# #         for j in range(len(data)):
# #             current_col.append(data[j][i])
# #         if (int(even_parity(current_col)) == parity_col[i]):
# #             if(COL == -1) :
# #                 COL = i
# #             else :
# #                 return data

# #     # return (ROW, COL)
# #     if (ROW == -1 or COL == -1):
# #         return data
# #     else:
# #         data[ROW][COL] = flip_bit(data[ROW][COL])
# #         return data

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

# def test_correct_errors():
#     questions = [[[0, 1, 1, 0], [1, 1, 0, 1], [0, 1], [1, 0, 1, 1]],
#                  [[1, 0, 0, 1], [0, 0, 1, 0], [1, 1], [1, 0, 1, 0]],
#                  [[0, 1, 1, 1], [1, 1, 1, 0], [1, 1], [1, 0, 0, 0]]]
#     for que in questions:
#         message_sequence = rect_parity(que, len(que), len(que[1]))
#         print(message_sequence, end="\n\n")

# test_correct_errors()