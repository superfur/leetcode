# 830. 较大分组的位置

## 题目描述

<p>在一个由小写字母构成的字符串 <code>s</code> 中，包含由一些连续的相同字符所构成的分组。</p>

<p>例如，在字符串 <code>s = "abbxxxxzyy"</code> 中，就含有 <code>"a"</code>, <code>"bb"</code>, <code>"xxxx"</code>, <code>"z"</code> 和 <code>"yy"</code> 这样的一些分组。</p>

<p>分组可以用区间 <code>[start, end]</code> 表示，其中 <code>start</code> 和 <code>end</code> 分别表示该分组的起始和终止位置的下标。上例中的 <code>"xxxx"</code> 分组用区间表示为 <code>[3,6]</code> 。</p>

<p>我们称所有包含大于或等于三个连续字符的分组为 <strong>较大分组</strong> 。</p>

<p>找到每一个 <strong>较大分组</strong> 的区间，<strong>按起始位置下标递增顺序排序后</strong>，返回结果。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "abbxxxxzzy"
<strong>输出：</strong>[[3,6]]
<strong>解释</strong><strong>：</strong><code>"xxxx" 是一个起始于 3 且终止于 6 的较大分组</code>。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "abc"
<strong>输出：</strong>[]
<strong>解释：</strong>"a","b" 和 "c" 均不是符合要求的较大分组。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>s = "abcdddeeeeaabbbcd"
<strong>输出：</strong>[[3,5],[6,9],[12,14]]
<strong>解释：</strong>较大分组为 "ddd", "eeee" 和 "bbb"</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>s = "aba"
<strong>输出：</strong>[]
</pre>
 

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length <= 1000</code></li>
	<li><code>s</code> 仅含小写英文字母</li>
</ul>


## 难度

Easy

## 标签

- 字符串

## 示例

```
"abbxxxxzzy"
"abc"
"abcdddeeeeaabbbcd"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> largeGroupPositions(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public List<List<Integer>> largeGroupPositions(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** largeGroupPositions(char* s, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<IList<int>> LargeGroupPositions(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number[][]}
 */
var largeGroupPositions = function(s) {
    
};
```

### TypeScript

```typescript
function largeGroupPositions(s: string): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer[][]
     */
    function largeGroupPositions($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largeGroupPositions(_ s: String) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largeGroupPositions(s: String): List<List<Int>> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> largeGroupPositions(String s) {
    
  }
}
```

### Go

```golang
func largeGroupPositions(s string) [][]int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer[][]}
def large_group_positions(s)
    
end
```

### Scala

```scala
object Solution {
    def largeGroupPositions(s: String): List[List[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn large_group_positions(s: String) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (large-group-positions s)
  (-> string? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec large_group_positions(S :: unicode:unicode_binary()) -> [[integer()]].
large_group_positions(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec large_group_positions(s :: String.t) :: [[integer]]
  def large_group_positions(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largeGroupPositions(s: String): ArrayList<ArrayList<Int64>> {

    }
}
```

