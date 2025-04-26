# 1054. 距离相等的条形码

## 题目描述

<p>在一个仓库里，有一排条形码，其中第 <code>i</code> 个条形码为&nbsp;<code>barcodes[i]</code>。</p>

<p>请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>barcodes = [1,1,1,2,2,2]
<strong>输出：</strong>[2,1,2,1,2,1]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>barcodes = [1,1,1,1,2,2,3,3]
<strong>输出：</strong>[1,3,1,3,2,1,2,1]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= barcodes.length &lt;= 10000</code></li>
	<li><code>1 &lt;= barcodes[i] &lt;= 10000</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 哈希表
- 计数
- 排序
- 堆（优先队列）

## 提示

1. We want to always choose the most common or second most common element to write next.  What data structure allows us to query this effectively?

## 示例

```
[1,1,1,2,2,2]
[1,1,1,1,2,2,3,3]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] rearrangeBarcodes(int[] barcodes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* rearrangeBarcodes(int* barcodes, int barcodesSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] RearrangeBarcodes(int[] barcodes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} barcodes
 * @return {number[]}
 */
var rearrangeBarcodes = function(barcodes) {
    
};
```

### TypeScript

```typescript
function rearrangeBarcodes(barcodes: number[]): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $barcodes
     * @return Integer[]
     */
    function rearrangeBarcodes($barcodes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func rearrangeBarcodes(_ barcodes: [Int]) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun rearrangeBarcodes(barcodes: IntArray): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> rearrangeBarcodes(List<int> barcodes) {
    
  }
}
```

### Go

```golang
func rearrangeBarcodes(barcodes []int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} barcodes
# @return {Integer[]}
def rearrange_barcodes(barcodes)
    
end
```

### Scala

```scala
object Solution {
    def rearrangeBarcodes(barcodes: Array[Int]): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn rearrange_barcodes(barcodes: Vec<i32>) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (rearrange-barcodes barcodes)
  (-> (listof exact-integer?) (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec rearrange_barcodes(Barcodes :: [integer()]) -> [integer()].
rearrange_barcodes(Barcodes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec rearrange_barcodes(barcodes :: [integer]) :: [integer]
  def rearrange_barcodes(barcodes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func rearrangeBarcodes(barcodes: Array<Int64>): Array<Int64> {

    }
}
```

