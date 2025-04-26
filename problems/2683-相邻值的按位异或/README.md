# 2683. 相邻值的按位异或

## 题目描述

<p>下标从 <strong>0</strong> 开始、长度为 <code>n</code> 的数组 <code>derived</code> 是由同样长度为 <code>n</code> 的原始 <strong>二进制数组</strong> <code>original</code> 通过计算相邻值的 <strong>按位异或（⊕）</strong>派生而来。</p>

<p>特别地，对于范围&nbsp;<code>[0, n - 1]</code> 内的每个下标 <code>i</code> ：</p>

<ul>
	<li>如果 <code>i = n - 1</code> ，那么 <code>derived[i] = original[i] ⊕ original[0]</code></li>
	<li>否则 <code>derived[i] = original[i] ⊕ original[i + 1]</code></li>
</ul>

<p>给你一个数组 <code>derived</code> ，请判断是否存在一个能够派生得到 <code>derived</code> 的 <strong>有效原始二进制数组</strong> <code>original</code> 。</p>

<p>如果存在满足要求的原始二进制数组，返回 <em><strong>true</strong> </em>；否则，返回<em> <strong>false</strong> </em>。</p>

<ul>
	<li>二进制数组是仅由 <strong>0</strong> 和 <strong>1</strong> 组成的数组。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>derived = [1,1,0]
<strong>输出：</strong>true
<strong>解释：</strong>能够派生得到 [1,1,0] 的有效原始二进制数组是 [0,1,0] ：
derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1 
derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>derived = [1,1]
<strong>输出：</strong>true
<strong>解释：</strong>能够派生得到 [1,1] 的有效原始二进制数组是 [0,1] ：
derived[0] = original[0] ⊕ original[1] = 1
derived[1] = original[1] ⊕ original[0] = 1
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>derived = [1,0]
<strong>输出：</strong>false
<strong>解释：</strong>不存在能够派生得到 [1,0] 的有效原始二进制数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == derived.length</code></li>
	<li><code>1 &lt;= n&nbsp;&lt;= 10<sup>5</sup></code></li>
	<li><code>derived</code> 中的值不是 <strong>0</strong> 就是 <strong>1</strong> 。</li>
</ul>


## 难度

Medium

## 标签

- 位运算
- 数组

## 提示

1. Understand that from the original element, we are using each element twice to construct the derived array
2. The xor-sum of the derived array should be 0 since there is always a duplicate occurrence of each element.

## 示例

```
[1,1,0]
[1,1]
[1,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool doesValidArrayExist(vector<int>& derived) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        
    }
}
```

### Python

```python
class Solution(object):
    def doesValidArrayExist(self, derived):
        """
        :type derived: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        
```

### C

```c
bool doesValidArrayExist(int* derived, int derivedSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool DoesValidArrayExist(int[] derived) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} derived
 * @return {boolean}
 */
var doesValidArrayExist = function(derived) {
    
};
```

### TypeScript

```typescript
function doesValidArrayExist(derived: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $derived
     * @return Boolean
     */
    function doesValidArrayExist($derived) {
        
    }
}
```

### Swift

```swift
class Solution {
    func doesValidArrayExist(_ derived: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun doesValidArrayExist(derived: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool doesValidArrayExist(List<int> derived) {
    
  }
}
```

### Go

```golang
func doesValidArrayExist(derived []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} derived
# @return {Boolean}
def does_valid_array_exist(derived)
    
end
```

### Scala

```scala
object Solution {
    def doesValidArrayExist(derived: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn does_valid_array_exist(derived: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (does-valid-array-exist derived)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec does_valid_array_exist(Derived :: [integer()]) -> boolean().
does_valid_array_exist(Derived) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec does_valid_array_exist(derived :: [integer]) :: boolean
  def does_valid_array_exist(derived) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func doesValidArrayExist(derived: Array<Int64>): Bool {

    }
}
```

