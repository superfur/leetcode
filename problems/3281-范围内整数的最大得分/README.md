# 3281. 范围内整数的最大得分

## 题目描述

<p>给你一个整数数组 <code>start</code> 和一个整数 <code>d</code>，代表 <code>n</code> 个区间 <code>[start[i], start[i] + d]</code>。</p>

<p>你需要选择 <code>n</code> 个整数，其中第 <code>i</code> 个整数必须属于第 <code>i</code> 个区间。所选整数的 <strong>得分</strong> 定义为所选整数两两之间的 <strong>最小 </strong>绝对差。</p>

<p>返回所选整数的 <strong>最大可能得分 </strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">start = [6,0,3], d = 2</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>可以选择整数 8, 0 和 4 获得最大可能得分，得分为 <code>min(|8 - 0|, |8 - 4|, |0 - 4|)</code>，等于 4。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">start = [2,6,13,13], d = 5</span></p>

<p><strong>输出：</strong> <span class="example-io">5</span></p>

<p><strong>解释：</strong></p>

<p>可以选择整数 2, 7, 13 和 18 获得最大可能得分，得分为 <code>min(|2 - 7|, |2 - 13|, |2 - 18|, |7 - 13|, |7 - 18|, |13 - 18|)</code>，等于 5。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= start.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= start[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= d &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 二分查找
- 排序

## 提示

1. Can we use binary search here?
2. Suppose that the answer is <code>x</code>. We can find a valid configuration of integers by sorting <code>start</code>, the first integer should be <code>start[0]</code>, then each subsequent integer should be the smallest one in <code>[start[i], start[i] + d]</code> that is greater than <code>last_chosen_value + x</code>.
3. Binary search over <code>x</code>

## 示例

```
[6,0,3]
2
[2,6,13,13]
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxPossibleScore(vector<int>& start, int d) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxPossibleScore(int[] start, int d) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxPossibleScore(self, start, d):
        """
        :type start: List[int]
        :type d: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        
```

### C

```c
int maxPossibleScore(int* start, int startSize, int d) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxPossibleScore(int[] start, int d) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} start
 * @param {number} d
 * @return {number}
 */
var maxPossibleScore = function(start, d) {
    
};
```

### TypeScript

```typescript
function maxPossibleScore(start: number[], d: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $start
     * @param Integer $d
     * @return Integer
     */
    function maxPossibleScore($start, $d) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxPossibleScore(_ start: [Int], _ d: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxPossibleScore(start: IntArray, d: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxPossibleScore(List<int> start, int d) {
    
  }
}
```

### Go

```golang
func maxPossibleScore(start []int, d int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} start
# @param {Integer} d
# @return {Integer}
def max_possible_score(start, d)
    
end
```

### Scala

```scala
object Solution {
    def maxPossibleScore(start: Array[Int], d: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_possible_score(start: Vec<i32>, d: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-possible-score start d)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec max_possible_score(Start :: [integer()], D :: integer()) -> integer().
max_possible_score(Start, D) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_possible_score(start :: [integer], d :: integer) :: integer
  def max_possible_score(start, d) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxPossibleScore(start: Array<Int64>, d: Int64): Int64 {

    }
}
```

