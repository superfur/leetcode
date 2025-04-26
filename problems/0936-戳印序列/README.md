# 936. 戳印序列

## 题目描述

<p>你想要用<strong>小写字母</strong>组成一个目标字符串&nbsp;<code>target</code>。&nbsp;</p>

<p>开始的时候，序列由&nbsp;<code>target.length</code>&nbsp;个&nbsp;<code>&#39;?&#39;</code>&nbsp;记号组成。而你有一个小写字母印章&nbsp;<code>stamp</code>。</p>

<p>在每个回合，你可以将印章放在序列上，并将序列中的每个字母替换为印章上的相应字母。你最多可以进行&nbsp;<code>10 * target.length</code>&nbsp; 个回合。</p>

<p>举个例子，如果初始序列为 &quot;?????&quot;，而你的印章 <code>stamp</code>&nbsp;是&nbsp;<code>&quot;abc&quot;</code>，那么在第一回合，你可以得到&nbsp;&quot;abc??&quot;、&quot;?abc?&quot;、&quot;??abc&quot;。（请注意，印章必须完全包含在序列的边界内才能盖下去。）</p>

<p>如果可以印出序列，那么返回一个数组，该数组由每个回合中被印下的最左边字母的索引组成。如果不能印出序列，就返回一个空数组。</p>

<p>例如，如果序列是 &quot;ababc&quot;，印章是 <code>&quot;abc&quot;</code>，那么我们就可以返回与操作&nbsp;&quot;?????&quot; -&gt; &quot;abc??&quot; -&gt; &quot;ababc&quot; 相对应的答案 <code>[0, 2]</code>；</p>

<p>另外，如果可以印出序列，那么需要保证可以在 <code>10 * target.length</code>&nbsp;个回合内完成。任何超过此数字的答案将不被接受。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>stamp = &quot;abc&quot;, target = &quot;ababc&quot;
<strong>输出：</strong>[0,2]
（[1,0,2] 以及其他一些可能的结果也将作为答案被接受）
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>stamp = &quot;abca&quot;, target = &quot;aabcaca&quot;
<strong>输出：</strong>[3,0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= stamp.length &lt;= target.length &lt;= 1000</code></li>
	<li><code>stamp</code> 和&nbsp;<code>target</code>&nbsp;只包含小写字母。</li>
</ol>


## 难度

Hard

## 标签

- 栈
- 贪心
- 队列
- 字符串

## 示例

```
"abc"
"ababc"
"abca"
"aabcaca"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> movesToStamp(string stamp, string target) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] movesToStamp(String stamp, String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def movesToStamp(self, stamp, target):
        """
        :type stamp: str
        :type target: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* movesToStamp(char* stamp, char* target, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MovesToStamp(string stamp, string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} stamp
 * @param {string} target
 * @return {number[]}
 */
var movesToStamp = function(stamp, target) {
    
};
```

### TypeScript

```typescript
function movesToStamp(stamp: string, target: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $stamp
     * @param String $target
     * @return Integer[]
     */
    function movesToStamp($stamp, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func movesToStamp(_ stamp: String, _ target: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun movesToStamp(stamp: String, target: String): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> movesToStamp(String stamp, String target) {
    
  }
}
```

### Go

```golang
func movesToStamp(stamp string, target string) []int {
    
}
```

### Ruby

```ruby
# @param {String} stamp
# @param {String} target
# @return {Integer[]}
def moves_to_stamp(stamp, target)
    
end
```

### Scala

```scala
object Solution {
    def movesToStamp(stamp: String, target: String): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn moves_to_stamp(stamp: String, target: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (moves-to-stamp stamp target)
  (-> string? string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec moves_to_stamp(Stamp :: unicode:unicode_binary(), Target :: unicode:unicode_binary()) -> [integer()].
moves_to_stamp(Stamp, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec moves_to_stamp(stamp :: String.t, target :: String.t) :: [integer]
  def moves_to_stamp(stamp, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func movesToStamp(stamp: String, target: String): Array<Int64> {

    }
}
```

