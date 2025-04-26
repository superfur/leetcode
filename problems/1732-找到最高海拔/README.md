# 1732. 找到最高海拔

## 题目描述

<p>有一个自行车手打算进行一场公路骑行，这条路线总共由 <code>n + 1</code> 个不同海拔的点组成。自行车手从海拔为 <code>0</code> 的点 <code>0</code> 开始骑行。</p>

<p>给你一个长度为 <code>n</code> 的整数数组 <code>gain</code> ，其中 <code>gain[i]</code> 是点 <code>i</code> 和点 <code>i + 1</code> 的 <strong>净海拔高度差</strong>（<code>0 <= i < n</code>）。请你返回 <strong>最高点的海拔</strong> 。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>gain = [-5,1,5,0,-7]
<b>输出：</b>1
<b>解释：</b>海拔高度依次为 [0,-5,-4,1,1,-6] 。最高海拔为 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>gain = [-4,-3,-2,-1,4,3,2]
<b>输出：</b>0
<b>解释：</b>海拔高度依次为 [0,-4,-7,-9,-10,-6,-3,-1] 。最高海拔为 0 。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == gain.length</code></li>
	<li><code>1 <= n <= 100</code></li>
	<li><code>-100 <= gain[i] <= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 前缀和

## 提示

1. Let's note that the altitude of an element is the sum of gains of all the elements behind it
2. Getting the altitudes can be done by getting the prefix sum array of the given array

## 示例

```
[-5,1,5,0,-7]
[-4,-3,-2,-1,4,3,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        
    }
};
```

### Java

```java
class Solution {
    public int largestAltitude(int[] gain) {
        
    }
}
```

### Python

```python
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
```

### C

```c
int largestAltitude(int* gain, int gainSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LargestAltitude(int[] gain) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    
};
```

### TypeScript

```typescript
function largestAltitude(gain: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $gain
     * @return Integer
     */
    function largestAltitude($gain) {
        
    }
}
```

### Swift

```swift
class Solution {
    func largestAltitude(_ gain: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun largestAltitude(gain: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int largestAltitude(List<int> gain) {
    
  }
}
```

### Go

```golang
func largestAltitude(gain []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} gain
# @return {Integer}
def largest_altitude(gain)
    
end
```

### Scala

```scala
object Solution {
    def largestAltitude(gain: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (largest-altitude gain)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec largest_altitude(Gain :: [integer()]) -> integer().
largest_altitude(Gain) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec largest_altitude(gain :: [integer]) :: integer
  def largest_altitude(gain) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func largestAltitude(gain: Array<Int64>): Int64 {

    }
}
```

