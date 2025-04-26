# 1643. 第 K 条最小指令

## 题目描述

<p>Bob 站在单元格 <code>(0, 0)</code> ，想要前往目的地 <code>destination</code> ：<code>(row, column)</code> 。他只能向 <strong>右</strong> 或向 <strong>下</strong> 走。你可以为 Bob 提供导航 <strong>指令</strong> 来帮助他到达目的地 <code>destination</code> 。</p>

<p><strong>指令</strong> 用字符串表示，其中每个字符：</p>

<ul>
	<li><code>'H'</code> ，意味着水平向右移动</li>
	<li><code>'V'</code> ，意味着竖直向下移动</li>
</ul>

<p>能够为 Bob 导航到目的地 <code>destination</code> 的指令可以有多种，例如，如果目的地 <code>destination</code> 是 <code>(2, 3)</code>，<code>"HHHVV"</code> 和 <code>"HVHVH"</code> 都是有效<strong> 指令</strong> 。</p>

<ul>
</ul>

<p>然而，Bob 很挑剔。因为他的幸运数字是 <code>k</code>，他想要遵循 <strong>按字典序排列后的第 <code>k</code> 条最小指令 </strong>的导航前往目的地 <code>destination</code> 。<code>k</code>  的编号 <strong>从 1 开始</strong> 。</p>

<p>给你一个整数数组 <code>destination</code> 和一个整数 <code>k</code> ，请你返回可以为<em> </em>Bob<em> </em>提供前往目的地 <code>destination</code> 导航的<strong> 按字典序排列后的第 <code>k</code> 条最小指令 </strong>。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/01/ex1.png" style="width: 300px;" /></p>

<pre>
<strong>输入：</strong>destination = [2,3], k = 1
<strong>输出：</strong>"HHHVV"
<strong>解释：</strong>能前往 (2, 3) 的所有导航指令 <strong>按字典序排列后</strong> 如下所示：
["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"].
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/01/ex2.png" style="width: 300px; height: 229px;" /></strong></p>

<pre>
<strong>输入：</strong>destination = [2,3], k = 2
<strong>输出：</strong>"HHVHV"
</pre>

<p><strong>示例 3：</strong></p>

<p><strong><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/01/ex3.png" style="width: 300px; height: 229px;" /></strong></p>

<pre>
<strong>输入：</strong>destination = [2,3], k = 3
<strong>输出：</strong>"HHVVH"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>destination.length == 2</code></li>
	<li><code>1 <= row, column <= 15</code></li>
	<li><code>1 <= k <= nCr(row + column, row)</code>，其中 <code>nCr(a, b)</code> 表示组合数，即从 <code>a</code> 个物品中选 <code>b</code> 个物品的不同方案数。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 动态规划
- 组合数学

## 提示

1. There are nCr(row + column, row) possible instructions to reach (row, column).
2. Try building the instructions one step at a time. How many instructions start with "H", and how does this compare with k?

## 示例

```
[2,3]
1
[2,3]
2
[2,3]
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string kthSmallestPath(vector<int>& destination, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public String kthSmallestPath(int[] destination, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def kthSmallestPath(self, destination, k):
        """
        :type destination: List[int]
        :type k: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        
```

### C

```c
char* kthSmallestPath(int* destination, int destinationSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public string KthSmallestPath(int[] destination, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} destination
 * @param {number} k
 * @return {string}
 */
var kthSmallestPath = function(destination, k) {
    
};
```

### TypeScript

```typescript
function kthSmallestPath(destination: number[], k: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $destination
     * @param Integer $k
     * @return String
     */
    function kthSmallestPath($destination, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func kthSmallestPath(_ destination: [Int], _ k: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun kthSmallestPath(destination: IntArray, k: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String kthSmallestPath(List<int> destination, int k) {
    
  }
}
```

### Go

```golang
func kthSmallestPath(destination []int, k int) string {
    
}
```

### Ruby

```ruby
# @param {Integer[]} destination
# @param {Integer} k
# @return {String}
def kth_smallest_path(destination, k)
    
end
```

### Scala

```scala
object Solution {
    def kthSmallestPath(destination: Array[Int], k: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn kth_smallest_path(destination: Vec<i32>, k: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (kth-smallest-path destination k)
  (-> (listof exact-integer?) exact-integer? string?)
  )
```

### Erlang

```erlang
-spec kth_smallest_path(Destination :: [integer()], K :: integer()) -> unicode:unicode_binary().
kth_smallest_path(Destination, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec kth_smallest_path(destination :: [integer], k :: integer) :: String.t
  def kth_smallest_path(destination, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func kthSmallestPath(destination: Array<Int64>, k: Int64): String {

    }
}
```

