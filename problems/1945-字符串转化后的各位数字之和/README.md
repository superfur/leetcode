# 1945. 字符串转化后的各位数字之和

## 题目描述

<p>给你一个由小写字母组成的字符串 <code>s</code> ，以及一个整数 <code>k</code> 。你的任务是通过一种特殊处理将字符串转为整数，然后通过重复对它的数位求和&nbsp;<code>k</code> 次来进行转换。更具体地说，执行以下步骤：</p>

<ol>
	<li>用字母在字母表中的位置&nbsp;<strong>替换&nbsp;</strong>该字母，将 <code>s</code> <strong>转化</strong> 为一个整数（也就是，<code>'a'</code> 用 <code>1</code> 替换，<code>'b'</code> 用 <code>2</code> 替换，... <code>'z'</code> 用 <code>26</code> 替换）。</li>
	<li>接着，将整数 <strong>转换</strong> 为其 <strong>各位数字之和</strong> 。</li>
	<li>共重复 <strong>转换</strong> 操作（第 2 步）&nbsp;<code>k</code><strong> 次</strong> 。</li>
</ol>

<p>例如，如果 <code>s = "zbax"</code> 且 <code>k = 2</code> ，那么执行下述步骤后得到的结果是整数 <code>8</code> ：</p>

<ul>
	<li><strong>转化：</strong><code>"zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124</code></li>
	<li><strong>转换 #1</strong>：<code>262124&nbsp;➝ 2 + 6 + 2 + 1 + 2 + 4&nbsp;➝ 17</code></li>
	<li><strong>转换 #2</strong>：<code>17 ➝ 1 + 7 ➝ 8</code></li>
</ul>

<p>返回执行上述 <strong>操作</strong> 后得到的 <strong>结果整数</strong>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<div class="example-block"><strong>输入：</strong>s = "iiii", k = 1</div>

<div class="example-block"><strong>输出：</strong>36</div>

<div class="example-block"><strong>解释：</strong></div>

<div class="example-block">操作如下：</div>

<ul>
	<li class="example-block">转化："iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999</li>
	<li class="example-block">转换 #1：9999 ➝ 9 + 9 + 9 + 9 ➝ 36</li>
</ul>

<div class="example-block">因此，结果整数为 36 。</div>

<div class="example-block">&nbsp;</div>

<p><strong>示例 2：</strong></p>

<div class="example-block"><strong>输入：</strong>s = "leetcode", k = 2</div>

<div class="example-block"><strong>输出：</strong>6</div>

<div class="example-block"><strong>解释：</strong></div>

<div class="example-block">操作如下：</div>

<ul>
	<li class="example-block">转化："leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545</li>
	<li class="example-block">转换 #1：12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33</li>
	<li class="example-block">转换 #2：33 ➝ 3 + 3 ➝ 6</li>
</ul>

<p class="example-block">因此，结果整数为 6 。</p>

<p class="example-block">&nbsp;</p>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "zbax", k = 2</span></p>

<p><span class="example-io"><b>输出：</b>8</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10</code></li>
	<li><code>s</code> 由小写英文字母组成</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 模拟

## 提示

1. First, let's note that after the first transform the value will be at most 100 * 10 which is not much
2. After The first transform, we can just do the rest of the transforms by brute force

## 示例

```
"iiii"
1
"leetcode"
2
"zbax"
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int getLucky(string s, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int getLucky(String s, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
```

### C

```c
int getLucky(char* s, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int GetLucky(string s, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLucky = function(s, k) {
    
};
```

### TypeScript

```typescript
function getLucky(s: string, k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @param Integer $k
     * @return Integer
     */
    function getLucky($s, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func getLucky(_ s: String, _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun getLucky(s: String, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int getLucky(String s, int k) {
    
  }
}
```

### Go

```golang
func getLucky(s string, k int) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @param {Integer} k
# @return {Integer}
def get_lucky(s, k)
    
end
```

### Scala

```scala
object Solution {
    def getLucky(s: String, k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn get_lucky(s: String, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (get-lucky s k)
  (-> string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec get_lucky(S :: unicode:unicode_binary(), K :: integer()) -> integer().
get_lucky(S, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec get_lucky(s :: String.t, k :: integer) :: integer
  def get_lucky(s, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func getLucky(s: String, k: Int64): Int64 {

    }
}
```

