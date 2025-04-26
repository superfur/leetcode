# 2976. 转换字符串的最小成本 I

## 题目描述

<p>给你两个下标从 <strong>0</strong> 开始的字符串 <code>source</code> 和 <code>target</code> ，它们的长度均为 <code>n</code> 并且由 <strong>小写 </strong>英文字母组成。</p>

<p>另给你两个下标从 <strong>0</strong> 开始的字符数组 <code>original</code> 和 <code>changed</code> ，以及一个整数数组 <code>cost</code> ，其中 <code>cost[i]</code> 代表将字符 <code>original[i]</code> 更改为字符 <code>changed[i]</code> 的成本。</p>

<p>你从字符串 <code>source</code> 开始。在一次操作中，<strong>如果 </strong>存在 <strong>任意</strong> 下标 <code>j</code> 满足 <code>cost[j] == z</code>&nbsp; 、<code>original[j] == x</code> 以及 <code>changed[j] == y</code> 。你就可以选择字符串中的一个字符 <code>x</code> 并以 <code>z</code> 的成本将其更改为字符 <code>y</code> 。</p>

<p>返回将字符串 <code>source</code> 转换为字符串 <code>target</code> 所需的<strong> 最小 </strong>成本。如果不可能完成转换，则返回 <code>-1</code> 。</p>

<p><strong>注意</strong>，可能存在下标 <code>i</code> 、<code>j</code> 使得 <code>original[j] == original[i]</code> 且 <code>changed[j] == changed[i]</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
<strong>输出：</strong>28
<strong>解释：</strong>将字符串 "abcd" 转换为字符串 "acbe" ：
- 更改下标 1 处的值 'b' 为 'c' ，成本为 5 。
- 更改下标 2 处的值 'c' 为 'e' ，成本为 1 。
- 更改下标 2 处的值 'e' 为 'b' ，成本为 2 。
- 更改下标 3 处的值 'd' 为 'e' ，成本为 20 。
产生的总成本是 5 + 1 + 2 + 20 = 28 。
可以证明这是可能的最小成本。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
<strong>输出：</strong>12
<strong>解释：</strong>要将字符 'a' 更改为 'b'：
- 将字符 'a' 更改为 'c'，成本为 1 
- 将字符 'c' 更改为 'b'，成本为 2 
产生的总成本是 1 + 2 = 3。
将所有 'a' 更改为 'b'，产生的总成本是 3 * 4 = 12 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
<strong>输出：</strong>-1
<strong>解释：</strong>无法将 source 字符串转换为 target 字符串，因为下标 3 处的值无法从 'd' 更改为 'e' 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= source.length == target.length &lt;= 10<sup>5</sup></code></li>
	<li><code>source</code>、<code>target</code> 均由小写英文字母组成</li>
	<li><code>1 &lt;= cost.length== original.length == changed.length &lt;= 2000</code></li>
	<li><code>original[i]</code>、<code>changed[i]</code> 是小写英文字母</li>
	<li><code>1 &lt;= cost[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>original[i] != changed[i]</code></li>
</ul>


## 难度

Medium

## 标签

- 图
- 数组
- 字符串
- 最短路

## 提示

1. Construct a graph with each letter as a node, and construct an edge <code>(a, b)</code> with weight <code>c</code> if we can change from character <code>a</code> to letter <code>b</code> with cost <code>c</code>. (Keep the one with the smallest cost in case there are multiple edges between <code>a</code> and <code>b</code>).
2. Calculate the shortest path for each pair of characters <code>(source[i], target[i])</code>. The sum of cost over all <code>i</code> in the range <code>[0, source.length - 1]</code>. If there is no path between <code>source[i]</code> and <code>target[i]</code>, the answer is <code>-1</code>.
3. Any shortest path algorithms will work since we only have <code>26</code> nodes. Since we only have at most <code>26 * 26</code> pairs, we can save the result to avoid re-calculation.
4. We can also use Floyd Warshall's algorithm to precompute all the results.

## 示例

```
"abcd"
"acbe"
["a","b","c","c","e","d"]
["b","c","b","e","b","e"]
[2,5,5,1,2,20]
"aaaa"
"bbbb"
["a","c"]
["c","b"]
[1,2]
"abcd"
"abce"
["a"]
["e"]
[10000]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumCost(string source, string target, vector<char>& original, vector<char>& changed, vector<int>& cost) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumCost(String source, String target, char[] original, char[] changed, int[] cost) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
```

### C

```c
long long minimumCost(char* source, char* target, char* original, int originalSize, char* changed, int changedSize, int* cost, int costSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumCost(string source, string target, char[] original, char[] changed, int[] cost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} source
 * @param {string} target
 * @param {character[]} original
 * @param {character[]} changed
 * @param {number[]} cost
 * @return {number}
 */
var minimumCost = function(source, target, original, changed, cost) {
    
};
```

### TypeScript

```typescript
function minimumCost(source: string, target: string, original: string[], changed: string[], cost: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $source
     * @param String $target
     * @param String[] $original
     * @param String[] $changed
     * @param Integer[] $cost
     * @return Integer
     */
    function minimumCost($source, $target, $original, $changed, $cost) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCost(_ source: String, _ target: String, _ original: [Character], _ changed: [Character], _ cost: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(source: String, target: String, original: CharArray, changed: CharArray, cost: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCost(String source, String target, List<String> original, List<String> changed, List<int> cost) {
    
  }
}
```

### Go

```golang
func minimumCost(source string, target string, original []byte, changed []byte, cost []int) int64 {
    
}
```

### Ruby

```ruby
# @param {String} source
# @param {String} target
# @param {Character[]} original
# @param {Character[]} changed
# @param {Integer[]} cost
# @return {Integer}
def minimum_cost(source, target, original, changed, cost)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(source: String, target: String, original: Array[Char], changed: Array[Char], cost: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(source: String, target: String, original: Vec<char>, changed: Vec<char>, cost: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost source target original changed cost)
  (-> string? string? (listof char?) (listof char?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_cost(Source :: unicode:unicode_binary(), Target :: unicode:unicode_binary(), Original :: [char()], Changed :: [char()], Cost :: [integer()]) -> integer().
minimum_cost(Source, Target, Original, Changed, Cost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(source :: String.t, target :: String.t, original :: [char], changed :: [char], cost :: [integer]) :: integer
  def minimum_cost(source, target, original, changed, cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(source: String, target: String, original: Array<Rune>, changed: Array<Rune>, cost: Array<Int64>): Int64 {

    }
}
```

