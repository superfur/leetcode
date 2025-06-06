# 1904. 你完成的完整对局数

## 题目描述

<p>一款新的在线电子游戏在近期发布，在该电子游戏中，以 <strong>刻钟</strong> 为周期规划若干时长为 <strong>15 分钟</strong> 的游戏对局。这意味着，在 <code>HH:00</code>、<code>HH:15</code>、<code>HH:30</code> 和 <code>HH:45</code> ，将会开始一个新的对局，其中 <code>HH</code> 用一个从 <code>00</code> 到 <code>23</code> 的整数表示。游戏中使用 <strong>24 小时制的时钟</strong> ，所以一天中最早的时间是 <code>00:00</code> ，最晚的时间是 <code>23:59</code> 。</p>

<p>给你两个字符串 <code>startTime</code> 和 <code>finishTime</code> ，均符合 <code>"HH:MM"</code> 格式，分别表示你 <strong>进入</strong> 和 <strong>退出</strong> 游戏的确切时间，请计算在整个游戏会话期间，你完成的 <strong>完整对局的对局数</strong> 。</p>

<ul>
	<li>例如，如果 <code>startTime = "05:20"</code> 且 <code>finishTime = "05:59"</code> ，这意味着你仅仅完成从 <code>05:30</code> 到 <code>05:45</code> 这一个完整对局。而你没有完成从 <code>05:15</code> 到 <code>05:30</code> 的完整对局，因为你是在对局开始后进入的游戏；同时，你也没有完成从 <code>05:45</code> 到 <code>06:00</code> 的完整对局，因为你是在对局结束前退出的游戏。</li>
</ul>

<p>如果 <code>finishTime</code> <strong>早于</strong> <code>startTime</code> ，这表示你玩了个通宵（也就是从 <code>startTime</code> 到午夜，再从午夜到 <code>finishTime</code>）。</p>

<p>假设你是从 <code>startTime</code> 进入游戏，并在 <code>finishTime</code> 退出游戏，请计算并返回你完成的 <strong>完整对局的对局数</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>startTime = "12:01", finishTime = "12:44"
<strong>输出：</strong>1
<strong>解释：</strong>你完成了从 12:15 到 12:30 的一个完整对局。
你没有完成从 12:00 到 12:15 的完整对局，因为你是在对局开始后的 12:01 进入的游戏。
你没有完成从 12:30 到 12:45 的完整对局，因为你是在对局结束前的 12:44 退出的游戏。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>startTime = "20:00", finishTime = "06:00"
<strong>输出：</strong>40
<strong>解释：</strong>你完成了从 20:00 到 00:00 的 16 个完整的对局，以及从 00:00 到 06:00 的 24 个完整的对局。
16 + 24 = 40
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>startTime = "00:00", finishTime = "23:59"
<strong>输出：</strong>95
<strong>解释：</strong>除最后一个小时你只完成了 3 个完整对局外，其余每个小时均完成了 4 场完整对局。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>startTime</code> 和 <code>finishTime</code> 的格式为 <code>HH:MM</code></li>
	<li><code>00 <= HH <= 23</code></li>
	<li><code>00 <= MM <= 59</code></li>
	<li><code>startTime</code> 和 <code>finishTime</code> 不相等</li>
</ul>


## 难度

Medium

## 标签

- 数学
- 字符串

## 提示

1. Consider the day as 48 hours instead of 24.
2. For each round check if you were playing.

## 示例

```
"09:31"
"10:14"
"21:30"
"03:00"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfRounds(string loginTime, string logoutTime) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfRounds(String loginTime, String logoutTime) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfRounds(self, loginTime, logoutTime):
        """
        :type loginTime: str
        :type logoutTime: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        
```

### C

```c
int numberOfRounds(char* loginTime, char* logoutTime) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfRounds(string loginTime, string logoutTime) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} loginTime
 * @param {string} logoutTime
 * @return {number}
 */
var numberOfRounds = function(loginTime, logoutTime) {
    
};
```

### TypeScript

```typescript
function numberOfRounds(loginTime: string, logoutTime: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $loginTime
     * @param String $logoutTime
     * @return Integer
     */
    function numberOfRounds($loginTime, $logoutTime) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfRounds(_ loginTime: String, _ logoutTime: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfRounds(loginTime: String, logoutTime: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfRounds(String loginTime, String logoutTime) {
    
  }
}
```

### Go

```golang
func numberOfRounds(loginTime string, logoutTime string) int {
    
}
```

### Ruby

```ruby
# @param {String} login_time
# @param {String} logout_time
# @return {Integer}
def number_of_rounds(login_time, logout_time)
    
end
```

### Scala

```scala
object Solution {
    def numberOfRounds(loginTime: String, logoutTime: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_rounds(login_time: String, logout_time: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-rounds loginTime logoutTime)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_rounds(LoginTime :: unicode:unicode_binary(), LogoutTime :: unicode:unicode_binary()) -> integer().
number_of_rounds(LoginTime, LogoutTime) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_rounds(login_time :: String.t, logout_time :: String.t) :: integer
  def number_of_rounds(login_time, logout_time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfRounds(loginTime: String, logoutTime: String): Int64 {

    }
}
```

