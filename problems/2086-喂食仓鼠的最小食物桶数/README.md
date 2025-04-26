# 2086. 喂食仓鼠的最小食物桶数

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的字符串&nbsp;<code>hamsters</code>&nbsp;，其中&nbsp;<code>hamsters[i]</code>&nbsp; 要么是：</p>

<ul>
	<li><code>'H'</code>&nbsp;表示有一个仓鼠在下标&nbsp;<code>i</code>&nbsp;，或者</li>
	<li><code>'.'</code>&nbsp;表示下标&nbsp;<code>i</code>&nbsp;是空的。</li>
</ul>

<p>你将要在空的位置上添加一定数量的食物桶来喂养仓鼠。如果仓鼠的左边或右边至少有一个食物桶，就可以喂食它。更正式地说，如果你在位置&nbsp;<code>i - 1</code>&nbsp;<strong>或者</strong> <code>i + 1</code>&nbsp;放置一个食物桶，就可以喂养位置为 <code>i</code>&nbsp;处的仓鼠。</p>

<p>在 <strong>空的位置</strong> 放置食物桶以喂养所有仓鼠的前提下，请你返回需要的 <strong>最少</strong>&nbsp;食物桶数。如果无解请返回 <code>-1</code>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><strong><img alt="" src="https://pic.leetcode.cn/1710141378-bfEGUX-image.png" style="width: 482px; height: 162px;" /></strong></p>

<pre>
<b>输入：</b>hamsters = "H..H"
<b>输出：</b>2
<strong>解释：</strong>
我们可以在下标为 1 和 2 处放食物桶。
可以发现如果我们只放置 1 个食物桶，其中一只仓鼠将得不到喂养。
</pre>

<p><strong>示例 2：</strong></p>

<p><strong><img alt="" src="https://pic.leetcode.cn/1710141384-oLAScv-image.png" style="width: 602px; height: 162px;" /></strong></p>

<pre>
<b>输入：</b>street = ".H.H."
<b>输出：</b>1
<strong>解释：</strong>
我们可以在下标为 2 处放置一个食物桶。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>street = ".HHH."
<b>输出：</b>-1
<strong>解释：</strong>
如果我们如图那样在每个空位放置食物桶，下标 2 处的仓鼠将吃不到食物。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= hamsters.length &lt;= 10<sup>5</sup></code></li>
	<li><code>hamsters[i]</code>&nbsp;要么是&nbsp;<code>'H'</code>&nbsp;，要么是&nbsp;<code>'.'</code> 。</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 字符串
- 动态规划

## 提示

1. When is it impossible to feed all the hamsters?
2. When one or more hamsters do not have an empty space adjacent to it.
3. Assuming all previous hamsters are fed. If there is a hamster at index i and you are able to place a bucket at index i - 1 or i + 1, where should you put it?
4. It is always better to place a bucket at index i + 1 because it can feed the next hamster as well.

## 示例

```
"H..H"
".H.H."
".HHH."
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumBuckets(string hamsters) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumBuckets(String hamsters) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumBuckets(self, hamsters):
        """
        :type hamsters: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        
```

### C

```c
int minimumBuckets(char* hamsters) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumBuckets(string hamsters) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} hamsters
 * @return {number}
 */
var minimumBuckets = function(hamsters) {
    
};
```

### TypeScript

```typescript
function minimumBuckets(hamsters: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $hamsters
     * @return Integer
     */
    function minimumBuckets($hamsters) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumBuckets(_ hamsters: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumBuckets(hamsters: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumBuckets(String hamsters) {
    
  }
}
```

### Go

```golang
func minimumBuckets(hamsters string) int {
    
}
```

### Ruby

```ruby
# @param {String} hamsters
# @return {Integer}
def minimum_buckets(hamsters)
    
end
```

### Scala

```scala
object Solution {
    def minimumBuckets(hamsters: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_buckets(hamsters: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-buckets hamsters)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_buckets(Hamsters :: unicode:unicode_binary()) -> integer().
minimum_buckets(Hamsters) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_buckets(hamsters :: String.t) :: integer
  def minimum_buckets(hamsters) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumBuckets(hamsters: String): Int64 {

    }
}
```

