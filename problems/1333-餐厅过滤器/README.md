# 1333. 餐厅过滤器

## 题目描述

<p>给你一个餐馆信息数组&nbsp;<code>restaurants</code>，其中&nbsp;&nbsp;<code>restaurants[i] = [id<sub>i</sub>, rating<sub>i</sub>, veganFriendly<sub>i</sub>, price<sub>i</sub>, distance<sub>i</sub>]</code>。你必须使用以下三个过滤器来过滤这些餐馆信息。</p>

<p>其中素食者友好过滤器&nbsp;<code>veganFriendly</code>&nbsp;的值可以为 <code>true</code> 或者 <code>false</code>，如果为 <em>true</em>&nbsp;就意味着你应该只包括&nbsp;<code>veganFriendly<sub>i</sub></code>&nbsp;为 true 的餐馆，为&nbsp;<em>false</em>&nbsp;则意味着可以包括任何餐馆。此外，我们还有最大价格&nbsp;<code>maxPrice</code>&nbsp;和最大距离&nbsp;<code>maxDistance</code>&nbsp;两个过滤器，它们分别考虑餐厅的价格因素和距离因素的最大值。</p>

<p>过滤后返回餐馆的 <strong><em>id</em></strong>，按照 <em><strong>rating</strong></em>&nbsp;从高到低排序。如果 <em><strong>rating</strong></em> 相同，那么按 <em><strong>id</strong></em> 从高到低排序。简单起见，&nbsp;<code>veganFriendly<sub>i</sub></code> 和 <code>veganFriendly</code>&nbsp;为&nbsp;<em>true</em>&nbsp;时取值为 <em>1</em>，为 <em>false</em> 时，取值为&nbsp;<em>0 。</em></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
<strong>输出：</strong>[3,1,5] 
<strong>解释： 
</strong>这些餐馆为：
餐馆 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
餐馆 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
餐馆 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
餐馆 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
餐馆 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1] 
在按照 veganFriendly = 1, maxPrice = 50 和 maxDistance = 10 进行过滤后，我们得到了餐馆 3, 餐馆 1 和 餐馆 5（按评分从高到低排序）。 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10
<strong>输出：</strong>[4,3,2,1,5]
<strong>解释：</strong>餐馆与示例 1 相同，但在 veganFriendly = 0 的过滤条件下，应该考虑所有餐馆。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3
<strong>输出：</strong>[4,5]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;restaurants.length &lt;= 10^4</code></li>
	<li><code>restaurants[i].length == 5</code></li>
	<li><code>1 &lt;=&nbsp;id<sub>i</sub>, rating<sub>i</sub>, price<sub>i</sub>, distance<sub>i </sub>&lt;= 10^5</code></li>
	<li><code>1 &lt;=&nbsp;maxPrice,&nbsp;maxDistance &lt;= 10^5</code></li>
	<li><code>veganFriendly<sub>i</sub></code> 和&nbsp;<code>veganFriendly</code>&nbsp;的值为 0 或 1 。</li>
	<li>所有 <code>id<sub>i</sub></code> 各不相同。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 排序

## 提示

1. Do the filtering and sort as said. Note that the id may not be the index in the array.

## 示例

```
[[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
1
50
10
[[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
0
50
10
[[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]
0
30
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> filterRestaurants(vector<vector<int>>& restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> filterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        
    }
}
```

### Python

```python
class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        """
        :type restaurants: List[List[int]]
        :type veganFriendly: int
        :type maxPrice: int
        :type maxDistance: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* filterRestaurants(int** restaurants, int restaurantsSize, int* restaurantsColSize, int veganFriendly, int maxPrice, int maxDistance, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> FilterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} restaurants
 * @param {number} veganFriendly
 * @param {number} maxPrice
 * @param {number} maxDistance
 * @return {number[]}
 */
var filterRestaurants = function(restaurants, veganFriendly, maxPrice, maxDistance) {
    
};
```

### TypeScript

```typescript
function filterRestaurants(restaurants: number[][], veganFriendly: number, maxPrice: number, maxDistance: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $restaurants
     * @param Integer $veganFriendly
     * @param Integer $maxPrice
     * @param Integer $maxDistance
     * @return Integer[]
     */
    function filterRestaurants($restaurants, $veganFriendly, $maxPrice, $maxDistance) {
        
    }
}
```

### Swift

```swift
class Solution {
    func filterRestaurants(_ restaurants: [[Int]], _ veganFriendly: Int, _ maxPrice: Int, _ maxDistance: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun filterRestaurants(restaurants: Array<IntArray>, veganFriendly: Int, maxPrice: Int, maxDistance: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> filterRestaurants(List<List<int>> restaurants, int veganFriendly, int maxPrice, int maxDistance) {
    
  }
}
```

### Go

```golang
func filterRestaurants(restaurants [][]int, veganFriendly int, maxPrice int, maxDistance int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} restaurants
# @param {Integer} vegan_friendly
# @param {Integer} max_price
# @param {Integer} max_distance
# @return {Integer[]}
def filter_restaurants(restaurants, vegan_friendly, max_price, max_distance)
    
end
```

### Scala

```scala
object Solution {
    def filterRestaurants(restaurants: Array[Array[Int]], veganFriendly: Int, maxPrice: Int, maxDistance: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn filter_restaurants(restaurants: Vec<Vec<i32>>, vegan_friendly: i32, max_price: i32, max_distance: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (filter-restaurants restaurants veganFriendly maxPrice maxDistance)
  (-> (listof (listof exact-integer?)) exact-integer? exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec filter_restaurants(Restaurants :: [[integer()]], VeganFriendly :: integer(), MaxPrice :: integer(), MaxDistance :: integer()) -> [integer()].
filter_restaurants(Restaurants, VeganFriendly, MaxPrice, MaxDistance) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec filter_restaurants(restaurants :: [[integer]], vegan_friendly :: integer, max_price :: integer, max_distance :: integer) :: [integer]
  def filter_restaurants(restaurants, vegan_friendly, max_price, max_distance) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func filterRestaurants(restaurants: Array<Array<Int64>>, veganFriendly: Int64, maxPrice: Int64, maxDistance: Int64): ArrayList<Int64> {

    }
}
```

