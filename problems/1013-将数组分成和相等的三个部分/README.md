# 1013. 将数组分成和相等的三个部分

## 题目描述

<p>给你一个整数数组 <code>arr</code>，只有可以将其划分为三个和相等的 <strong>非空</strong> 部分时才返回 <code>true</code>，否则返回 <code>false</code>。</p>

<p>形式上，如果可以找出索引 <code>i + 1 < j</code> 且满足 <code>(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])</code> 就可以将数组三等分。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,2,1,-6,6,-7,9,1,2,0,1]
<strong>输出：</strong>true
<strong>解释：</strong>0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,2,1,-6,6,7,9,-1,2,0,1]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [3,3,6,5,-2,2,5,1,-9,4]
<strong>输出：</strong>true
<strong>解释：</strong>3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 <= arr.length <= 5 * 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> <= arr[i] <= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 贪心
- 数组

## 提示

1. If we have three parts with the same sum, what is the sum of each?
If you can find the first part, can you find the second part?

## 示例

```
[0,2,1,-6,6,-7,9,1,2,0,1]
[0,2,1,-6,6,7,9,-1,2,0,1]
[3,3,6,5,-2,2,5,1,-9,4]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canThreePartsEqualSum(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canThreePartsEqualSum(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        
```

### C

```c
bool canThreePartsEqualSum(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanThreePartsEqualSum(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var canThreePartsEqualSum = function(arr) {
    
};
```

### TypeScript

```typescript
function canThreePartsEqualSum(arr: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function canThreePartsEqualSum($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canThreePartsEqualSum(_ arr: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canThreePartsEqualSum(arr: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canThreePartsEqualSum(List<int> arr) {
    
  }
}
```

### Go

```golang
func canThreePartsEqualSum(arr []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Boolean}
def can_three_parts_equal_sum(arr)
    
end
```

### Scala

```scala
object Solution {
    def canThreePartsEqualSum(arr: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_three_parts_equal_sum(arr: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-three-parts-equal-sum arr)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec can_three_parts_equal_sum(Arr :: [integer()]) -> boolean().
can_three_parts_equal_sum(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_three_parts_equal_sum(arr :: [integer]) :: boolean
  def can_three_parts_equal_sum(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canThreePartsEqualSum(arr: Array<Int64>): Bool {

    }
}
```

