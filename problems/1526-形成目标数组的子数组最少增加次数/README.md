# 1526. 形成目标数组的子数组最少增加次数

## 题目描述

<p>给你一个整数数组&nbsp;<code>target</code>&nbsp;和一个数组&nbsp;<code>initial</code>&nbsp;，<code>initial</code>&nbsp;数组与 <code>target</code>&nbsp; 数组有同样的维度，且一开始全部为 0 。</p>

<p>请你返回从 <code>initial</code>&nbsp;得到&nbsp; <code>target</code>&nbsp;的最少操作次数，每次操作需遵循以下规则：</p>

<ul>
	<li>在 <code>initial</code>&nbsp;中选择 <strong>任意</strong>&nbsp;子数组，并将子数组中每个元素增加 1 。</li>
</ul>

<p>答案保证在 32 位有符号整数以内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>target = [1,2,3,2,1]
<strong>输出：</strong>3
<strong>解释：</strong>我们需要至少 3 次操作从 intial 数组得到 target 数组。
[0,0,0,0,0] 将下标为 0 到 4&nbsp;的元素（包含二者）加 1 。
[1,1,1,1,1] 将下标为 1 到 3 的元素（包含二者）加 1 。
[1,2,2,2,1] 将下表为 2 的元素增加 1 。
[1,2,3,2,1] 得到了目标数组。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>target = [3,1,1,2]
<strong>输出：</strong>4
<strong>解释：</strong>(initial)[0,0,0,0] -&gt; [1,1,1,1] -&gt; [1,1,1,2] -&gt; [2,1,1,2] -&gt; [3,1,1,2] (target) 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>target = [3,1,5,4,2]
<strong>输出：</strong>7
<strong>解释：</strong>(initial)[0,0,0,0,0] -&gt; [1,1,1,1,1] -&gt; [2,1,1,1,1] -&gt; [3,1,1,1,1] 
                                  -&gt; [3,1,2,2,2] -&gt; [3,1,3,3,2] -&gt; [3,1,4,4,2] -&gt; [3,1,5,4,2] (target)。
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>target = [1,1,1,1]
<strong>输出：</strong>1
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= target.length &lt;= 10^5</code></li>
	<li><code>1 &lt;= target[i] &lt;= 10^5</code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 贪心
- 数组
- 动态规划
- 单调栈

## 提示

1. For a given range of values in target, an optimal strategy is to increment the entire range by the minimum value. The minimum in a range could be obtained with Range minimum query or Segment trees algorithm.

## 示例

```
[1,2,3,2,1]
[3,1,1,2]
[3,1,5,4,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minNumberOperations(vector<int>& target) {
        
    }
};
```

### Java

```java
class Solution {
    public int minNumberOperations(int[] target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minNumberOperations(self, target):
        """
        :type target: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        
```

### C

```c
int minNumberOperations(int* target, int targetSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinNumberOperations(int[] target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} target
 * @return {number}
 */
var minNumberOperations = function(target) {
    
};
```

### TypeScript

```typescript
function minNumberOperations(target: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $target
     * @return Integer
     */
    function minNumberOperations($target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minNumberOperations(_ target: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minNumberOperations(target: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minNumberOperations(List<int> target) {
    
  }
}
```

### Go

```golang
func minNumberOperations(target []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} target
# @return {Integer}
def min_number_operations(target)
    
end
```

### Scala

```scala
object Solution {
    def minNumberOperations(target: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_number_operations(target: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-number-operations target)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_number_operations(Target :: [integer()]) -> integer().
min_number_operations(Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_number_operations(target :: [integer]) :: integer
  def min_number_operations(target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minNumberOperations(target: Array<Int64>): Int64 {

    }
}
```

