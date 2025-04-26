# 1207. 独一无二的出现次数

## 题目描述

<p>给你一个整数数组&nbsp;<code>arr</code>，如果每个数的出现次数都是独一无二的，就返回&nbsp;<code>true</code>；否则返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2,2,1,1,3]
<strong>输出：</strong>true
<strong>解释：</strong>在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [1,2]
<strong>输出：</strong>false
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [-3,0,1,-3,1,1,1,-3,10,0]
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 1000</code></li>
	<li><code>-1000 &lt;= arr[i] &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表

## 提示

1. Find the number of occurrences of each element in the array using a hash map.
2. Iterate through the hash map and check if there is a repeated value.

## 示例

```
[1,2,2,1,1,3]
[1,2]
[-3,0,1,-3,1,1,1,-3,10,0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        
    }
}
```

### Python

```python
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
```

### C

```c
bool uniqueOccurrences(int* arr, int arrSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool UniqueOccurrences(int[] arr) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @return {boolean}
 */
var uniqueOccurrences = function(arr) {
    
};
```

### TypeScript

```typescript
function uniqueOccurrences(arr: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function uniqueOccurrences($arr) {
        
    }
}
```

### Swift

```swift
class Solution {
    func uniqueOccurrences(_ arr: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun uniqueOccurrences(arr: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool uniqueOccurrences(List<int> arr) {
    
  }
}
```

### Go

```golang
func uniqueOccurrences(arr []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @return {Boolean}
def unique_occurrences(arr)
    
end
```

### Scala

```scala
object Solution {
    def uniqueOccurrences(arr: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (unique-occurrences arr)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec unique_occurrences(Arr :: [integer()]) -> boolean().
unique_occurrences(Arr) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec unique_occurrences(arr :: [integer]) :: boolean
  def unique_occurrences(arr) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func uniqueOccurrences(arr: Array<Int64>): Bool {

    }
}
```

