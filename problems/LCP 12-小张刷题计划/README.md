# LCP 12. 小张刷题计划

## 题目描述

<p>为了提高自己的代码能力，小张制定了 <code>LeetCode</code> 刷题计划，他选中了 <code>LeetCode</code> 题库中的 <code>n</code> 道题，编号从 <code>0</code> 到 <code>n-1</code>，并计划在 <code>m</code> 天内<strong>按照题目编号顺序</strong>刷完所有的题目（注意，小张不能用多天完成同一题）。</p>

<p>在小张刷题计划中，小张需要用 <code>time[i]</code> 的时间完成编号 <code>i</code> 的题目。此外，小张还可以使用场外求助功能，通过询问他的好朋友小杨题目的解法，可以省去该题的做题时间。为了防止&ldquo;小张刷题计划&rdquo;变成&ldquo;小杨刷题计划&rdquo;，小张每天最多使用一次求助。</p>

<p>我们定义 <code>m</code> 天中做题时间最多的一天耗时为 <code>T</code>（小杨完成的题目不计入做题总时间）。请你帮小张求出最小的 <code>T</code>是多少。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>time = [1,2,3,3], m = 2</code></p>

<p>输出：<code>3</code></p>

<p>解释：第一天小张完成前三题，其中第三题找小杨帮忙；第二天完成第四题，并且找小杨帮忙。这样做题时间最多的一天花费了 3 的时间，并且这个值是最小的。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>time = [999,999,999], m = 4</code></p>

<p>输出：<code>0</code></p>

<p>解释：在前三天中，小张每天求助小杨一次，这样他可以在三天内完成所有的题目并不花任何时间。</p>
</blockquote>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= time.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= time[i] &lt;= 10000</code></li>
	<li><code>1 &lt;= m &lt;= 1000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找

## 示例

```
[1,2,3,3]
2
[1,2,3,3,3]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minTime(vector<int>& time, int m) {
        
    }
};
```

### Java

```java
class Solution {
    public int minTime(int[] time, int m) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minTime(self, time, m):
        """
        :type time: List[int]
        :type m: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        
```

### C

```c
int minTime(int* time, int timeSize, int m) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinTime(int[] time, int m) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} time
 * @param {number} m
 * @return {number}
 */
var minTime = function(time, m) {
    
};
```

### TypeScript

```typescript
function minTime(time: number[], m: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $time
     * @param Integer $m
     * @return Integer
     */
    function minTime($time, $m) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minTime(_ time: [Int], _ m: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minTime(time: IntArray, m: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minTime(List<int> time, int m) {
    
  }
}
```

### Go

```golang
func minTime(time []int, m int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} time
# @param {Integer} m
# @return {Integer}
def min_time(time, m)
    
end
```

### Scala

```scala
object Solution {
    def minTime(time: Array[Int], m: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_time(time: Vec<i32>, m: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-time time m)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_time(Time :: [integer()], M :: integer()) -> integer().
min_time(Time, M) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_time(time :: [integer], m :: integer) :: integer
  def min_time(time, m) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minTime(time: Array<Int64>, m: Int64): Int64 {

    }
}
```

