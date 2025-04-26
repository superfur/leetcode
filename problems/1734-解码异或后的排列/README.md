# 1734. 解码异或后的排列

## 题目描述

<p>给你一个整数数组 <code>perm</code> ，它是前 <code>n</code> 个正整数的排列，且 <code>n</code> 是个 <strong>奇数</strong> 。</p>

<p>它被加密成另一个长度为 <code>n - 1</code> 的整数数组 <code>encoded</code> ，满足 <code>encoded[i] = perm[i] XOR perm[i + 1]</code> 。比方说，如果 <code>perm = [1,3,2]</code> ，那么 <code>encoded = [2,1]</code> 。</p>

<p>给你 <code>encoded</code> 数组，请你返回原始数组 <code>perm</code> 。题目保证答案存在且唯一。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>encoded = [3,1]
<b>输出：</b>[1,2,3]
<b>解释：</b>如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>encoded = [6,5,4,6]
<b>输出：</b>[2,4,1,5,3]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= n &lt; 10<sup>5</sup></code></li>
	<li><code>n</code> 是奇数。</li>
	<li><code>encoded.length == n - 1</code></li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组

## 提示

1. Compute the XOR of the numbers between 1 and n, and think about how it can be used. Let it be x.
2. Think why n is odd.
3. perm[0] = x XOR encoded[1] XOR encoded[3] XOR encoded[5] ...
4. perm[i] = perm[i-1] XOR encoded[i-1]

## 示例

```
[3,1]
[6,5,4,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> decode(vector<int>& encoded) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] decode(int[] encoded) {
        
    }
}
```

### Python

```python
class Solution(object):
    def decode(self, encoded):
        """
        :type encoded: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] Decode(int[] encoded) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} encoded
 * @return {number[]}
 */
var decode = function(encoded) {
    
};
```

### TypeScript

```typescript
function decode(encoded: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $encoded
     * @return Integer[]
     */
    function decode($encoded) {
        
    }
}
```

### Swift

```swift
class Solution {
    func decode(_ encoded: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun decode(encoded: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> decode(List<int> encoded) {
    
  }
}
```

### Go

```golang
func decode(encoded []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} encoded
# @return {Integer[]}
def decode(encoded)
    
end
```

### Scala

```scala
object Solution {
    def decode(encoded: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn decode(encoded: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (decode encoded)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec decode(Encoded :: [integer()]) -> [integer()].
decode(Encoded) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec decode(encoded :: [integer]) :: [integer]
  def decode(encoded) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func decode(encoded: Array<Int64>): Array<Int64> {

    }
}
```

