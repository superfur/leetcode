# 2327. 知道秘密的人数

## 题目描述

<p>在第 <code>1</code>&nbsp;天，有一个人发现了一个秘密。</p>

<p>给你一个整数&nbsp;<code>delay</code>&nbsp;，表示每个人会在发现秘密后的 <code>delay</code>&nbsp;天之后，<strong>每天</strong>&nbsp;给一个新的人&nbsp;<strong>分享</strong>&nbsp;秘密。同时给你一个整数&nbsp;<code>forget</code>&nbsp;，表示每个人在发现秘密&nbsp;<code>forget</code>&nbsp;天之后会&nbsp;<strong>忘记</strong>&nbsp;这个秘密。一个人&nbsp;<strong>不能</strong>&nbsp;在忘记秘密那一天及之后的日子里分享秘密。</p>

<p>给你一个整数&nbsp;<code>n</code>&nbsp;，请你返回在第 <code>n</code>&nbsp;天结束时，知道秘密的人数。由于答案可能会很大，请你将结果对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>n = 6, delay = 2, forget = 4
<b>输出：</b>5
<strong>解释：</strong>
第 1 天：假设第一个人叫 A 。（一个人知道秘密）
第 2 天：A 是唯一一个知道秘密的人。（一个人知道秘密）
第 3 天：A 把秘密分享给 B 。（两个人知道秘密）
第 4 天：A 把秘密分享给一个新的人 C 。（三个人知道秘密）
第 5 天：A 忘记了秘密，B 把秘密分享给一个新的人 D 。（三个人知道秘密）
第 6 天：B 把秘密分享给 E，C 把秘密分享给 F 。（五个人知道秘密）
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 4, delay = 1, forget = 3
<b>输出：</b>6
<strong>解释：</strong>
第 1 天：第一个知道秘密的人为 A 。（一个人知道秘密）
第 2 天：A 把秘密分享给 B 。（两个人知道秘密）
第 3 天：A 和 B 把秘密分享给 2 个新的人 C 和 D 。（四个人知道秘密）
第 4 天：A 忘记了秘密，B、C、D 分别分享给 3 个新的人。（六个人知道秘密）
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
	<li><code>1 &lt;= delay &lt; forget &lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 队列
- 动态规划
- 模拟

## 提示

1. Let dp[i][j] be the number of people who have known the secret for exactly j + 1 days, at day i.
2. If j > 0, dp[i][j] = dp[i – 1][j – 1].
3. dp[i][0] = sum(dp[i – 1][j]) for j in [delay – 1, forget – 2].

## 示例

```
6
2
4
4
1
3
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int peopleAwareOfSecret(int n, int delay, int forget) {
        
    }
};
```

### Java

```java
class Solution {
    public int peopleAwareOfSecret(int n, int delay, int forget) {
        
    }
}
```

### Python

```python
class Solution(object):
    def peopleAwareOfSecret(self, n, delay, forget):
        """
        :type n: int
        :type delay: int
        :type forget: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        
```

### C

```c
int peopleAwareOfSecret(int n, int delay, int forget) {
    
}
```

### C#

```csharp
public class Solution {
    public int PeopleAwareOfSecret(int n, int delay, int forget) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} delay
 * @param {number} forget
 * @return {number}
 */
var peopleAwareOfSecret = function(n, delay, forget) {
    
};
```

### TypeScript

```typescript
function peopleAwareOfSecret(n: number, delay: number, forget: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $delay
     * @param Integer $forget
     * @return Integer
     */
    function peopleAwareOfSecret($n, $delay, $forget) {
        
    }
}
```

### Swift

```swift
class Solution {
    func peopleAwareOfSecret(_ n: Int, _ delay: Int, _ forget: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun peopleAwareOfSecret(n: Int, delay: Int, forget: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int peopleAwareOfSecret(int n, int delay, int forget) {
    
  }
}
```

### Go

```golang
func peopleAwareOfSecret(n int, delay int, forget int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} delay
# @param {Integer} forget
# @return {Integer}
def people_aware_of_secret(n, delay, forget)
    
end
```

### Scala

```scala
object Solution {
    def peopleAwareOfSecret(n: Int, delay: Int, forget: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn people_aware_of_secret(n: i32, delay: i32, forget: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (people-aware-of-secret n delay forget)
  (-> exact-integer? exact-integer? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec people_aware_of_secret(N :: integer(), Delay :: integer(), Forget :: integer()) -> integer().
people_aware_of_secret(N, Delay, Forget) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec people_aware_of_secret(n :: integer, delay :: integer, forget :: integer) :: integer
  def people_aware_of_secret(n, delay, forget) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func peopleAwareOfSecret(n: Int64, delay: Int64, forget: Int64): Int64 {

    }
}
```

