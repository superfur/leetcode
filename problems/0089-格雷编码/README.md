# 89. 格雷编码

## 题目描述

<strong>n 位格雷码序列</strong> 是一个由 <code>2<sup>n</sup></code> 个整数组成的序列，其中：
<ul>
	<li>每个整数都在范围 <code>[0, 2<sup>n</sup> - 1]</code> 内（含 <code>0</code> 和 <code>2<sup>n</sup> - 1</code>）</li>
	<li>第一个整数是 <code>0</code></li>
	<li>一个整数在序列中出现 <strong>不超过一次</strong></li>
	<li>每对 <strong>相邻</strong> 整数的二进制表示 <strong>恰好一位不同</strong> ，且</li>
	<li><strong>第一个</strong> 和 <strong>最后一个</strong> 整数的二进制表示 <strong>恰好一位不同</strong></li>
</ul>

<p>给你一个整数 <code>n</code> ，返回任一有效的 <strong>n 位格雷码序列</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 2
<strong>输出：</strong>[0,1,3,2]
<strong>解释：</strong>
[0,1,3,2] 的二进制表示是 [00,01,11,10] 。
- 0<strong><em>0</em></strong> 和 0<em><strong>1</strong></em> 有一位不同
- <em><strong>0</strong></em>1 和 <em><strong>1</strong></em>1 有一位不同
- 1<em><strong>1</strong></em> 和 1<em><strong>0</strong></em> 有一位不同
- <em><strong>1</strong></em>0 和 <em><strong>0</strong></em>0 有一位不同
[0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
- <em><strong>0</strong></em>0 和 <em><strong>1</strong></em>0 有一位不同
- 1<em><strong>0</strong></em> 和 1<em><strong>1</strong></em> 有一位不同
- <em><strong>1</strong></em>1 和 <em><strong>0</strong></em>1 有一位不同
- 0<em><strong>1</strong></em> 和 0<em><strong>0</strong></em> 有一位不同
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>[0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 16</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数学
- 回溯

## 示例

```
2
1
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> grayCode(int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def grayCode(self, n: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* grayCode(int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> GrayCode(int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    
};
```

### TypeScript

```typescript
function grayCode(n: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @return Integer[]
     */
    function grayCode($n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func grayCode(_ n: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun grayCode(n: Int): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> grayCode(int n) {
    
  }
}
```

### Go

```golang
func grayCode(n int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @return {Integer[]}
def gray_code(n)
    
end
```

### Scala

```scala
object Solution {
    def grayCode(n: Int): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn gray_code(n: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (gray-code n)
  (-> exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec gray_code(N :: integer()) -> [integer()].
gray_code(N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec gray_code(n :: integer) :: [integer]
  def gray_code(n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func grayCode(n: Int64): ArrayList<Int64> {

    }
}
```

