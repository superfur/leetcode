# 3447. 将元素分配给有约束条件的组

## 题目描述

<p>给你一个整数数组 <code>groups</code>，其中 <code>groups[i]</code> 表示第 <code>i</code> 组的大小。另给你一个整数数组 <code>elements</code>。</p>

<p>请你根据以下规则为每个组分配&nbsp;<strong>一个&nbsp;</strong>元素：</p>

<ul>
	<li>如果 <code>groups[i]</code> 能被 <code>elements[j]</code> 整除，则下标为&nbsp;<code>j</code>&nbsp;的元素可以分配给组 <code>i</code>。</li>
	<li>如果有多个元素满足条件，则分配 <strong>最小的下标</strong>&nbsp;<code>j</code>&nbsp;的元素。</li>
	<li>如果没有元素满足条件，则分配 -1 。</li>
</ul>

<p>返回一个整数数组 <code>assigned</code>，其中 <code>assigned[i]</code> 是分配给组 <code>i</code> 的元素的索引，若无合适的元素，则为 -1。</p>

<p><strong>注意：</strong>一个元素可以分配给多个组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">groups = [8,4,3,2,4], elements = [4,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">[0,0,-1,1,0]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>elements[0] = 4</code> 被分配给组 0、1 和 4。</li>
	<li><code>elements[1] = 2</code> 被分配给组 3。</li>
	<li>无法为组 2 分配任何元素，分配 -1 。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">groups = [2,3,5,7], elements = [5,3,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">[-1,1,0,-1]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>elements[1] = 3</code> 被分配给组 1。</li>
	<li><code>elements[0] = 5</code> 被分配给组 2。</li>
	<li>无法为组 0 和组 3 分配任何元素，分配 -1 。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">groups = [10,21,30,41], elements = [2,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">[0,1,0,1]</span></p>

<p><strong>解释：</strong></p>

<p><code>elements[0] = 2</code> 被分配给所有偶数值的组，而 <code>elements[1] = 1</code> 被分配给所有奇数值的组。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= groups.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= elements.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= groups[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= elements[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表

## 提示

1. Can a sieve-like approach be applied here?
2. Starting from the smallest index, iterate through the multiples of the element and assign it to groups divisible by that value.
3. Process each element once.
4. Find all divisors of each group, then match them with elements.

## 示例

```
[8,4,3,2,4]
[4,2]
[2,3,5,7]
[5,3,3]
[10,21,30,41]
[2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> assignElements(vector<int>& groups, vector<int>& elements) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] assignElements(int[] groups, int[] elements) {
        
    }
}
```

### Python

```python
class Solution(object):
    def assignElements(self, groups, elements):
        """
        :type groups: List[int]
        :type elements: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* assignElements(int* groups, int groupsSize, int* elements, int elementsSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] AssignElements(int[] groups, int[] elements) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} groups
 * @param {number[]} elements
 * @return {number[]}
 */
var assignElements = function(groups, elements) {
    
};
```

### TypeScript

```typescript
function assignElements(groups: number[], elements: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $groups
     * @param Integer[] $elements
     * @return Integer[]
     */
    function assignElements($groups, $elements) {
        
    }
}
```

### Swift

```swift
class Solution {
    func assignElements(_ groups: [Int], _ elements: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun assignElements(groups: IntArray, elements: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> assignElements(List<int> groups, List<int> elements) {
    
  }
}
```

### Go

```golang
func assignElements(groups []int, elements []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} groups
# @param {Integer[]} elements
# @return {Integer[]}
def assign_elements(groups, elements)
    
end
```

### Scala

```scala
object Solution {
    def assignElements(groups: Array[Int], elements: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn assign_elements(groups: Vec<i32>, elements: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (assign-elements groups elements)
  (-> (listof exact-integer?) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec assign_elements(Groups :: [integer()], Elements :: [integer()]) -> [integer()].
assign_elements(Groups, Elements) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec assign_elements(groups :: [integer], elements :: [integer]) :: [integer]
  def assign_elements(groups, elements) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func assignElements(groups: Array<Int64>, elements: Array<Int64>): Array<Int64> {

    }
}
```

