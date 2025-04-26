# 978. 最长湍流子数组

## 题目描述

<p>给定一个整数数组 <code>arr</code>&nbsp;，返回 <code>arr</code>&nbsp;的&nbsp;<em>最大湍流子数组的<strong>长度</strong></em><strong>&nbsp;</strong>。</p>

<p>如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是&nbsp;<strong>湍流子数组</strong>&nbsp;。</p>

<p>更正式地来说，当 <code>arr</code>&nbsp;的子数组&nbsp;<code>A[i], A[i+1], ..., A[j]</code>&nbsp;满足仅满足下列条件时，我们称其为<em>湍流子数组</em>：</p>

<ul>
	<li>若&nbsp;<code>i &lt;= k &lt; j</code>&nbsp;：

	<ul>
		<li>当 <code>k</code>&nbsp;为奇数时，&nbsp;<code>A[k] &gt; A[k+1]</code>，且</li>
		<li>当 <code>k</code> 为偶数时，<code>A[k] &lt; A[k+1]</code>；</li>
	</ul>
	</li>
	<li><strong>或 </strong>若&nbsp;<code>i &lt;= k &lt; j</code>&nbsp;：
	<ul>
		<li>当 <code>k</code> 为偶数时，<code>A[k] &gt; A[k+1]</code>&nbsp;，且</li>
		<li>当 <code>k</code>&nbsp;为奇数时，&nbsp;<code>A[k] &lt; A[k+1]</code>。</li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [9,4,2,10,7,8,8,1,9]
<strong>输出：</strong>5
<strong>解释：</strong>arr[1] &gt; arr[2] &lt; arr[3] &gt; arr[4] &lt; arr[5]</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [4,8,12,16]
<strong>输出：</strong>2
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [100]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 动态规划
- 滑动窗口

## 示例

```
[9,4,2,10,7,8,8,1,9]
[4,8,12,16]
[100]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int maxTurbulenceSize(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
```

### C

```c
int maxTurbulenceSize(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MaxTurbulenceSize(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var maxTurbulenceSize = function(arr) {
    
};
```

### TypeScript

```typescript
function maxTurbulenceSize(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function maxTurbulenceSize($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func maxTurbulenceSize(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun maxTurbulenceSize(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int maxTurbulenceSize(List<int> arr) {
    
  }
}
```

### Go

```golang
func maxTurbulenceSize(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def max_turbulence_size(arr)
    
end
```

### Scala

```scala
object Solution {
    def maxTurbulenceSize(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn max_turbulence_size(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (max-turbulence-size arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec max_turbulence_size(Arr :: [integer()]) -> integer().
max_turbulence_size(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec max_turbulence_size(arr :: [integer]) :: integer
  def max_turbulence_size(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func maxTurbulenceSize(arr: Array<Int64>): Int64 {

    }
}
```

