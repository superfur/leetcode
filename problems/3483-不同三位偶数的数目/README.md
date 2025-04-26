# 3483. 不同三位偶数的数目

## 题目描述

<p>给你一个数字数组 <code>digits</code>，你需要从中选择三个数字组成一个三位偶数，你的任务是求出&nbsp;<strong>不同&nbsp;</strong>三位偶数的数量。</p>

<p><strong>注意</strong>：每个数字在三位偶数中都只能使用&nbsp;<strong>一次&nbsp;</strong>，并且&nbsp;<strong>不能&nbsp;</strong>有前导零。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">digits = [1,2,3,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">12</span></p>

<p><strong>解释：</strong> 可以形成的 12 个不同的三位偶数是 124，132，134，142，214，234，312，314，324，342，412 和 432。注意，不能形成 222，因为数字 2 只有一个。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">digits = [0,2,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong> 可以形成的三位偶数是 202 和 220。注意，数字 2 可以使用两次，因为数组中有两个 2 。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">digits = [6,6,6]</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong> 只能形成 666。</p>
</div>

<p><strong class="example">示例 4：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">digits = [1,3,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong> 无法形成三位偶数。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= digits.length &lt;= 10</code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
</ul>


## 难度

Easy

## 标签

- 递归
- 数组
- 哈希表
- 枚举

## 提示

1. Use brute force to try all possibilities

## 示例

```
[1,2,3,4]
[0,2,2]
[6,6,6]
[1,3,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        
    }
};
```

### Java

```java
class Solution {
    public int totalNumbers(int[] digits) {
        
    }
}
```

### Python

```python
class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        
```

### C

```c
int totalNumbers(int* digits, int digitsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int TotalNumbers(int[] digits) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} digits
 * @return {number}
 */
var totalNumbers = function(digits) {
    
};
```

### TypeScript

```typescript
function totalNumbers(digits: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $digits
     * @return Integer
     */
    function totalNumbers($digits) {
        
    }
}
```

### Swift

```swift
class Solution {
    func totalNumbers(_ digits: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun totalNumbers(digits: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int totalNumbers(List<int> digits) {
    
  }
}
```

### Go

```golang
func totalNumbers(digits []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} digits
# @return {Integer}
def total_numbers(digits)
    
end
```

### Scala

```scala
object Solution {
    def totalNumbers(digits: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn total_numbers(digits: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (total-numbers digits)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec total_numbers(Digits :: [integer()]) -> integer().
total_numbers(Digits) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec total_numbers(digits :: [integer]) :: integer
  def total_numbers(digits) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func totalNumbers(digits: Array<Int64>): Int64 {

    }
}
```

