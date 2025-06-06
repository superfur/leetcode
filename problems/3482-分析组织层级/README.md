# 3482. 分析组织层级

## 题目描述

<p>表：<code>Employees</code></p>

<pre>
+----------------+---------+
| Column Name    | Type    | 
+----------------+---------+
| employee_id    | int     |
| employee_name  | varchar |
| manager_id     | int     |
| salary         | int     |
| department     | varchar |
+----------------+----------+
employee_id 是这张表的唯一主键。
每一行包含关于一名员工的信息，包括他们的 ID，姓名，他们经理的 ID，薪水和部门。
顶级经理（CEO）的 manager_id 是空的。
</pre>

<p>编写一个解决方案来分析组织层级并回答下列问题：</p>

<ol>
	<li><strong>层级：</strong>对于每名员工，确定他们在组织中的层级（CEO 层级为&nbsp;<code>1</code>，CEO 的直接下属员工层级为&nbsp;<code>2</code>，以此类推）。</li>
	<li><strong>团队大小：</strong>对于每个是经理的员工，计算他们手下的（直接或间接下属）总员工数。</li>
	<li><strong>薪资预算：</strong>对于每个经理，计算他们控制的总薪资预算（所有手下员工的工资总和，包括间接下属，加上自己的工资）。</li>
</ol>

<p>返回结果表以 <strong>层级</strong>&nbsp;<strong>升序</strong>&nbsp;排序，然后以预算 <strong>降序</strong> 排序，最后以 <strong>employee_name&nbsp;升序 </strong>排序。</p>

<p>结果格式如下所示。</p>

<p>&nbsp;</p>

<p><strong class="example">示例：</strong></p>

<div class="example-block">
<p><strong>输入：</strong></p>

<p>Employees 表：</p>

<pre class="example-io">
+-------------+---------------+------------+--------+-------------+
| employee_id | employee_name | manager_id | salary | department  |
+-------------+---------------+------------+--------+-------------+
| 1           | Alice         | null       | 12000  | Executive   |
| 2           | Bob           | 1          | 10000  | Sales       |
| 3           | Charlie       | 1          | 10000  | Engineering |
| 4           | David         | 2          | 7500   | Sales       |
| 5           | Eva           | 2          | 7500   | Sales       |
| 6           | Frank         | 3          | 9000   | Engineering |
| 7           | Grace         | 3          | 8500   | Engineering |
| 8           | Hank          | 4          | 6000   | Sales       |
| 9           | Ivy           | 6          | 7000   | Engineering |
| 10          | Judy          | 6          | 7000   | Engineering |
+-------------+---------------+------------+--------+-------------+
</pre>

<p><strong>输出：</strong></p>

<pre class="example-io">
+-------------+---------------+-------+-----------+--------+
| employee_id | employee_name | level | team_size | budget |
+-------------+---------------+-------+-----------+--------+
| 1           | Alice         | 1     | 9         | 84500  |
| 3           | Charlie       | 2     | 4         | 41500  |
| 2           | Bob           | 2     | 3         | 31000  |
| 6           | Frank         | 3     | 2         | 23000  |
| 4           | David         | 3     | 1         | 13500  |
| 7           | Grace         | 3     | 0         | 8500   |
| 5           | Eva           | 3     | 0         | 7500   |
| 9           | Ivy           | 4     | 0         | 7000   |
| 10          | Judy          | 4     | 0         | 7000   |
| 8           | Hank          | 4     | 0         | 6000   |
+-------------+---------------+-------+-----------+--------+
</pre>

<p><strong>解释：</strong></p>

<ul>
	<li><strong>组织结构：</strong>

	<ul>
		<li>Alice（ID：1）是 CEO（层级 1）没有经理。</li>
		<li>Bob（ID：2）和&nbsp;Charlie（ID：3）是&nbsp;Alice 的直接下属（层级 2）</li>
		<li>David（ID：4），Eva（ID：5）从属于&nbsp;Bob，而 Frank（ID：6）和 Grace（ID：7）从属于&nbsp;Charlie（层级 3）</li>
		<li>Hank（ID：8）从属于&nbsp;David，而 Ivy（ID：9）和&nbsp;Judy（ID：10）从属于&nbsp;Frank（层级 4）</li>
	</ul>
	</li>
	<li><strong>层级计算：</strong>
	<ul>
		<li>CEO（Alice）层级为 1</li>
		<li>每个后续的管理层级都会使层级数加 1</li>
	</ul>
	</li>
	<li><strong>团队大小计算：</strong>
	<ul>
		<li>Alice 手下有 9 个员工（除她以外的整个公司）</li>
		<li>Bob 手下有 3 个员工（David，Eva 和 Hank）</li>
		<li>Charlie 手下有 4 个员工（Frank，Grace，Ivy 和 Judy）</li>
		<li>David 手下有 1 个员工（Hank）</li>
		<li>Frank 手下有 2 个员工（Ivy 和 Judy）</li>
		<li>Eva，Grace，Hank，Ivy 和 Judy 没有直接下属（team_size = 0）</li>
	</ul>
	</li>
	<li><strong>预算计算：</strong>
	<ul>
		<li>Alice 的预算：她的工资（12000）+ 所有员工的工资（72500）= 84500</li>
		<li>Charlie 的预算：他的工资（10000）+ Frank 的预算（23000）+ Grace 的工资（8500）= 41500</li>
		<li>Bob 的预算：他的工资 (10000) + David&nbsp;的预算（13500）+ Eva&nbsp;的工资（7500）= 31000</li>
		<li>Frank 的预算：他的工资 (9000) + Ivy 的工资（7000）+ Judy&nbsp;的工资（7000）= 23000</li>
		<li>David 的预算：他的工资 (7500) + Hank 的工资（6000）= 13500</li>
		<li>没有直接下属的员工的预算等于他们自己的工资。</li>
	</ul>
	</li>
</ul>

<p><strong>注意：</strong></p>

<ul>
	<li>结果先以层级升序排序</li>
	<li>在同一层级内，员工按预算降序排序，然后按姓名升序排序</li>
</ul>
</div>


## 难度

Hard

## 标签

- 数据库

## 示例

```
{"headers":{"Employees":["employee_id","employee_name","manager_id","salary","department"]},"rows":{"Employees":[[1,"Alice",null,12000,"Executive"],[2,"Bob",1,10000,"Sales"],[3,"Charlie",1,10000,"Engineering"],[4,"David",2,7500,"Sales"],[5,"Eva",2,7500,"Sales"],[6,"Frank",3,9000,"Engineering"],[7,"Grace",3,8500,"Engineering"],[8,"Hank",4,6000,"Sales"],[9,"Ivy",6,7000,"Engineering"],[10,"Judy",6,7000,"Engineering"]]}}
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

def analyze_organization_hierarchy(employees: pd.DataFrame) -> pd.DataFrame:
    
```

### PostgreSQL

```postgresql
-- Write your PostgreSQL query statement below
```

