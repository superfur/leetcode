# 2483. 商店的最少代价

## 题目描述

<p>给你一个顾客访问商店的日志，用一个下标从 <strong>0</strong>&nbsp;开始且只包含字符&nbsp;<code>'N'</code> 和&nbsp;<code>'Y'</code>&nbsp;的字符串&nbsp;<code>customers</code>&nbsp;表示：</p>

<ul>
	<li>如果第&nbsp;<code>i</code>&nbsp;个字符是&nbsp;<code>'Y'</code>&nbsp;，它表示第&nbsp;<code>i</code>&nbsp;小时有顾客到达。</li>
	<li>如果第&nbsp;<code>i</code>&nbsp;个字符是&nbsp;<code>'N'</code>&nbsp;，它表示第 <code>i</code>&nbsp;小时没有顾客到达。</li>
</ul>

<p>如果商店在第&nbsp;<code>j</code>&nbsp;小时关门（<code>0 &lt;= j &lt;= n</code>），代价按如下方式计算：</p>

<ul>
	<li>在开门期间，如果某一个小时没有顾客到达，代价增加 <code>1</code>&nbsp;。</li>
	<li>在关门期间，如果某一个小时有顾客到达，代价增加&nbsp;<code>1</code>&nbsp;。</li>
</ul>

<p>请你返回在确保代价 <strong>最小</strong>&nbsp;的前提下，商店的&nbsp;<strong>最早</strong>&nbsp;关门时间。</p>

<p>注意，商店在第 <code>j</code>&nbsp;小时关门表示在第 <code>j</code> 小时以及之后商店处于关门状态。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>customers = "YYNY"
<b>输出：</b>2
<b>解释：</b>
- 第 0 小时关门，总共 1+1+0+1 = 3 代价。
- 第 1 小时关门，总共 0+1+0+1 = 2 代价。
- 第 2 小时关门，总共 0+0+0+1 = 1 代价。
- 第 3 小时关门，总共 0+0+1+1 = 2 代价。
- 第 4 小时关门，总共 0+0+1+0 = 1 代价。
在第 2 或第 4 小时关门代价都最小。由于第 2 小时更早，所以最优关门时间是 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>customers = "NNNNN"
<b>输出：</b>0
<b>解释：</b>最优关门时间是 0 ，因为自始至终没有顾客到达。</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>customers = "YYYY"
<b>输出：</b>4
<b>解释：</b>最优关门时间是 4 ，因为每一小时均有顾客到达。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= customers.length &lt;= 10<sup>5</sup></code></li>
	<li><code>customers</code>&nbsp;只包含字符&nbsp;<code>'Y'</code>&nbsp;和&nbsp;<code>'N'</code>&nbsp;。</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 前缀和

## 提示

1. At any index, the penalty is the sum of prefix count of ‘N’ and suffix count of ‘Y’.
2. Enumerate all indices and find the minimum such value.

## 示例

```
"YYNY"
"NNNNN"
"YYYY"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int bestClosingTime(string customers) {
        
    }
};
```

### Java

```java
class Solution {
    public int bestClosingTime(String customers) {
        
    }
}
```

### Python

```python
class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        
```

### C

```c
int bestClosingTime(char* customers) {
    
}
```

### C#

```csharp
public class Solution {
    public int BestClosingTime(string customers) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} customers
 * @return {number}
 */
var bestClosingTime = function(customers) {
    
};
```

### TypeScript

```typescript
function bestClosingTime(customers: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $customers
     * @return Integer
     */
    function bestClosingTime($customers) {
        
    }
}
```

### Swift

```swift
class Solution {
    func bestClosingTime(_ customers: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun bestClosingTime(customers: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int bestClosingTime(String customers) {
    
  }
}
```

### Go

```golang
func bestClosingTime(customers string) int {
    
}
```

### Ruby

```ruby
# @param {String} customers
# @return {Integer}
def best_closing_time(customers)
    
end
```

### Scala

```scala
object Solution {
    def bestClosingTime(customers: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn best_closing_time(customers: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (best-closing-time customers)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec best_closing_time(Customers :: unicode:unicode_binary()) -> integer().
best_closing_time(Customers) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec best_closing_time(customers :: String.t) :: integer
  def best_closing_time(customers) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func bestClosingTime(customers: String): Int64 {

    }
}
```

