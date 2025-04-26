# 967. 连续差相同的数字

## 题目描述

<p>返回所有长度为 <code>n</code> 且满足其每两个连续位上的数字之间的差的绝对值为 <code>k</code> 的<strong> 非负整数 </strong>。</p>

<p>请注意，<strong>除了 </strong>数字 <code>0</code> 本身之外，答案中的每个数字都 <strong>不能 </strong>有前导零。例如，<code>01</code> 有一个前导零，所以是无效的；但 <code>0</code>&nbsp;是有效的。</p>

<p>你可以按 <strong>任何顺序</strong> 返回答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 7
<strong>输出：</strong>[181,292,707,818,929]
<strong>解释：</strong>注意，070 不是一个有效的数字，因为它有前导零。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 2, k = 1
<strong>输出：</strong>[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 2, k = 0
<strong>输出：</strong>[11,22,33,44,55,66,77,88,99]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>n = 2, k = 2
<strong>输出：</strong>[13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 9</code></li>
	<li><code>0 &lt;= k &lt;= 9</code></li>
</ul>


## 难度

Medium

## 标签

- 广度优先搜索
- 回溯

## 示例

```
3
7
2
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> numsSameConsecDiff(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] numsSameConsecDiff(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numsSameConsecDiff(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* numsSameConsecDiff(int n, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] NumsSameConsecDiff(int n, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
var numsSameConsecDiff = function(n, k) {
    
};
```

### TypeScript

```typescript
function numsSameConsecDiff(n: number, k: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer $k
     * @return Integer[]
     */
    function numsSameConsecDiff($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numsSameConsecDiff(_ n: Int, _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numsSameConsecDiff(n: Int, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> numsSameConsecDiff(int n, int k) {
    
  }
}
```

### Go

```golang
func numsSameConsecDiff(n int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def nums_same_consec_diff(n, k)
    
end
```

### Scala

```scala
object Solution {
    def numsSameConsecDiff(n: Int, k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn nums_same_consec_diff(n: i32, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (nums-same-consec-diff n k)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec nums_same_consec_diff(N :: integer(), K :: integer()) -> [integer()].
nums_same_consec_diff(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec nums_same_consec_diff(n :: integer, k :: integer) :: [integer]
  def nums_same_consec_diff(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numsSameConsecDiff(n: Int64, k: Int64): Array<Int64> {

    }
}
```

