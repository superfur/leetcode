# 2306. 公司命名

## 题目描述

<p>给你一个字符串数组 <code>ideas</code> 表示在公司命名过程中使用的名字列表。公司命名流程如下：</p>

<ol>
	<li>从 <code>ideas</code> 中选择 2 个 <strong>不同</strong> 名字，称为 <code>idea<sub>A</sub></code> 和 <code>idea<sub>B</sub></code> 。</li>
	<li>交换 <code>idea<sub>A</sub></code> 和 <code>idea<sub>B</sub></code> 的首字母。</li>
	<li>如果得到的两个新名字 <strong>都</strong> 不在 <code>ideas</code> 中，那么 <code>idea<sub>A</sub> idea<sub>B</sub></code>（<strong>串联</strong> <code>idea<sub>A</sub></code> 和 <code>idea<sub>B</sub></code> ，中间用一个空格分隔）是一个有效的公司名字。</li>
	<li>否则，不是一个有效的名字。</li>
</ol>

<p>返回 <strong>不同</strong> 且有效的公司名字的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>ideas = ["coffee","donuts","time","toffee"]
<strong>输出：</strong>6
<strong>解释：</strong>下面列出一些有效的选择方案：
- ("coffee", "donuts")：对应的公司名字是 "doffee conuts" 。
- ("donuts", "coffee")：对应的公司名字是 "conuts doffee" 。
- ("donuts", "time")：对应的公司名字是 "tonuts dime" 。
- ("donuts", "toffee")：对应的公司名字是 "tonuts doffee" 。
- ("time", "donuts")：对应的公司名字是 "dime tonuts" 。
- ("toffee", "donuts")：对应的公司名字是 "doffee tonuts" 。
因此，总共有 6 个不同的公司名字。

下面列出一些无效的选择方案：
- ("coffee", "time")：在原数组中存在交换后形成的名字 "toffee" 。
- ("time", "toffee")：在原数组中存在交换后形成的两个名字。
- ("coffee", "toffee")：在原数组中存在交换后形成的两个名字。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>ideas = ["lack","back"]
<strong>输出：</strong>0
<strong>解释：</strong>不存在有效的选择方案。因此，返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= ideas.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= ideas[i].length &lt;= 10</code></li>
	<li><code>ideas[i]</code> 由小写英文字母组成</li>
	<li><code>ideas</code> 中的所有字符串 <strong>互不相同</strong></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 数组
- 哈希表
- 字符串
- 枚举

## 提示

1. How can we divide the ideas into groups to make it easier to find valid pairs?
2. Group ideas that share the same suffix (all characters except the first) together and notice that a pair of ideas from the same group is invalid. What about pairs of ideas from different groups?
3. The first letter of the idea in the first group must not be the first letter of an idea in the second group and vice versa.
4. We can efficiently count the valid pairings for an idea if we already know how many ideas starting with a letter x are within a group that does not contain any ideas with starting letter y for all letters x and y.

## 示例

```
["coffee","donuts","time","toffee"]
["lack","back"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long distinctNames(vector<string>& ideas) {
        
    }
};
```

### Java

```java
class Solution {
    public long distinctNames(String[] ideas) {
        
    }
}
```

### Python

```python
class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        
```

### C

```c
long long distinctNames(char** ideas, int ideasSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long DistinctNames(string[] ideas) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} ideas
 * @return {number}
 */
var distinctNames = function(ideas) {
    
};
```

### TypeScript

```typescript
function distinctNames(ideas: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $ideas
     * @return Integer
     */
    function distinctNames($ideas) {
        
    }
}
```

### Swift

```swift
class Solution {
    func distinctNames(_ ideas: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun distinctNames(ideas: Array<String>): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int distinctNames(List<String> ideas) {
    
  }
}
```

### Go

```golang
func distinctNames(ideas []string) int64 {
    
}
```

### Ruby

```ruby
# @param {String[]} ideas
# @return {Integer}
def distinct_names(ideas)
    
end
```

### Scala

```scala
object Solution {
    def distinctNames(ideas: Array[String]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn distinct_names(ideas: Vec<String>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (distinct-names ideas)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec distinct_names(Ideas :: [unicode:unicode_binary()]) -> integer().
distinct_names(Ideas) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec distinct_names(ideas :: [String.t]) :: integer
  def distinct_names(ideas) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func distinctNames(ideas: Array<String>): Int64 {

    }
}
```

