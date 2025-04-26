# 1982. 从子集的和还原数组

## 题目描述

<p>存在一个未知数组需要你进行还原，给你一个整数 <code>n</code> 表示该数组的长度。另给你一个数组 <code>sums</code> ，由未知数组中全部 <code>2<sup>n</sup></code> 个 <strong>子集的和</strong> 组成（子集中的元素没有特定的顺序）。</p>

<p>返回一个长度为 <code>n</code> 的数组<em> </em><code>ans</code><em> </em>表示还原得到的未知数组。如果存在 <strong>多种</strong> 答案，只需返回其中 <strong>任意一个</strong> 。</p>

<p>如果可以由数组 <code>arr</code> 删除部分元素（也可能不删除或全删除）得到数组 <code>sub</code> ，那么数组 <code>sub</code> 就是数组 <code>arr</code> 的一个<strong> 子集</strong> 。<code>sub</code> 的元素之和就是 <code>arr</code> 的一个 <strong>子集的和</strong> 。一个空数组的元素之和为 <code>0</code> 。</p>

<p><strong>注意：</strong>生成的测试用例将保证至少存在一个正确答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, sums = [-3,-2,-1,0,0,1,2,3]
<strong>输出：</strong>[1,2,-3]
<strong>解释：</strong>[1,2,-3] 能够满足给出的子集的和：
- []：和是 0
- [1]：和是 1
- [2]：和是 2
- [1,2]：和是 3
- [-3]：和是 -3
- [1,-3]：和是 -2
- [2,-3]：和是 -1
- [1,2,-3]：和是 0
注意，[1,2,-3] 的任何排列和 [-1,-2,3] 的任何排列都会被视作正确答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, sums = [0,0,0,0]
<strong>输出：</strong>[0,0]
<strong>解释：</strong>唯一的正确答案是 [0,0] 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
<strong>输出：</strong>[0,-1,4,5]
<strong>解释：</strong>[0,-1,4,5] 能够满足给出的子集的和。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 15</code></li>
	<li><code>sums.length == 2<sup>n</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= sums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 分治

## 提示

1. What information do the two largest elements tell us?
2. Can we use recursion to check all possible states?

## 示例

```
3
[-3,-2,-1,0,0,1,2,3]
2
[0,0,0,0]
4
[0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> recoverArray(int n, vector<int>& sums) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] recoverArray(int n, int[] sums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def recoverArray(self, n, sums):
        """
        :type n: int
        :type sums: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* recoverArray(int n, int* sums, int sumsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] RecoverArray(int n, int[] sums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} sums
 * @return {number[]}
 */
var recoverArray = function(n, sums) {
    
};
```

### TypeScript

```typescript
function recoverArray(n: number, sums: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $sums
     * @return Integer[]
     */
    function recoverArray($n, $sums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func recoverArray(_ n: Int, _ sums: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun recoverArray(n: Int, sums: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> recoverArray(int n, List<int> sums) {
    
  }
}
```

### Go

```golang
func recoverArray(n int, sums []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} sums
# @return {Integer[]}
def recover_array(n, sums)
    
end
```

### Scala

```scala
object Solution {
    def recoverArray(n: Int, sums: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn recover_array(n: i32, sums: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (recover-array n sums)
  (-> exact-integer? (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec recover_array(N :: integer(), Sums :: [integer()]) -> [integer()].
recover_array(N, Sums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec recover_array(n :: integer, sums :: [integer]) :: [integer]
  def recover_array(n, sums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func recoverArray(n: Int64, sums: Array<Int64>): Array<Int64> {

    }
}
```

