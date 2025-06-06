# 2055. 蜡烛之间的盘子

## 题目描述

<p>给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>s</code>&nbsp;，它只包含字符&nbsp;<code>'*'</code> 和&nbsp;<code>'|'</code>&nbsp;，其中&nbsp;<code>'*'</code>&nbsp;表示一个 <strong>盘子</strong>&nbsp;，<code>'|'</code>&nbsp;表示一支&nbsp;<strong>蜡烛</strong>&nbsp;。</p>

<p>同时给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>queries</code>&nbsp;，其中&nbsp;<code>queries[i] = [left<sub>i</sub>, right<sub>i</sub>]</code>&nbsp;表示 <strong>子字符串</strong>&nbsp;<code>s[left<sub>i</sub>...right<sub>i</sub>]</code>&nbsp;（<strong>包含左右端点的字符</strong>）。对于每个查询，你需要找到 <strong>子字符串中</strong>&nbsp;在 <strong>两支蜡烛之间</strong>&nbsp;的盘子的 <b>数目</b>&nbsp;。如果一个盘子在 <strong>子字符串中</strong>&nbsp;左边和右边 <strong>都</strong>&nbsp;至少有一支蜡烛，那么这个盘子满足在 <strong>两支蜡烛之间</strong>&nbsp;。</p>

<ul>
	<li>比方说，<code>s = "||**||**|*"</code>&nbsp;，查询&nbsp;<code>[3, 8]</code>&nbsp;，表示的是子字符串&nbsp;<code>"*||<strong><em>**</em></strong>|"</code>&nbsp;。子字符串中在两支蜡烛之间的盘子数目为&nbsp;<code>2</code>&nbsp;，子字符串中右边两个盘子在它们左边和右边 <strong>都 </strong>至少有一支蜡烛。</li>
</ul>

<p>请你返回一个整数数组&nbsp;<code>answer</code>&nbsp;，其中&nbsp;<code>answer[i]</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;个查询的答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<p><img alt="ex-1" src="https://assets.leetcode.com/uploads/2021/10/04/ex-1.png" style="width: 400px; height: 134px;"></p>

<pre><b>输入：</b>s = "**|**|***|", queries = [[2,5],[5,9]]
<b>输出：</b>[2,3]
<b>解释：</b>
- queries[0] 有两个盘子在蜡烛之间。
- queries[1] 有三个盘子在蜡烛之间。
</pre>

<p><strong>示例 2:</strong></p>

<p><img alt="ex-2" src="https://assets.leetcode.com/uploads/2021/10/04/ex-2.png" style="width: 600px; height: 193px;"></p>

<pre><b>输入：</b>s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
<b>输出：</b>[9,0,0,0,0]
<strong>解释：</strong>
- queries[0] 有 9 个盘子在蜡烛之间。
- 另一个查询没有盘子在蜡烛之间。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code>&nbsp;只包含字符&nbsp;<code>'*'</code> 和&nbsp;<code>'|'</code>&nbsp;。</li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 2</code></li>
	<li><code>0 &lt;= left<sub>i</sub> &lt;= right<sub>i</sub> &lt; s.length</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串
- 二分查找
- 前缀和

## 提示

1. Can you find the indices of the most left and right candles for a given substring, perhaps by using binary search (or better) over an array of indices of all the bars?
2. Once the indices of the most left and right bars are determined, how can you efficiently count the number of plates within the range? Prefix sums?

## 示例

```
"**|**|***|"
[[2,5],[5,9]]
"***|**|*****|**||**|*"
[[1,17],[4,5],[14,17],[5,11],[15,16]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> platesBetweenCandles(string s, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] platesBetweenCandles(String s, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def platesBetweenCandles(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* platesBetweenCandles(char* s, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] PlatesBetweenCandles(string s, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number[][]} queries
 * @return {number[]}
 */
var platesBetweenCandles = function(s, queries) {
    
};
```

### TypeScript

```typescript
function platesBetweenCandles(s: string, queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function platesBetweenCandles($s, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func platesBetweenCandles(_ s: String, _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun platesBetweenCandles(s: String, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> platesBetweenCandles(String s, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func platesBetweenCandles(s string, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer[][]} queries
# @return {Integer[]}
def plates_between_candles(s, queries)
    
end
```

### Scala

```scala
object Solution {
    def platesBetweenCandles(s: String, queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn plates_between_candles(s: String, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (plates-between-candles s queries)
  (-> string? (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec plates_between_candles(S :: unicode:unicode_binary(), Queries :: [[integer()]]) -> [integer()].
plates_between_candles(S, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec plates_between_candles(s :: String.t, queries :: [[integer]]) :: [integer]
  def plates_between_candles(s, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func platesBetweenCandles(s: String, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

