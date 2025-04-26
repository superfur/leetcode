# 763. 划分字母区间

## 题目描述

<p>给你一个字符串 <code>s</code> 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。例如，字符串&nbsp;<code>"ababcc"</code> 能够被分为 <code>["abab", "cc"]</code>，但类似&nbsp;<code>["aba", "bcc"]</code> 或&nbsp;<code>["ab", "ab", "cc"]</code> 的划分是非法的。</p>

<p>注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 <code>s</code> 。</p>

<p>返回一个表示每个字符串片段的长度的列表。</p>

<p>&nbsp;</p>
<strong class="example">示例 1：</strong>

<pre>
<strong>输入：</strong>s = "ababcbacadefegdehijhklij"
<strong>输出：</strong>[9,7,8]
<strong>解释：</strong>
划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。 </pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "eccbbbbdec"
<strong>输出：</strong>[10]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 500</code></li>
	<li><code>s</code> 仅由小写英文字母组成</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 哈希表
- 双指针
- 字符串

## 提示

1. Try to greedily choose the smallest partition that includes the first letter.  If you have something like "abaccbdeffed", then you might need to add b.  You can use an map like "last['b'] = 5" to help you expand the width of your partition.

## 示例

```
"ababcbacadefegdehijhklij"
"eccbbbbdec"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> partitionLabels(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> partitionLabels(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* partitionLabels(char* s, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> PartitionLabels(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number[]}
 */
var partitionLabels = function(s) {
    
};
```

### TypeScript

```typescript
function partitionLabels(s: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer[]
     */
    function partitionLabels($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func partitionLabels(_ s: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun partitionLabels(s: String): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> partitionLabels(String s) {
    
  }
}
```

### Go

```golang
func partitionLabels(s string) []int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer[]}
def partition_labels(s)
    
end
```

### Scala

```scala
object Solution {
    def partitionLabels(s: String): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn partition_labels(s: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (partition-labels s)
  (-> string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec partition_labels(S :: unicode:unicode_binary()) -> [integer()].
partition_labels(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec partition_labels(s :: String.t) :: [integer]
  def partition_labels(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func partitionLabels(s: String): ArrayList<Int64> {

    }
}
```

