# 3412. 计算字符串的镜像分数

## 题目描述

<p>给你一个字符串 <code>s</code>。</p>

<p>英文字母中每个字母的&nbsp;<strong>镜像&nbsp;</strong>定义为反转字母表之后对应位置上的字母。例如，<code>'a'</code> 的镜像是 <code>'z'</code>，<code>'y'</code> 的镜像是 <code>'b'</code>。</p>

<p>最初，字符串 <code>s</code> 中的所有字符都&nbsp;<strong>未标记&nbsp;</strong>。</p>

<p>字符串 <code>s</code>&nbsp;的初始分数为 0 ，你需要对其执行以下过程：</p>

<ul>
	<li>从左到右遍历字符串。</li>
	<li>对于每个下标&nbsp;<code>i&nbsp;</code>，找到距离最近的&nbsp;<strong>未标记</strong> 下标&nbsp;<code>j</code>，下标 <code>j</code> 需要满足&nbsp;<code>j &lt; i</code> 且 <code>s[j]</code> 是 <code>s[i]</code> 的镜像。然后&nbsp;<strong>标记</strong> 下标&nbsp;<code>i</code> 和 <code>j</code>，总分加上&nbsp;<code>i - j</code>&nbsp;的值。</li>
	<li>如果对于下标&nbsp;<code>i</code>，不存在满足条件的下标&nbsp;<code>j</code>，则跳过该下标，继续处理下一个下标，不需要进行标记。</li>
</ul>

<p>返回最终的总分。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "aczzx"</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>i = 0</code>。没有符合条件的下标&nbsp;<code>j</code>，跳过。</li>
	<li><code>i = 1</code>。没有符合条件的下标&nbsp;<code>j</code>，跳过。</li>
	<li><code>i = 2</code>。距离最近的符合条件的下标是 <code>j = 0</code>，因此标记下标&nbsp;0 和 2，然后将总分加上&nbsp;<code>2 - 0 = 2</code>&nbsp;。</li>
	<li><code>i = 3</code>。没有符合条件的下标&nbsp;<code>j</code>，跳过。</li>
	<li><code>i = 4</code>。距离最近的符合条件的下标是 <code>j = 1</code>，因此标记下标&nbsp;1 和 4，然后将总分加上&nbsp;<code>4 - 1 = 3</code>&nbsp;。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "abcdef"</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>对于每个下标&nbsp;<code>i</code>，都不存在满足条件的下标&nbsp;<code>j</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 哈希表
- 字符串
- 模拟

## 提示

1. Create a stack for every character.
2. For each index, check if the stack for mirror of the letter at that index is empty.

## 示例

```
"aczzx"
"abcdef"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long calculateScore(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public long calculateScore(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def calculateScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def calculateScore(self, s: str) -> int:
        
```

### C

```c
long long calculateScore(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public long CalculateScore(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var calculateScore = function(s) {
    
};
```

### TypeScript

```typescript
function calculateScore(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function calculateScore($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func calculateScore(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun calculateScore(s: String): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int calculateScore(String s) {
    
  }
}
```

### Go

```golang
func calculateScore(s string) int64 {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def calculate_score(s)
    
end
```

### Scala

```scala
object Solution {
    def calculateScore(s: String): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn calculate_score(s: String) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (calculate-score s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec calculate_score(S :: unicode:unicode_binary()) -> integer().
calculate_score(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec calculate_score(s :: String.t) :: integer
  def calculate_score(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func calculateScore(s: String): Int64 {

    }
}
```

