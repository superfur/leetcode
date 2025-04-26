# 954. 二倍数对数组

## 题目描述

<p>给定一个长度为偶数的整数数组 <code>arr</code>，只有对 <code>arr</code> 进行重组后可以满足 “对于每个 <code>0 &lt;=&nbsp;i &lt; len(arr) / 2</code>，都有 <code>arr[2 * i + 1] = 2 * arr[2 * i]</code>”&nbsp;时，返回 <code>true</code>；否则，返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [3,1,3,6]
<strong>输出：</strong>false
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [2,1,2,6]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [4,-2,2,-4]
<strong>输出：</strong>true
<strong>解释：</strong>可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= arr.length &lt;= 3 * 10<sup>4</sup></code></li>
	<li><code>arr.length</code> 是偶数</li>
	<li><code>-10<sup>5</sup> &lt;= arr[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 排序

## 示例

```
[3,1,3,6]
[2,1,2,6]
[4,-2,2,-4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canReorderDoubled(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canReorderDoubled(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
```

### C

```c
bool canReorderDoubled(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanReorderDoubled(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canReorderDoubled = function(arr) {
    
};
```

### TypeScript

```typescript
function canReorderDoubled(arr: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function canReorderDoubled($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canReorderDoubled(_ arr: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canReorderDoubled(arr: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canReorderDoubled(List<int> arr) {
    
  }
}
```

### Go

```golang
func canReorderDoubled(arr []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Boolean}
def can_reorder_doubled(arr)
    
end
```

### Scala

```scala
object Solution {
    def canReorderDoubled(arr: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_reorder_doubled(arr: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-reorder-doubled arr)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec can_reorder_doubled(Arr :: [integer()]) -> boolean().
can_reorder_doubled(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_reorder_doubled(arr :: [integer]) :: boolean
  def can_reorder_doubled(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canReorderDoubled(arr: Array<Int64>): Bool {

    }
}
```

