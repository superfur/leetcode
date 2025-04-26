# 1354. 多次求和构造目标数组

## 题目描述

<p>给你一个整数数组&nbsp;<code>target</code> 。一开始，你有一个数组&nbsp;<code>A</code> ，它的所有元素均为 1 ，你可以执行以下操作：</p>

<ul>
	<li>令&nbsp;<code>x</code>&nbsp;为你数组里所有元素的和</li>
	<li>选择满足&nbsp;<code>0 &lt;= i &lt; target.size</code>&nbsp;的任意下标&nbsp;<code>i</code>&nbsp;，并让&nbsp;<code>A</code>&nbsp;数组里下标为&nbsp;<code>i</code>&nbsp;处的值为&nbsp;<code>x</code>&nbsp;。</li>
	<li>你可以重复该过程任意次</li>
</ul>

<p>如果能从&nbsp;<code>A</code>&nbsp;开始构造出目标数组&nbsp;<code>target</code>&nbsp;，请你返回 True ，否则返回 False 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>target = [9,3,5]
<strong>输出：</strong>true
<strong>解释：</strong>从 [1, 1, 1] 开始
[1, 1, 1], 和为 3 ，选择下标 1
[1, 3, 1], 和为 5， 选择下标 2
[1, 3, 5], 和为 9， 选择下标 0
[9, 3, 5] 完成
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>target = [1,1,1,2]
<strong>输出：</strong>false
<strong>解释：</strong>不可能从 [1,1,1,1] 出发构造目标数组。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>target = [8,5]
<strong>输出：</strong>true
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>N == target.length</code></li>
	<li><code>1 &lt;= target.length&nbsp;&lt;= 5 * 10^4</code></li>
	<li><code>1 &lt;= target[i] &lt;= 10^9</code></li>
</ul>


## 难度

Hard

## 标签

- 数组
- 堆（优先队列）

## 提示

1. Given that the sum is strictly increasing, the largest element in the target must be formed in the last step by adding the total sum in the previous step. Thus, we can simulate the process in a reversed way.
2. Subtract the largest with the rest of the array, and put the new element into the array. Repeat until all elements become one

## 示例

```
[9,3,5]
[1,1,1,2]
[8,5]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isPossible(vector<int>& target) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isPossible(int[] target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isPossible(self, target):
        """
        :type target: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        
```

### C

```c
bool isPossible(int* target, int targetSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsPossible(int[] target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} target
 * @return {boolean}
 */
var isPossible = function(target) {
    
};
```

### TypeScript

```typescript
function isPossible(target: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $target
     * @return Boolean
     */
    function isPossible($target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isPossible(_ target: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isPossible(target: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isPossible(List<int> target) {
    
  }
}
```

### Go

```golang
func isPossible(target []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} target
# @return {Boolean}
def is_possible(target)
    
end
```

### Scala

```scala
object Solution {
    def isPossible(target: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_possible(target: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-possible target)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec is_possible(Target :: [integer()]) -> boolean().
is_possible(Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_possible(target :: [integer]) :: boolean
  def is_possible(target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isPossible(target: Array<Int64>): Bool {

    }
}
```

