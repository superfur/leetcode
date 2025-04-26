# 面试题 08.03. 魔术索引

## 题目描述

<p>魔术索引。 在数组<code>A[0...n-1]</code>中，有所谓的魔术索引，满足条件<code>A[i] = i</code>。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：nums = [0, 2, 3, 4, 5]
<strong> 输出</strong>：0
<strong> 说明：</strong>0下标的元素为0
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：nums = [1, 1, 1]
<strong> 输出</strong>：1
</pre>

<p><strong>说明：</strong></p>

<ol>
	<li>nums长度在[1, 1000000]之间</li>
	<li>此题为原书中的 Follow-up，即数组中可能包含重复元素的版本</li>
</ol>


## 难度

Easy

## 标签

- 数组
- 二分查找

## 示例

```
[0, 2, 3, 4, 5]
[1, 1, 1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int findMagicIndex(vector<int>& nums) {
        
    }
};
```

### Java

```java
class Solution {
    public int findMagicIndex(int[] nums) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        
```

### C

```c
int findMagicIndex(int* nums, int numsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int FindMagicIndex(int[] nums) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @return {number}
 */
var findMagicIndex = function(nums) {
    
};
```

### TypeScript

```typescript
function findMagicIndex(nums: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function findMagicIndex($nums) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findMagicIndex(_ nums: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findMagicIndex(nums: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int findMagicIndex(List<int> nums) {
    
  }
}
```

### Go

```golang
func findMagicIndex(nums []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @return {Integer}
def find_magic_index(nums)
    
end
```

### Scala

```scala
object Solution {
    def findMagicIndex(nums: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_magic_index(nums: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (find-magic-index nums)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec find_magic_index(Nums :: [integer()]) -> integer().
find_magic_index(Nums) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_magic_index(nums :: [integer]) :: integer
  def find_magic_index(nums) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findMagicIndex(nums: Array<Int64>): Int64 {

    }
}
```

