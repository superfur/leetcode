# 1363. 形成三的最大倍数

## 题目描述

<p>给你一个整数数组&nbsp;<code>digits</code>，你可以通过按 <strong>任意顺序</strong> 连接其中某些数字来形成 <strong>3</strong> 的倍数，请你返回所能得到的最大的 3 的倍数。</p>

<p>由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。如果无法得到答案，请返回一个空字符串。返回的结果不应包含不必要的前导零。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>digits = [8,1,9]
<strong>输出：</strong>"981"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>digits = [8,6,7,1,0]
<strong>输出：</strong>"8760"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>digits = [1]
<strong>输出：</strong>""
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>digits = [0,0,0,0,0,0]
<strong>输出：</strong>"0"
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 10^4</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组
- 数学
- 动态规划
- 排序

## 提示

1. A number is a multiple of three if and only if its sum of digits is a multiple of three.
2. Use dynamic programming.
3. To find the maximum number, try to maximize the number of digits of the number.
4. Sort the digits in descending order to find the maximum number.

## 示例

```
[8,1,9]
[8,6,7,1,0]
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string largestMultipleOfThree(vector<int>& digits) {
        
    }
};
```

### Java

```java
class Solution {
    public String largestMultipleOfThree(int[] digits) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestMultipleOfThree(self, digits):
        """
        :type digits: List[int]
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        
```

### C

```c
char* largestMultipleOfThree(int* digits, int digitsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public string LargestMultipleOfThree(int[] digits) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} digits
 * @return {string}
 */
var largestMultipleOfThree = function(digits) {
    
};
```

### TypeScript

```typescript
function largestMultipleOfThree(digits: number[]): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $digits
     * @return String
     */
    function largestMultipleOfThree($digits) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestMultipleOfThree(_ digits: [Int]) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestMultipleOfThree(digits: IntArray): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String largestMultipleOfThree(List<int> digits) {
    
  }
}
```

### Go

```golang
func largestMultipleOfThree(digits []int) string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} digits
# @return {String}
def largest_multiple_of_three(digits)
    
end
```

### Scala

```scala
object Solution {
    def largestMultipleOfThree(digits: Array[Int]): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_multiple_of_three(digits: Vec<i32>) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (largest-multiple-of-three digits)
  (-> (listof exact-integer?) string?)
  )
```

### Erlang

```erlang
-spec largest_multiple_of_three(Digits :: [integer()]) -> unicode:unicode_binary().
largest_multiple_of_three(Digits) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_multiple_of_three(digits :: [integer]) :: String.t
  def largest_multiple_of_three(digits) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestMultipleOfThree(digits: Array<Int64>): String {

    }
}
```

