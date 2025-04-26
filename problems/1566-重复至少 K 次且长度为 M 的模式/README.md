# 1566. 重复至少 K 次且长度为 M 的模式

## 题目描述

<p>给你一个正整数数组 <code>arr</code>，请你找出一个长度为 <code>m</code> 且在数组中至少重复 <code>k</code> 次的模式。</p>

<p><strong>模式</strong> 是由一个或多个值组成的子数组（连续的子序列），<strong>连续</strong> 重复多次但 <strong>不重叠</strong> 。 模式由其长度和重复次数定义。</p>

<p>如果数组中存在至少重复 <code>k</code> 次且长度为 <code>m</code> 的模式，则返回 <code>true</code> ，否则返回&nbsp; <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,4,4,4,4], m = 1, k = 3
<strong>输出：</strong>true
<strong>解释：</strong>模式 <strong>(4)</strong> 的长度为 1 ，且连续重复 4 次。注意，模式可以重复 k 次或更多次，但不能少于 k 次。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
<strong>输出：</strong>true
<strong>解释：</strong>模式 <strong>(1,2)</strong> 长度为 2 ，且连续重复 2 次。另一个符合题意的模式是 <strong>(2,1) </strong>，同样重复 2 次。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,1,2,1,3], m = 2, k = 3
<strong>输出：</strong>false
<strong>解释：</strong>模式 <strong>(1,2)</strong> 长度为 2 ，但是只连续重复 2 次。不存在长度为 2 且至少重复 3 次的模式。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>arr = [1,2,3,1,2], m = 2, k = 2
<strong>输出：</strong>false
<strong>解释：</strong>模式 <strong>(1,2)</strong> 出现 2 次但并不连续，所以不能算作连续重复 2 次。
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>arr = [2,2,2,2], m = 2, k = 3
<strong>输出：</strong>false
<strong>解释：</strong>长度为 2 的模式只有 <strong>(2,2)</strong> ，但是只连续重复 2 次。注意，不能计算重叠的重复次数。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 100</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 100</code></li>
	<li><code>1 &lt;= m&nbsp;&lt;= 100</code></li>
	<li><code>2 &lt;= k&nbsp;&lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 枚举

## 提示

1. Use a three-layer loop to check all possible patterns by iterating through all possible starting positions, all indexes less than m, and if the character at the index is repeated k times.

## 示例

```
[1,2,4,4,4,4]
1
3
[1,2,1,2,1,1,1,3]
2
2
[1,2,1,2,1,3]
2
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool containsPattern(vector<int>& arr, int m, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean containsPattern(int[] arr, int m, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def containsPattern(self, arr, m, k):
        """
        :type arr: List[int]
        :type m: int
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        
```

### C

```c
bool containsPattern(int* arr, int arrSize, int m, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ContainsPattern(int[] arr, int m, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} m
 * @param {number} k
 * @return {boolean}
 */
var containsPattern = function(arr, m, k) {
    
};
```

### TypeScript

```typescript
function containsPattern(arr: number[], m: number, k: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $m
     * @param Integer $k
     * @return Boolean
     */
    function containsPattern($arr, $m, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func containsPattern(_ arr: [Int], _ m: Int, _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun containsPattern(arr: IntArray, m: Int, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool containsPattern(List<int> arr, int m, int k) {
    
  }
}
```

### Go

```golang
func containsPattern(arr []int, m int, k int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} m
# @param {Integer} k
# @return {Boolean}
def contains_pattern(arr, m, k)
    
end
```

### Scala

```scala
object Solution {
    def containsPattern(arr: Array[Int], m: Int, k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn contains_pattern(arr: Vec<i32>, m: i32, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (contains-pattern arr m k)
  (-> (listof exact-integer?) exact-integer? exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec contains_pattern(Arr :: [integer()], M :: integer(), K :: integer()) -> boolean().
contains_pattern(Arr, M, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec contains_pattern(arr :: [integer], m :: integer, k :: integer) :: boolean
  def contains_pattern(arr, m, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func containsPattern(arr: Array<Int64>, m: Int64, k: Int64): Bool {

    }
}
```

