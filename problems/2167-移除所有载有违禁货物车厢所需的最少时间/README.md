# 2167. 移除所有载有违禁货物车厢所需的最少时间

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的二进制字符串 <code>s</code> ，表示一个列车车厢序列。<code>s[i] = '0'</code> 表示第 <code>i</code> 节车厢 <strong>不</strong> 含违禁货物，而 <code>s[i] = '1'</code> 表示第 <code>i</code> 节车厢含违禁货物。</p>

<p>作为列车长，你需要清理掉所有载有违禁货物的车厢。你可以不限次数执行下述三种操作中的任意一个：</p>

<ol>
	<li>从列车 <strong>左</strong> 端移除一节车厢（即移除 <code>s[0]</code>），用去 1 单位时间。</li>
	<li>从列车 <strong>右</strong> 端移除一节车厢（即移除 <code>s[s.length - 1]</code>），用去 1 单位时间。</li>
	<li>从列车车厢序列的 <strong>任意位置</strong> 移除一节车厢，用去 2 单位时间。</li>
</ol>

<p>返回移除所有载有违禁货物车厢所需要的 <strong>最少</strong> 单位时间数。</p>

<p>注意，空的列车车厢序列视为没有车厢含违禁货物。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "<em><strong>11</strong></em>00<em><strong>1</strong></em>0<em><strong>1</strong></em>"
<strong>输出：</strong>5
<strong>解释：</strong>
一种从序列中移除所有载有违禁货物的车厢的方法是：
- 从左端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
- 从右端移除一节车厢 1 次。所用时间是 1 。
- 移除序列中间位置载有违禁货物的车厢。所用时间是 2 。
总时间是 2 + 1 + 2 = 5 。

一种替代方法是：
- 从左端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
- 从右端移除一节车厢 3 次。所用时间是 3 * 1 = 3 。
总时间也是 2 + 3 = 5 。

5 是移除所有载有违禁货物的车厢所需要的最少单位时间数。
没有其他方法能够用更少的时间移除这些车厢。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "00<em><strong>1</strong></em>0"
<strong>输出：</strong>2
<strong>解释：</strong>
一种从序列中移除所有载有违禁货物的车厢的方法是：
- 从左端移除一节车厢 3 次。所用时间是 3 * 1 = 3 。
总时间是 3.

另一种从序列中移除所有载有违禁货物的车厢的方法是：
- 移除序列中间位置载有违禁货物的车厢。所用时间是 2 。
总时间是 2.

另一种从序列中移除所有载有违禁货物的车厢的方法是：
- 从右端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
总时间是 2.

2 是移除所有载有违禁货物的车厢所需要的最少单位时间数。
没有其他方法能够用更少的时间移除这些车厢。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s[i]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. Build an array withoutFirst where withoutFirst[i] stores the minimum time to remove all the cars containing illegal goods from the ‘suffix’ of the sequence starting from the ith car without using any type 1 operations.
2. Next, build an array onlyFirst where onlyFirst[i] stores the minimum time to remove all the cars containing illegal goods from the ‘prefix’ of the sequence ending on the ith car using only type 1 operations.
3. Finally, we can compare the best way to split the operations amongst these two types by finding the minimum time across all onlyFirst[i] + withoutFirst[i + 1].

## 示例

```
"1100101"
"0010"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumTime(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumTime(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumTime(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumTime(self, s: str) -> int:
        
```

### C

```c
int minimumTime(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumTime(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumTime = function(s) {
    
};
```

### TypeScript

```typescript
function minimumTime(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumTime($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumTime(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumTime(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumTime(String s) {
    
  }
}
```

### Go

```golang
func minimumTime(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def minimum_time(s)
    
end
```

### Scala

```scala
object Solution {
    def minimumTime(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_time(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-time s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_time(S :: unicode:unicode_binary()) -> integer().
minimum_time(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_time(s :: String.t) :: integer
  def minimum_time(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumTime(s: String): Int64 {

    }
}
```

