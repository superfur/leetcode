# 3159. 查询数组中元素的出现位置

## 题目描述

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;，一个整数数组&nbsp;<code>queries</code>&nbsp;和一个整数&nbsp;<code>x</code>&nbsp;。</p>

<p>对于每个查询&nbsp;<code>queries[i]</code>&nbsp;，你需要找到&nbsp;<code>nums</code>&nbsp;中第&nbsp;<code>queries[i]</code>&nbsp;个&nbsp;<code>x</code>&nbsp;的位置，并返回它的下标。如果数组中&nbsp;<code>x</code>&nbsp;的出现次数少于&nbsp;<code>queries[i]</code>&nbsp;，该查询的答案为 -1 。</p>

<p>请你返回一个整数数组&nbsp;<code>answer</code>&nbsp;，包含所有查询的答案。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,3,1,7], queries = [1,3,2,4], x = 1</span></p>

<p><span class="example-io"><b>输出：</b>[0,-1,2,-1]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>第 1 个查询，第一个 1 出现在下标 0 处。</li>
	<li>第 2 个查询，<code>nums</code>&nbsp;中只有两个 1 ，所以答案为 -1 。</li>
	<li>第 3 个查询，第二个 1 出现在下标 2 处。</li>
	<li>第 4 个查询，<code>nums</code>&nbsp;中只有两个 1 ，所以答案为 -1 。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3], queries = [10], x = 5</span></p>

<p><span class="example-io"><b>输出：</b>[-1]</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>第 1 个查询，<code>nums</code>&nbsp;中没有 5 ，所以答案为 -1 。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length, queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i], x &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表

## 提示

1. Compress the array <code>nums</code> and save all the occurrences of each element in the separate arrays.

## 示例

```
[1,3,1,7]
[1,3,2,4]
1
[1,2,3]
[10]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> occurrencesOfElement(vector<int>& nums, vector<int>& queries, int x) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] occurrencesOfElement(int[] nums, int[] queries, int x) {
        
    }
}
```

### Python

```python
class Solution(object):
    def occurrencesOfElement(self, nums, queries, x):
        """
        :type nums: List[int]
        :type queries: List[int]
        :type x: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* occurrencesOfElement(int* nums, int numsSize, int* queries, int queriesSize, int x, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] OccurrencesOfElement(int[] nums, int[] queries, int x) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @param {number} x
 * @return {number[]}
 */
var occurrencesOfElement = function(nums, queries, x) {
    
};
```

### TypeScript

```typescript
function occurrencesOfElement(nums: number[], queries: number[], x: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer[] $queries
     * @param Integer $x
     * @return Integer[]
     */
    function occurrencesOfElement($nums, $queries, $x) {
        
    }
}
```

### Swift

```swift
class Solution {
    func occurrencesOfElement(_ nums: [Int], _ queries: [Int], _ x: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun occurrencesOfElement(nums: IntArray, queries: IntArray, x: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> occurrencesOfElement(List<int> nums, List<int> queries, int x) {
    
  }
}
```

### Go

```golang
func occurrencesOfElement(nums []int, queries []int, x int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer[]} queries
# @param {Integer} x
# @return {Integer[]}
def occurrences_of_element(nums, queries, x)
    
end
```

### Scala

```scala
object Solution {
    def occurrencesOfElement(nums: Array[Int], queries: Array[Int], x: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn occurrences_of_element(nums: Vec<i32>, queries: Vec<i32>, x: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (occurrences-of-element nums queries x)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec occurrences_of_element(Nums :: [integer()], Queries :: [integer()], X :: integer()) -> [integer()].
occurrences_of_element(Nums, Queries, X) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec occurrences_of_element(nums :: [integer], queries :: [integer], x :: integer) :: [integer]
  def occurrences_of_element(nums, queries, x) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func occurrencesOfElement(nums: Array<Int64>, queries: Array<Int64>, x: Int64): Array<Int64> {

    }
}
```

