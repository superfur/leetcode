# 1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的正整数数组 <code>candiesCount</code> ，其中 <code>candiesCount[i]</code> 表示你拥有的第 <code>i</code> 类糖果的数目。同时给你一个二维数组 <code>queries</code> ，其中 <code>queries[i] = [favoriteType<sub>i</sub>, favoriteDay<sub>i</sub>, dailyCap<sub>i</sub>]</code> 。</p>

<p>你按照如下规则进行一场游戏：</p>

<ul>
	<li>你从第 <code><strong>0</strong></code><strong> </strong>天开始吃糖果。</li>
	<li>你在吃完 <strong>所有</strong> 第 <code>i - 1</code> 类糖果之前，<strong>不能</strong> 吃任何一颗第 <code>i</code> 类糖果。</li>
	<li>在吃完所有糖果之前，你必须每天 <strong>至少</strong> 吃 <strong>一颗</strong> 糖果。</li>
</ul>

<p>请你构建一个布尔型数组 <code>answer</code> ，用以给出 <code>queries</code> 中每一项的对应答案。此数组满足：</p>

<ul>
	<li><code>answer.length == queries.length</code> 。<code>answer[i]</code> 是 <code>queries[i]</code> 的答案。</li>
	<li><code>answer[i]</code> 为 <code>true</code> 的条件是：在每天吃 <strong>不超过</strong> <code>dailyCap<sub>i</sub></code><sub> </sub>颗糖果的前提下，你可以在第 <code>favoriteDay<sub>i</sub></code> 天吃到第 <code>favoriteType<sub>i</sub></code> 类糖果；否则 <code>answer[i]</code> 为 <code>false</code> 。</li>
</ul>

<p>注意，只要满足上面 3 条规则中的第二条规则，你就可以在同一天吃不同类型的糖果。</p>

<p>请你返回得到的数组<em> </em><code>answer</code> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
<b>输出：</b>[true,false,true]
<strong>提示：</strong>
1- 在第 0 天吃 2 颗糖果(类型 0），第 1 天吃 2 颗糖果（类型 0），第 2 天你可以吃到类型 0 的糖果。
2- 每天你最多吃 4 颗糖果。即使第 0 天吃 4 颗糖果（类型 0），第 1 天吃 4 颗糖果（类型 0 和类型 1），你也没办法在第 2 天吃到类型 4 的糖果。换言之，你没法在每天吃 4 颗糖果的限制下在第 2 天吃到第 4 类糖果。
3- 如果你每天吃 1 颗糖果，你可以在第 13 天吃到类型 2 的糖果。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
<b>输出：</b>[false,true,true,false,false]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= candiesCount.length <= 10<sup>5</sup></code></li>
	<li><code>1 <= candiesCount[i] <= 10<sup>5</sup></code></li>
	<li><code>1 <= queries.length <= 10<sup>5</sup></code></li>
	<li><code>queries[i].length == 3</code></li>
	<li><code>0 <= favoriteType<sub>i</sub> < candiesCount.length</code></li>
	<li><code>0 <= favoriteDay<sub>i</sub> <= 10<sup>9</sup></code></li>
	<li><code>1 <= dailyCap<sub>i</sub> <= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 前缀和

## 提示

1. The query is true if and only if your favorite day is in between the earliest and latest possible days to eat your favorite candy.
2. To get the earliest day, you need to eat dailyCap candies every day. To get the latest day, you need to eat 1 candy every day.
3. The latest possible day is the total number of candies with a smaller type plus the number of your favorite candy minus 1.
4. The earliest possible day that you can eat your favorite candy is the total number of candies with a smaller type divided by dailyCap.

## 示例

```
[7,4,5,3,8]
[[0,2,2],[4,2,4],[2,13,1000000000]]
[5,2,6,4,1]
[[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<bool> canEat(vector<int>& candiesCount, vector<vector<int>>& queries) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean[] canEat(int[] candiesCount, int[][] queries) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canEat(self, candiesCount, queries):
        """
        :type candiesCount: List[int]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        
```

### Python3

```python3
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* canEat(int* candiesCount, int candiesCountSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool[] CanEat(int[] candiesCount, int[][] queries) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} candiesCount
 * @param {number[][]} queries
 * @return {boolean[]}
 */
var canEat = function(candiesCount, queries) {
    
};
```

### TypeScript

```typescript
function canEat(candiesCount: number[], queries: number[][]): boolean[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $candiesCount
     * @param Integer[][] $queries
     * @return Boolean[]
     */
    function canEat($candiesCount, $queries) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canEat(_ candiesCount: [Int], _ queries: [[Int]]) -> [Bool] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canEat(candiesCount: IntArray, queries: Array<IntArray>): BooleanArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<bool> canEat(List<int> candiesCount, List<List<int>> queries) {
    
  }
}
```

### Go

```golang
func canEat(candiesCount []int, queries [][]int) []bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} candies_count
# @param {Integer[][]} queries
# @return {Boolean[]}
def can_eat(candies_count, queries)
    
end
```

### Scala

```scala
object Solution {
    def canEat(candiesCount: Array[Int], queries: Array[Array[Int]]): Array[Boolean] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_eat(candies_count: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<bool> {
        
    }
}
```

### Racket

```racket
(define/contract (can-eat candiesCount queries)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) (listof boolean?))
  )
```

### Erlang

```erlang
-spec can_eat(CandiesCount :: [integer()], Queries :: [[integer()]]) -> [boolean()].
can_eat(CandiesCount, Queries) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_eat(candies_count :: [integer], queries :: [[integer]]) :: [boolean]
  def can_eat(candies_count, queries) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canEat(candiesCount: Array<Int64>, queries: Array<Array<Int64>>): Array<Bool> {

    }
}
```

