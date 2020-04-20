import os

def scale(token):
    if token[-2:] == ';\n':
        return 'calc(' + token[:-2] + ' / var(--size-divisor));\n'
    elif token[-3:] == ');\n':
        return '(' + token[:-3] + ' / var(--size-divisor));\n'
    return 'calc(' + token + ' / var(--size-divisor))'

def build_file(scss):
    out = ':root {\n\t--size-divisor: 3;\n}\n\n'
    for line in scss:
        tokens = line.split(' ')
        for i in range(len(tokens)):
            if 'px' in tokens[i]:
                tokens[i] = scale(tokens[i])
        out += ' '.join(tokens)
    out += "@media (min-width: 576px) {\n  \
            :root {\n\t--size-divisor: 2;\n  \
            }\n}\n\n@media (min-width: 768px) {\n \
            :root {\n\t--size-divisor: 1.5;\n  \
            }\n}\n\n@media (min-width: 992px) { \
            \n  :root {\n\t--size-divisor: 1;\n  \
            }\n}\n\n@media (min-width: 1200px) { \
            \n  :root {\n\t--size-divisor: .67;\n  }\n}"
    return out

if __name__ == '__main__':
    f = open('devices_old.scss', 'r')
    scss = f.readlines()
    f.close()
    out = build_file(scss)
    f = open('devices_new.scss', 'w')
    f.write(out)
    f.close()
    os.system("sass devices_new.scss devices.css")

