from itertools import groupby

def encode(seq):
    chunks = []
    prev = 'xx'
    for c in seq:
        if c != prev:
            prev = c
            chunk = [c]
            chunks.append(chunk)
        else:
            chunks[-1].append(c)
    return ''.join([f'{len(ch)}{ch[0]}' for ch in chunks])


def encode2(seq):
    res = []
    for val, subseq in groupby(seq):
        length = len(list(subseq))
        res.append(f'{length}{val}')
    return ''.join(res)


def decode(seq):
    chunks = [seq[i:i+2] for i in range(len(seq)-1) if i % 2 == 0]
    return ''.join([int(a)*b for a, b in chunks])


if __name__ == '__main__':
    assert encode('aabbbc') == '2a3b1c'
    assert encode2('aabbbc') == '2a3b1c'
    assert decode('2a3b1c') == 'aabbbc'
    assert encode('aabbc') == '2a2b1c'
    assert encode2('aabbc') == '2a2b1c'
    assert decode('2a2b1c') == 'aabbc'
    assert encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW') == '12W1B12W3B24W1B14W'
    assert encode2('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW') == '12W1B12W3B24W1B14W'
    assert encode2('') == ''
    assert decode('') == ''
