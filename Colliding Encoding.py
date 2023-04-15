def has_collisions(mapping, words):
    encoded_words = set()
    for word in words:
        encoded_word = ''.join(mapping[ord(letter) - ord('A')] for letter in word)
        if encoded_word in encoded_words:
            return True
        encoded_words.add(encoded_word)
    return False

T = int(input())

for t in range(1, T + 1):
    mapping = input().strip().split()
    mapping = list(map(int, mapping))
    mapping = [str(x) for x in mapping]
    words = []
    N = int(input())
    for _ in range(N):
        words.append(input().strip())

    if has_collisions(mapping, words):
        print("Case #{}: YES".format(t))
    else:
        print("Case #{}: NO".format(t))
