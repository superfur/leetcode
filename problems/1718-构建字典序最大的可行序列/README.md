# 1718. 构建字典序最大的可行序列

## 题目描述

<p>给你一个整数 <code>n</code> ，请你找到满足下面条件的一个序列：</p>

<ul>
	<li>整数 <code>1</code> 在序列中只出现一次。</li>
	<li><code>2</code> 到 <code>n</code> 之间每个整数都恰好出现两次。</li>
	<li>对于每个 <code>2</code> 到 <code>n</code> 之间的整数 <code>i</code> ，两个 <code>i</code> 之间出现的距离恰好为 <code>i</code> 。</li>
</ul>

<p>序列里面两个数 <code>a[i]</code> 和 <code>a[j]</code> 之间的 <strong>距离</strong> ，我们定义为它们下标绝对值之差 <code>|j - i|</code> 。</p>

<p>请你返回满足上述条件中 <strong>字典序最大</strong> 的序列。题目保证在给定限制条件下，一定存在解。</p>

<p>一个序列 <code>a</code> 被认为比序列 <code>b</code> （两者长度相同）字典序更大的条件是： <code>a</code> 和 <code>b</code> 中第一个不一样的数字处，<code>a</code> 序列的数字比 <code>b</code> 序列的数字大。比方说，<code>[0,1,9,0]</code> 比 <code>[0,1,5,6]</code> 字典序更大，因为第一个不同的位置是第三个数字，且 <code>9</code> 比 <code>5</code> 大。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>n = 3
<b>输出：</b>[3,1,2,3,2]
<b>解释：</b>[2,3,2,1,3] 也是一个可行的序列，但是 [3,1,2,3,2] 是字典序最大的序列。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>n = 5
<b>输出：</b>[5,3,1,4,3,5,2,4,2]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 回溯

## 提示

1. Heuristic algorithm may work.

## 示例

```
3
5
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> constructDistancedSequence(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] constructDistancedSequence(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def constructDistancedSequence(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructDistancedSequence(int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ConstructDistancedSequence(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var constructDistancedSequence = function(n) {
    
};
```

### TypeScript

```typescript
function constructDistancedSequence(n: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function constructDistancedSequence($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func constructDistancedSequence(_ n: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun constructDistancedSequence(n: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> constructDistancedSequence(int n) {
    
  }
}
```

### Go

```golang
func constructDistancedSequence(n int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer[]}
def construct_distanced_sequence(n)
    
end
```

### Scala

```scala
object Solution {
    def constructDistancedSequence(n: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn construct_distanced_sequence(n: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (construct-distanced-sequence n)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec construct_distanced_sequence(N :: integer()) -> [integer()].
construct_distanced_sequence(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec construct_distanced_sequence(n :: integer) :: [integer]
  def construct_distanced_sequence(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func constructDistancedSequence(n: Int64): Array<Int64> {

    }
}
```

