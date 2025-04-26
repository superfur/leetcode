# 667. 优美的排列 II

## 题目描述

<p>给你两个整数 <code>n</code> 和 <code>k</code> ，请你构造一个答案列表 <code>answer</code> ，该列表应当包含从 <code>1</code> 到 <code>n</code> 的 <code>n</code> 个不同正整数，并同时满足下述条件：</p>

<ul>
	<li>假设该列表是 <code>answer = [a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ... , a<sub>n</sub>]</code> ，那么列表 <code>[|a<sub>1</sub> - a<sub>2</sub>|, |a<sub>2</sub> - a<sub>3</sub>|, |a<sub>3</sub> - a<sub>4</sub>|, ... , |a<sub>n-1</sub> - a<sub>n</sub>|]</code> 中应该有且仅有 <code>k</code> 个不同整数。</li>
</ul>

<p>返回列表 <code>answer</code> 。如果存在多种答案，只需返回其中 <strong>任意一种</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 1
<strong>输出：</strong>[1, 2, 3]
<strong>解释：</strong>[1, 2, 3] 包含 3 个范围在 1-3 的不同整数，并且 [1, 1] 中有且仅有 1 个不同整数：1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 3, k = 2
<strong>输出：</strong>[1, 3, 2]
<strong>解释：</strong>[1, 3, 2] 包含 3 个范围在 1-3 的不同整数，并且 [2, 1] 中有且仅有 2 个不同整数：1 和 2
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= k < n <= 10<sup>4</sup></code></li>
</ul>

<p> </p>


## 难度

Medium

## 标签

- 数组
- 数学

## 示例

```
3
1
3
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> constructArray(int n, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] constructArray(int n, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* constructArray(int n, int k, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ConstructArray(int n, int k) {
        
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
var constructArray = function(n, k) {
    
};
```

### TypeScript

```typescript
function constructArray(n: number, k: number): number[] {
    
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
    function constructArray($n, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func constructArray(_ n: Int, _ k: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun constructArray(n: Int, k: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> constructArray(int n, int k) {
    
  }
}
```

### Go

```golang
func constructArray(n int, k int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer} k
# @return {Integer[]}
def construct_array(n, k)
    
end
```

### Scala

```scala
object Solution {
    def constructArray(n: Int, k: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn construct_array(n: i32, k: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (construct-array n k)
  (-> exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec construct_array(N :: integer(), K :: integer()) -> [integer()].
construct_array(N, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec construct_array(n :: integer, k :: integer) :: [integer]
  def construct_array(n, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func constructArray(n: Int64, k: Int64): Array<Int64> {

    }
}
```

