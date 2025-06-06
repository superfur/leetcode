# 2190. 数组中紧跟 key 之后出现最频繁的数字

## 题目描述

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;，同时给你一个整数&nbsp;<code>key</code>&nbsp;，它在&nbsp;<code>nums</code>&nbsp;出现过。</p>

<p><strong>统计&nbsp;</strong>在 <code>nums</code>&nbsp;数组中紧跟着 <code>key</code>&nbsp;后面出现的不同整数&nbsp;<code>target</code>&nbsp;的出现次数。换言之，<code>target</code>&nbsp;的出现次数为满足以下条件的 <code>i</code>&nbsp;的数目：</p>

<ul>
	<li><code>0 &lt;= i &lt;= n - 2</code></li>
	<li><code>nums[i] == key</code>&nbsp;且</li>
	<li><code>nums[i + 1] == target</code>&nbsp;。</li>
</ul>

<p>请你返回出现 <strong>最多</strong>&nbsp;次数的<em>&nbsp;</em><code>target</code>&nbsp;。测试数据保证出现次数最多的 <code>target</code>&nbsp;是唯一的。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>nums = [1,100,200,1,100], key = 1
<b>输出：</b>100
<b>解释：</b>对于 target = 100 ，在下标 1 和 4 处出现过 2 次，且都紧跟着 key 。
没有其他整数在 key 后面紧跟着出现，所以我们返回 100 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>nums = [2,2,2,2,3], key = 2
<b>输出：</b>2
<b>解释：</b>对于 target = 2 ，在下标 1 ，2 和 3 处出现过 3 次，且都紧跟着 key 。
对于 target = 3 ，在下标 4 出出现过 1 次，且紧跟着 key 。
target = 2 是紧跟着 key 之后出现次数最多的数字，所以我们返回 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 1000</code></li>
	<li>测试数据保证答案是唯一的。</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 计数

## 提示

1. Count the number of times each target value follows the key in the array.
2. Choose the target with the maximum count and return it.

## 示例

```
[1,100,200,1,100]
1
[2,2,2,2,3]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int mostFrequent(vector<int>& nums, int key) {
        
    }
};
```

### Java

```java
class Solution {
    public int mostFrequent(int[] nums, int key) {
        
    }
}
```

### Python

```python
class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        
```

### C

```c
int mostFrequent(int* nums, int numsSize, int key) {
    
}
```

### C#

```csharp
public class Solution {
    public int MostFrequent(int[] nums, int key) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} nums
 * @param {number} key
 * @return {number}
 */
var mostFrequent = function(nums, key) {
    
};
```

### TypeScript

```typescript
function mostFrequent(nums: number[], key: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $key
     * @return Integer
     */
    function mostFrequent($nums, $key) {
        
    }
}
```

### Swift

```swift
class Solution {
    func mostFrequent(_ nums: [Int], _ key: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun mostFrequent(nums: IntArray, key: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int mostFrequent(List<int> nums, int key) {
    
  }
}
```

### Go

```golang
func mostFrequent(nums []int, key int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} nums
# @param {Integer} key
# @return {Integer}
def most_frequent(nums, key)
    
end
```

### Scala

```scala
object Solution {
    def mostFrequent(nums: Array[Int], key: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn most_frequent(nums: Vec<i32>, key: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (most-frequent nums key)
  (-> (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec most_frequent(Nums :: [integer()], Key :: integer()) -> integer().
most_frequent(Nums, Key) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec most_frequent(nums :: [integer], key :: integer) :: integer
  def most_frequent(nums, key) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func mostFrequent(nums: Array<Int64>, key: Int64): Int64 {

    }
}
```

