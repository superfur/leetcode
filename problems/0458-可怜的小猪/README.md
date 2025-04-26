# 458. 可怜的小猪

## 题目描述

<p>有<code> buckets</code> 桶液体，其中 <strong>正好有一桶</strong>&nbsp;含有毒药，其余装的都是水。它们从外观看起来都一样。为了弄清楚哪只水桶含有毒药，你可以喂一些猪喝，通过观察猪是否会死进行判断。不幸的是，你只有&nbsp;<code>minutesToTest</code> 分钟时间来确定哪桶液体是有毒的。</p>

<p>喂猪的规则如下：</p>

<ol>
	<li>选择若干活猪进行喂养</li>
	<li>可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。</li>
	<li>小猪喝完水后，必须有 <code>minutesToDie</code> 分钟的冷却时间。在这段时间里，你只能观察，而不允许继续喂猪。</li>
	<li>过了 <code>minutesToDie</code> 分钟后，所有喝到毒药的猪都会死去，其他所有猪都会活下来。</li>
	<li>重复这一过程，直到时间用完。</li>
</ol>

<p>给你桶的数目 <code>buckets</code> ，<code>minutesToDie</code> 和 <code>minutesToTest</code> ，返回&nbsp;<em>在规定时间内判断哪个桶有毒所需的 <strong>最小</strong> 猪数</em>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>buckets = 1000, minutesToDie = 15, minutesToTest = 60
<strong>输出：</strong>5
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>buckets = 4, minutesToDie = 15, minutesToTest = 15
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>buckets = 4, minutesToDie = 15, minutesToTest = 30
<strong>输出：</strong>2
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= buckets &lt;= 1000</code></li>
	<li><code>1 &lt;=&nbsp;minutesToDie &lt;=&nbsp;minutesToTest &lt;= 100</code></li>
</ul>


## 难度

Hard

## 标签

- 数学
- 动态规划
- 组合数学

## 提示

1. What if you only have one shot? Eg. 4 buckets, 15 mins to die, and 15 mins to test.
2. How many states can we generate with x pigs and T tests?
3. Find minimum <code>x</code> such that <code>(T+1)^x >= N</code>

## 示例

```
4
15
15
4
15
30
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        
    }
};
```

### Java

```java
class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        
    }
}
```

### Python

```python
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        
```

### C

```c
int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
    
}
```

### C#

```csharp
public class Solution {
    public int PoorPigs(int buckets, int minutesToDie, int minutesToTest) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} buckets
 * @param {number} minutesToDie
 * @param {number} minutesToTest
 * @return {number}
 */
var poorPigs = function(buckets, minutesToDie, minutesToTest) {
    
};
```

### TypeScript

```typescript
function poorPigs(buckets: number, minutesToDie: number, minutesToTest: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $buckets
     * @param Integer $minutesToDie
     * @param Integer $minutesToTest
     * @return Integer
     */
    function poorPigs($buckets, $minutesToDie, $minutesToTest) {
        
    }
}
```

### Swift

```swift
class Solution {
    func poorPigs(_ buckets: Int, _ minutesToDie: Int, _ minutesToTest: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun poorPigs(buckets: Int, minutesToDie: Int, minutesToTest: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
    
  }
}
```

### Go

```golang
func poorPigs(buckets int, minutesToDie int, minutesToTest int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} buckets
# @param {Integer} minutes_to_die
# @param {Integer} minutes_to_test
# @return {Integer}
def poor_pigs(buckets, minutes_to_die, minutes_to_test)
    
end
```

### Scala

```scala
object Solution {
    def poorPigs(buckets: Int, minutesToDie: Int, minutesToTest: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn poor_pigs(buckets: i32, minutes_to_die: i32, minutes_to_test: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (poor-pigs buckets minutesToDie minutesToTest)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec poor_pigs(Buckets :: integer(), MinutesToDie :: integer(), MinutesToTest :: integer()) -> integer().
poor_pigs(Buckets, MinutesToDie, MinutesToTest) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec poor_pigs(buckets :: integer, minutes_to_die :: integer, minutes_to_test :: integer) :: integer
  def poor_pigs(buckets, minutes_to_die, minutes_to_test) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func poorPigs(buckets: Int64, minutesToDie: Int64, minutesToTest: Int64): Int64 {

    }
}
```

