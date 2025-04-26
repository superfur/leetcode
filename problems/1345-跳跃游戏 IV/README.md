# 1345. 跳跃游戏 IV

## 题目描述

<p>给你一个整数数组&nbsp;<code>arr</code>&nbsp;，你一开始在数组的第一个元素处（下标为 0）。</p>

<p>每一步，你可以从下标&nbsp;<code>i</code>&nbsp;跳到下标&nbsp;<code>i + 1</code> 、<code>i - 1</code> 或者 <code>j</code> ：</p>

<ul>
	<li><code>i + 1</code> 需满足：<code>i + 1 &lt; arr.length</code></li>
	<li><code>i - 1</code>&nbsp;需满足：<code>i - 1 &gt;= 0</code></li>
	<li><code>j</code>&nbsp;需满足：<code>arr[i] == arr[j]</code>&nbsp;且&nbsp;<code>i != j</code></li>
</ul>

<p>请你返回到达数组最后一个元素的下标处所需的&nbsp;<strong>最少操作次数</strong>&nbsp;。</p>

<p>注意：任何时候你都不能跳到数组外面。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [100,-23,-23,404,100,23,23,23,3,404]
<strong>输出：</strong>3
<strong>解释：</strong>那你需要跳跃 3 次，下标依次为 0 --&gt; 4 --&gt; 3 --&gt; 9 。下标 9 为数组的最后一个元素的下标。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [7]
<strong>输出：</strong>0
<strong>解释：</strong>一开始就在最后一个元素处，所以你不需要跳跃。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [7,6,9,6,9,6,9,7]
<strong>输出：</strong>1
<strong>解释：</strong>你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>
<meta charset="UTF-8" />

<ul>
	<li><code>1 &lt;= arr.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>8</sup>&nbsp;&lt;= arr[i] &lt;= 10<sup>8</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 数组
- 哈希表

## 提示

1. Build a graph of n nodes where nodes are the indices of the array and edges for node i are nodes i+1, i-1, j where arr[i] == arr[j].
2. Start bfs from node 0 and keep distance. The answer is the distance when you reach node n-1.

## 示例

```
[100,-23,-23,404,100,23,23,23,3,404]
[7]
[7,6,9,6,9,6,9,7]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minJumps(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int minJumps(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
```

### C

```c
int minJumps(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinJumps(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var minJumps = function(arr) {
    
};
```

### TypeScript

```typescript
function minJumps(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function minJumps($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minJumps(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minJumps(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minJumps(List<int> arr) {
    
  }
}
```

### Go

```golang
func minJumps(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def min_jumps(arr)
    
end
```

### Scala

```scala
object Solution {
    def minJumps(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-jumps arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_jumps(Arr :: [integer()]) -> integer().
min_jumps(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_jumps(arr :: [integer]) :: integer
  def min_jumps(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minJumps(arr: Array<Int64>): Int64 {

    }
}
```

