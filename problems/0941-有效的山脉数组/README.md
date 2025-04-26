# 941. 有效的山脉数组

## 题目描述

<p>给定一个整数数组 <code>arr</code>，如果它是有效的山脉数组就返回&nbsp;<code>true</code>，否则返回 <code>false</code>。</p>

<p>让我们回顾一下，如果 <code>arr</code>&nbsp;满足下述条件，那么它是一个山脉数组：</p>

<ul>
	<li><code>arr.length &gt;= 3</code></li>
	<li>在&nbsp;<code>0 &lt; i&nbsp;&lt; arr.length - 1</code>&nbsp;条件下，存在&nbsp;<code>i</code>&nbsp;使得：
	<ul>
		<li><code>arr[0] &lt; arr[1] &lt; ... arr[i-1] &lt; arr[i] </code></li>
		<li><code>arr[i] &gt; arr[i+1] &gt; ... &gt; arr[arr.length - 1]</code></li>
	</ul>
	</li>
</ul>

<p>&nbsp;</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png" style="height: 316px; width: 500px;" /></p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [2,1]
<strong>输出：</strong>false
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [3,5,5]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [0,3,2,1]
<strong>输出：</strong>true</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= arr[i] &lt;= 10<sup>4</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数组

## 提示

1. It's very easy to keep track of a monotonically increasing or decreasing ordering of elements. You just need to be able to determine the start of the valley in the mountain and from that point onwards, it should be a valley i.e. no mini-hills after that. Use this information in regards to the values in the array and you will be able to come up with a straightforward solution.

## 示例

```
[2,1]
[3,5,5]
[0,3,2,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean validMountainArray(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
```

### C

```c
bool validMountainArray(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool ValidMountainArray(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var validMountainArray = function(arr) {
    
};
```

### TypeScript

```typescript
function validMountainArray(arr: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function validMountainArray($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func validMountainArray(_ arr: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun validMountainArray(arr: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool validMountainArray(List<int> arr) {
    
  }
}
```

### Go

```golang
func validMountainArray(arr []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Boolean}
def valid_mountain_array(arr)
    
end
```

### Scala

```scala
object Solution {
    def validMountainArray(arr: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn valid_mountain_array(arr: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (valid-mountain-array arr)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec valid_mountain_array(Arr :: [integer()]) -> boolean().
valid_mountain_array(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec valid_mountain_array(arr :: [integer]) :: boolean
  def valid_mountain_array(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func validMountainArray(arr: Array<Int64>): Bool {

    }
}
```

