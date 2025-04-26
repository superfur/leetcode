# 1534. 统计好三元组

## 题目描述

<p>给你一个整数数组 <code>arr</code> ，以及 <code>a</code>、<code>b</code> 、<code>c</code> 三个整数。请你统计其中好三元组的数量。</p>

<p>如果三元组 <code>(arr[i], arr[j], arr[k])</code> 满足下列全部条件，则认为它是一个 <strong>好三元组</strong> 。</p>

<ul>
	<li><code>0 &lt;= i &lt; j &lt; k &lt;&nbsp;arr.length</code></li>
	<li><code>|arr[i] - arr[j]| &lt;= a</code></li>
	<li><code>|arr[j] - arr[k]| &lt;= b</code></li>
	<li><code>|arr[i] - arr[k]| &lt;= c</code></li>
</ul>

<p>其中 <code>|x|</code> 表示 <code>x</code> 的绝对值。</p>

<p>返回 <strong>好三元组的数量</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
<strong>输出：</strong>4
<strong>解释：</strong>一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [1,1,2,2,3], a = 0, b = 0, c = 1
<strong>输出：</strong>0
<strong>解释：</strong>不存在满足所有条件的三元组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= arr.length &lt;= 100</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= a, b, c &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 枚举

## 提示

1. Notice that the constraints are small enough for a brute force solution to pass.
2. Loop through all triplets, and count the ones that are good.

## 示例

```
[3,0,1,1,9,7]
7
2
3
[1,1,2,2,3]
0
0
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        
    }
};
```

### Java

```java
class Solution {
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        
```

### C

```c
int countGoodTriplets(int* arr, int arrSize, int a, int b, int c) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountGoodTriplets(int[] arr, int a, int b, int c) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} a
 * @param {number} b
 * @param {number} c
 * @return {number}
 */
var countGoodTriplets = function(arr, a, b, c) {
    
};
```

### TypeScript

```typescript
function countGoodTriplets(arr: number[], a: number, b: number, c: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function countGoodTriplets($arr, $a, $b, $c) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countGoodTriplets(_ arr: [Int], _ a: Int, _ b: Int, _ c: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countGoodTriplets(arr: IntArray, a: Int, b: Int, c: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countGoodTriplets(List<int> arr, int a, int b, int c) {
    
  }
}
```

### Go

```golang
func countGoodTriplets(arr []int, a int, b int, c int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {Integer}
def count_good_triplets(arr, a, b, c)
    
end
```

### Scala

```scala
object Solution {
    def countGoodTriplets(arr: Array[Int], a: Int, b: Int, c: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_good_triplets(arr: Vec<i32>, a: i32, b: i32, c: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-good-triplets arr a b c)
  (-> (listof exact-integer?) exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_good_triplets(Arr :: [integer()], A :: integer(), B :: integer(), C :: integer()) -> integer().
count_good_triplets(Arr, A, B, C) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_good_triplets(arr :: [integer], a :: integer, b :: integer, c :: integer) :: integer
  def count_good_triplets(arr, a, b, c) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countGoodTriplets(arr: Array<Int64>, a: Int64, b: Int64, c: Int64): Int64 {

    }
}
```

