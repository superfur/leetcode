# 691. 贴纸拼词

## 题目描述

<p>我们有 <code>n</code> 种不同的贴纸。每个贴纸上都有一个小写的英文单词。</p>

<p>您想要拼写出给定的字符串 <code>target</code>&nbsp;，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。</p>

<p>返回你需要拼出 <code>target</code>&nbsp;的最小贴纸数量。如果任务不可能，则返回 <code>-1</code> 。</p>

<p><strong>注意：</strong>在所有的测试用例中，所有的单词都是从 <code>1000</code> 个最常见的美国英语单词中随机选择的，并且 <code>target</code>&nbsp;被选择为两个随机单词的连接。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong> stickers = ["with","example","science"], target = "thehat"
<b>输出：</b>3
<strong>解释：
</strong>我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
此外，这是形成目标字符串所需的最小贴纸数量。
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<b>输入：</b>stickers = ["notice","possible"], target = "basicbasic"
<b>输出：</b>-1
<strong>解释：</strong>我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>n == stickers.length</code></li>
	<li><code>1 &lt;= n &lt;= 50</code></li>
	<li><code>1 &lt;= stickers[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= target.length &lt;= 15</code></li>
	<li><code>stickers[i]</code>&nbsp;和&nbsp;<code>target</code>&nbsp;由小写英文单词组成</li>
</ul>


## 难度

Hard

## 标签

- 位运算
- 记忆化搜索
- 数组
- 哈希表
- 字符串
- 动态规划
- 回溯
- 状态压缩

## 提示

1. We want to perform an exhaustive search, but we need to speed it up based on the input data being random.  

For all stickers, we can ignore any letters that are not in the target word.  

When our candidate answer won't be smaller than an answer we have already found, we can stop searching this path.  

When a sticker dominates another, we shouldn't include the dominated sticker in our sticker collection.  [Here, we say a sticker `A` dominates `B` if `A.count(letter) >= B.count(letter)` for all letters.]

## 示例

```
["with","example","science"]
"thehat"
["notice","possible"]
"basicbasic"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minStickers(vector<string>& stickers, string target) {
        
    }
};
```

### Java

```java
class Solution {
    public int minStickers(String[] stickers, String target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
```

### C

```c
int minStickers(char** stickers, int stickersSize, char* target) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinStickers(string[] stickers, string target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} stickers
 * @param {string} target
 * @return {number}
 */
var minStickers = function(stickers, target) {
    
};
```

### TypeScript

```typescript
function minStickers(stickers: string[], target: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $stickers
     * @param String $target
     * @return Integer
     */
    function minStickers($stickers, $target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minStickers(_ stickers: [String], _ target: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minStickers(stickers: Array<String>, target: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minStickers(List<String> stickers, String target) {
    
  }
}
```

### Go

```golang
func minStickers(stickers []string, target string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} stickers
# @param {String} target
# @return {Integer}
def min_stickers(stickers, target)
    
end
```

### Scala

```scala
object Solution {
    def minStickers(stickers: Array[String], target: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_stickers(stickers: Vec<String>, target: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-stickers stickers target)
  (-> (listof string?) string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_stickers(Stickers :: [unicode:unicode_binary()], Target :: unicode:unicode_binary()) -> integer().
min_stickers(Stickers, Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_stickers(stickers :: [String.t], target :: String.t) :: integer
  def min_stickers(stickers, target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minStickers(stickers: Array<String>, target: String): Int64 {

    }
}
```

