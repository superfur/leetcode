# 2251. 花期内花的数目

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的二维整数数组&nbsp;<code>flowers</code>&nbsp;，其中&nbsp;<code>flowers[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;朵花的 <strong>花期</strong>&nbsp;从&nbsp;<code>start<sub>i</sub></code>&nbsp;到&nbsp;<code>end<sub>i</sub></code>&nbsp;（都 <strong>包含</strong>）。同时给你一个下标从 <strong>0</strong>&nbsp;开始大小为 <code>n</code>&nbsp;的整数数组&nbsp;<code>people</code> ，<code>people[i]</code>&nbsp;是第&nbsp;<code>i</code>&nbsp;个人来看花的时间。</p>

<p>请你返回一个大小为 <code>n</code>&nbsp;的整数数组<em>&nbsp;</em><code>answer</code>&nbsp;，其中&nbsp;<code>answer[i]</code>是第&nbsp;<code>i</code>&nbsp;个人到达时在花期内花的&nbsp;<strong>数目</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/02/ex1new.jpg" style="width: 550px; height: 216px;" /></p>

<pre>
<b>输入：</b>flowers = [[1,6],[3,7],[9,12],[4,13]], people = [2,3,7,11]
<b>输出：</b>[1,2,2,2]
<strong>解释：</strong>上图展示了每朵花的花期时间，和每个人的到达时间。
对每个人，我们返回他们到达时在花期内花的数目。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2022/03/02/ex2new.jpg" style="width: 450px; height: 195px;" /></p>

<pre>
<b>输入：</b>flowers = [[1,10],[3,3]], people = [3,3,2]
<b>输出：</b>[2,2,1]
<b>解释：</b>上图展示了每朵花的花期时间，和每个人的到达时间。
对每个人，我们返回他们到达时在花期内花的数目。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= flowers.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>flowers[i].length == 2</code></li>
	<li><code>1 &lt;= start<sub>i</sub> &lt;= end<sub>i</sub> &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= people.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= people[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 哈希表
- 二分查找
- 有序集合
- 前缀和
- 排序

## 提示

1. Notice that for any given time t, the number of flowers blooming at time t is equal to the number of flowers that have started blooming minus the number of flowers that have already stopped blooming.
2. We can obtain these values efficiently using binary search.
3. We can store the starting times in sorted order, which then allows us to binary search to find how many flowers have started blooming for a given time t.
4. We do the same for the ending times to find how many flowers have stopped blooming at time t.

## 示例

```
[[1,6],[3,7],[9,12],[4,13]]
[2,3,7,11]
[[1,10],[3,3]]
[3,3,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> fullBloomFlowers(vector<vector<int>>& flowers, vector<int>& people) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] fullBloomFlowers(int[][] flowers, int[] people) {
        
    }
}
```

### Python

```python
class Solution(object):
    def fullBloomFlowers(self, flowers, people):
        """
        :type flowers: List[List[int]]
        :type people: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* fullBloomFlowers(int** flowers, int flowersSize, int* flowersColSize, int* people, int peopleSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] FullBloomFlowers(int[][] flowers, int[] people) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} flowers
 * @param {number[]} people
 * @return {number[]}
 */
var fullBloomFlowers = function(flowers, people) {
    
};
```

### TypeScript

```typescript
function fullBloomFlowers(flowers: number[][], people: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $flowers
     * @param Integer[] $people
     * @return Integer[]
     */
    function fullBloomFlowers($flowers, $people) {
        
    }
}
```

### Swift

```swift
class Solution {
    func fullBloomFlowers(_ flowers: [[Int]], _ people: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun fullBloomFlowers(flowers: Array<IntArray>, people: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> fullBloomFlowers(List<List<int>> flowers, List<int> people) {
    
  }
}
```

### Go

```golang
func fullBloomFlowers(flowers [][]int, people []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} flowers
# @param {Integer[]} people
# @return {Integer[]}
def full_bloom_flowers(flowers, people)
    
end
```

### Scala

```scala
object Solution {
    def fullBloomFlowers(flowers: Array[Array[Int]], people: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn full_bloom_flowers(flowers: Vec<Vec<i32>>, people: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (full-bloom-flowers flowers people)
  (-> (listof (listof exact-integer?)) (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec full_bloom_flowers(Flowers :: [[integer()]], People :: [integer()]) -> [integer()].
full_bloom_flowers(Flowers, People) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec full_bloom_flowers(flowers :: [[integer]], people :: [integer]) :: [integer]
  def full_bloom_flowers(flowers, people) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func fullBloomFlowers(flowers: Array<Array<Int64>>, people: Array<Int64>): Array<Int64> {

    }
}
```

