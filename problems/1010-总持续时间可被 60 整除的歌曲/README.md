# 1010. 总持续时间可被 60 整除的歌曲

## 题目描述

<p>在歌曲列表中，第 <code>i</code> 首歌曲的持续时间为 <code>time[i]</code> 秒。</p>

<p>返回其总持续时间（以秒为单位）可被 <code>60</code> 整除的歌曲对的数量。形式上，我们希望下标数字 <code>i</code> 和 <code>j</code> 满足&nbsp; <code>i &lt; j</code> 且有&nbsp;<code>(time[i] + time[j]) % 60 == 0</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>time = [30,20,150,100,40]
<strong>输出：</strong>3
<strong>解释：</strong>这三对的总持续时间可被 60 整除：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>time = [60,60,60]
<strong>输出：</strong>3
<strong>解释：</strong>所有三对的总持续时间都是 120，可以被 60 整除。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= time.length &lt;= 6 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= time[i] &lt;= 500</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. We only need to consider each song length modulo 60.
2. We can count the number of songs having same (length % 60), and store that in an array of size 60.

## 示例

```
[30,20,150,100,40]
[60,60,60]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        
    }
};
```

### Java

```java
class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
```

### C

```c
int numPairsDivisibleBy60(int* time, int timeSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumPairsDivisibleBy60(int[] time) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} time
 * @return {number}
 */
var numPairsDivisibleBy60 = function(time) {
    
};
```

### TypeScript

```typescript
function numPairsDivisibleBy60(time: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $time
     * @return Integer
     */
    function numPairsDivisibleBy60($time) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numPairsDivisibleBy60(_ time: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numPairsDivisibleBy60(time: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numPairsDivisibleBy60(List<int> time) {
    
  }
}
```

### Go

```golang
func numPairsDivisibleBy60(time []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} time
# @return {Integer}
def num_pairs_divisible_by60(time)
    
end
```

### Scala

```scala
object Solution {
    def numPairsDivisibleBy60(time: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn num_pairs_divisible_by60(time: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (num-pairs-divisible-by60 time)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec num_pairs_divisible_by60(Time :: [integer()]) -> integer().
num_pairs_divisible_by60(Time) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec num_pairs_divisible_by60(time :: [integer]) :: integer
  def num_pairs_divisible_by60(time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numPairsDivisibleBy60(time: Array<Int64>): Int64 {

    }
}
```

