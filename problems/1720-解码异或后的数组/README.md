# 1720. 解码异或后的数组

## 题目描述

<p><strong>未知</strong> 整数数组 <code>arr</code> 由 <code>n</code> 个非负整数组成。</p>

<p>经编码后变为长度为 <code>n - 1</code> 的另一个整数数组 <code>encoded</code> ，其中 <code>encoded[i] = arr[i] XOR arr[i + 1]</code> 。例如，<code>arr = [1,0,2,1]</code> 经编码后得到 <code>encoded = [1,2,3]</code> 。</p>

<p>给你编码后的数组 <code>encoded</code> 和原数组 <code>arr</code> 的第一个元素 <code>first</code>（<code>arr[0]</code>）。</p>

<p>请解码返回原数组 <code>arr</code> 。可以证明答案存在并且是唯一的。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>encoded = [1,2,3], first = 1
<strong>输出：</strong>[1,0,2,1]
<strong>解释：</strong>若 arr = [1,0,2,1] ，那么 first = 1 且 encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>encoded = [6,2,7,3], first = 4
<strong>输出：</strong>[4,2,0,7,4]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 <= n <= 10<sup>4</sup></code></li>
	<li><code>encoded.length == n - 1</code></li>
	<li><code>0 <= encoded[i] <= 10<sup>5</sup></code></li>
	<li><code>0 <= first <= 10<sup>5</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 位运算
- 数组

## 提示

1. Since that encoded[i] = arr[i] XOR arr[i+1], then arr[i+1] = encoded[i] XOR arr[i].
2. Iterate on i from beginning to end, and set arr[i+1] = encoded[i] XOR arr[i].

## 示例

```
[1,2,3]
1
[6,2,7,3]
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] decode(int[] encoded, int first) {
        
    }
}
```

### Python

```python
class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int first, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] Decode(int[] encoded, int first) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} encoded
 * @param {number} first
 * @return {number[]}
 */
var decode = function(encoded, first) {
    
};
```

### TypeScript

```typescript
function decode(encoded: number[], first: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $encoded
     * @param Integer $first
     * @return Integer[]
     */
    function decode($encoded, $first) {
        
    }
}
```

### Swift

```swift
class Solution {
    func decode(_ encoded: [Int], _ first: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun decode(encoded: IntArray, first: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> decode(List<int> encoded, int first) {
    
  }
}
```

### Go

```golang
func decode(encoded []int, first int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} encoded
# @param {Integer} first
# @return {Integer[]}
def decode(encoded, first)
    
end
```

### Scala

```scala
object Solution {
    def decode(encoded: Array[Int], first: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn decode(encoded: Vec<i32>, first: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (decode encoded first)
  (-> (listof exact-integer?) exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec decode(Encoded :: [integer()], First :: integer()) -> [integer()].
decode(Encoded, First) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec decode(encoded :: [integer], first :: integer) :: [integer]
  def decode(encoded, first) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func decode(encoded: Array<Int64>, first: Int64): Array<Int64> {

    }
}
```

