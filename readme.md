# 拼图

## 问题描述

本问题是一个不规则图块的拼图问题。图块与放置区域均为由大小相等的矩形方格组成。将若干个形状不规则的图块，无重叠的放置到一个放置区域（内部可以存在不可放置的方格）之中，使得所有图块正好完全填充满该区域。图块在放置时可以向任意方向连续旋转90度，但不可以翻转。

## 数学分析

### 变量表示

#### 图块

图块以C表示。设图块的数量为n，低n个图块记为Cn。每个图块存在4种可能的旋转状态，状态记为S，4种状态分别为S1, S2, S3, S4。

#### 放置区域

放置区域以B表示。放置区域存在最大外接矩形，大小为w * h。

### 可能性分析

1. 如何描述问题的解：
图块与区域均为大小相等的单元方格组成，所以问题可以形象的以矩阵的形式表示。但在分析可能存在的结果时，矩阵的表达方式并不直观且难以分析。所以在此将问题简化为n个图块的排列组合问题。设R为一个有序集合，集合的元素为C(S)，即图块(状态)。当问题存在解时，初始空的集合R0。从区域左上角出发，以从左到右，从上到下的顺序遍历每一个单元格。若填充当前单元格的图块Cx(Sy)不在集合中，则将其添加到集合中。当遍历完成后，得到集合R0 = {..., Cx(Sy), ...}，大小为n，即为问题的解。

2. 可能存在的结果：
对于n个元素，其可能存在的排列组合数量为n!。同时，对于集合R中的每一个元素C(S)，S存在4种取值，所以对于一个确定的有序集合{C1, C2, ..., Cn}, 当为C添加属性S得到C(S)后，会存在4^n个可能的组合。因此对于问题的解R，存在 4^n * n! 种可能存在的结果。
