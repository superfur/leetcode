# 1320. 二指输入的的最小距离

## 题目描述

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/11/leetcode_keyboard.png" /></p>

<p>二指输入法定制键盘在 <strong>X-Y</strong> 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处。</p>

<ul>
	<li>例如字母&nbsp;<strong>A</strong>&nbsp;位于坐标&nbsp;<strong>(0,0)</strong>，字母&nbsp;<strong>B</strong>&nbsp;位于坐标&nbsp;<strong>(0,1)</strong>，字母&nbsp;<strong>P</strong>&nbsp;位于坐标&nbsp;<strong>(2,3)</strong>&nbsp;且字母 <strong>Z</strong>&nbsp;位于坐标&nbsp;<strong>(4,1)</strong>。</li>
</ul>

<p>给你一个待输入字符串&nbsp;<code>word</code>，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。</p>

<p>坐标<code>&nbsp;<strong>(x<sub>1</sub>,y<sub>1</sub>)</strong> </code>和 <code><strong>(x<sub>2</sub>,y<sub>2</sub>)</strong></code> 之间的 <strong>距离</strong> 是&nbsp;<code><strong>|x<sub>1</sub> - x<sub>2</sub>| + |y<sub>1</sub> - y<sub>2</sub>|</strong></code>。&nbsp;</p>

<p><strong>注意</strong>，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>word = "CAKE"
<strong>输出：</strong>3
<strong>解释： 
</strong>使用两根手指输入 "CAKE" 的最佳方案之一是： 
手指 1 在字母 'C' 上 -&gt; 移动距离 = 0 
手指 1 在字母 'A' 上 -&gt; 移动距离 = 从字母 'C' 到字母 'A' 的距离 = 2 
手指 2 在字母 'K' 上 -&gt; 移动距离 = 0 
手指 2 在字母 'E' 上 -&gt; 移动距离 = 从字母 'K' 到字母 'E' 的距离  = 1 
总距离 = 3
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>word = "HAPPY"
<strong>输出：</strong>6
<strong>解释： </strong>
使用两根手指输入 "HAPPY" 的最佳方案之一是：
手指 1 在字母 'H' 上 -&gt; 移动距离 = 0
手指 1 在字母 'A' 上 -&gt; 移动距离 = 从字母 'H' 到字母 'A' 的距离 = 2
手指 2 在字母 'P' 上 -&gt; 移动距离 = 0
手指 2 在字母 'P' 上 -&gt; 移动距离 = 从字母 'P' 到字母 'P' 的距离 = 0
手指 1 在字母 'Y' 上 -&gt; 移动距离 = 从字母 'A' 到字母 'Y' 的距离 = 4
总距离 = 6
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= word.length &lt;= 300</code></li>
	<li>每个 <code>word[i]</code>&nbsp;都是一个大写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 字符串
- 动态规划

## 提示

1. Use dynamic programming.
2. dp[i][j][k]: smallest movements when you have one finger on i-th char and the other one on j-th char already having written k first characters from word.

## 示例

```
"CAKE"
"HAPPY"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumDistance(string word) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumDistance(String word) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumDistance(self, word: str) -> int:
        
```

### C

```c
int minimumDistance(char* word) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumDistance(string word) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} word
 * @return {number}
 */
var minimumDistance = function(word) {
    
};
```

### TypeScript

```typescript
function minimumDistance(word: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $word
     * @return Integer
     */
    function minimumDistance($word) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumDistance(_ word: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumDistance(word: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumDistance(String word) {
    
  }
}
```

### Go

```golang
func minimumDistance(word string) int {
    
}
```

### Ruby

```ruby
# @param {String} word
# @return {Integer}
def minimum_distance(word)
    
end
```

### Scala

```scala
object Solution {
    def minimumDistance(word: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_distance(word: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-distance word)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_distance(Word :: unicode:unicode_binary()) -> integer().
minimum_distance(Word) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_distance(word :: String.t) :: integer
  def minimum_distance(word) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumDistance(word: String): Int64 {

    }
}
```

