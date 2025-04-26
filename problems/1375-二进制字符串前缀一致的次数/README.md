# 1375. 二进制字符串前缀一致的次数

## 题目描述

<p>给你一个长度为 <code>n</code> 、下标从 <strong>1</strong> 开始的二进制字符串，所有位最开始都是 <code>0</code> 。我们会按步翻转该二进制字符串的所有位（即，将 <code>0</code> 变为 <code>1</code>）。</p>

<p>给你一个下标从 <strong>1</strong> 开始的整数数组 <code>flips</code> ，其中 <code>flips[i]</code> 表示对应下标 <code>i</code> 的位将会在第 <code>i</code> 步翻转。</p>

<p>二进制字符串 <strong>前缀一致</strong> 需满足：在第 <code>i</code> 步之后，在 <strong>闭</strong> 区间&nbsp;<code>[1, i]</code> 内的所有位都是 1 ，而其他位都是 0 。</p>

<p>返回二进制字符串在翻转过程中 <strong>前缀一致</strong> 的次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>flips = [3,2,4,1,5]
<strong>输出：</strong>2
<strong>解释：</strong>二进制字符串最开始是 "00000" 。
执行第 1 步：字符串变为 "00100" ，不属于前缀一致的情况。
执行第 2 步：字符串变为 "01100" ，不属于前缀一致的情况。
执行第 3 步：字符串变为 "01110" ，不属于前缀一致的情况。
执行第 4 步：字符串变为 "11110" ，属于前缀一致的情况。
执行第 5 步：字符串变为 "11111" ，属于前缀一致的情况。
在翻转过程中，前缀一致的次数为 2 ，所以返回 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>flips = [4,1,2,3]
<strong>输出：</strong>1
<strong>解释：</strong>二进制字符串最开始是 "0000" 。
执行第 1 步：字符串变为 "0001" ，不属于前缀一致的情况。
执行第 2 步：字符串变为 "1001" ，不属于前缀一致的情况。
执行第 3 步：字符串变为 "1101" ，不属于前缀一致的情况。
执行第 4 步：字符串变为 "1111" ，属于前缀一致的情况。
在翻转过程中，前缀一致的次数为 1 ，所以返回 1 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == flips.length</code></li>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>flips</code> 是范围 <code>[1, n]</code> 中所有整数构成的一个排列</li>
</ul>


## 难度

Medium

## 标签

- 数组

## 提示

1. If in the step x all bulb shines then bulbs 1,2,3,..,x should shines too.

## 示例

```
[3,2,4,1,5]
[4,1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numTimesAllBlue(vector<int>& flips) {
        
    }
};
```

### Java

```java
class Solution {
    public int numTimesAllBlue(int[] flips) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        
```

### C

```c
int numTimesAllBlue(int* flips, int flipsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumTimesAllBlue(int[] flips) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} flips
 * @return {number}
 */
var numTimesAllBlue = function(flips) {
    
};
```

### TypeScript

```typescript
function numTimesAllBlue(flips: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $flips
     * @return Integer
     */
    function numTimesAllBlue($flips) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numTimesAllBlue(_ flips: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numTimesAllBlue(flips: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numTimesAllBlue(List<int> flips) {
    
  }
}
```

### Go

```golang
func numTimesAllBlue(flips []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} flips
# @return {Integer}
def num_times_all_blue(flips)
    
end
```

### Scala

```scala
object Solution {
    def numTimesAllBlue(flips: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_times_all_blue(flips: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-times-all-blue flips)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_times_all_blue(Flips :: [integer()]) -> integer().
num_times_all_blue(Flips) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_times_all_blue(flips :: [integer]) :: integer
  def num_times_all_blue(flips) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numTimesAllBlue(flips: Array<Int64>): Int64 {

    }
}
```

