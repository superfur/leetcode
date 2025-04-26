# 433. 最小基因变化

## 题目描述

<p>基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 <code>'A'</code>、<code>'C'</code>、<code>'G'</code> 和 <code>'T'</code> 之一。</p>

<p>假设我们需要调查从基因序列&nbsp;<code>start</code> 变为 <code>end</code> 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。</p>

<ul>
	<li>例如，<code>"AACCGGTT" --&gt; "AACCGGTA"</code> 就是一次基因变化。</li>
</ul>

<p>另有一个基因库 <code>bank</code> 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。（变化后的基因必须位于基因库 <code>bank</code> 中）</p>

<p>给你两个基因序列 <code>start</code> 和 <code>end</code> ，以及一个基因库 <code>bank</code> ，请你找出并返回能够使&nbsp;<code>start</code> 变化为 <code>end</code> 所需的最少变化次数。如果无法完成此基因变化，返回 <code>-1</code> 。</p>

<p>注意：起始基因序列&nbsp;<code>start</code> 默认是有效的，但是它并不一定会出现在基因库中。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
<strong>输出：</strong>3
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>start.length == 8</code></li>
	<li><code>end.length == 8</code></li>
	<li><code>0 &lt;= bank.length &lt;= 10</code></li>
	<li><code>bank[i].length == 8</code></li>
	<li><code>start</code>、<code>end</code> 和 <code>bank[i]</code> 仅由字符 <code>['A', 'C', 'G', 'T']</code> 组成</li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 哈希表
- 字符串

## 示例

```
"AACCGGTT"
"AACCGGTA"
["AACCGGTA"]
"AACCGGTT"
"AAACGGTA"
["AACCGGTA","AACCGCTA","AAACGGTA"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        
    }
};
```

### Java

```java
class Solution {
    public int minMutation(String startGene, String endGene, String[] bank) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        
```

### C

```c
int minMutation(char* startGene, char* endGene, char** bank, int bankSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinMutation(string startGene, string endGene, string[] bank) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} startGene
 * @param {string} endGene
 * @param {string[]} bank
 * @return {number}
 */
var minMutation = function(startGene, endGene, bank) {
    
};
```

### TypeScript

```typescript
function minMutation(startGene: string, endGene: string, bank: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $startGene
     * @param String $endGene
     * @param String[] $bank
     * @return Integer
     */
    function minMutation($startGene, $endGene, $bank) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minMutation(_ startGene: String, _ endGene: String, _ bank: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minMutation(startGene: String, endGene: String, bank: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minMutation(String startGene, String endGene, List<String> bank) {
    
  }
}
```

### Go

```golang
func minMutation(startGene string, endGene string, bank []string) int {
    
}
```

### Ruby

```ruby
# @param {String} start_gene
# @param {String} end_gene
# @param {String[]} bank
# @return {Integer}
def min_mutation(start_gene, end_gene, bank)
    
end
```

### Scala

```scala
object Solution {
    def minMutation(startGene: String, endGene: String, bank: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_mutation(start_gene: String, end_gene: String, bank: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-mutation startGene endGene bank)
  (-> string? string? (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_mutation(StartGene :: unicode:unicode_binary(), EndGene :: unicode:unicode_binary(), Bank :: [unicode:unicode_binary()]) -> integer().
min_mutation(StartGene, EndGene, Bank) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_mutation(start_gene :: String.t, end_gene :: String.t, bank :: [String.t]) :: integer
  def min_mutation(start_gene, end_gene, bank) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minMutation(startGene: String, endGene: String, bank: Array<String>): Int64 {

    }
}
```

