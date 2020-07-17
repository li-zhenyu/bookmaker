# BookMaker

## 简介

凭借 FictonDown 的 YAML 使用 LaTeX 排版小说。

## 示例

链接：https://share.weiyun.com/ORqoNPL7 密码：phu4z4

或在 `./example` 中下载。

## 依赖

- FictionDown https://github.com/ma6254/FictionDown

- TeXLive 或其他 TeX 发行。

- Python 3

## 用法

1. 使用 FictionDown 下载源文件（×.FictionDown）。

2. 把源文件更名为 novel.yaml,置于本程序根目录下。

3. 运行 `python3 bmaker`。

4. 进入 `.\output`，两次运行 `xelatex -synctex=1 -interaction=nonstopmode output.tex`。


## 作者

li-zhenyu
