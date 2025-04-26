# 845. 数组中的最长山脉

## 题目描述

<p>把符合下列属性的数组 <code>arr</code> 称为 <strong>山脉数组</strong> ：</p>

<ul>
	<li><code>arr.length &gt;= 3</code></li>
	<li>存在下标 <code>i</code>（<code>0 &lt; i &lt; arr.length - 1</code>），满足
	<ul>
		<li><code>arr[0] &lt; arr[1] &lt; ... &lt; arr[i - 1] &lt; arr[i]</code></li>
		<li><code>arr[i] &gt; arr[i + 1] &gt; ... &gt; arr[arr.length - 1]</code></li>
	</ul>
	</li>
</ul>

<p>给出一个整数数组 <code>arr</code>，返回最长山脉子数组的长度。如果不存在山脉子数组，返回 <code>0</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [2,1,4,7,3,2,5]
<strong>输出：</strong>5
<strong>解释：</strong>最长的山脉子数组是 [1,4,7,3,2]，长度为 5。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [2,2,2]
<strong>输出：</strong>0
<strong>解释：</strong>不存在山脉子数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong></p>

<ul>
	<li>你可以仅用一趟扫描解决此问题吗？</li>
	<li>你可以用 <code>O(1)</code> 空间解决此问题吗？</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 双指针
- 动态规划
- 枚举

## 示例

```
[2,1,4,7,3,2,5]
[2,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int longestMountain(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public int longestMountain(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
```

### C

```c
int longestMountain(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int LongestMountain(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {number}
 */
var longestMountain = function(arr) {
    
};
```

### TypeScript

```typescript
function longestMountain(arr: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Integer
     */
    function longestMountain($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func longestMountain(_ arr: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun longestMountain(arr: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int longestMountain(List<int> arr) {
    
  }
}
```

### Go

```golang
func longestMountain(arr []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Integer}
def longest_mountain(arr)
    
end
```

### Scala

```scala
object Solution {
    def longestMountain(arr: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn longest_mountain(arr: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (longest-mountain arr)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec longest_mountain(Arr :: [integer()]) -> integer().
longest_mountain(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec longest_mountain(arr :: [integer]) :: integer
  def longest_mountain(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func longestMountain(arr: Array<Int64>): Int64 {

    }
}
```

