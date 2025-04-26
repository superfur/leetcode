# 749. 隔离病毒

## 题目描述

<p>病毒扩散得很快，现在你的任务是尽可能地通过安装防火墙来隔离病毒。</p>

<p>假设世界由&nbsp;<code>m x n</code>&nbsp;的二维矩阵&nbsp;<code>isInfected</code>&nbsp;组成，&nbsp;<code>isInfected[i][j] == 0</code>&nbsp;表示该区域未感染病毒，而 &nbsp;<code>isInfected[i][j] == 1</code>&nbsp;表示该区域已感染病毒。可以在任意 2 个相邻单元之间的共享边界上安装一个防火墙（并且只有一个防火墙）。</p>

<p>每天晚上，病毒会从被感染区域向相邻未感染区域扩散，除非被防火墙隔离。现由于资源有限，每天你只能安装一系列防火墙来隔离其中一个被病毒感染的区域（一个区域或连续的一片区域），且该感染区域对未感染区域的威胁最大且 <strong>保证唯一&nbsp;</strong>。</p>

<p>你需要努力使得最后有部分区域不被病毒感染，如果可以成功，那么返回需要使用的防火墙个数; 如果无法实现，则返回在世界被病毒全部感染时已安装的防火墙个数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/06/01/virus11-grid.jpg" style="height: 255px; width: 500px;" /></p>

<pre>
<strong>输入:</strong> isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
<strong>输出:</strong> 10
<strong>解释:</strong>一共有两块被病毒感染的区域。
在第一天，添加 5 墙隔离病毒区域的左侧。病毒传播后的状态是:
<img src="https://assets.leetcode.com/uploads/2021/06/01/virus12edited-grid.jpg" style="height: 261px; width: 500px;" />
第二天，在右侧添加 5 个墙来隔离病毒区域。此时病毒已经被完全控制住了。
<img src="https://assets.leetcode.com/uploads/2021/06/01/virus13edited-grid.jpg" style="height: 261px; width: 500px;" />
</pre>

<p><strong>示例 2：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2021/06/01/virus2-grid.jpg" style="height: 253px; width: 653px;" /></p>

<pre>
<strong>输入:</strong> isInfected = [[1,1,1],[1,0,1],[1,1,1]]
<strong>输出:</strong> 4
<strong>解释:</strong> 虽然只保存了一个小区域，但却有四面墙。
注意，防火墙只建立在两个不同区域的共享边界上。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre>
<strong>输入:</strong> isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
<strong>输出:</strong> 13
<strong>解释:</strong> 在隔离右边感染区域后，隔离左边病毒区域只需要 2 个防火墙。
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>m ==&nbsp;isInfected.length</code></li>
	<li><code>n ==&nbsp;isInfected[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 50</code></li>
	<li><code>isInfected[i][j]</code>&nbsp;is either&nbsp;<code>0</code>&nbsp;or&nbsp;<code>1</code></li>
	<li>在整个描述的过程中，总有一个相邻的病毒区域，它将在下一轮 <strong>严格地感染更多未受污染的方块</strong>&nbsp;</li>
</ul>

<p>&nbsp;</p>


## 难度

Hard

## 标签

- 深度优先搜索
- 广度优先搜索
- 数组
- 矩阵
- 模拟

## 提示

1. The implementation is long - we want to perfrom the following steps:

* Find all viral regions (connected components), additionally for each region keeping track of the frontier (neighboring uncontaminated cells), and the perimeter of the region.

* Disinfect the most viral region, adding it's perimeter to the answer.

* Spread the virus in the remaining regions outward by 1 square.

## 示例

```
[[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
[[1,1,1],[1,0,1],[1,1,1]]
[[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int containVirus(vector<vector<int>>& isInfected) {
        
    }
};
```

### Java

```java
class Solution {
    public int containVirus(int[][] isInfected) {
        
    }
}
```

### Python

```python
class Solution(object):
    def containVirus(self, isInfected):
        """
        :type isInfected: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        
```

### C

```c
int containVirus(int** isInfected, int isInfectedSize, int* isInfectedColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int ContainVirus(int[][] isInfected) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} isInfected
 * @return {number}
 */
var containVirus = function(isInfected) {
    
};
```

### TypeScript

```typescript
function containVirus(isInfected: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $isInfected
     * @return Integer
     */
    function containVirus($isInfected) {
        
    }
}
```

### Swift

```swift
class Solution {
    func containVirus(_ isInfected: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun containVirus(isInfected: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int containVirus(List<List<int>> isInfected) {
    
  }
}
```

### Go

```golang
func containVirus(isInfected [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} is_infected
# @return {Integer}
def contain_virus(is_infected)
    
end
```

### Scala

```scala
object Solution {
    def containVirus(isInfected: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn contain_virus(is_infected: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (contain-virus isInfected)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec contain_virus(IsInfected :: [[integer()]]) -> integer().
contain_virus(IsInfected) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec contain_virus(is_infected :: [[integer]]) :: integer
  def contain_virus(is_infected) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func containVirus(isInfected: Array<Array<Int64>>): Int64 {

    }
}
```

