import yaml
import os
import re
import pylatex


def latexize_str(str):
    tmpdoc = pylatex.Document()
    tmpdoc.append(str)
    uncutstr = tmpdoc.dumps()
    uncutstr = uncutstr.replace('\\documentclass{article}%\n\\usepackage[T1]{fontenc}%\n\\usepackage[utf8]{inputenc}%\n\\usepackage{lmodern}%\n\\usepackage{textcomp}%\n\\usepackage{lastpage}%\n%\n%\n%\n\\begin{document}%\n\\normalsize%\n','')
    return uncutstr.replace("%\n\\end{document}", "")


def read_file():
	n = open("novel.yaml", encoding='utf-8')
	nstr = n.read()
	n.close()
	nyaml = yaml.load(nstr)
	nstr = None
	os.chdir("./temp")
	f = open('dict', 'w')
	print(nyaml, file=f)
	f.close()
	os.chdir("..")
	print(type(nyaml))
	return nyaml


def maker(yaml):
    os.chdir("output")
    body = r'''
\documentclass[UTF-8]{ctexbook}
\usepackage{geometry}
\usepackage{ctex}
\usepackage{hyperref}
\geometry{a4paper,scale=0.8}
\begin{document}
\frontmatter
\title{TITLE}
\author{AUTHOR}
\date{}
\maketitle

\input{lists}
\end{document}
    
    '''
    print(666666)
    body = re.sub(r"TITLE",latexize_str(yaml['bookname']), body)
    body = re.sub(r"AUTHOR", latexize_str(yaml['author']), body)
    lists = open("lists.tex", "w")
    lists.write("\\tableofcontents\n\\mainmatter\n")
    i = 0
    for chapter in yaml['volumes'][0]['chapters']:
        i = i + 1
        c = open("c"+str(i)+".tex", 'w')
        c.write(r"\chapter{"+re.sub(r"第.*?章\s", "", chapter['name'])+'}\n')
        for paragraph in chapter['text']:
            if ".com" in paragraph:
                continue
            c.write(latexize_str(paragraph)+'\n\n')
        c.close()
        lists.write(r'\input{'+'c'+str(i)+'}\n')
    lists.close()
    o = open("output.tex", 'w')
    o.write(body)
    o.close()


yaml = read_file()
maker(yaml)
