# 1520. 最多的不重叠子字符串

## 题目描述

<p>给你一个只包含小写字母的字符串&nbsp;<code>s</code>&nbsp;，你需要找到 <code>s</code>&nbsp;中最多数目的非空子字符串，满足如下条件：</p>

<ol>
	<li>这些字符串之间互不重叠，也就是说对于任意两个子字符串&nbsp;<code>s[i..j]</code> 和&nbsp;<code>s[x..y]</code>&nbsp;，要么&nbsp;<code>j &lt; x</code>&nbsp;要么&nbsp;<code>i &gt; y</code>&nbsp;。</li>
	<li>如果一个子字符串包含字符&nbsp;<code>char</code> ，那么&nbsp;<code>s</code>&nbsp;中所有&nbsp;<code>char</code> 字符都应该在这个子字符串中。</li>
</ol>

<p>请你找到满足上述条件的最多子字符串数目。如果有多个解法有相同的子字符串数目，请返回这些子字符串总长度最小的一个解。可以证明最小总长度解是唯一的。</p>

<p>请注意，你可以以 <strong>任意</strong>&nbsp;顺序返回最优解的子字符串。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "adefaddaccc"
<strong>输出：</strong>["e","f","ccc"]
<strong>解释：</strong>下面为所有满足第二个条件的子字符串：
[
&nbsp; "adefaddaccc"
&nbsp; "adefadda",
&nbsp; "ef",
&nbsp; "e",
  "f",
&nbsp; "ccc",
]
如果我们选择第一个字符串，那么我们无法再选择其他任何字符串，所以答案为 1 。如果我们选择 "adefadda" ，剩下子字符串中我们只可以选择 "ccc" ，它是唯一不重叠的子字符串，所以答案为 2 。同时我们可以发现，选择 "ef" 不是最优的，因为它可以被拆分成 2 个子字符串。所以最优解是选择 ["e","f","ccc"] ，答案为 3 。不存在别的相同数目子字符串解。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abbaccd"
<strong>输出：</strong>["d","bb","cc"]
<strong>解释：</strong>注意到解 ["d","abba","cc"] 答案也为 3 ，但它不是最优解，因为它的总长度更长。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10^5</code></li>
	<li><code>s</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Hard

## 标签

- 贪心
- 字符串

## 提示

1. Notice that it's impossible for any two valid substrings to overlap unless one is inside another.
2. We can start by finding the starting and ending index for each character.
3. From these indices, we can form the substrings by expanding each character's range if necessary (if another character exists in the range with smaller/larger starting/ending index).
4. Sort the valid substrings by length and greedily take those with the smallest length, discarding the ones that overlap those we took.

## 示例

```
"adefaddaccc"
"abbaccd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> maxNumOfSubstrings(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> maxNumOfSubstrings(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** maxNumOfSubstrings(char* s, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> MaxNumOfSubstrings(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {string[]}
 */
var maxNumOfSubstrings = function(s) {
    
};
```

### TypeScript

```typescript
function maxNumOfSubstrings(s: string): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return String[]
     */
    function maxNumOfSubstrings($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxNumOfSubstrings(_ s: String) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxNumOfSubstrings(s: String): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> maxNumOfSubstrings(String s) {
    
  }
}
```

### Go

```golang
func maxNumOfSubstrings(s string) []string {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {String[]}
def max_num_of_substrings(s)
    
end
```

### Scala

```scala
object Solution {
    def maxNumOfSubstrings(s: String): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_num_of_substrings(s: String) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (max-num-of-substrings s)
  (-> string? (listof string?))
  )
```

### Erlang

```erlang
-spec max_num_of_substrings(S :: unicode:unicode_binary()) -> [unicode:unicode_binary()].
max_num_of_substrings(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_num_of_substrings(s :: String.t) :: [String.t]
  def max_num_of_substrings(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxNumOfSubstrings(s: String): ArrayList<String> {

    }
}
```

