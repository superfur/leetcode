# 608. 树节点

## 题目描述

<p>表：<code>Tree</code></p>

<pre>
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| p_id        | int  |
+-------------+------+
id 是该表中具有唯一值的列。
该表的每行包含树中节点的 id 及其父节点的 id 信息。
给定的结构总是一个有效的树。
</pre>

<p>&nbsp;</p>

<p>树中的每个节点可以是以下三种类型之一：</p>

<ul>
	<li><strong>"Leaf"</strong>：节点是叶子节点。</li>
	<li><strong>"Root"</strong>：节点是树的根节点。</li>
	<li><strong>"lnner"</strong>：节点既不是叶子节点也不是根节点。</li>
</ul>

<p>编写一个解决方案来报告树中每个节点的类型。</p>

<p>以 <strong>任意顺序</strong> 返回结果表。</p>

<p>结果格式如下所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/22/tree1.jpg" style="width: 304px; height: 224px;" />
<pre>
<b>输入：</b>
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
| 2  | 1    |
| 3  | 1    |
| 4  | 2    |
| 5  | 2    |
+----+------+
<b>输出：</b>
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
| 2  | Inner |
| 3  | Leaf  |
| 4  | Leaf  |
| 5  | Leaf  |
+----+-------+
<b>解释：</b>
节点 1 是根节点，因为它的父节点为空，并且它有子节点 2 和 3。
节点 2 是一个内部节点，因为它有父节点 1 和子节点 4 和 5。
节点 3、4 和 5 是叶子节点，因为它们有父节点而没有子节点。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/22/tree2.jpg" style="width: 64px; height: 65px;" />
<pre>
<b>输入：</b>
Tree table:
+----+------+
| id | p_id |
+----+------+
| 1  | null |
+----+------+
<b>输出：</b>
+----+-------+
| id | type  |
+----+-------+
| 1  | Root  |
+----+-------+
<b>解释：</b>如果树中只有一个节点，则只需要输出其根属性。
</pre>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与 <a href="https://leetcode.cn/problems/binary-tree-nodes/">3054. 二叉树节点</a> 一致。</p>


## 难度

Medium

## 标签

- 数据库

## 提示

1. You can judge the node type by querying whether the node's id shows up in p_id column and whether the node's p_id is null.

## 示例

```
{"headers":{"Tree":["id","p_id"]},"rows":{"Tree":[[1,null],[2,1],[3,1],[4,2],[5,2]]}}
{"headers":{"Tree":["id","p_id"]},"rows":{"Tree":[[1,null]]}}
```

## 示例代码

### MySQL

```mysql
# Write your MySQL query statement below
```

### MS SQL Server

```mssql
/* Write your T-SQL query statement below */
```

### Oracle

```oraclesql
/* Write your PL/SQL query statement below */
```

### Pandas

```pythondata
import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

