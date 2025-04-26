# 1502. 判断能否形成等差数列

## 题目描述

<p>给你一个数字数组 <code>arr</code> 。</p>

<p>如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 <strong>等差数列</strong> 。</p>

<p>如果可以重新排列数组形成等差数列，请返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [3,5,1]
<strong>输出：</strong>true
<strong>解释：</strong>对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,4]
<strong>输出：</strong>false
<strong>解释：</strong>无法通过重新排序得到等差数列。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>-10^6 &lt;= arr[i] &lt;= 10^6</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 排序

## 提示

1. Consider that any valid arithmetic progression will be in sorted order.
2. Sort the array, then check if the differences of all consecutive elements are equal.

## 示例

```
[3,5,1]
[1,2,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canMakeArithmeticProgression(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
```

### C

```c
bool canMakeArithmeticProgression(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanMakeArithmeticProgression(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canMakeArithmeticProgression = function(arr) {
    
};
```

### TypeScript

```typescript
function canMakeArithmeticProgression(arr: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function canMakeArithmeticProgression($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canMakeArithmeticProgression(_ arr: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canMakeArithmeticProgression(arr: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canMakeArithmeticProgression(List<int> arr) {
    
  }
}
```

### Go

```golang
func canMakeArithmeticProgression(arr []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Boolean}
def can_make_arithmetic_progression(arr)
    
end
```

### Scala

```scala
object Solution {
    def canMakeArithmeticProgression(arr: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_make_arithmetic_progression(arr: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-make-arithmetic-progression arr)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec can_make_arithmetic_progression(Arr :: [integer()]) -> boolean().
can_make_arithmetic_progression(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_make_arithmetic_progression(arr :: [integer]) :: boolean
  def can_make_arithmetic_progression(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canMakeArithmeticProgression(arr: Array<Int64>): Bool {

    }
}
```

