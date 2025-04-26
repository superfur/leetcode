# 2977. 转换字符串的最小成本 II

## 题目描述

<p>给你两个下标从 <strong>0</strong> 开始的字符串 <code>source</code> 和 <code>target</code> ，它们的长度均为 <code>n</code> 并且由 <strong>小写 </strong>英文字母组成。</p>

<p>另给你两个下标从 <strong>0</strong> 开始的字符串数组 <code>original</code> 和 <code>changed</code> ，以及一个整数数组 <code>cost</code> ，其中 <code>cost[i]</code> 代表将字符串 <code>original[i]</code> 更改为字符串 <code>changed[i]</code> 的成本。</p>

<p>你从字符串 <code>source</code> 开始。在一次操作中，<strong>如果 </strong>存在 <strong>任意</strong> 下标 <code>j</code> 满足 <code>cost[j] == z</code>&nbsp; 、<code>original[j] == x</code> 以及 <code>changed[j] == y</code> ，你就可以选择字符串中的 <strong>子串</strong> <code>x</code> 并以 <code>z</code> 的成本将其更改为 <code>y</code> 。 你可以执行 <strong>任意数量 </strong>的操作，但是任两次操作必须满足<strong> 以下两个 </strong>条件 <strong>之一</strong> ：</p>

<ul>
	<li>在两次操作中选择的子串分别是 <code>source[a..b]</code> 和 <code>source[c..d]</code> ，满足 <code>b &lt; c</code>&nbsp; <strong>或</strong> <code>d &lt; a</code> 。换句话说，两次操作中选择的下标<strong> 不相交 </strong>。</li>
	<li>在两次操作中选择的子串分别是 <code>source[a..b]</code> 和 <code>source[c..d]</code> ，满足 <code>a == c</code> <strong>且</strong> <code>b == d</code> 。换句话说，两次操作中选择的下标<strong> 相同 </strong>。</li>
</ul>

<p>返回将字符串 <code>source</code> 转换为字符串 <code>target</code> 所需的<strong> 最小 </strong>成本。如果不可能完成转换，则返回 <code>-1</code> 。</p>

<p><strong>注意</strong>，可能存在下标 <code>i</code> 、<code>j</code> 使得 <code>original[j] == original[i]</code> 且 <code>changed[j] == changed[i]</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
<strong>输出：</strong>28
<strong>解释：</strong>将 "abcd" 转换为 "acbe"，执行以下操作：
- 将子串 source[1..1] 从 "b" 改为 "c" ，成本为 5 。
- 将子串 source[2..2] 从 "c" 改为 "e" ，成本为 1 。
- 将子串 source[2..2] 从 "e" 改为 "b" ，成本为 2 。
- 将子串 source[3..3] 从 "d" 改为 "e" ，成本为 20 。
产生的总成本是 5 + 1 + 2 + 20 = 28 。 
可以证明这是可能的最小成本。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5]
<strong>输出：</strong>9
<strong>解释：</strong>将 "abcdefgh" 转换为 "acdeeghh"，执行以下操作：
- 将子串 source[1..3] 从 "bcd" 改为 "cde" ，成本为 1 。
- 将子串 source[5..7] 从 "fgh" 改为 "thh" ，成本为 3 。可以执行此操作，因为下标 [5,7] 与第一次操作选中的下标不相交。
- 将子串 source[5..7] 从 "thh" 改为 "ghh" ，成本为 5 。可以执行此操作，因为下标 [5,7] 与第一次操作选中的下标不相交，且与第二次操作选中的下标相同。
产生的总成本是 1 + 3 + 5 = 9 。
可以证明这是可能的最小成本。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>source = "abcdefgh", target = "addddddd", original = ["bcd","defgh"], changed = ["ddd","ddddd"], cost = [100,1578]
<strong>输出：</strong>-1
<strong>解释：</strong>无法将 "abcdefgh" 转换为 "addddddd" 。
如果选择子串 source[1..3] 执行第一次操作，以将 "abcdefgh" 改为 "adddefgh" ，你无法选择子串 source[3..7] 执行第二次操作，因为两次操作有一个共用下标 3 。
如果选择子串 source[3..7] 执行第一次操作，以将 "abcdefgh" 改为 "abcddddd" ，你无法选择子串 source[1..3] 执行第二次操作，因为两次操作有一个共用下标 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= source.length == target.length &lt;= 1000</code></li>
	<li><code>source</code>、<code>target</code> 均由小写英文字母组成</li>
	<li><code>1 &lt;= cost.length == original.length == changed.length &lt;= 100</code></li>
	<li><code>1 &lt;= original[i].length == changed[i].length &lt;= source.length</code></li>
	<li><code>original[i]</code>、<code>changed[i]</code> 均由小写英文字母组成</li>
	<li><code>original[i] != changed[i]</code></li>
	<li><code>1 &lt;= cost[i] &lt;= 10<sup>6</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 图
- 字典树
- 数组
- 字符串
- 动态规划
- 最短路

## 提示

1. Give each unique string in <code>original</code> and <code>changed</code> arrays a unique id. There are at most <code>2 * m</code> unique strings in total where <code>m</code> is the length of the arrays. We can put them into a hash map to assign ids.
2. We can pre-compute the smallest costs between all pairs of unique strings using Floyd Warshall algorithm in <code>O(m ^ 3)</code> time complexity.
3. Let <code>dp[i]</code> be the smallest cost to change the first <code>i</code> characters (prefix) of <code>source</code> into <code>target</code>, leaving the suffix untouched.
We have <code>dp[0] = 0</code>.
<code>dp[i] = min(
dp[i - 1] if (source[i - 1] == target[i - 1]),
dp[j-1] + cost[x][y] where x is the id of source[j..(i - 1)] and y is the id of target e[j..(i - 1)])
)</code>.
If neither of the two conditions is satisfied, <code>dp[i] = infinity</code>.
4. We can use Trie to check for the second condition in <code>O(1)</code>.
5. The answer is <code>dp[n]</code> where <code>n</code> is <code>source.length</code>.

## 示例

```
"abcd"
"acbe"
["a","b","c","c","e","d"]
["b","c","b","e","b","e"]
[2,5,5,1,2,20]
"abcdefgh"
"acdeeghh"
["bcd","fgh","thh"]
["cde","thh","ghh"]
[1,3,5]
"abcdefgh"
"addddddd"
["bcd","defgh"]
["ddd","ddddd"]
[100,1578]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long minimumCost(string source, string target, vector<string>& original, vector<string>& changed, vector<int>& cost) {
        
    }
};
```

### Java

```java
class Solution {
    public long minimumCost(String source, String target, String[] original, String[] changed, int[] cost) {
        
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
long long minimumCost(char* source, char* target, char** original, int originalSize, char** changed, int changedSize, int* cost, int costSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long MinimumCost(string source, string target, string[] original, string[] changed, int[] cost) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} source
 * @param {string} target
 * @param {string[]} original
 * @param {string[]} changed
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
    func minimumCost(_ source: String, _ target: String, _ original: [String], _ changed: [String], _ cost: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(source: String, target: String, original: Array<String>, changed: Array<String>, cost: IntArray): Long {
        
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
func minimumCost(source string, target string, original []string, changed []string, cost []int) int64 {
    
}
```

### Ruby

```ruby
# @param {String} source
# @param {String} target
# @param {String[]} original
# @param {String[]} changed
# @param {Integer[]} cost
# @return {Integer}
def minimum_cost(source, target, original, changed, cost)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(source: String, target: String, original: Array[String], changed: Array[String], cost: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(source: String, target: String, original: Vec<String>, changed: Vec<String>, cost: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost source target original changed cost)
  (-> string? string? (listof string?) (listof string?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_cost(Source :: unicode:unicode_binary(), Target :: unicode:unicode_binary(), Original :: [unicode:unicode_binary()], Changed :: [unicode:unicode_binary()], Cost :: [integer()]) -> integer().
minimum_cost(Source, Target, Original, Changed, Cost) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(source :: String.t, target :: String.t, original :: [String.t], changed :: [String.t], cost :: [integer]) :: integer
  def minimum_cost(source, target, original, changed, cost) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(source: String, target: String, original: Array<String>, changed: Array<String>, cost: Array<Int64>): Int64 {

    }
}
```

