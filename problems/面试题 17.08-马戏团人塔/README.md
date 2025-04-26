# 面试题 17.08. 马戏团人塔

## 题目描述

<p>有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
<strong>输出：</strong>6
<strong>解释：</strong>从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>height.length == weight.length <= 10000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 二分查找
- 动态规划
- 排序

## 提示

1. 这个问题要求我们找出可以构建的最长的序列对，使其每个序列都在不断增长。如果你只需要一个元素不断增长呢?
2. 如果你只需要序列对中的一个元素为递增序列，那么只对该序列排序就好了。你的最长序列实际上是所有序列对(而不是重复的序列，因为最长序列是需要严格递增的)。对于最初的问题，这说明了什么?
3. 如果你根据高度对值进行排序，那么这将告诉你最后序列对的排序。最长序列必定符合这个相对顺序(但不一定包含所有的序列对)。现在只需要找到权重尺度上的最长递增子序列，并保持这些项的相对顺序不变。这本质上与下面的问题相同:对于一个整数数组找到最长的序列(不重新排序)。
4. 尝试用递归方法来评估所有的可能性。
5. 另一种思考这个问题的方法是:如果有结束于 A[0]到 A[n-1]每个元素的最长序列，你能用它来找出结束于元素 A[n]的最长序列吗?

## 示例

```
[65,70,56,75,60,68]
[100,150,90,190,95,110]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int bestSeqAtIndex(vector<int>& height, vector<int>& weight) {
        
    }
};
```

### Java

```java
class Solution {
    public int bestSeqAtIndex(int[] height, int[] weight) {
        
    }
}
```

### Python

```python
class Solution(object):
    def bestSeqAtIndex(self, height, weight):
        """
        :type height: List[int]
        :type weight: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        
```

### C

```c
int bestSeqAtIndex(int* height, int heightSize, int* weight, int weightSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int BestSeqAtIndex(int[] height, int[] weight) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} height
 * @param {number[]} weight
 * @return {number}
 */
var bestSeqAtIndex = function(height, weight) {
    
};
```

### TypeScript

```typescript
function bestSeqAtIndex(height: number[], weight: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $height
     * @param Integer[] $weight
     * @return Integer
     */
    function bestSeqAtIndex($height, $weight) {
        
    }
}
```

### Swift

```swift
class Solution {
    func bestSeqAtIndex(_ height: [Int], _ weight: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun bestSeqAtIndex(height: IntArray, weight: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int bestSeqAtIndex(List<int> height, List<int> weight) {
    
  }
}
```

### Go

```golang
func bestSeqAtIndex(height []int, weight []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} height
# @param {Integer[]} weight
# @return {Integer}
def best_seq_at_index(height, weight)
    
end
```

### Scala

```scala
object Solution {
    def bestSeqAtIndex(height: Array[Int], weight: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn best_seq_at_index(height: Vec<i32>, weight: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (best-seq-at-index height weight)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec best_seq_at_index(Height :: [integer()], Weight :: [integer()]) -> integer().
best_seq_at_index(Height, Weight) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec best_seq_at_index(height :: [integer], weight :: [integer]) :: integer
  def best_seq_at_index(height, weight) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func bestSeqAtIndex(height: Array<Int64>, weight: Array<Int64>): Int64 {

    }
}
```

