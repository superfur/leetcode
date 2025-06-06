# 842. 将数组拆分成斐波那契序列

## 题目描述

<p>给定一个数字字符串 <code>num</code>，比如 <code>"123456579"</code>，我们可以将它分成「斐波那契式」的序列 <code>[123, 456, 579]</code>。</p>

<p>形式上，<strong>斐波那契式&nbsp;</strong>序列是一个非负整数列表 <code>f</code>，且满足：</p>

<ul>
	<li><code>0 &lt;= f[i] &lt; 2<sup>31</sup></code>&nbsp;，（也就是说，每个整数都符合 <strong>32 位</strong>&nbsp;有符号整数类型）</li>
	<li><code>f.length &gt;= 3</code></li>
	<li>对于所有的<code>0 &lt;= i &lt; f.length - 2</code>，都有 <code>f[i] + f[i + 1] = f[i + 2]</code></li>
</ul>

<p>另外，请注意，将字符串拆分成小块时，每个块的数字一定不要以零开头，除非这个块是数字 <code>0</code> 本身。</p>

<p>返回从 <code>num</code> 拆分出来的任意一组斐波那契式的序列块，如果不能拆分则返回 <code>[]</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>num = "1101111"
<strong>输出：</strong>[11,0,11,11]
<strong>解释：</strong>输出 [110,1,111] 也可以。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入: </strong>num = "112358130"
<strong>输出: </strong>[]
<strong>解释: </strong>无法拆分。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>"0123"
<strong>输出：</strong>[]
<strong>解释：</strong>每个块的数字不能以零开头，因此 "01"，"2"，"3" 不是有效答案。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 200</code></li>
	<li><code>num</code>&nbsp;中只含有数字</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 回溯

## 示例

```
"1101111"
"112358130"
"0123"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> splitIntoFibonacci(string num) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> splitIntoFibonacci(String num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def splitIntoFibonacci(self, num):
        """
        :type num: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* splitIntoFibonacci(char* num, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> SplitIntoFibonacci(string num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @return {number[]}
 */
var splitIntoFibonacci = function(num) {
    
};
```

### TypeScript

```typescript
function splitIntoFibonacci(num: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @return Integer[]
     */
    function splitIntoFibonacci($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func splitIntoFibonacci(_ num: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun splitIntoFibonacci(num: String): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> splitIntoFibonacci(String num) {
    
  }
}
```

### Go

```golang
func splitIntoFibonacci(num string) []int {
    
}
```

### Ruby

```ruby
# @param {String} num
# @return {Integer[]}
def split_into_fibonacci(num)
    
end
```

### Scala

```scala
object Solution {
    def splitIntoFibonacci(num: String): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn split_into_fibonacci(num: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (split-into-fibonacci num)
  (-> string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec split_into_fibonacci(Num :: unicode:unicode_binary()) -> [integer()].
split_into_fibonacci(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec split_into_fibonacci(num :: String.t) :: [integer]
  def split_into_fibonacci(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func splitIntoFibonacci(num: String): ArrayList<Int64> {

    }
}
```

