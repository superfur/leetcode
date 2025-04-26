# 2028. 找出缺失的观测数据

## 题目描述

<p>现有一份 <code>n + m</code>&nbsp;次投掷单个<strong> 六面</strong> 骰子的观测数据，骰子的每个面从 <code>1</code> 到 <code>6</code> 编号。观测数据中缺失了 <code>n</code> 份，你手上只拿到剩余&nbsp;<code>m</code> 次投掷的数据。幸好你有之前计算过的这 <code>n + m</code> 次投掷数据的 <strong>平均值</strong> 。</p>

<p>给你一个长度为 <code>m</code> 的整数数组 <code>rolls</code> ，其中&nbsp;<code>rolls[i]</code> 是第 <code>i</code> 次观测的值。同时给你两个整数 <code>mean</code> 和 <code>n</code> 。</p>

<p>返回一个长度为<em> </em><code>n</code><em> </em>的数组，包含所有缺失的观测数据，且满足这<em> </em><code>n + m</code><em> </em>次投掷的 <strong>平均值</strong> 是<em> </em><code>mean</code> 。如果存在多组符合要求的答案，只需要返回其中任意一组即可。如果不存在答案，返回一个空数组。</p>

<p><code>k</code>&nbsp;个数字的 <strong>平均值</strong> 为这些数字求和后再除以&nbsp;<code>k</code> 。</p>

<p>注意 <code>mean</code> 是一个整数，所以 <code>n + m</code> 次投掷的总和需要被&nbsp;<code>n + m</code>&nbsp;整除。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>rolls = [3,2,4,3], mean = 4, n = 2
<strong>输出：</strong>[6,6]
<strong>解释：</strong>所有 n + m 次投掷的平均值是 (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>rolls = [1,5,6], mean = 3, n = 4
<strong>输出：</strong>[2,3,2,2]
<strong>解释：</strong>所有 n + m 次投掷的平均值是 (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>rolls = [1,2,3,4], mean = 6, n = 4
<strong>输出：</strong>[]
<strong>解释：</strong>无论丢失的 4 次数据是什么，平均值都不可能是 6 。
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>rolls = [1], mean = 3, n = 1
<strong>输出：</strong>[5]
<strong>解释：</strong>所有 n + m 次投掷的平均值是 (1 + 5) / 2 = 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == rolls.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= rolls[i], mean &lt;= 6</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 模拟

## 提示

1. What should the sum of the n rolls be?
2. Could you generate an array of size n such that each element is between 1 and 6?

## 示例

```
[3,2,4,3]
4
2
[1,5,6]
3
4
[1,2,3,4]
6
4
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        
    }
}
```

### Python

```python
class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* missingRolls(int* rolls, int rollsSize, int mean, int n, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MissingRolls(int[] rolls, int mean, int n) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} rolls
 * @param {number} mean
 * @param {number} n
 * @return {number[]}
 */
var missingRolls = function(rolls, mean, n) {
    
};
```

### TypeScript

```typescript
function missingRolls(rolls: number[], mean: number, n: number): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $rolls
     * @param Integer $mean
     * @param Integer $n
     * @return Integer[]
     */
    function missingRolls($rolls, $mean, $n) {
        
    }
}
```

### Swift

```swift
class Solution {
    func missingRolls(_ rolls: [Int], _ mean: Int, _ n: Int) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun missingRolls(rolls: IntArray, mean: Int, n: Int): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> missingRolls(List<int> rolls, int mean, int n) {
    
  }
}
```

### Go

```golang
func missingRolls(rolls []int, mean int, n int) []int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} rolls
# @param {Integer} mean
# @param {Integer} n
# @return {Integer[]}
def missing_rolls(rolls, mean, n)
    
end
```

### Scala

```scala
object Solution {
    def missingRolls(rolls: Array[Int], mean: Int, n: Int): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn missing_rolls(rolls: Vec<i32>, mean: i32, n: i32) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (missing-rolls rolls mean n)
  (-> (listof exact-integer?) exact-integer? exact-integer? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec missing_rolls(Rolls :: [integer()], Mean :: integer(), N :: integer()) -> [integer()].
missing_rolls(Rolls, Mean, N) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec missing_rolls(rolls :: [integer], mean :: integer, n :: integer) :: [integer]
  def missing_rolls(rolls, mean, n) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func missingRolls(rolls: Array<Int64>, mean: Int64, n: Int64): Array<Int64> {

    }
}
```

