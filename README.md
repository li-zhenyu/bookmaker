# BookMaker
## 2021 年 6 月更新

- 增加了对 pylatex 的依赖。

- 兼容了特殊字符。（测试小说：《超神制卡师》）

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

1. 创建 `output`、`temp` 文件夹。

1. 使用 FictionDown 下载源文件（×.FictionDown）。

2. 把源文件更名为 novel.yaml,置于本程序根目录下。

3. 运行 `python3 bmaker`。

4. 进入 `.\output`，两次运行 `xelatex -synctex=1 -interaction=nonstopmode output.tex`。

5. `./output` 里的 `output.pdf` 即生成的文件。

## 可用性

目前只测试了 https://www.biqiuge.com 。

## 作者

li-zhenyu
