# 1987. 不同的好子序列数目

## 题目描述

<p>给你一个二进制字符串&nbsp;<code>binary</code>&nbsp;。&nbsp;<code>binary</code>&nbsp;的一个 <strong>子序列</strong>&nbsp;如果是 <strong>非空</strong>&nbsp;的且没有 <b>前导</b>&nbsp;<strong>0</strong>&nbsp;（除非数字是 <code>"0"</code>&nbsp;本身），那么它就是一个 <strong>好</strong>&nbsp;的子序列。</p>

<p>请你找到&nbsp;<code>binary</code>&nbsp;<strong>不同好子序列</strong>&nbsp;的数目。</p>

<ul>
	<li>比方说，如果&nbsp;<code>binary = "001"</code>&nbsp;，那么所有 <strong>好</strong>&nbsp;子序列为&nbsp;<code>["0", "0", "1"]</code>&nbsp;，所以 <b>不同</b>&nbsp;的好子序列为&nbsp;<code>"0"</code> 和&nbsp;<code>"1"</code>&nbsp;。 注意，子序列&nbsp;<code>"00"</code>&nbsp;，<code>"01"</code>&nbsp;和&nbsp;<code>"001"</code>&nbsp;不是好的，因为它们有前导 0 。</li>
</ul>

<p>请你返回&nbsp;<code>binary</code>&nbsp;中&nbsp;<strong>不同好子序列</strong>&nbsp;的数目。由于答案可能很大，请将它对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong> 后返回。</p>

<p>一个 <strong>子序列</strong>&nbsp;指的是从原数组中删除若干个（可以一个也不删除）元素后，不改变剩余元素顺序得到的序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>binary = "001"
<b>输出：</b>2
<b>解释：</b>好的二进制子序列为 ["0", "0", "1"] 。
不同的好子序列为 "0" 和 "1" 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>binary = "11"
<b>输出：</b>2
<b>解释：</b>好的二进制子序列为 ["1", "1", "11"] 。
不同的好子序列为 "1" 和 "11" 。</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>binary = "101"
<b>输出：</b>5
<b>解释：</b>好的二进制子序列为 ["1", "0", "1", "10", "11", "101"] 。
不同的好子序列为 "0" ，"1" ，"10" ，"11" 和 "101" 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= binary.length &lt;= 10<sup>5</sup></code></li>
	<li><code>binary</code>&nbsp;只含有&nbsp;<code>'0'</code>&nbsp;和&nbsp;<code>'1'</code> 。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. The number of unique good subsequences is equal to the number of unique decimal values there are for all possible subsequences.
2. Find the answer at each index based on the previous indexes' answers.

## 示例

```
"001"
"11"
"101"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfUniqueGoodSubsequences(string binary) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfUniqueGoodSubsequences(String binary) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfUniqueGoodSubsequences(self, binary):
        """
        :type binary: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        
```

### C

```c
int numberOfUniqueGoodSubsequences(char* binary) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfUniqueGoodSubsequences(string binary) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} binary
 * @return {number}
 */
var numberOfUniqueGoodSubsequences = function(binary) {
    
};
```

### TypeScript

```typescript
function numberOfUniqueGoodSubsequences(binary: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $binary
     * @return Integer
     */
    function numberOfUniqueGoodSubsequences($binary) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfUniqueGoodSubsequences(_ binary: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfUniqueGoodSubsequences(binary: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfUniqueGoodSubsequences(String binary) {
    
  }
}
```

### Go

```golang
func numberOfUniqueGoodSubsequences(binary string) int {
    
}
```

### Ruby

```ruby
# @param {String} binary
# @return {Integer}
def number_of_unique_good_subsequences(binary)
    
end
```

### Scala

```scala
object Solution {
    def numberOfUniqueGoodSubsequences(binary: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_unique_good_subsequences(binary: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-unique-good-subsequences binary)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_unique_good_subsequences(Binary :: unicode:unicode_binary()) -> integer().
number_of_unique_good_subsequences(Binary) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_unique_good_subsequences(binary :: String.t) :: integer
  def number_of_unique_good_subsequences(binary) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfUniqueGoodSubsequences(binary: String): Int64 {

    }
}
```

