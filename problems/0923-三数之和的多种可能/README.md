# 923. 三数之和的多种可能

## 题目描述

<p>给定一个整数数组<meta charset="UTF-8" />&nbsp;<code>arr</code>&nbsp;，以及一个整数&nbsp;<code>target</code>&nbsp;作为目标值，返回满足 <code>i &lt; j &lt; k</code> 且<meta charset="UTF-8" />&nbsp;<code>arr[i] + arr[j] + arr[k] == target</code>&nbsp;的元组&nbsp;<code>i, j, k</code>&nbsp;的数量。</p>

<p>由于结果会非常大，请返回 <code>10<sup>9</sup>&nbsp;+ 7</code>&nbsp;的模。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,1,2,2,3,3,4,4,5,5], target = 8
<strong>输出：</strong>20
<strong>解释：</strong>
按值枚举(arr[i], arr[j], arr[k])：
(1, 2, 5) 出现 8 次；
(1, 3, 4) 出现 8 次；
(2, 2, 4) 出现 2 次；
(2, 3, 3) 出现 2 次。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,1,2,2,2,2], target = 5
<strong>输出：</strong>12
<strong>解释：</strong>
arr[i] = 1, arr[j] = arr[k] = 2 出现 12 次：
我们从 [1,1] 中选择一个 1，有 2 种情况，
从 [2,2,2,2] 中选出两个 2，有 6 种情况。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= arr.length &lt;= 3000</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 100</code></li>
	<li><code>0 &lt;= target &lt;= 300</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 双指针
- 计数
- 排序

## 示例

```
[1,1,2,2,3,3,4,4,5,5]
8
[1,1,2,2,2,2]
5
[2,1,3]
6
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int threeSumMulti(vector<int>& arr, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int threeSumMulti(int[] arr, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
```

### C

```c
int threeSumMulti(int* arr, int arrSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int ThreeSumMulti(int[] arr, int target) {
        
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
var threeSumMulti = function(arr, target) {
    
};
```

### TypeScript

```typescript
function threeSumMulti(arr: number[], target: number): number {
    
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
    function threeSumMulti($arr, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func threeSumMulti(_ arr: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun threeSumMulti(arr: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int threeSumMulti(List<int> arr, int target) {
    
  }
}
```

### Go

```golang
func threeSumMulti(arr []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} target
# @return {Integer}
def three_sum_multi(arr, target)
    
end
```

### Scala

```scala
object Solution {
    def threeSumMulti(arr: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn three_sum_multi(arr: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (three-sum-multi arr target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec three_sum_multi(Arr :: [integer()], Target :: integer()) -> integer().
three_sum_multi(Arr, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec three_sum_multi(arr :: [integer], target :: integer) :: integer
  def three_sum_multi(arr, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func threeSumMulti(arr: Array<Int64>, target: Int64): Int64 {

    }
}
```

