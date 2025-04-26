# 1395. 统计作战单位数

## 题目描述

<p>&nbsp;<code>n</code> 名士兵站成一排。每个士兵都有一个 <strong>独一无二</strong> 的评分 <code>rating</code> 。</p>

<p>从中选出 <strong>3</strong> 个士兵组成一个作战单位，规则如下：</p>

<ul>
	<li>从队伍中选出下标分别为 <code>i</code>、<code>j</code>、<code>k</code> 的 3 名士兵，他们的评分分别为 <code>rating[i]</code>、<code>rating[j]</code>、<code>rating[k]</code></li>
	<li>作战单位需满足： <code>rating[i] &lt; rating[j] &lt; rating[k]</code> 或者 <code>rating[i] &gt; rating[j] &gt; rating[k]</code> ，其中&nbsp; <code>0&nbsp;&lt;= i &lt;&nbsp;j &lt;&nbsp;k &lt;&nbsp;n</code></li>
</ul>

<p>请你返回按上述条件组建的作战单位的方案数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>rating = [2,5,3,4,1]
<strong>输出：</strong>3
<strong>解释：</strong>我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>rating = [2,1,3]
<strong>输出：</strong>0
<strong>解释：</strong>根据题目条件，我们无法组建作战单位。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>rating = [1,2,3,4]
<strong>输出：</strong>4
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == rating.length</code></li>
	<li><code>3 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= rating[i] &lt;= 10^5</code></li>
	<li><code>rating</code>&nbsp;中的元素都是唯一的</li>
</ul>


## 难度

Medium

## 标签

- 树状数组
- 线段树
- 数组
- 动态规划

## 提示

1. BruteForce, check all possibilities.

## 示例

```
[2,5,3,4,1]
[2,1,3]
[1,2,3,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numTeams(vector<int>& rating) {
        
    }
};
```

### Java

```java
class Solution {
    public int numTeams(int[] rating) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numTeams(self, rating):
        """
        :type rating: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
```

### C

```c
int numTeams(int* rating, int ratingSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumTeams(int[] rating) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} rating
 * @return {number}
 */
var numTeams = function(rating) {
    
};
```

### TypeScript

```typescript
function numTeams(rating: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $rating
     * @return Integer
     */
    function numTeams($rating) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numTeams(_ rating: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numTeams(rating: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numTeams(List<int> rating) {
    
  }
}
```

### Go

```golang
func numTeams(rating []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} rating
# @return {Integer}
def num_teams(rating)
    
end
```

### Scala

```scala
object Solution {
    def numTeams(rating: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_teams(rating: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-teams rating)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_teams(Rating :: [integer()]) -> integer().
num_teams(Rating) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_teams(rating :: [integer]) :: integer
  def num_teams(rating) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numTeams(rating: Array<Int64>): Int64 {

    }
}
```

