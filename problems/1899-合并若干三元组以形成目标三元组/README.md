# 1899. 合并若干三元组以形成目标三元组

## 题目描述

<p><strong>三元组</strong> 是一个由三个整数组成的数组。给你一个二维整数数组 <code>triplets</code> ，其中 <code>triplets[i] = [a<sub>i</sub>, b<sub>i</sub>, c<sub>i</sub>]</code> 表示第 <code>i</code> 个 <strong>三元组</strong> 。同时，给你一个整数数组 <code>target = [x, y, z]</code> ，表示你想要得到的 <strong>三元组</strong> 。</p>

<p>为了得到 <code>target</code> ，你需要对 <code>triplets</code> 执行下面的操作 <strong>任意次</strong>（可能 <strong>零</strong> 次）：</p>

<ul>
	<li>选出两个下标（下标 <strong>从 0 开始</strong> 计数）<code>i</code> 和 <code>j</code>（<code>i != j</code>），并 <strong>更新</strong> <code>triplets[j]</code> 为 <code>[max(a<sub>i</sub>, a<sub>j</sub>), max(b<sub>i</sub>, b<sub>j</sub>), max(c<sub>i</sub>, c<sub>j</sub>)]</code> 。

	<ul>
		<li>例如，<code>triplets[i] = [2, 5, 3]</code> 且 <code>triplets[j] = [1, 7, 5]</code>，<code>triplets[j]</code> 将会更新为 <code>[max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5]</code> 。</li>
	</ul>
	</li>
</ul>

<p>如果通过以上操作我们可以使得目标 <strong>三元组</strong> <code>target</code> 成为 <code>triplets</code> 的一个 <strong>元素</strong> ，则返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
<strong>输出：</strong>true
<strong>解释：</strong>执行下述操作：
- 选择第一个和最后一个三元组 [<strong>[2,5,3]</strong>,[1,8,4],<strong>[1,7,5]</strong>] 。更新最后一个三元组为 [max(2,1), max(5,7), max(3,5)] = [2,7,5] 。triplets = [[2,5,3],[1,8,4],<strong>[2,7,5]</strong>]
目标三元组 [2,7,5] 现在是 triplets 的一个元素。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>triplets = [[1,3,4],[2,5,8]], target = [2,5,8]
<strong>输出：</strong>true
<strong>解释：</strong>目标三元组 [2,5,8] 已经是 triplets 的一个元素。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
<strong>输出：</strong>true
<strong>解释：</strong>执行下述操作：
- 选择第一个和第三个三元组 [<strong>[2,5,3]</strong>,[2,3,4],<strong>[1,2,5]</strong>,[5,2,3]] 。更新第三个三元组为 [max(2,1), max(5,2), max(3,5)] = [2,5,5] 。triplets = [[2,5,3],[2,3,4],<strong>[2,5,5]</strong>,[5,2,3]] 。
- 选择第三个和第四个三元组 [[2,5,3],[2,3,4],<strong>[2,5,5]</strong>,<strong>[5,2,3]</strong>] 。更新第四个三元组为 [max(2,5), max(5,2), max(5,3)] = [5,5,5] 。triplets = [[2,5,3],[2,3,4],[2,5,5],<strong>[5,5,5]</strong>] 。
目标三元组 [5,5,5] 现在是 triplets 的一个元素。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
<strong>输出：</strong>false
<strong>解释：</strong>无法得到 [3,2,5] ，因为 triplets 不含 2 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= triplets.length <= 10<sup>5</sup></code></li>
	<li><code>triplets[i].length == target.length == 3</code></li>
	<li><code>1 <= a<sub>i</sub>, b<sub>i</sub>, c<sub>i</sub>, x, y, z <= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组

## 提示

1. Which triplets do you actually care about?
2. What property of max can you use to solve the problem?

## 示例

```
[[2,5,3],[1,8,4],[1,7,5]]
[2,7,5]
[[3,4,5],[4,5,6]]
[3,2,5]
[[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
[5,5,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean mergeTriplets(int[][] triplets, int[] target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
```

### C

```c
bool mergeTriplets(int** triplets, int tripletsSize, int* tripletsColSize, int* target, int targetSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool MergeTriplets(int[][] triplets, int[] target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} triplets
 * @param {number[]} target
 * @return {boolean}
 */
var mergeTriplets = function(triplets, target) {
    
};
```

### TypeScript

```typescript
function mergeTriplets(triplets: number[][], target: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $triplets
     * @param Integer[] $target
     * @return Boolean
     */
    function mergeTriplets($triplets, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mergeTriplets(_ triplets: [[Int]], _ target: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mergeTriplets(triplets: Array<IntArray>, target: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool mergeTriplets(List<List<int>> triplets, List<int> target) {
    
  }
}
```

### Go

```golang
func mergeTriplets(triplets [][]int, target []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} triplets
# @param {Integer[]} target
# @return {Boolean}
def merge_triplets(triplets, target)
    
end
```

### Scala

```scala
object Solution {
    def mergeTriplets(triplets: Array[Array[Int]], target: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn merge_triplets(triplets: Vec<Vec<i32>>, target: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (merge-triplets triplets target)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec merge_triplets(Triplets :: [[integer()]], Target :: [integer()]) -> boolean().
merge_triplets(Triplets, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec merge_triplets(triplets :: [[integer]], target :: [integer]) :: boolean
  def merge_triplets(triplets, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mergeTriplets(triplets: Array<Array<Int64>>, target: Array<Int64>): Bool {

    }
}
```

