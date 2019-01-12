def print_multiline_alignment(alignment, n=80):
    seq1 = [alignment[0][i:i+n] for i in range(0, len(alignment[0]), n)]
    seq2 =  [alignment[1][i:i+n] for i in range(0, len(alignment[1]), n)]
    nstart1, nend1 = 1, 0
    nstart2, nend2 = 0, 0
    for s1, s2 in zip(seq1, seq2):
        print(s1)
        print(''.join(['|' if x == y else ' ' for x, y in zip(s1, s2)]))
        print(s2)
        print()