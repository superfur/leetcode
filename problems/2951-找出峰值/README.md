# 2951. 找出峰值

## 题目描述

<p>给你一个下标从 <strong>0</strong> 开始的数组 <code>mountain</code> 。你的任务是找出数组&nbsp;<code>mountain</code> 中的所有 <strong>峰值</strong>。</p>

<p>以数组形式返回给定数组中 <strong>峰值</strong> 的下标，<strong>顺序不限</strong> 。</p>

<p><strong>注意：</strong></p>

<ul>
	<li><strong>峰值</strong> 是指一个严格大于其相邻元素的元素。</li>
	<li>数组的第一个和最后一个元素 <strong>不</strong> 是峰值。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>mountain = [2,4,4]
<strong>输出：</strong>[]
<strong>解释：</strong>mountain[0] 和 mountain[2] 不可能是峰值，因为它们是数组的第一个和最后一个元素。
mountain[1] 也不可能是峰值，因为它不严格大于 mountain[2] 。
因此，答案为 [] 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>mountain = [1,4,3,8,5]
<strong>输出：</strong>[1,3]
<strong>解释：</strong>mountain[0] 和 mountain[4] 不可能是峰值，因为它们是数组的第一个和最后一个元素。
mountain[2] 也不可能是峰值，因为它不严格大于 mountain[3] 和 mountain[1] 。
但是 mountain[1] 和 mountain[3] 严格大于它们的相邻元素。
因此，答案是 [1,3] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>3 &lt;= mountain.length &lt;= 100</code></li>
	<li><code>1 &lt;= mountain[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 枚举

## 提示

1. If <code>nums[i] > num[i - 1]</code> and <code>nums[i] > nums[i + 1]</code> <code>nums[i]</code> is a peak.

## 示例

```
[2,4,4]
[1,4,3,8,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> findPeaks(vector<int>& mountain) {
        
    }
};
```

### Java

```java
class Solution {
    public List<Integer> findPeaks(int[] mountain) {
        
    }
}
```

### Python

```python
class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findPeaks(int* mountain, int mountainSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<int> FindPeaks(int[] mountain) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} mountain
 * @return {number[]}
 */
var findPeaks = function(mountain) {
    
};
```

### TypeScript

```typescript
function findPeaks(mountain: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $mountain
     * @return Integer[]
     */
    function findPeaks($mountain) {
        
    }
}
```

### Swift

```swift
class Solution {
    func findPeaks(_ mountain: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun findPeaks(mountain: IntArray): List<Int> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> findPeaks(List<int> mountain) {
    
  }
}
```

### Go

```golang
func findPeaks(mountain []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} mountain
# @return {Integer[]}
def find_peaks(mountain)
    
end
```

### Scala

```scala
object Solution {
    def findPeaks(mountain: Array[Int]): List[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn find_peaks(mountain: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (find-peaks mountain)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec find_peaks(Mountain :: [integer()]) -> [integer()].
find_peaks(Mountain) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec find_peaks(mountain :: [integer]) :: [integer]
  def find_peaks(mountain) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func findPeaks(mountain: Array<Int64>): ArrayList<Int64> {

    }
}
```

