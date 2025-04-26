# 2070. 每一个查询的最大美丽值

## 题目描述

<p>给你一个二维整数数组&nbsp;<code>items</code>&nbsp;，其中&nbsp;<code>items[i] = [price<sub>i</sub>, beauty<sub>i</sub>]</code>&nbsp;分别表示每一个物品的 <strong>价格</strong>&nbsp;和 <strong>美丽值</strong>&nbsp;。</p>

<p>同时给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>queries</code>&nbsp;。对于每个查询&nbsp;<code>queries[j]</code>&nbsp;，你想求出价格小于等于&nbsp;<code>queries[j]</code>&nbsp;的物品中，<strong>最大的美丽值</strong>&nbsp;是多少。如果不存在符合条件的物品，那么查询的结果为&nbsp;<code>0</code>&nbsp;。</p>

<p>请你返回一个长度与 <code>queries</code>&nbsp;相同的数组<em>&nbsp;</em><code>answer</code>，其中<em>&nbsp;</em><code>answer[j]</code>是第&nbsp;<code>j</code>&nbsp;个查询的答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
<b>输出：</b>[2,4,5,5,6,6]
<strong>解释：</strong>
- queries[0]=1 ，[1,2] 是唯一价格 &lt;= 1 的物品。所以这个查询的答案为 2 。
- queries[1]=2 ，符合条件的物品有 [1,2] 和 [2,4] 。
  它们中的最大美丽值为 4 。
- queries[2]=3 和 queries[3]=4 ，符合条件的物品都为 [1,2] ，[3,2] ，[2,4] 和 [3,5] 。
  它们中的最大美丽值为 5 。
- queries[4]=5 和 queries[5]=6 ，所有物品都符合条件。
  所以，答案为所有物品中的最大美丽值，为 6 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
<b>输出：</b>[4]
<b>解释：</b>
每个物品的价格均为 1 ，所以我们选择最大美丽值 4 。
注意，多个物品可能有相同的价格和美丽值。
</pre>

<p><strong>示例 3：</strong></p>

<pre><b>输入：</b>items = [[10,1000]], queries = [5]
<b>输出：</b>[0]
<strong>解释：</strong>
没有物品的价格小于等于 5 ，所以没有物品可以选择。
因此，查询的结果为 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= items.length, queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>items[i].length == 2</code></li>
	<li><code>1 &lt;= price<sub>i</sub>, beauty<sub>i</sub>, queries[j] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 排序

## 提示

1. Can we process the queries in a smart order to avoid repeatedly checking the same items?
2. How can we use the answer to a query for other queries?

## 示例

```
[[1,2],[3,2],[2,4],[5,6],[3,5]]
[1,2,3,4,5,6]
[[1,2],[1,2],[1,3],[1,4]]
[1]
[[10,1000]]
[5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> maximumBeauty(vector<vector<int>>& items, vector<int>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] maximumBeauty(int[][] items, int[] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maximumBeauty(int** items, int itemsSize, int* itemsColSize, int* queries, int queriesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MaximumBeauty(int[][] items, int[] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} items
 * @param {number[]} queries
 * @return {number[]}
 */
var maximumBeauty = function(items, queries) {
    
};
```

### TypeScript

```typescript
function maximumBeauty(items: number[][], queries: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $items
     * @param Integer[] $queries
     * @return Integer[]
     */
    function maximumBeauty($items, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maximumBeauty(_ items: [[Int]], _ queries: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maximumBeauty(items: Array<IntArray>, queries: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> maximumBeauty(List<List<int>> items, List<int> queries) {
    
  }
}
```

### Go

```golang
func maximumBeauty(items [][]int, queries []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} items
# @param {Integer[]} queries
# @return {Integer[]}
def maximum_beauty(items, queries)
    
end
```

### Scala

```scala
object Solution {
    def maximumBeauty(items: Array[Array[Int]], queries: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn maximum_beauty(items: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (maximum-beauty items queries)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec maximum_beauty(Items :: [[integer()]], Queries :: [integer()]) -> [integer()].
maximum_beauty(Items, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec maximum_beauty(items :: [[integer]], queries :: [integer]) :: [integer]
  def maximum_beauty(items, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maximumBeauty(items: Array<Array<Int64>>, queries: Array<Int64>): Array<Int64> {

    }
}
```

