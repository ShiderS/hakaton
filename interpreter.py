import sys, pymorphy2, re

text = sys.stdin.read()
text = text.split('\n')
morph = pymorphy2.MorphAnalyzer()
output = []

for i in range(len(text)):
    text1 = re.split('\W', text[i])
    text2 = []
    for j in range(len(text1)):
        if text1[j] != '' and len(text1[j]) > 1:
            text2.append(morph.parse(text1[j])[0].normal_form.lower())
    output.append(' '.join(text2))
print(*output, sep='\n')
