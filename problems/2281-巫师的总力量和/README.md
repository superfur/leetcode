# 2281. 巫师的总力量和

## 题目描述

<p>作为国王的统治者，你有一支巫师军队听你指挥。</p>

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>strength</code>&nbsp;，其中&nbsp;<code>strength[i]</code>&nbsp;表示第&nbsp;<code>i</code>&nbsp;位巫师的力量值。对于连续的一组巫师（也就是这些巫师的力量值是&nbsp;<code>strength</code>&nbsp;的&nbsp;<strong>子数组</strong>），<strong>总力量</strong>&nbsp;定义为以下两个值的&nbsp;<strong>乘积</strong>&nbsp;：</p>

<ul>
	<li>巫师中 <strong>最弱</strong>&nbsp;的能力值。</li>
	<li>组中所有巫师的个人力量值 <strong>之和</strong>&nbsp;。</li>
</ul>

<p>请你返回 <strong>所有</strong>&nbsp;巫师组的 <strong>总</strong>&nbsp;力量之和。由于答案可能很大，请将答案对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;<strong>取余</strong>&nbsp;后返回。</p>

<p><strong>子数组</strong>&nbsp;是一个数组里 <strong>非空</strong>&nbsp;连续子序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><b>输入：</b>strength = [1,3,1,2]
<b>输出：</b>44
<b>解释：</b>以下是所有连续巫师组：
- [<em><strong>1</strong></em>,3,1,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1
- [1,<em><strong>3</strong></em>,1,2] 中 [3] ，总力量值为 min([3]) * sum([3]) = 3 * 3 = 9
- [1,3,<em><strong>1</strong></em>,2] 中 [1] ，总力量值为 min([1]) * sum([1]) = 1 * 1 = 1
- [1,3,1,<em><strong>2</strong></em>] 中 [2] ，总力量值为 min([2]) * sum([2]) = 2 * 2 = 4
- [<em><strong>1,3</strong></em>,1,2] 中 [1,3] ，总力量值为 min([1,3]) * sum([1,3]) = 1 * 4 = 4
- [1,<em><strong>3,1</strong></em>,2] 中 [3,1] ，总力量值为 min([3,1]) * sum([3,1]) = 1 * 4 = 4
- [1,3,<em><strong>1,2</strong></em>] 中 [1,2] ，总力量值为 min([1,2]) * sum([1,2]) = 1 * 3 = 3
- [<em><strong>1,3,1</strong></em>,2] 中 [1,3,1] ，总力量值为 min([1,3,1]) * sum([1,3,1]) = 1 * 5 = 5
- [1,<em><strong>3,1,2</strong></em>] 中 [3,1,2] ，总力量值为 min([3,1,2]) * sum([3,1,2]) = 1 * 6 = 6
- [<em><strong>1,3,1,2</strong></em>] 中 [1,3,1,2] ，总力量值为 min([1,3,1,2]) * sum([1,3,1,2]) = 1 * 7 = 7
所有力量值之和为 1 + 9 + 1 + 4 + 4 + 4 + 3 + 5 + 6 + 7 = 44 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><b>输入：</b>strength = [5,4,6]
<b>输出：</b>213
<b>解释：</b>以下是所有连续巫师组：
- [<em><strong>5</strong></em>,4,6] 中 [5] ，总力量值为 min([5]) * sum([5]) = 5 * 5 = 25
- [5,<em><strong>4</strong></em>,6] 中 [4] ，总力量值为 min([4]) * sum([4]) = 4 * 4 = 16
- [5,4,<em><strong>6</strong></em>] 中 [6] ，总力量值为 min([6]) * sum([6]) = 6 * 6 = 36
- [<em><strong>5,4</strong></em>,6] 中 [5,4] ，总力量值为 min([5,4]) * sum([5,4]) = 4 * 9 = 36
- [5,<em><strong>4,6</strong></em>] 中 [4,6] ，总力量值为 min([4,6]) * sum([4,6]) = 4 * 10 = 40
- [<em><strong>5,4,6</strong></em>] 中 [5,4,6] ，总力量值为 min([5,4,6]) * sum([5,4,6]) = 4 * 15 = 60
所有力量值之和为 25 + 16 + 36 + 36 + 40 + 60 = 213 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= strength.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= strength[i] &lt;= 10<sup>9</sup></code></li>
</ul>


## 难度

Hard

## 标签

- 栈
- 数组
- 前缀和
- 单调栈

## 提示

1. Consider the contribution of each wizard to the answer.
2. Can you efficiently calculate the total contribution to the answer for all subarrays that end at each index?
3. Denote the total contribution of all subarrays ending at index i as solve[i]. Can you express solve[i] in terms of solve[m] for some m < i?

## 示例

```
[1,3,1,2]
[5,4,6]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int totalStrength(vector<int>& strength) {
        
    }
};
```

### Java

```java
class Solution {
    public int totalStrength(int[] strength) {
        
    }
}
```

### Python

```python
class Solution(object):
    def totalStrength(self, strength):
        """
        :type strength: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        
```

### C

```c
int totalStrength(int* strength, int strengthSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int TotalStrength(int[] strength) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} strength
 * @return {number}
 */
var totalStrength = function(strength) {
    
};
```

### TypeScript

```typescript
function totalStrength(strength: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $strength
     * @return Integer
     */
    function totalStrength($strength) {
        
    }
}
```

### Swift

```swift
class Solution {
    func totalStrength(_ strength: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun totalStrength(strength: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int totalStrength(List<int> strength) {
    
  }
}
```

### Go

```golang
func totalStrength(strength []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} strength
# @return {Integer}
def total_strength(strength)
    
end
```

### Scala

```scala
object Solution {
    def totalStrength(strength: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn total_strength(strength: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (total-strength strength)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec total_strength(Strength :: [integer()]) -> integer().
total_strength(Strength) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec total_strength(strength :: [integer]) :: integer
  def total_strength(strength) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func totalStrength(strength: Array<Int64>): Int64 {

    }
}
```

