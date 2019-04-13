def scale(word):
    if word[-2:] == ';\n':
        return 'calc(' + word[:-2] + ' / #{$size_divisor});\n'
    elif word[-3:] == ');\n':
        return '(' + word[:-3] + ' / #{$size_divisor}));\n'
    return 'calc(' + word + ' / #{$size_divisor})'


if __name__ == '__main__':
    f = open('devices_old.scss', 'r')
    scss = f.readlines()
    f.close()
    out = '$size_divisor: 2;\n\n'
    for line in scss:
        words = line.split(' ')
        for i in range(len(words)):
            if 'px' in words[i]:
                words[i] = scale(words[i])
        out += ' '.join(words)
    f = open('devices_new.scss', 'w')
    f.write(out)
    f.close()
