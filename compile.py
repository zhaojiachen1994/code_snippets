# encdoing: utf-8
import os
import re
from icecream import ic

# 代码模块的分类
SECTIONS = ['plot',  # code for plt images
            'chatgpt'
            ]

# 每个.md中所含的项
ITEMS = ['TITLE', 'INTRODUCTION', 'FIGURE', 'CODE']

def read_md(f):
    with open(f, 'r', encoding='utf-8') as file:
        content=file.read()

    patterns = {
        'TITLE': r'\\TITLE\n(.*?)\\END TITLE',
        'INTRODUCTION': r'\\INTRODUCTION\n(.*?)\\END INTRODUCTION',
        'FIGURE': r'\\FIGURE\n(.*?)\\END FIGURE',
        'CODE': r'\\CODE\n(.*?)\\END CODE'
    }
    items = {}
    for i in ITEMS:
        pattern = patterns[i]
        match = re.search(pattern, content, re.DOTALL)
        if match:
            items[i] = match.group(1).splitlines()
        else:
            items[i] = None
    return items


def write_md(contents, file):

    with open(file, 'w', encoding='utf-8') as f:
        for content in contents:
            f.write("<details>\n")
            f.write(f"<summary><strong>  {''.join(content['TITLE'])} </strong></summary>\n\n")
            if content['INTRODUCTION'] is not None:
                for l in content['INTRODUCTION']:
                    f.write(l)
                    f.write("\n\n")
            if content['CODE'] is not None:
                for l in content['CODE']:
                    f.write(l)
                    f.write("\n")
            f.write("\n")
            f.write("</details>")
            if content['FIGURE'] is not None:
                fig = content['FIGURE'][0]
                f.write(f"<div align=left><img src='figures/{fig}' width='200' height='120'/></div>")
                f.write("\n")
            f.write("\n---\n\n")

def write_README(file, titles):
    with open(file, 'w', encoding='utf-8') as f:
        f.write("# Code snippets \n\n")
        for s in SECTIONS:
            f.write(f"## {s} \n")
            for title in titles[s]:
                f.write(f"* {title} \n")
            f.write("---\n")




if __name__ == "__main__":
    print('-----')
    # read markdowns

    titles = {}
    for s in SECTIONS:
        files = sorted([f"lib/{s}/{x}" for x in os.listdir(f"lib/{s}") if x.endswith(".md")])
        contents = [read_md(file) for file in files]
        out_md = f"{s.lower()}.md"
        write_md(contents, out_md)
        titles[s] = [content['TITLE'][0] for content in contents]
    write_README('README.md', titles)







