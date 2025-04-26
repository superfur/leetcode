# 3213. 最小代价构造字符串

## 题目描述

<p>给你一个字符串 <code>target</code>、一个字符串数组 <code>words</code> 以及一个整数数组 <code>costs</code>，这两个数组长度相同。</p>

<p>设想一个空字符串 <code>s</code>。</p>

<p>你可以执行以下操作任意次数（包括&nbsp;<strong>零&nbsp;</strong>次）：</p>

<ul>
	<li>选择一个在范围&nbsp; <code>[0, words.length - 1]</code> 的索引 <code>i</code>。</li>
	<li>将 <code>words[i]</code> 追加到 <code>s</code>。</li>
	<li>该操作的成本是 <code>costs[i]</code>。</li>
</ul>

<p>返回使 <code>s</code> 等于 <code>target</code> 的 <strong>最小</strong> 成本。如果不可能，返回 <code>-1</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">7</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>选择索引 1 并以成本 1 将 <code>"abc"</code> 追加到 <code>s</code>，得到 <code>s = "abc"</code>。</li>
	<li>选择索引 2 并以成本 1 将 <code>"d"</code> 追加到 <code>s</code>，得到 <code>s = "abcd"</code>。</li>
	<li>选择索引 4 并以成本 5 将 <code>"ef"</code> 追加到 <code>s</code>，得到 <code>s = "abcdef"</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<p>无法使 <code>s</code> 等于 <code>target</code>，因此返回 -1。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words.length == costs.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= words[i].length &lt;= target.length</code></li>
	<li>所有 <code>words[i].length</code> 的总和小于或等于 <code>5 * 10<sup>4</sup></code></li>
	<li><code>target</code> 和 <code>words[i]</code> 仅由小写英文字母组成。</li>
	<li><code>1 &lt;= costs[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 字符串
- 动态规划
- 后缀数组

## 提示

1. Use Dynamic Programming along with Aho-Corasick or Hashing.

## 示例

```
"abcdef"
["abdef","abc","d","def","ef"]
[100,1,1,10,5]
"aaaa"
["z","zz","zzz"]
[1,10,100]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumCost(string target, vector<string>& words, vector<int>& costs) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumCost(String target, String[] words, int[] costs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumCost(self, target, words, costs):
        """
        :type target: str
        :type words: List[str]
        :type costs: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        
```

### C

```c
int minimumCost(char* target, char** words, int wordsSize, int* costs, int costsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumCost(string target, string[] words, int[] costs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} target
 * @param {string[]} words
 * @param {number[]} costs
 * @return {number}
 */
var minimumCost = function(target, words, costs) {
    
};
```

### TypeScript

```typescript
function minimumCost(target: string, words: string[], costs: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $target
     * @param String[] $words
     * @param Integer[] $costs
     * @return Integer
     */
    function minimumCost($target, $words, $costs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumCost(_ target: String, _ words: [String], _ costs: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumCost(target: String, words: Array<String>, costs: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumCost(String target, List<String> words, List<int> costs) {
    
  }
}
```

### Go

```golang
func minimumCost(target string, words []string, costs []int) int {
    
}
```

### Ruby

```ruby
# @param {String} target
# @param {String[]} words
# @param {Integer[]} costs
# @return {Integer}
def minimum_cost(target, words, costs)
    
end
```

### Scala

```scala
object Solution {
    def minimumCost(target: String, words: Array[String], costs: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_cost(target: String, words: Vec<String>, costs: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-cost target words costs)
  (-> string? (listof string?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_cost(Target :: unicode:unicode_binary(), Words :: [unicode:unicode_binary()], Costs :: [integer()]) -> integer().
minimum_cost(Target, Words, Costs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_cost(target :: String.t, words :: [String.t], costs :: [integer]) :: integer
  def minimum_cost(target, words, costs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumCost(target: String, words: Array<String>, costs: Array<Int64>): Int64 {

    }
}
```

