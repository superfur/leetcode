# 823. 带因子的二叉树

## 题目描述

<p>给出一个含有不重复整数元素的数组 <code>arr</code> ，每个整数 <code>arr[i]</code> 均大于 1。</p>

<p>用这些整数来构建二叉树，每个整数可以使用任意次数。其中：每个非叶结点的值应等于它的两个子结点的值的乘积。</p>

<p>满足条件的二叉树一共有多少个？答案可能很大，返回<strong> 对 </strong><code>10<sup>9</sup> + 7</code> <strong>取余</strong> 的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> <code>arr = [2, 4]</code>
<strong>输出:</strong> 3
<strong>解释:</strong> 可以得到这些二叉树: <code>[2], [4], [4, 2, 2]</code></pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> <code>arr = [2, 4, 5, 10]</code>
<strong>输出:</strong> <code>7</code>
<strong>解释:</strong> 可以得到这些二叉树: <code>[2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2]</code>.</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 1000</code></li>
	<li><code>2 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>arr</code> 中的所有值 <strong>互不相同</strong></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 动态规划
- 排序

## 示例

```
[2,4]
[2,4,5,10]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int numFactoredBinaryTrees(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numFactoredBinaryTrees(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        
```

### C

```c
int numFactoredBinaryTrees(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumFactoredBinaryTrees(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var numFactoredBinaryTrees = function(arr) {
    
};
```

### TypeScript

```typescript
function numFactoredBinaryTrees(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function numFactoredBinaryTrees($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numFactoredBinaryTrees(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numFactoredBinaryTrees(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numFactoredBinaryTrees(List<int> arr) {
    
  }
}
```

### Go

```golang
func numFactoredBinaryTrees(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def num_factored_binary_trees(arr)
    
end
```

### Scala

```scala
object Solution {
    def numFactoredBinaryTrees(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_factored_binary_trees(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-factored-binary-trees arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_factored_binary_trees(Arr :: [integer()]) -> integer().
num_factored_binary_trees(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_factored_binary_trees(arr :: [integer]) :: integer
  def num_factored_binary_trees(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numFactoredBinaryTrees(arr: Array<Int64>): Int64 {

    }
}
```

