# 面试题 05.04. 下一个数

## 题目描述

<p>下一个数。给定一个正整数，找出与其二进制表达式中1的个数相同且大小最接近的那两个数（一个略大，一个略小）。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：num = 2（或者0b10）
<strong> 输出</strong>：[4, 1] 或者（[0b100, 0b1]）
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：num = 1
<strong> 输出</strong>：[2, -1]
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li><code>num</code>&nbsp;的范围在[1, 2147483647]之间；</li>
	<li>如果找不到前一个或者后一个满足条件的正数，那么输出 -1。</li>
</ol>


## 难度

Medium

## 标签

- 位运算

## 提示

1. 下一步：从每个蛮力解法开始。
2. 下一个：想象一个二进制数，在整个数中分布一串1和0。假设你把一个1翻转成0，把一个0翻转成1。在什么情况下数会更大？在什么情况下数会更小？
3. 下一步：如果你将1翻转成0，0翻转成1，假设 0 -> 1位更大，那么它就会变大。你如何使用这个来创建下一个最大的数字（具有相同数量的1）？
4. 下一步：你能翻转0到1，创建下一个最大的数字吗？
5. 下一步：把0翻转为1将创建一个更大的数字。索引越靠右，数字越大。如果有一个1001这样的数字，那么我们就想翻转最右边的0（创建1011）。但是如果有一个1010这样的数字，我们就不应该翻转最右边的1。
6. 下一步：我们应该翻转最右边但非拖尾的0。数字1010会变成1110。完成后，我们需要把1翻转成0让数字尽可能小，但要大于原始数字（1010）。该怎么办？如何缩小数字？
7. 下一步：我们可以通过将所有的1移动到翻转位的右侧，并尽可能地向右移动来缩小数字（在这个过程中去掉一个1）。
8. 获取前一个：一旦你解决了“获取后一个”，请尝试翻转“获取前一个”的逻辑。

## 示例

```
2
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findClosedNumbers(int num) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findClosedNumbers(int num) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findClosedNumbers(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findClosedNumbers(int num, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindClosedNumbers(int num) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} num
 * @return {number[]}
 */
var findClosedNumbers = function(num) {
    
};
```

### TypeScript

```typescript
function findClosedNumbers(num: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $num
     * @return Integer[]
     */
    function findClosedNumbers($num) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findClosedNumbers(_ num: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findClosedNumbers(num: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findClosedNumbers(int num) {
    
  }
}
```

### Go

```golang
func findClosedNumbers(num int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} num
# @return {Integer[]}
def find_closed_numbers(num)
    
end
```

### Scala

```scala
object Solution {
    def findClosedNumbers(num: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_closed_numbers(num: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-closed-numbers num)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_closed_numbers(Num :: integer()) -> [integer()].
find_closed_numbers(Num) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_closed_numbers(num :: integer) :: [integer]
  def find_closed_numbers(num) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findClosedNumbers(num: Int64): Array<Int64> {

    }
}
```

