# 1497. 检查数组对是否可以被 k 整除

## 题目描述

<p>给你一个整数数组 <code>arr</code> 和一个整数 <code>k</code> ，其中数组长度是偶数，值为 <code>n</code> 。</p>

<p>现在需要把数组恰好分成 <code>n /&nbsp;2</code> 对，以使每对数字的和都能够被 <code>k</code> 整除。</p>

<p>如果存在这样的分法，请返回&nbsp;<code>true</code> ；否则，返回<i>&nbsp;</i><code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,4,5,10,6,7,8,9], k = 5
<strong>输出：</strong>true
<strong>解释：</strong>划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10) 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,4,5,6], k = 7
<strong>输出：</strong>true
<strong>解释：</strong>划分后的数字对为 (1,6),(2,5) 以及 (3,4) 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,3,4,5,6], k = 10
<strong>输出：</strong>false
<strong>解释：</strong>无法在将数组中的数字分为三对的同时满足每对数字和能够被 10 整除的条件。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>arr.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n</code> 为偶数<meta charset="UTF-8" /></li>
	<li><code>-10<sup>9</sup>&nbsp;&lt;= arr[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. Keep an array of the frequencies of ((x % k) + k) % k for each x in arr.
2. for each i in [0, k - 1] we need to check if freq[i] == freq[k - i]
3. Take care of the case when i == k - i and when i == 0

## 示例

```
[1,2,3,4,5,10,6,7,8,9]
5
[1,2,3,4,5,6]
7
[1,2,3,4,5,6]
10
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canArrange(int[] arr, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        
```

### C

```c
bool canArrange(int* arr, int arrSize, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanArrange(int[] arr, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} k
 * @return {boolean}
 */
var canArrange = function(arr, k) {
    
};
```

### TypeScript

```typescript
function canArrange(arr: number[], k: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $k
     * @return Boolean
     */
    function canArrange($arr, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canArrange(_ arr: [Int], _ k: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canArrange(arr: IntArray, k: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canArrange(List<int> arr, int k) {
    
  }
}
```

### Go

```golang
func canArrange(arr []int, k int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} k
# @return {Boolean}
def can_arrange(arr, k)
    
end
```

### Scala

```scala
object Solution {
    def canArrange(arr: Array[Int], k: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_arrange(arr: Vec<i32>, k: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-arrange arr k)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_arrange(Arr :: [integer()], K :: integer()) -> boolean().
can_arrange(Arr, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_arrange(arr :: [integer], k :: integer) :: boolean
  def can_arrange(arr, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canArrange(arr: Array<Int64>, k: Int64): Bool {

    }
}
```

