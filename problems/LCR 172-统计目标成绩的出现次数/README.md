# LCR 172. 统计目标成绩的出现次数

## 题目描述

<p>某班级考试成绩按非严格递增顺序记录于整数数组 <code>scores</code>，请返回目标成绩 <code>target</code> 的出现次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> scores = [2, 2, 3, 4, 4, 4, 5, 6, 6, 8], target = 4
<strong>输出:</strong> 3</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入:</strong> scores = [1, 2, 3, 5, 7, 9], target = 6
<strong>输出:</strong> 0</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= scores.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= scores[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
	<li><code>scores</code>&nbsp;是一个非递减数组</li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= target&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与主站 34 题相同（仅返回值不同）：<a href="https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/">https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/</a></p>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 数组
- 二分查找

## 示例

```
[2,2,3,4,4,4,5,6,6,8]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countTarget(vector<int>& scores, int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int countTarget(int[] scores, int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countTarget(self, scores, target):
        """
        :type scores: List[int]
        :type target: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        
```

### C

```c
int countTarget(int* scores, int scoresSize, int target) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountTarget(int[] scores, int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} scores
 * @param {number} target
 * @return {number}
 */
var countTarget = function(scores, target) {
    
};
```

### TypeScript

```typescript
function countTarget(scores: number[], target: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $scores
     * @param Integer $target
     * @return Integer
     */
    function countTarget($scores, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countTarget(_ scores: [Int], _ target: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countTarget(scores: IntArray, target: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countTarget(List<int> scores, int target) {
    
  }
}
```

### Go

```golang
func countTarget(scores []int, target int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} scores
# @param {Integer} target
# @return {Integer}
def count_target(scores, target)
    
end
```

### Scala

```scala
object Solution {
    def countTarget(scores: Array[Int], target: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_target(scores: Vec<i32>, target: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-target scores target)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_target(Scores :: [integer()], Target :: integer()) -> integer().
count_target(Scores, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_target(scores :: [integer], target :: integer) :: integer
  def count_target(scores, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countTarget(scores: Array<Int64>, target: Int64): Int64 {

    }
}
```

