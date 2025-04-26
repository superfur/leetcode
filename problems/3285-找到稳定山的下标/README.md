# 3285. 找到稳定山的下标

## 题目描述

<p>有&nbsp;<code>n</code>&nbsp;座山排成一列，每座山都有一个高度。给你一个整数数组&nbsp;<code>height</code>&nbsp;，其中&nbsp;<code>height[i]</code>&nbsp;表示第 <code>i</code>&nbsp;座山的高度，再给你一个整数&nbsp;<code>threshold</code>&nbsp;。</p>

<p>对于下标不为 <code>0</code>&nbsp;的一座山，如果它左侧相邻的山的高度 <strong>严格</strong><strong>大于</strong>&nbsp;<code>threshold</code>&nbsp;，那么我们称它是 <strong>稳定</strong>&nbsp;的。我们定义下标为 <code>0</code>&nbsp;的山 <strong>不是</strong>&nbsp;稳定的。</p>

<p>请你返回一个数组，包含所有 <strong>稳定</strong>&nbsp;山的下标，你可以以 <strong>任意</strong>&nbsp;顺序返回下标数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>height = [1,2,3,4,5], threshold = 2</span></p>

<p><span class="example-io"><b>输出：</b>[3,4]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>下标为 3 的山是稳定的，因为&nbsp;<code>height[2] == 3</code>&nbsp;大于&nbsp;<code>threshold == 2</code>&nbsp;。</li>
	<li>下标为 4 的山是稳定的，因为&nbsp;<code>height[3] == 4</code> 大于 <code>threshold == 2</code>.</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>height = [10,1,10,1,10], threshold = 3</span></p>

<p><span class="example-io"><b>输出：</b>[1,3]</span></p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>height = [10,1,10,1,10], threshold = 10</span></p>

<p><span class="example-io"><b>输出：</b>[]</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n == height.length &lt;= 100</code></li>
	<li><code>1 &lt;= height[i] &lt;= 100</code></li>
	<li><code>1 &lt;= threshold &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 示例

```
[1,2,3,4,5]
2
[10,1,10,1,10]
3
[10,1,10,1,10]
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> stableMountains(vector<int>& height, int threshold) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> stableMountains(int[] height, int threshold) {
        
    }
}
```

### Python

```python
class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* stableMountains(int* height, int heightSize, int threshold, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> StableMountains(int[] height, int threshold) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} height
 * @param {number} threshold
 * @return {number[]}
 */
var stableMountains = function(height, threshold) {
    
};
```

### TypeScript

```typescript
function stableMountains(height: number[], threshold: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $height
     * @param Integer $threshold
     * @return Integer[]
     */
    function stableMountains($height, $threshold) {
        
    }
}
```

### Swift

```swift
class Solution {
    func stableMountains(_ height: [Int], _ threshold: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun stableMountains(height: IntArray, threshold: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> stableMountains(List<int> height, int threshold) {
    
  }
}
```

### Go

```golang
func stableMountains(height []int, threshold int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} height
# @param {Integer} threshold
# @return {Integer[]}
def stable_mountains(height, threshold)
    
end
```

### Scala

```scala
object Solution {
    def stableMountains(height: Array[Int], threshold: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn stable_mountains(height: Vec<i32>, threshold: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (stable-mountains height threshold)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec stable_mountains(Height :: [integer()], Threshold :: integer()) -> [integer()].
stable_mountains(Height, Threshold) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec stable_mountains(height :: [integer], threshold :: integer) :: [integer]
  def stable_mountains(height, threshold) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func stableMountains(height: Array<Int64>, threshold: Int64): ArrayList<Int64> {

    }
}
```

