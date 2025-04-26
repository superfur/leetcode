# 927. 三等分

## 题目描述

<p>给定一个由 <code>0</code> 和 <code>1</code> 组成的数组<meta charset="UTF-8" />&nbsp;<code>arr</code>&nbsp;，将数组分成 &nbsp;<strong>3&nbsp;个非空的部分</strong> ，使得所有这些部分表示相同的二进制值。</p>

<p>如果可以做到，请返回<strong>任何</strong>&nbsp;<code>[i, j]</code>，其中 <code>i+1 &lt; j</code>，这样一来：</p>

<ul>
	<li><code>arr[0], arr[1], ..., arr[i]</code>&nbsp;为第一部分；</li>
	<li><code>arr[i + 1], arr[i + 2], ..., arr[j - 1]</code>&nbsp;为第二部分；</li>
	<li><code>arr[j], arr[j + 1], ..., arr[arr.length - 1]</code>&nbsp;为第三部分。</li>
	<li>这三个部分所表示的二进制值相等。</li>
</ul>

<p>如果无法做到，就返回&nbsp;<code>[-1, -1]</code>。</p>

<p>注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，<code>[1,1,0]</code>&nbsp;表示十进制中的&nbsp;<code>6</code>，而不会是&nbsp;<code>3</code>。此外，前导零也是<strong>被允许</strong>的，所以&nbsp;<code>[0,1,1]</code> 和&nbsp;<code>[1,1]</code>&nbsp;表示相同的值。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,0,1,0,1]
<strong>输出：</strong>[0,3]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,1,0,1,1]
<strong>输出：</strong>[-1,-1]</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入：</strong>arr = [1,1,0,0,1]
<strong>输出：</strong>[0,2]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>
<meta charset="UTF-8" />

<ul>
	<li><code>3 &lt;= arr.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>arr[i]</code>&nbsp;是&nbsp;<code>0</code>&nbsp;或&nbsp;<code>1</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学

## 示例

```
[1,0,1,0,1]
[1,1,0,1,1]
[1,1,0,0,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> threeEqualParts(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] threeEqualParts(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* threeEqualParts(int* arr, int arrSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ThreeEqualParts(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var threeEqualParts = function(arr) {
    
};
```

### TypeScript

```typescript
function threeEqualParts(arr: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer[]
     */
    function threeEqualParts($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func threeEqualParts(_ arr: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun threeEqualParts(arr: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> threeEqualParts(List<int> arr) {
    
  }
}
```

### Go

```golang
func threeEqualParts(arr []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer[]}
def three_equal_parts(arr)
    
end
```

### Scala

```scala
object Solution {
    def threeEqualParts(arr: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn three_equal_parts(arr: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (three-equal-parts arr)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec three_equal_parts(Arr :: [integer()]) -> [integer()].
three_equal_parts(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec three_equal_parts(arr :: [integer]) :: [integer]
  def three_equal_parts(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func threeEqualParts(arr: Array<Int64>): Array<Int64> {

    }
}
```

