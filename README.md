# BTED 教程网站

本教程网站基于 [mkdocs-material](https://github.com/squidfunk/mkdocs-material) 构建。整个仓库的目录结构如下：

```
├── README.md
├── docs
│   ├── assets             // 用于存放当前目录下 md 文件的图片
│   ├── basic              // 【基础教程】栏目
│   ├── index.md           // 主页
│   ├── lib                // 拓展库
│   └── reference          // 【参考】栏目
├── mkdocs-wavedrom-plugin // wavedrom 插件目录
├── mkdocs.yml             // 配置文件
└── requirements.txt
```

## 在本地构建并预览网站

1. 安装 Python3；
1. fork 本仓库，并克隆到本地；
1. 在本地的仓库根目录下，创建 Python 虚拟环境：

    ```shell
    python -m venv venv
    ```

    此时，当前目录下应该出现 `venv` 文件夹，在 `.gitignore` 文件中已经排除了它，所以不用担心它会被加入版本管理中。

1. 激活虚拟环境：

    在 Linux 下：`source venv/bin/activate`
    
    在 Windows 的 CMD 内：`venv\Script\activate.bat`

    在 Windows 的 PowerShell 内：`.\venv\Scripts\Activate.ps1`

    激活完成后，提示符应该出现 `(venv)` 字样。在激活的状态输入 `deactivate` 即可退出虚拟环境。

1. **第一次**激活虚拟环境，需要安装需要的包：

    ```shell
    pip install mkdocs-material
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
    pip install -e mkdocs-wavedrom-plugin
    ```

1. 安装完毕后，测试 mkdocs 是否能够运行，在根目录下运行：

    ```shell
    mkdocs serve
    ```

    若出现 `INFO     -  [13:27:03] Serving on http://127.0.0.1:8000/` 则说明 mkdocs 成功构建了网站，使用浏览器打开 http://127.0.0.1:8000 即可访问网站的预览，**mkdocs 会在检测到文档文件更新后自动重新构建，而无需重复启动**。

**请在本地预览无误后再提交！！**

## 文档规范

### 目录组织

```
docs/
├── assets
├── index.md
├── basic
│   ├── assets
│   │   ├── Arduino-IDE-Blink.png
│   │   ├── BTED-ESP32-Blockdiagram.drawio
│   │   ├── BTED-ESP32-Blockdiagram.drawio.svg
│   │   └── （以下省略）
│   ├── esp32-core.md
│   ├── get-started.md
│   └── install.md
└── reference
    ├── assets
    ├── hardware-ref.md
    └── software-ref.md
```
* 每个栏目（导航栏）**必须**对应一个文件夹，比如 `basic` 和 `reference` 分别对应【基础文档】和【参考资料】两个栏目；
* `index.md` 为首页即【欢迎】栏目；
* 其他每个 `md` **必须**对应一个文档页面；
    * 命名要求：**全小写**英语，使用减号 `'-'` 分词，尽量不要使用例如 `basic-1`，`basic-2 ` 此类意义不明的命名；
    * 页面创建后需要在 `mkdocs.yml` 中**手动添加**并设置路径才会加入构建。
* `assets` 文件夹：用于保存**当前目录下**文档的附件，在文档中使用 `assets/xxx.png` 来引用。
    * 新建栏目时，请在栏目文件夹内手动创建 `assets` 文件夹；
    * **要求**图片的命名使用 ASCII 字符，使用减号 `'-'` 分词；
    * **要求**使用 [wavedrom](https://wavedrom.com) 绘制波形图，通过代码块嵌入文档中；
    * **推荐**使用 [draw.io](http://draw.io) 绘图，并导出 `svg` 矢量图，并将 `.drawio` 源文件也存入该文件夹以便编辑。
    

### 配置文件

`mkdocs.yml` 是整个文档的配置文件，其中包含了主题、插件、导航栏和外部引用等配置信息，正常情况下，只需要修改 `nav` 栏目下的导航配置：

```yml
nav:
  - index.md
  - 基础文档：# 栏目的名字
  # 以下是该栏目下的所有文档，这里的次序即显示的次序
    - basic/esp32-core.md # 文档的路径
    - basic/install.md
    - basic/get-started.md
  - 参考资料：
    - reference/hardware-ref.md
    - reference/software-ref.md
```

当增减了文档或栏目时，需要对应修改。

### Markdown 文件

在编写 Markdown 文字时，**需要**遵守以下规范：
* 汉字和字母或数字混用时，在字母或数字前后各添加一个空格，比如 `实用 Arduino 教程第 1 篇`；
* 与汉字相邻的标点符号使用全角，比如 `（中文）`；

**建议** 使用 VS Code 编辑文档，并安装 `Pangu-Markdown` 插件，它能自动格式化 Markdown 文档以符合上述要求。

* 在添加图片时，请将图片存入 `assets` 文件夹，而不要使用外部链接；

* 在添加链接时，除非在文档内部跳转，需要在末尾加上 `{:target="_blank"}` 以确保点击该链接时的行为是【在新标签栏内打开】；

* 目前条件下，文档内部跳转时，**无法**使用相对路径如 `[get-started](basic/get-started.md)`，请使用发布后的**完整链接** `https://buaa-bted.github.io/docs/` + 目标路径 `basic/get-started.md`。

## 特性

### Mkdocs-material

该框架提供了许多实用的特性，**建议**在编写文档时充分利用这些特性。[Mkdocs-material Reference](https://squidfunk.github.io/mkdocs-material/reference/)

### Wavedrom 波形渲染库

Wavedrom 能将 WaveJson 渲染为波形图。在文档中使用代码段，并指明语言为 `wavedrom` 即可。

````markdown
```wavedrom
{ signal: [
  { name: "clk",  wave: "P......" },
  { name: "bus",  wave: "x.==.=x", data: ["head", "body", "tail", "data"] },
  { name: "wire", wave: "0.1..0." }
]}
```
````

[在线编辑器](https://wavedrom.com/editor.html)

[Wavedrom 教程](https://wavedrom.com/tutorial.html)