# 3184. 构成整天的下标对数目 I

## 题目描述

<p>给你一个整数数组 <code>hours</code>，表示以 <strong>小时 </strong>为单位的时间，返回一个整数，表示满足 <code>i &lt; j</code> 且 <code>hours[i] + hours[j]</code> 构成 <strong>整天 </strong>的下标对&nbsp;<code>i</code>, <code>j</code> 的数目。</p>

<p><strong>整天 </strong>定义为时间持续时间是 24 小时的 <strong>整数倍 </strong>。</p>

<p>例如，1 天是 24 小时，2 天是 48 小时，3 天是 72 小时，以此类推。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">hours = [12,12,30,24,24]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>构成整天的下标对分别是 <code>(0, 1)</code> 和 <code>(3, 4)</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">hours = [72,48,24,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>构成整天的下标对分别是 <code>(0, 1)</code>、<code>(0, 2)</code> 和 <code>(1, 2)</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= hours.length &lt;= 100</code></li>
	<li><code>1 &lt;= hours[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. Brute force all pairs <code>(i, j)</code> and check if they form a valid complete day. It is considered a complete day if <code>(hours[i] + hours[j]) % 24 == 0</code>.

## 示例

```
[12,12,30,24,24]
[72,48,24,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countCompleteDayPairs(vector<int>& hours) {
        
    }
};
```

### Java

```java
class Solution {
    public int countCompleteDayPairs(int[] hours) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countCompleteDayPairs(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        
```

### C

```c
int countCompleteDayPairs(int* hours, int hoursSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountCompleteDayPairs(int[] hours) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} hours
 * @return {number}
 */
var countCompleteDayPairs = function(hours) {
    
};
```

### TypeScript

```typescript
function countCompleteDayPairs(hours: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $hours
     * @return Integer
     */
    function countCompleteDayPairs($hours) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countCompleteDayPairs(_ hours: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countCompleteDayPairs(hours: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countCompleteDayPairs(List<int> hours) {
    
  }
}
```

### Go

```golang
func countCompleteDayPairs(hours []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} hours
# @return {Integer}
def count_complete_day_pairs(hours)
    
end
```

### Scala

```scala
object Solution {
    def countCompleteDayPairs(hours: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_complete_day_pairs(hours: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-complete-day-pairs hours)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_complete_day_pairs(Hours :: [integer()]) -> integer().
count_complete_day_pairs(Hours) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_complete_day_pairs(hours :: [integer]) :: integer
  def count_complete_day_pairs(hours) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countCompleteDayPairs(hours: Array<Int64>): Int64 {

    }
}
```

