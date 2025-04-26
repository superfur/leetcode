# 1444. 切披萨的方案数

## 题目描述

<p>给你一个&nbsp;<code>rows x cols</code>&nbsp;大小的矩形披萨和一个整数 <code>k</code>&nbsp;，矩形包含两种字符：&nbsp;<code>&#39;A&#39;</code> （表示苹果）和&nbsp;<code>&#39;.&#39;</code>&nbsp;（表示空白格子）。你需要切披萨 <code>k-1</code> 次，得到&nbsp;<code>k</code>&nbsp;块披萨并送给别人。</p>

<p>切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。</p>

<p>请你返回确保每一块披萨包含&nbsp;<strong>至少</strong>&nbsp;一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/10/ways_to_cut_apple_1.png" style="height: 378px; width: 500px;"></strong></p>

<pre><strong>输入：</strong>pizza = [&quot;A..&quot;,&quot;AAA&quot;,&quot;...&quot;], k = 3
<strong>输出：</strong>3 
<strong>解释：</strong>上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>pizza = [&quot;A..&quot;,&quot;AA.&quot;,&quot;...&quot;], k = 3
<strong>输出：</strong>1
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>pizza = [&quot;A..&quot;,&quot;A..&quot;,&quot;...&quot;], k = 1
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= rows, cols &lt;= 50</code></li>
	<li><code>rows ==&nbsp;pizza.length</code></li>
	<li><code>cols ==&nbsp;pizza[i].length</code></li>
	<li><code>1 &lt;= k &lt;= 10</code></li>
	<li><code>pizza</code>&nbsp;只包含字符&nbsp;<code>&#39;A&#39;</code>&nbsp;和&nbsp;<code>&#39;.&#39;</code>&nbsp;。</li>
</ul>


## 难度

Hard

## 标签

- 记忆化搜索
- 数组
- 动态规划
- 矩阵
- 前缀和

## 提示

1. Note that after each cut the remaining piece of pizza always has the lower right coordinate at (rows-1,cols-1).
2. Use dynamic programming approach with states (row1, col1, c) which computes the number of ways of cutting the pizza using "c" cuts where the current piece of pizza has upper left coordinate at (row1,col1) and lower right coordinate at (rows-1,cols-1).
3. For the transitions try all vertical and horizontal cuts such that the piece of pizza you have to give a person must contain at least one apple. The base case is when c=k-1.
4. Additionally use a 2D dynamic programming to respond in O(1) if a piece of pizza contains at least one apple.

## 示例

```
["A..","AAA","..."]
3
["A..","AA.","..."]
3
["A..","A..","..."]
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int ways(vector<string>& pizza, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int ways(String[] pizza, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        
```

### C

```c
int ways(char** pizza, int pizzaSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int Ways(string[] pizza, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} pizza
 * @param {number} k
 * @return {number}
 */
var ways = function(pizza, k) {
    
};
```

### TypeScript

```typescript
function ways(pizza: string[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $pizza
     * @param Integer $k
     * @return Integer
     */
    function ways($pizza, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func ways(_ pizza: [String], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun ways(pizza: Array<String>, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int ways(List<String> pizza, int k) {
    
  }
}
```

### Go

```golang
func ways(pizza []string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String[]} pizza
# @param {Integer} k
# @return {Integer}
def ways(pizza, k)
    
end
```

### Scala

```scala
object Solution {
    def ways(pizza: Array[String], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn ways(pizza: Vec<String>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (ways pizza k)
  (-> (listof string?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec ways(Pizza :: [unicode:unicode_binary()], K :: integer()) -> integer().
ways(Pizza, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec ways(pizza :: [String.t], k :: integer) :: integer
  def ways(pizza, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func ways(pizza: Array<String>, k: Int64): Int64 {

    }
}
```

