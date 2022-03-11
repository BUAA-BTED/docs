# 特性简介
mkdocs-material 支持 Markdown 的大部分特性，同时也提供了一些特殊的特性，比如 emojis 
:smile: ，比如按键图标化 ++ctrl+alt+delete++ ，完整的特性可以查阅[官方文档](https://squidfunk.github.io/mkdocs-material/reference/){target=_blank}。强烈建议在编写文档前打开这个页面作为 “Cookbook” 查阅。

*[emojis]: An emoji is a pictogram, logogram, ideogram or smiley embedded in text and used in electronic messages and web pages.

### 表格
$A$|$B$|$Y=A\oplus B$|
:-:|:-:|:-:
0|0|:material-close: 
0|1|:material-check: 
1|0|:material-check: 
1|1|:material-close: 

### 任务列表
- [ ] 二季度工作计划
    - [X] BEDT 课程运行
    - [ ] 空间无线电接收
        - [X] PlutoSDR 的 IIO 驱动
- [ ] 三季度工作计划


### MathJex 公式
```latex
X_n \oplus R_n \oplus R_n = X_n \oplus(R_n \oplus R_n) = X_n \oplus 0 = X_n
```

$$
X_n \oplus R_n \oplus R_n = X_n \oplus(R_n \oplus R_n) = X_n \oplus 0 = X_n
$$

!!! tip "一些增强或拓展了的特性"
    除了 material 提供的特性外，我们还增强了代码块的功能，可以通过在多行代码块起始符号后跟语言名字（例如 <code>```python</code>）来指定高亮的语言。
    

### 代码高亮
```verilog
// 前提条件： reg [6:0] shift_register
wire feedback = shift_register[6] ^ shift_register[3];
// 这是常见的组合逻辑描述方法之一：直接定义 wire
```

### 波形图
基于 [wavedrom](https://wavedrom.com){target=_blank}。当语言指定为 `wavedrom` 时，在代码框内填入对应的波形代码，即可渲染出波形图：

```wavedrom
{signal: [
  {name: 'clk', wave: 'P......'},
  {name: 'fcw', wave: 'x..3x..', data: ['fcw'],node:'...K', phase:0.5},
  {name: 'load', wave: '0..10..', phase: 0.5},
  {name: 'fcw_reg', wave: '4..3...', data: ['last_fcw','fcw']},
  {},
  ['buffered',
    {name: 'phase_acc_next1', wave: '4443333', node:'...a'},
    {name: 'phase_acc', wave: '4444333', node:'....b'}
  ],
  {},
  ['direct',
    {name: 'phase_acc_next2', wave: '4443333', node:'...c', phase:0.5},
    {name: 'phase_acc', wave: '4443333', node:'...d'}
  ]
  ],
  edge: [
      'a~b', 'c~d', 'K-c'
  ]
}
```

描述这个波形图的代码如下，你可以通过 [在线编辑器](https://wavedrom.com/editor.html){target=_blank} 来交互式地创建波形图，或使用 VSCode 的 Markdown Preview Enhanced
 插件。

```json
{signal: [
  {name: 'clk', wave: 'P......'},
  {name: 'fcw', wave: 'x..3x..', data: ['fcw'],node:'...K', phase:0.5},
  {name: 'load', wave: '0..10..', phase: 0.5},
  {name: 'fcw_reg', wave: '4..3...', data: ['last_fcw','fcw']},
  {},
  ['buffered',
    {name: 'phase_acc_next1', wave: '4443333', node:'...a'},
    {name: 'phase_acc', wave: '4444333', node:'....b'}
  ],
  {},
  ['direct',
    {name: 'phase_acc_next2', wave: '4443333', node:'...c', phase:0.5},
    {name: 'phase_acc', wave: '4443333', node:'...d'}
  ]
  ],
  edge: [
      'a~b', 'c~d', 'K-c'
  ]
}
```
