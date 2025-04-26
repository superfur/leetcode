# 1130. 叶值的最小代价生成树

## 题目描述

<p>给你一个正整数数组&nbsp;<code>arr</code>，考虑所有满足以下条件的二叉树：</p>

<ul>
	<li>每个节点都有 <code>0</code> 个或是 <code>2</code> 个子节点。</li>
	<li>数组&nbsp;<code>arr</code>&nbsp;中的值与树的中序遍历中每个叶节点的值一一对应。</li>
	<li>每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。</li>
</ul>

<p>在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个&nbsp;32 位整数。</p>

<p>如果一个节点有 0 个子节点，那么该节点为叶节点。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/10/tree1.jpg" style="width: 500px; height: 169px;" />
<pre>
<strong>输入：</strong>arr = [6,2,4]
<strong>输出：</strong>32
<strong>解释：</strong>有两种可能的树，第一种的非叶节点的总和为 36 ，第二种非叶节点的总和为 32 。 
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/10/tree2.jpg" style="width: 224px; height: 145px;" />
<pre>
<strong>输入：</strong>arr = [4,11]
<strong>输出：</strong>44
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= arr.length &lt;= 40</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 15</code></li>
	<li>答案保证是一个 32 位带符号整数，即小于&nbsp;<code>2<sup>31</sup></code> 。</li>
</ul>


## 难度

Medium

## 标签

- 栈
- 贪心
- 数组
- 动态规划
- 单调栈

## 提示

1. Do a DP, where dp(i, j) is the answer for the subarray arr[i]..arr[j].
2. For each possible way to partition the subarray i <= k < j, the answer is max(arr[i]..arr[k]) * max(arr[k+1]..arr[j]) + dp(i, k) + dp(k+1, j).

## 示例

```
[6,2,4]
[4,11]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int mctFromLeafValues(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
```

### C

```c
int mctFromLeafValues(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MctFromLeafValues(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var mctFromLeafValues = function(arr) {
    
};
```

### TypeScript

```typescript
function mctFromLeafValues(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function mctFromLeafValues($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mctFromLeafValues(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mctFromLeafValues(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int mctFromLeafValues(List<int> arr) {
    
  }
}
```

### Go

```golang
func mctFromLeafValues(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def mct_from_leaf_values(arr)
    
end
```

### Scala

```scala
object Solution {
    def mctFromLeafValues(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn mct_from_leaf_values(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (mct-from-leaf-values arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec mct_from_leaf_values(Arr :: [integer()]) -> integer().
mct_from_leaf_values(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec mct_from_leaf_values(arr :: [integer]) :: integer
  def mct_from_leaf_values(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mctFromLeafValues(arr: Array<Int64>): Int64 {

    }
}
```

