from typing import List

def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    result = []
    i = 0

    while i < len(words):
        line_len = len(words[i])
        j = i + 1
        while j < len(words) and line_len + 1 + len(words[j]) <= maxWidth:
            line_len += 1 + len(words[j])
            j += 1

        line_words = words[i:j]
        total_chars = sum(len(w) for w in line_words)
        gaps = len(line_words) - 1
        is_last_line = j == len(words)

        if gaps == 0 or is_last_line:
            line = ' '.join(line_words)
            line += ' ' * (maxWidth - len(line))
            result.append(line)
        else:
            total_spaces = maxWidth - total_chars
            space_per_gap = total_spaces // gaps
            extra_spaces = total_spaces % gaps
            line = ''
            for k in range(len(line_words)):
                line += line_words[k]
                if k < gaps:
                    line += ' ' * (space_per_gap + (1 if extra_spaces > 0 else 0))
                    if extra_spaces > 0:
                        extra_spaces -= 1
            result.append(line)

        i = j

    return result

if __name__ == "__main__":
    test_cases = [
        (["This", "is", "an", "example", "of", "text", "justification."], 16),
        (["What","must","be","acknowledgment","shall","be"], 16),
        (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20),
    ]
    expected = [
        ["This    is    an", "example  of text", "justification.  "],
        ["What   must   be", "acknowledgment  ", "shall be        "],
        ["Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "],
    ]
    for i, ((words, maxWidth), exp) in enumerate(zip(test_cases, expected), 1):
        result = fullJustify(words, maxWidth)
        ok = result == exp
        print(f"测试用例 {i}: {'PASS' if ok else 'FAIL'}")
        if not ok:
            print(f"  expected: {exp}")
            print(f"  got:      {result}")
