# 1847. 最近的房间

## 题目描述

<p>一个酒店里有 <code>n</code> 个房间，这些房间用二维整数数组 <code>rooms</code> 表示，其中 <code>rooms[i] = [roomId<sub>i</sub>, size<sub>i</sub>]</code> 表示有一个房间号为 <code>roomId<sub>i</sub></code> 的房间且它的面积为 <code>size<sub>i</sub></code> 。每一个房间号 <code>roomId<sub>i</sub></code> 保证是 <strong>独一无二</strong> 的。</p>

<p>同时给你 <code>k</code> 个查询，用二维数组 <code>queries</code> 表示，其中 <code>queries[j] = [preferred<sub>j</sub>, minSize<sub>j</sub>]</code> 。第 <code>j</code> 个查询的答案是满足如下条件的房间 <code>id</code> ：</p>

<ul>
	<li>房间的面积 <b>至少</b> 为 <code>minSize<sub>j</sub></code> ，且</li>
	<li><code>abs(id - preferred<sub>j</sub>)</code> 的值 <strong>最小</strong> ，其中 <code>abs(x)</code> 是 <code>x</code> 的绝对值。</li>
</ul>

<p>如果差的绝对值有 <strong>相等</strong> 的，选择 <strong>最小</strong> 的 <code>id</code> 。如果 <strong>没有满足条件的房间</strong> ，答案为 <code>-1</code> 。</p>

<p>请你返回长度为 <code>k</code> 的数组 <code>answer</code> ，其中<em> </em><code>answer[j]</code> 为第 <code>j</code> 个查询的结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
<b>输出：</b>[3,-1,3]
<strong>解释：</strong>查询的答案如下：
查询 [3,1] ：房间 3 的面积为 2 ，大于等于 1 ，且号码是最接近 3 的，为 abs(3 - 3) = 0 ，所以答案为 3 。
查询 [3,3] ：没有房间的面积至少为 3 ，所以答案为 -1 。
查询 [5,2] ：房间 3 的面积为 2 ，大于等于 2 ，且号码是最接近 5 的，为 abs(3 - 5) = 2 ，所以答案为 3 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
<b>输出：</b>[2,1,3]
<strong>解释：</strong>查询的答案如下：
查询 [2,3] ：房间 2 的面积为 3 ，大于等于 3 ，且号码是最接近的，为 abs(2 - 2) = 0 ，所以答案为 2 。
查询 [2,4] ：房间 1 和 3 的面积都至少为 4 ，答案为 1 因为它房间编号更小。
查询 [2,5] ：房间 3 是唯一面积大于等于 5 的，所以答案为 3 。</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == rooms.length</code></li>
	<li><code>1 <= n <= 10<sup>5</sup></code></li>
	<li><code>k == queries.length</code></li>
	<li><code>1 <= k <= 10<sup>4</sup></code></li>
	<li><code>1 <= roomId<sub>i</sub>, preferred<sub>j</sub> <= 10<sup>7</sup></code></li>
	<li><code>1 <= size<sub>i</sub>, minSize<sub>j</sub> <= 10<sup>7</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 有序集合
- 排序

## 提示

1. Is there a way to sort the queries so it's easier to search the closest room larger than the size?
2. Use binary search to speed up the search time.

## 示例

```
[[2,2],[1,2],[3,2]]
[[3,1],[3,3],[5,2]]
[[1,4],[2,3],[3,5],[4,1],[5,2]]
[[2,3],[2,4],[2,5]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> closestRoom(vector<vector<int>>& rooms, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] closestRoom(int[][] rooms, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def closestRoom(self, rooms, queries):
        """
        :type rooms: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* closestRoom(int** rooms, int roomsSize, int* roomsColSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ClosestRoom(int[][] rooms, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} rooms
 * @param {number[][]} queries
 * @return {number[]}
 */
var closestRoom = function(rooms, queries) {
    
};
```

### TypeScript

```typescript
function closestRoom(rooms: number[][], queries: number[][]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $rooms
     * @param Integer[][] $queries
     * @return Integer[]
     */
    function closestRoom($rooms, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func closestRoom(_ rooms: [[Int]], _ queries: [[Int]]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun closestRoom(rooms: Array<IntArray>, queries: Array<IntArray>): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> closestRoom(List<List<int>> rooms, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func closestRoom(rooms [][]int, queries [][]int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} rooms
# @param {Integer[][]} queries
# @return {Integer[]}
def closest_room(rooms, queries)
    
end
```

### Scala

```scala
object Solution {
    def closestRoom(rooms: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn closest_room(rooms: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (closest-room rooms queries)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec closest_room(Rooms :: [[integer()]], Queries :: [[integer()]]) -> [integer()].
closest_room(Rooms, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec closest_room(rooms :: [[integer]], queries :: [[integer]]) :: [integer]
  def closest_room(rooms, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func closestRoom(rooms: Array<Array<Int64>>, queries: Array<Array<Int64>>): Array<Int64> {

    }
}
```

