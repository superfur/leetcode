# 455. 分发饼干

## 题目描述

<p>假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。</p>

<p>对每个孩子 <code>i</code>，都有一个胃口值&nbsp;<code>g[i]</code><sub>，</sub>这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 <code>j</code>，都有一个尺寸 <code>s[j]</code><sub>&nbsp;</sub>。如果 <code>s[j]&nbsp;&gt;= g[i]</code>，我们可以将这个饼干 <code>j</code> 分配给孩子 <code>i</code> ，这个孩子会得到满足。你的目标是满足尽可能多的孩子，并输出这个最大数值。</p>
&nbsp;

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> g = [1,2,3], s = [1,1]
<strong>输出:</strong> 1
<strong>解释:</strong> 
你有三个孩子和两块小饼干，3 个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是 1，你只能让胃口值是 1 的孩子满足。
所以你应该输出 1。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre>
<strong>输入:</strong> g = [1,2], s = [1,2,3]
<strong>输出:</strong> 2
<strong>解释:</strong> 
你有两个孩子和三块小饼干，2 个孩子的胃口值分别是 1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出 2。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= g.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= s.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= g[i], s[j] &lt;=&nbsp;2<sup>31</sup> - 1</code></li>
</ul>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与&nbsp;<a href="https://leetcode.cn/problems/maximum-matching-of-players-with-trainers/">2410. 运动员和训练师的最大匹配数</a>&nbsp;题相同。</p>


## 难度

Easy

## 标签

- 贪心
- 数组
- 双指针
- 排序

## 示例

```
[1,2,3]
[1,1]
[1,2]
[1,2,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        
    }
};
```

### Java

```java
class Solution {
    public int findContentChildren(int[] g, int[] s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
```

### C

```c
int findContentChildren(int* g, int gSize, int* s, int sSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindContentChildren(int[] g, int[] s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s) {
    
};
```

### TypeScript

```typescript
function findContentChildren(g: number[], s: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $g
     * @param Integer[] $s
     * @return Integer
     */
    function findContentChildren($g, $s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findContentChildren(_ g: [Int], _ s: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findContentChildren(g: IntArray, s: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findContentChildren(List<int> g, List<int> s) {
    
  }
}
```

### Go

```golang
func findContentChildren(g []int, s []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} g
# @param {Integer[]} s
# @return {Integer}
def find_content_children(g, s)
    
end
```

### Scala

```scala
object Solution {
    def findContentChildren(g: Array[Int], s: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_content_children(g: Vec<i32>, s: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-content-children g s)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_content_children(G :: [integer()], S :: [integer()]) -> integer().
find_content_children(G, S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_content_children(g :: [integer], s :: [integer]) :: integer
  def find_content_children(g, s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findContentChildren(g: Array<Int64>, s: Array<Int64>): Int64 {

    }
}
```

