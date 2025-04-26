# 1521. 找到最接近目标值的函数值

## 题目描述

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/change.png" style="height: 312px; width: 635px;"></p>

<p>Winston 构造了一个如上所示的函数&nbsp;<code>func</code>&nbsp;。他有一个整数数组&nbsp;<code>arr</code>&nbsp;和一个整数&nbsp;<code>target</code>&nbsp;，他想找到让&nbsp;<code>|func(arr, l, r) - target|</code>&nbsp;最小的 <code>l</code>&nbsp;和 <code>r</code>&nbsp;。</p>

<p>请你返回&nbsp;<code>|func(arr, l, r) - target|</code>&nbsp;的最小值。</p>

<p>请注意，&nbsp;<code>func</code> 的输入参数&nbsp;<code>l</code> 和&nbsp;<code>r</code>&nbsp;需要满足&nbsp;<code>0 &lt;= l, r &lt; arr.length</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [9,12,3,7,15], target = 5
<strong>输出：</strong>2
<strong>解释：</strong>所有可能的 [l,r] 数对包括 [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]]， Winston 得到的相应结果为 [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0] 。最接近 5 的值是 7 和 3，所以最小差值为 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [1000000,1000000,1000000], target = 1
<strong>输出：</strong>999999
<strong>解释：</strong>Winston 输入函数的所有可能 [l,r] 数对得到的函数值都为 1000000 ，所以最小差值为 999999 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,4,8,16], target = 0
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10^6</code></li>
	<li><code>0 &lt;= target &lt;= 10^7</code></li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 线段树
- 数组
- 二分查找

## 提示

1. If the and value of sub-array arr[i...j] is ≥ the and value of the sub-array arr[i...j+1].
2. For each index i using binary search or ternary search find the index j where |target - AND(arr[i...j])| is minimum, minimize this value with the global answer.

## 示例

```
[9,12,3,7,15]
5
[1000000,1000000,1000000]
1
[1,2,4,8,16]
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int closestToTarget(vector<int>& arr, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int closestToTarget(int[] arr, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def closestToTarget(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        
```

### C

```c
int closestToTarget(int* arr, int arrSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int ClosestToTarget(int[] arr, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} target
 * @return {number}
 */
var closestToTarget = function(arr, target) {
    
};
```

### TypeScript

```typescript
function closestToTarget(arr: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $target
     * @return Integer
     */
    function closestToTarget($arr, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func closestToTarget(_ arr: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun closestToTarget(arr: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int closestToTarget(List<int> arr, int target) {
    
  }
}
```

### Go

```golang
func closestToTarget(arr []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def closest_to_target(arr, target)
    
end
```

### Scala

```scala
object Solution {
    def closestToTarget(arr: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn closest_to_target(arr: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (closest-to-target arr target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec closest_to_target(Arr :: [integer()], Target :: integer()) -> integer().
closest_to_target(Arr, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec closest_to_target(arr :: [integer], target :: integer) :: integer
  def closest_to_target(arr, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func closestToTarget(arr: Array<Int64>, target: Int64): Int64 {

    }
}
```

