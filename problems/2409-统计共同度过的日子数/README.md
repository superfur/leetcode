# 2409. 统计共同度过的日子数

## 题目描述

<p>Alice 和 Bob 计划分别去罗马开会。</p>

<p>给你四个字符串&nbsp;<code>arriveAlice</code>&nbsp;，<code>leaveAlice</code>&nbsp;，<code>arriveBob</code>&nbsp;和&nbsp;<code>leaveBob</code>&nbsp;。Alice 会在日期&nbsp;<code>arriveAlice</code>&nbsp;到&nbsp;<code>leaveAlice</code>&nbsp;之间在城市里（<strong>日期为闭区间</strong>），而 Bob 在日期&nbsp;<code>arriveBob</code>&nbsp;到&nbsp;<code>leaveBob</code>&nbsp;之间在城市里（<strong>日期为闭区间</strong>）。每个字符串都包含 5 个字符，格式为&nbsp;<code>"MM-DD"</code>&nbsp;，对应着一个日期的月和日。</p>

<p>请你返回 Alice和 Bob 同时在罗马的天数。</p>

<p>你可以假设所有日期都在 <strong>同一个</strong>&nbsp;自然年，而且 <strong>不是</strong>&nbsp;闰年。每个月份的天数分别为：<code>[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
<b>输出：</b>3
<b>解释：</b>Alice 从 8 月 15 号到 8 月 18 号在罗马。Bob 从 8 月 16 号到 8 月 19 号在罗马，他们同时在罗马的日期为 8 月 16、17 和 18 号。所以答案为 3 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"
<b>输出：</b>0
<b>解释：</b>Alice 和 Bob 没有同时在罗马的日子，所以我们返回 0 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li>所有日期的格式均为&nbsp;<code>"MM-DD"</code>&nbsp;。</li>
	<li>Alice 和 Bob 的到达日期都 <strong>早于或等于</strong> 他们的离开日期。</li>
	<li>题目测试用例所给出的日期均为 <strong>非闰年</strong> 的有效日期。</li>
</ul>


## 难度

Easy

## 标签

- 数学
- 字符串

## 提示

1. For a given day, determine if Alice or Bob or both are in Rome.
2. Brute force all 365 days for both Alice and Bob.

## 示例

```
"08-15"
"08-18"
"08-16"
"08-19"
"10-01"
"10-31"
"11-01"
"12-31"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        
    }
};
```

### Java

```java
class Solution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        """
        :type arriveAlice: str
        :type leaveAlice: str
        :type arriveBob: str
        :type leaveBob: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
```

### C

```c
int countDaysTogether(char* arriveAlice, char* leaveAlice, char* arriveBob, char* leaveBob) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountDaysTogether(string arriveAlice, string leaveAlice, string arriveBob, string leaveBob) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} arriveAlice
 * @param {string} leaveAlice
 * @param {string} arriveBob
 * @param {string} leaveBob
 * @return {number}
 */
var countDaysTogether = function(arriveAlice, leaveAlice, arriveBob, leaveBob) {
    
};
```

### TypeScript

```typescript
function countDaysTogether(arriveAlice: string, leaveAlice: string, arriveBob: string, leaveBob: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $arriveAlice
     * @param String $leaveAlice
     * @param String $arriveBob
     * @param String $leaveBob
     * @return Integer
     */
    function countDaysTogether($arriveAlice, $leaveAlice, $arriveBob, $leaveBob) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countDaysTogether(_ arriveAlice: String, _ leaveAlice: String, _ arriveBob: String, _ leaveBob: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countDaysTogether(arriveAlice: String, leaveAlice: String, arriveBob: String, leaveBob: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
    
  }
}
```

### Go

```golang
func countDaysTogether(arriveAlice string, leaveAlice string, arriveBob string, leaveBob string) int {
    
}
```

### Ruby

```ruby
# @param {String} arrive_alice
# @param {String} leave_alice
# @param {String} arrive_bob
# @param {String} leave_bob
# @return {Integer}
def count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob)
    
end
```

### Scala

```scala
object Solution {
    def countDaysTogether(arriveAlice: String, leaveAlice: String, arriveBob: String, leaveBob: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_days_together(arrive_alice: String, leave_alice: String, arrive_bob: String, leave_bob: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-days-together arriveAlice leaveAlice arriveBob leaveBob)
  (-> string? string? string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec count_days_together(ArriveAlice :: unicode:unicode_binary(), LeaveAlice :: unicode:unicode_binary(), ArriveBob :: unicode:unicode_binary(), LeaveBob :: unicode:unicode_binary()) -> integer().
count_days_together(ArriveAlice, LeaveAlice, ArriveBob, LeaveBob) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_days_together(arrive_alice :: String.t, leave_alice :: String.t, arrive_bob :: String.t, leave_bob :: String.t) :: integer
  def count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countDaysTogether(arriveAlice: String, leaveAlice: String, arriveBob: String, leaveBob: String): Int64 {

    }
}
```

