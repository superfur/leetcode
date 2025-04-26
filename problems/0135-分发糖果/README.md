# 135. 分发糖果

## 题目描述

<p><code>n</code> 个孩子站成一排。给你一个整数数组 <code>ratings</code> 表示每个孩子的评分。</p>

<p>你需要按照以下要求，给这些孩子分发糖果：</p>

<ul>
	<li>每个孩子至少分配到 <code>1</code> 个糖果。</li>
	<li>相邻两个孩子评分更高的孩子会获得更多的糖果。</li>
</ul>

<p>请你给每个孩子分发糖果，计算并返回需要准备的 <strong>最少糖果数目</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1：</strong></p>

<pre>
<strong>输入：</strong>ratings = [1,0,2]
<strong>输出：</strong>5
<strong>解释：</strong>你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>ratings = [1,2,2]
<strong>输出：</strong>4
<strong>解释：</strong>你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == ratings.length</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= ratings[i] &lt;= 2 * 10<sup>4</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 数组

## 示例

```
[1,0,2]
[1,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int candy(vector<int>& ratings) {
        
    }
};
```

### Java

```java
class Solution {
    public int candy(int[] ratings) {
        
    }
}
```

### Python

```python
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def candy(self, ratings: List[int]) -> int:
        
```

### C

```c
int candy(int* ratings, int ratingsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int Candy(int[] ratings) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} ratings
 * @return {number}
 */
var candy = function(ratings) {
    
};
```

### TypeScript

```typescript
function candy(ratings: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $ratings
     * @return Integer
     */
    function candy($ratings) {
        
    }
}
```

### Swift

```swift
class Solution {
    func candy(_ ratings: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun candy(ratings: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int candy(List<int> ratings) {
    
  }
}
```

### Go

```golang
func candy(ratings []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} ratings
# @return {Integer}
def candy(ratings)
    
end
```

### Scala

```scala
object Solution {
    def candy(ratings: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn candy(ratings: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (candy ratings)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec candy(Ratings :: [integer()]) -> integer().
candy(Ratings) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec candy(ratings :: [integer]) :: integer
  def candy(ratings) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func candy(ratings: Array<Int64>): Int64 {

    }
}
```

