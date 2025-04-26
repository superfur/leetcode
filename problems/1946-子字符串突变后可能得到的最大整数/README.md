# 1946. 子字符串突变后可能得到的最大整数

## 题目描述

<p>给你一个字符串 <code>num</code> ，该字符串表示一个大整数。另给你一个长度为 <code>10</code> 且 <strong>下标从 0&nbsp; 开始</strong> 的整数数组 <code>change</code> ，该数组将 <code>0-9</code> 中的每个数字映射到另一个数字。更规范的说法是，数字 <code>d</code> 映射为数字 <code>change[d]</code> 。</p>

<p>你可以选择 <strong>突变</strong>&nbsp; <code>num</code> 的任一子字符串。<strong>突变</strong> 子字符串意味着将每位数字 <code>num[i]</code> 替换为该数字在 <code>change</code> 中的映射（也就是说，将 <code>num[i]</code> 替换为 <code>change[num[i]]</code>）。</p>

<p>请你找出在对 <code>num</code> 的任一子字符串执行突变操作（也可以不执行）后，可能得到的 <strong>最大整数</strong> ，并用字符串表示返回。</p>

<p><strong>子字符串</strong> 是字符串中的一个连续序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>num = "<strong><em>1</em></strong>32", change = [9,8,5,0,3,6,4,2,6,8]
<strong>输出：</strong>"<strong><em>8</em></strong>32"
<strong>解释：</strong>替换子字符串 "1"：
- 1 映射为 change[1] = 8 。
因此 "<strong><em>1</em></strong>32" 变为 "<strong><em>8</em></strong>32" 。
"832" 是可以构造的最大整数，所以返回它的字符串表示。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>num = "<strong><em>021</em></strong>", change = [9,4,3,5,7,2,1,9,0,6]
<strong>输出：</strong>"<strong><em>934</em></strong>"
<strong>解释：</strong>替换子字符串 "021"：
- 0 映射为 change[0] = 9 。
- 2 映射为 change[2] = 3 。
- 1 映射为 change[1] = 4 。
因此，"<strong><em>021</em></strong>" 变为 "<strong><em>934</em></strong>" 。
"934" 是可以构造的最大整数，所以返回它的字符串表示。 
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>num = "5", change = [1,4,7,5,3,2,5,6,9,4]
<strong>输出：</strong>"5"
<strong>解释：</strong>"5" 已经是可以构造的最大整数，所以返回它的字符串表示。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= num.length &lt;= 10<sup>5</sup></code></li>
	<li><code>num</code> 仅由数字 <code>0-9</code> 组成</li>
	<li><code>change.length == 10</code></li>
	<li><code>0 &lt;= change[d] &lt;= 9</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 字符串

## 提示

1. Should you change a digit if the new digit is smaller than the original?
2. If changing the first digit and the last digit both make the number bigger, but you can only change one of them; which one should you change?
3. Changing numbers closer to the front is always better

## 示例

```
"132"
[9,8,5,0,3,6,4,2,6,8]
"021"
[9,4,3,5,7,2,1,9,0,6]
"5"
[1,4,7,5,3,2,5,6,9,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string maximumNumber(string num, vector<int>& change) {
        
    }
};
```

### Java

```java
class Solution {
    public String maximumNumber(String num, int[] change) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        
```

### C

```c
char* maximumNumber(char* num, int* change, int changeSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string MaximumNumber(string num, int[] change) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} num
 * @param {number[]} change
 * @return {string}
 */
var maximumNumber = function(num, change) {
    
};
```

### TypeScript

```typescript
function maximumNumber(num: string, change: number[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $num
     * @param Integer[] $change
     * @return String
     */
    function maximumNumber($num, $change) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumNumber(_ num: String, _ change: [Int]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumNumber(num: String, change: IntArray): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String maximumNumber(String num, List<int> change) {
    
  }
}
```

### Go

```golang
func maximumNumber(num string, change []int) string {
    
}
```

### Ruby

```ruby
# @param {String} num
# @param {Integer[]} change
# @return {String}
def maximum_number(num, change)
    
end
```

### Scala

```scala
object Solution {
    def maximumNumber(num: String, change: Array[Int]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_number(num: String, change: Vec<i32>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-number num change)
  (-> string? (listof exact-integer?) string?)
  )
```

### Erlang

```erlang
-spec maximum_number(Num :: unicode:unicode_binary(), Change :: [integer()]) -> unicode:unicode_binary().
maximum_number(Num, Change) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_number(num :: String.t, change :: [integer]) :: String.t
  def maximum_number(num, change) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumNumber(num: String, change: Array<Int64>): String {

    }
}
```

