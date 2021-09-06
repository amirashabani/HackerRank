import re

tags_pattern = r"<\s*([\w]+)\s*(.*?)\s*\/?>"
attrs_pattern = r'\s*([\w]+)\s*=\s*[\'\"][^\'\"]*?[\'\"]\s*'

n = int(input())
sentences = [input() for _ in range(n)]


tags = {}
for s in sentences:
    for m in re.finditer(tags_pattern, s):
        name = m.group(1)
        attrs = set(re.findall(attrs_pattern, m.group(2)))
        if name in tags:
            tags[name].update(attrs)
        else:
            tags[name] = set()
            tags[name].update(attrs)

for k in sorted(tags.keys()):
    line = "{}:{}".format(
        k,
        ','.join(sorted(tags[k]))
    )
    print(line)

