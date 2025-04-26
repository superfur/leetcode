# 406. 根据身高重建队列

## 题目描述

<p>假设有打乱顺序的一群人站成一个队列，数组 <code>people</code> 表示队列中一些人的属性（不一定按顺序）。每个 <code>people[i] = [h<sub>i</sub>, k<sub>i</sub>]</code> 表示第 <code>i</code> 个人的身高为 <code>h<sub>i</sub></code> ，前面 <strong>正好</strong> 有 <code>k<sub>i</sub></code><sub> </sub>个身高大于或等于 <code>h<sub>i</sub></code> 的人。</p>

<p>请你重新构造并返回输入数组 <code>people</code> 所表示的队列。返回的队列应该格式化为数组 <code>queue</code> ，其中 <code>queue[j] = [h<sub>j</sub>, k<sub>j</sub>]</code> 是队列中第 <code>j</code> 个人的属性（<code>queue[0]</code> 是排在队列前面的人）。</p>

<p> </p>

<ul>
</ul>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
<strong>输出：</strong>[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
<strong>解释：</strong>
编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
<strong>输出：</strong>[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= people.length <= 2000</code></li>
	<li><code>0 <= h<sub>i</sub> <= 10<sup>6</sup></code></li>
	<li><code>0 <= k<sub>i</sub> < people.length</code></li>
	<li>题目数据确保队列可以被重建</li>
</ul>


## 难度

Medium

## 标签

- 树状数组
- 线段树
- 数组
- 排序

## 提示

1. What can you say about the position of the shortest person? </br>
If the position of the shortest person is <i>i</i>, how many people would be in front of the shortest person?
2. Once you fix the position of the shortest person, what can you say about the position of the second shortest person?

## 示例

```
[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
[[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] reconstructQueue(int[][] people) {
        
    }
}
```

### Python

```python
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** reconstructQueue(int** people, int peopleSize, int* peopleColSize, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] ReconstructQueue(int[][] people) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} people
 * @return {number[][]}
 */
var reconstructQueue = function(people) {
    
};
```

### TypeScript

```typescript
function reconstructQueue(people: number[][]): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $people
     * @return Integer[][]
     */
    function reconstructQueue($people) {
        
    }
}
```

### Swift

```swift
class Solution {
    func reconstructQueue(_ people: [[Int]]) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun reconstructQueue(people: Array<IntArray>): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> reconstructQueue(List<List<int>> people) {
    
  }
}
```

### Go

```golang
func reconstructQueue(people [][]int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} people
# @return {Integer[][]}
def reconstruct_queue(people)
    
end
```

### Scala

```scala
object Solution {
    def reconstructQueue(people: Array[Array[Int]]): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn reconstruct_queue(people: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (reconstruct-queue people)
  (-> (listof (listof exact-integer?)) (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec reconstruct_queue(People :: [[integer()]]) -> [[integer()]].
reconstruct_queue(People) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec reconstruct_queue(people :: [[integer]]) :: [[integer]]
  def reconstruct_queue(people) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func reconstructQueue(people: Array<Array<Int64>>): Array<Array<Int64>> {

    }
}
```

