# 1282. 用户分组

## 题目描述

<p>有&nbsp;<code>n</code>&nbsp;个人被分成数量未知的组。每个人都被标记为一个从 <code>0</code> 到 <code>n - 1</code> 的<strong>唯一ID</strong>&nbsp;。</p>

<p>给定一个整数数组 <code>groupSizes</code> ，其中<meta charset="UTF-8" />&nbsp;<code>groupSizes[i]</code>&nbsp;是第 <code>i</code> 个人所在的组的大小。例如，如果&nbsp;<code>groupSizes[1] = 3</code>&nbsp;，则第 <code>1</code> 个人必须位于大小为 <code>3</code> 的组中。</p>

<p>返回一个组列表，使每个人 <code>i</code> 都在一个大小为<meta charset="UTF-8" /><em>&nbsp;<code>groupSizes[i]</code>&nbsp;</em>的组中。</p>

<p>每个人应该&nbsp;<strong>恰好只&nbsp;</strong>出现在&nbsp;<strong>一个组&nbsp;</strong>中，并且每个人必须在一个组中。如果有多个答案，返回其中&nbsp;<strong>任何&nbsp;</strong>一个。可以&nbsp;<strong>保证&nbsp;</strong>给定输入&nbsp;<strong>至少有一个&nbsp;</strong>有效的解。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>groupSizes = [3,3,3,3,3,1,3]
<strong>输出：</strong>[[5],[0,1,2],[3,4,6]]
<strong>解释：
</strong>第一组是 [5]，大小为 1，groupSizes[5] = 1。
第二组是 [0,1,2]，大小为 3，groupSizes[0] = groupSizes[1] = groupSizes[2] = 3。
第三组是 [3,4,6]，大小为 3，groupSizes[3] = groupSizes[4] = groupSizes[6] = 3。 
其他可能的解决方案有 [[2,1,6],[5],[0,4,3]] 和 [[5],[0,6,2],[4,3,1]]。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>groupSizes = [2,1,3,3,3,2]
<strong>输出：</strong>[[1],[0,5],[2,3,4]]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>groupSizes.length == n</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 500</code></li>
	<li><code>1 &lt;=&nbsp;groupSizes[i] &lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表

## 提示

1. Put people's IDs with same groupSize into buckets, then split each bucket into groups.
2. Greedy fill until you need a new group.

## 示例

```
[3,3,3,3,3,1,3]
[2,1,3,3,3,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** groupThePeople(int* groupSizes, int groupSizesSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> GroupThePeople(int[] groupSizes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} groupSizes
 * @return {number[][]}
 */
var groupThePeople = function(groupSizes) {
    
};
```

### TypeScript

```typescript
function groupThePeople(groupSizes: number[]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $groupSizes
     * @return Integer[][]
     */
    function groupThePeople($groupSizes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func groupThePeople(_ groupSizes: [Int]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun groupThePeople(groupSizes: IntArray): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> groupThePeople(List<int> groupSizes) {
    
  }
}
```

### Go

```golang
func groupThePeople(groupSizes []int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} group_sizes
# @return {Integer[][]}
def group_the_people(group_sizes)
    
end
```

### Scala

```scala
object Solution {
    def groupThePeople(groupSizes: Array[Int]): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (group-the-people groupSizes)
  (-> (listof exact-integer?) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec group_the_people(GroupSizes :: [integer()]) -> [[integer()]].
group_the_people(GroupSizes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec group_the_people(group_sizes :: [integer]) :: [[integer]]
  def group_the_people(group_sizes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func groupThePeople(groupSizes: Array<Int64>): ArrayList<ArrayList<Int64>> {

    }
}
```

