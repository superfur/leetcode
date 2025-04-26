# 1977. 划分数字的方案数

## 题目描述

<p>你写下了若干 <strong>正整数</strong>&nbsp;，并将它们连接成了一个字符串&nbsp;<code>num</code>&nbsp;。但是你忘记给这些数字之间加逗号了。你只记得这一列数字是 <strong>非递减</strong>&nbsp;的且&nbsp;<strong>没有</strong> 任何数字有前导 0 。</p>

<p>请你返回有多少种可能的 <strong>正整数数组</strong>&nbsp;可以得到字符串&nbsp;<code>num</code>&nbsp;。由于答案可能很大，将结果对 <code>10<sup>9</sup> + 7</code>&nbsp;<b>取余</b>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>num = "327"
<b>输出：</b>2
<b>解释：</b>以下为可能的方案：
3, 27
327
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>num = "094"
<b>输出：</b>0
<b>解释：</b>不能有数字有前导 0 ，且所有数字均为正数。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>num = "0"
<b>输出：</b>0
<strong>解释：</strong>不能有数字有前导 0 ，且所有数字均为正数。
</pre>

<p><strong>示例 4：</strong></p>

<pre><b>输入：</b>num = "9999999999999"
<b>输出：</b>101
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 3500</code></li>
	<li><code>num</code>&nbsp;只含有数字&nbsp;<code>'0'</code> 到&nbsp;<code>'9'</code>&nbsp;。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划
- 后缀数组

## 提示

1. If we know the current number has d digits, how many digits can the previous number have?
2. Is there a quick way of calculating the number of possibilities for the previous number if we know that it must have less than or equal to d digits? Try to do some pre-processing.

## 示例

```
"327"
"094"
"0"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfCombinations(string num) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfCombinations(String num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfCombinations(self, num):
        """
        :type num: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        
```

### C

```c
int numberOfCombinations(char* num) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfCombinations(string num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @return {number}
 */
var numberOfCombinations = function(num) {
    
};
```

### TypeScript

```typescript
function numberOfCombinations(num: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @return Integer
     */
    function numberOfCombinations($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfCombinations(_ num: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfCombinations(num: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfCombinations(String num) {
    
  }
}
```

### Go

```golang
func numberOfCombinations(num string) int {
    
}
```

### Ruby

```ruby
# @param {String} num
# @return {Integer}
def number_of_combinations(num)
    
end
```

### Scala

```scala
object Solution {
    def numberOfCombinations(num: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_combinations(num: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-combinations num)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_combinations(Num :: unicode:unicode_binary()) -> integer().
number_of_combinations(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_combinations(num :: String.t) :: integer
  def number_of_combinations(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfCombinations(num: String): Int64 {

    }
}
```

