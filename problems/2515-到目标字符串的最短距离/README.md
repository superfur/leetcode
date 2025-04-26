# 2515. 到目标字符串的最短距离

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的 <strong>环形</strong> 字符串数组 <code>words</code> 和一个字符串 <code>target</code> 。<strong>环形数组</strong> 意味着数组首尾相连。</p>

<ul>
	<li>形式上， <code>words[i]</code> 的下一个元素是 <code>words[(i + 1) % n]</code> ，而 <code>words[i]</code> 的前一个元素是 <code>words[(i - 1 + n) % n]</code> ，其中 <code>n</code> 是 <code>words</code> 的长度。</li>
</ul>

<p>从 <code>startIndex</code> 开始，你一次可以用 <code>1</code> 步移动到下一个或者前一个单词。</p>

<p>返回到达目标字符串 <code>target</code> 所需的最短距离。如果 <code>words</code> 中不存在字符串 <code>target</code> ，返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
<strong>输出：</strong>1
<strong>解释：</strong>从下标 1 开始，可以经由以下步骤到达 "hello" ：
- 向右移动 3 个单位，到达下标 4 。
- 向左移动 2 个单位，到达下标 4 。
- 向右移动 4 个单位，到达下标 0 。
- 向左移动 1 个单位，到达下标 0 。
到达 "hello" 的最短距离是 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
<strong>输出：</strong>1
<strong>解释：</strong>从下标 0 开始，可以经由以下步骤到达 "leetcode" ：
- 向右移动 2 个单位，到达下标 3 。
- 向左移动 1 个单位，到达下标 3 。
到达 "leetcode" 的最短距离是 1 。</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>words = ["i","eat","leetcode"], target = "ate", startIndex = 0
<strong>输出：</strong>-1
<strong>解释：</strong>因为 words 中不存在字符串 "ate" ，所以返回 -1 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 100</code></li>
	<li><code>words[i]</code> 和 <code>target</code> 仅由小写英文字母组成</li>
	<li><code>0 &lt;= startIndex &lt; words.length</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 字符串

## 提示

1. You have two options, either move straight to the left or move straight to the right.
2. Find the first target word and record the distance.
3. Choose the one with the minimum distance.

## 示例

```
["hello","i","am","leetcode","hello"]
"hello"
1
["a","b","leetcode"]
"leetcode"
0
["i","eat","leetcode"]
"ate"
0
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int closestTarget(vector<string>& words, string target, int startIndex) {
        
    }
};
```

### Java

```java
class Solution {
    public int closestTarget(String[] words, String target, int startIndex) {
        
    }
}
```

### Python

```python
class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
```

### C

```c
int closestTarget(char** words, int wordsSize, char* target, int startIndex) {
    
}
```

### C#

```csharp
public class Solution {
    public int ClosestTarget(string[] words, string target, int startIndex) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} words
 * @param {string} target
 * @param {number} startIndex
 * @return {number}
 */
var closestTarget = function(words, target, startIndex) {
    
};
```

### TypeScript

```typescript
function closestTarget(words: string[], target: string, startIndex: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $words
     * @param String $target
     * @param Integer $startIndex
     * @return Integer
     */
    function closestTarget($words, $target, $startIndex) {
        
    }
}
```

### Swift

```swift
class Solution {
    func closestTarget(_ words: [String], _ target: String, _ startIndex: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun closestTarget(words: Array<String>, target: String, startIndex: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int closestTarget(List<String> words, String target, int startIndex) {
    
  }
}
```

### Go

```golang
func closestTarget(words []string, target string, startIndex int) int {
    
}
```

### Ruby

```ruby
# @param {String[]} words
# @param {String} target
# @param {Integer} start_index
# @return {Integer}
def closest_target(words, target, start_index)
    
end
```

### Scala

```scala
object Solution {
    def closestTarget(words: Array[String], target: String, startIndex: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn closest_target(words: Vec<String>, target: String, start_index: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (closest-target words target startIndex)
  (-> (listof string?) string? exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec closest_target(Words :: [unicode:unicode_binary()], Target :: unicode:unicode_binary(), StartIndex :: integer()) -> integer().
closest_target(Words, Target, StartIndex) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec closest_target(words :: [String.t], target :: String.t, start_index :: integer) :: integer
  def closest_target(words, target, start_index) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func closestTarget(words: Array<String>, target: String, startIndex: Int64): Int64 {

    }
}
```

