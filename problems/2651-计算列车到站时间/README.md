# 2651. 计算列车到站时间

## 题目描述

<p>给你一个正整数 <code>arrivalTime</code> 表示列车正点到站的时间（单位：小时），另给你一个正整数 <code>delayedTime</code> 表示列车延误的小时数。</p>

<p>返回列车实际到站的时间。</p>

<p>注意，该问题中的时间采用 24 小时制。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arrivalTime = 15, delayedTime = 5 
<strong>输出：</strong>20 
<strong>解释：</strong>列车正点到站时间是 15:00 ，延误 5 小时，所以列车实际到站的时间是 15 + 5 = 20（20:00）。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arrivalTime = 13, delayedTime = 11
<strong>输出：</strong>0
<strong>解释：</strong>列车正点到站时间是 13:00 ，延误 11 小时，所以列车实际到站的时间是 13 + 11 = 24（在 24 小时制中表示为 00:00 ，所以返回 0）。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arrivaltime &lt;&nbsp;24</code></li>
	<li><code>1 &lt;= delayedTime &lt;= 24</code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. Use the modulo operator to handle the case when the arrival time plus the delayed time goes beyond 24 hours.
2. If the arrival time plus the delayed time is greater than or equal to 24, you can also subtract 24 to get the time in the 24-hour format.

## 示例

```
15
5
13
11
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        
    }
};
```

### Java

```java
class Solution {
    public int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        
```

### C

```c
int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindDelayedArrivalTime(int arrivalTime, int delayedTime) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} arrivalTime
 * @param {number} delayedTime
 * @return {number}
 */
var findDelayedArrivalTime = function(arrivalTime, delayedTime) {
    
};
```

### TypeScript

```typescript
function findDelayedArrivalTime(arrivalTime: number, delayedTime: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $arrivalTime
     * @param Integer $delayedTime
     * @return Integer
     */
    function findDelayedArrivalTime($arrivalTime, $delayedTime) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findDelayedArrivalTime(_ arrivalTime: Int, _ delayedTime: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findDelayedArrivalTime(arrivalTime: Int, delayedTime: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
    
  }
}
```

### Go

```golang
func findDelayedArrivalTime(arrivalTime int, delayedTime int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} arrival_time
# @param {Integer} delayed_time
# @return {Integer}
def find_delayed_arrival_time(arrival_time, delayed_time)
    
end
```

### Scala

```scala
object Solution {
    def findDelayedArrivalTime(arrivalTime: Int, delayedTime: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_delayed_arrival_time(arrival_time: i32, delayed_time: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-delayed-arrival-time arrivalTime delayedTime)
  (-> exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec find_delayed_arrival_time(ArrivalTime :: integer(), DelayedTime :: integer()) -> integer().
find_delayed_arrival_time(ArrivalTime, DelayedTime) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_delayed_arrival_time(arrival_time :: integer, delayed_time :: integer) :: integer
  def find_delayed_arrival_time(arrival_time, delayed_time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findDelayedArrivalTime(arrivalTime: Int64, delayedTime: Int64): Int64 {

    }
}
```

