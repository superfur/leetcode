# 2094. 找出 3 位偶数

## 题目描述

<p>给你一个整数数组 <code>digits</code> ，其中每个元素是一个数字（<code>0 - 9</code>）。数组中可能存在重复元素。</p>

<p>你需要找出 <strong>所有</strong> 满足下述条件且 <strong>互不相同</strong> 的整数：</p>

<ul>
	<li>该整数由 <code>digits</code> 中的三个元素按 <strong>任意</strong> 顺序 <strong>依次连接</strong> 组成。</li>
	<li>该整数不含 <strong>前导零</strong></li>
	<li>该整数是一个 <strong>偶数</strong></li>
</ul>

<p>例如，给定的 <code>digits</code> 是 <code>[1, 2, 3]</code> ，整数 <code>132</code> 和 <code>312</code> 满足上面列出的全部条件。</p>

<p>将找出的所有互不相同的整数按 <strong>递增顺序</strong> 排列，并以数组形式返回<em>。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>digits = [2,1,3,0]
<strong>输出：</strong>[102,120,130,132,210,230,302,310,312,320]
<strong>解释：</strong>
所有满足题目条件的整数都在输出数组中列出。 
注意，答案数组中不含有 <strong>奇数</strong> 或带 <strong>前导零</strong> 的整数。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>digits = [2,2,8,8,2]
<strong>输出：</strong>[222,228,282,288,822,828,882]
<strong>解释：</strong>
同样的数字（0 - 9）在构造整数时可以重复多次，重复次数最多与其在 <code>digits</code> 中出现的次数一样。 
在这个例子中，数字 8 在构造 288、828 和 882 时都重复了两次。 
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>digits = [3,7,5]
<strong>输出：</strong>[]
<strong>解释：</strong>
使用给定的 digits 无法构造偶数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;=&nbsp;digits.length &lt;= 100</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 枚举
- 排序

## 提示

1. The range of possible answers includes all even numbers between 100 and 999 inclusive. Could you check each possible answer to see if it could be formed from the digits in the array?

## 示例

```
[2,1,3,0]
[2,2,8,8,2]
[3,7,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] findEvenNumbers(int[] digits) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findEvenNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findEvenNumbers(int* digits, int digitsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FindEvenNumbers(int[] digits) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var findEvenNumbers = function(digits) {
    
};
```

### TypeScript

```typescript
function findEvenNumbers(digits: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $digits
     * @return Integer[]
     */
    function findEvenNumbers($digits) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findEvenNumbers(_ digits: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findEvenNumbers(digits: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findEvenNumbers(List<int> digits) {
    
  }
}
```

### Go

```golang
func findEvenNumbers(digits []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} digits
# @return {Integer[]}
def find_even_numbers(digits)
    
end
```

### Scala

```scala
object Solution {
    def findEvenNumbers(digits: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_even_numbers(digits: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-even-numbers digits)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_even_numbers(Digits :: [integer()]) -> [integer()].
find_even_numbers(Digits) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_even_numbers(digits :: [integer]) :: [integer]
  def find_even_numbers(digits) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findEvenNumbers(digits: Array<Int64>): Array<Int64> {

    }
}
```

