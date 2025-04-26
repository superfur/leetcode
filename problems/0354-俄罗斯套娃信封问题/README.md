# 354. 俄罗斯套娃信封问题

## 题目描述

<p>给你一个二维整数数组 <code>envelopes</code> ，其中 <code>envelopes[i] = [w<sub>i</sub>, h<sub>i</sub>]</code> ，表示第 <code>i</code> 个信封的宽度和高度。</p>

<p>当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。</p>

<p>请计算 <strong>最多能有多少个</strong> 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。</p>

<p><strong>注意</strong>：不允许旋转信封。</p>
&nbsp;

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>envelopes = [[5,4],[6,4],[6,7],[2,3]]
<strong>输出：</strong>3
<strong>解释：</strong>最多信封的个数为 <code>3, 组合为: </code>[2,3] =&gt; [5,4] =&gt; [6,7]。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>envelopes = [[1,1],[1,1],[1,1]]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= envelopes.length &lt;= 10<sup>5</sup></code></li>
	<li><code>envelopes[i].length == 2</code></li>
	<li><code>1 &lt;= w<sub>i</sub>, h<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 二分查找
- 动态规划
- 排序

## 示例

```
[[5,4],[6,4],[6,7],[2,3]]
[[1,1],[1,1],[1,1]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
```

### C

```c
int maxEnvelopes(int** envelopes, int envelopesSize, int* envelopesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxEnvelopes(int[][] envelopes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[][]} envelopes
 * @return {number}
 */
var maxEnvelopes = function(envelopes) {
    
};
```

### TypeScript

```typescript
function maxEnvelopes(envelopes: number[][]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[][] $envelopes
     * @return Integer
     */
    function maxEnvelopes($envelopes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxEnvelopes(_ envelopes: [[Int]]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxEnvelopes(envelopes: Array<IntArray>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxEnvelopes(List<List<int>> envelopes) {
    
  }
}
```

### Go

```golang
func maxEnvelopes(envelopes [][]int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[][]} envelopes
# @return {Integer}
def max_envelopes(envelopes)
    
end
```

### Scala

```scala
object Solution {
    def maxEnvelopes(envelopes: Array[Array[Int]]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_envelopes(envelopes: Vec<Vec<i32>>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-envelopes envelopes)
  (-> (listof (listof exact-integer?)) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_envelopes(Envelopes :: [[integer()]]) -> integer().
max_envelopes(Envelopes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_envelopes(envelopes :: [[integer]]) :: integer
  def max_envelopes(envelopes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxEnvelopes(envelopes: Array<Array<Int64>>): Int64 {

    }
}
```

