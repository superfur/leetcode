# 1131. 绝对值表达式的最大值

## 题目描述

<p>给你两个长度相等的整数数组，返回下面表达式的最大值：</p>

<p><code>|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|</code></p>

<p>其中下标 <code>i</code>，<code>j</code> 满足&nbsp;<code>0 &lt;= i, j &lt; arr1.length</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
<strong>输出：</strong>13
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
<strong>输出：</strong>20</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= arr1.length == arr2.length &lt;= 40000</code></li>
	<li><code>-10^6 &lt;= arr1[i], arr2[i] &lt;= 10^6</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学

## 提示

1. Use the idea that abs(A) + abs(B) = max(A+B, A-B, -A+B, -A-B).

## 示例

```
[1,2,3,4]
[-1,4,5,6]
[1,-2,-5,0,10]
[0,-2,-1,-7,-4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxAbsValExpr(vector<int>& arr1, vector<int>& arr2) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxAbsValExpr(int[] arr1, int[] arr2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        
```

### C

```c
int maxAbsValExpr(int* arr1, int arr1Size, int* arr2, int arr2Size) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxAbsValExpr(int[] arr1, int[] arr2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var maxAbsValExpr = function(arr1, arr2) {
    
};
```

### TypeScript

```typescript
function maxAbsValExpr(arr1: number[], arr2: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr1
     * @param Integer[] $arr2
     * @return Integer
     */
    function maxAbsValExpr($arr1, $arr2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxAbsValExpr(_ arr1: [Int], _ arr2: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxAbsValExpr(arr1: IntArray, arr2: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxAbsValExpr(List<int> arr1, List<int> arr2) {
    
  }
}
```

### Go

```golang
func maxAbsValExpr(arr1 []int, arr2 []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr1
# @param {Integer[]} arr2
# @return {Integer}
def max_abs_val_expr(arr1, arr2)
    
end
```

### Scala

```scala
object Solution {
    def maxAbsValExpr(arr1: Array[Int], arr2: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_abs_val_expr(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-abs-val-expr arr1 arr2)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_abs_val_expr(Arr1 :: [integer()], Arr2 :: [integer()]) -> integer().
max_abs_val_expr(Arr1, Arr2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_abs_val_expr(arr1 :: [integer], arr2 :: [integer]) :: integer
  def max_abs_val_expr(arr1, arr2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxAbsValExpr(arr1: Array<Int64>, arr2: Array<Int64>): Int64 {

    }
}
```

