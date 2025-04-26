# 2954. 统计感冒序列的数目

## 题目描述

<p>给你一个整数&nbsp;<code>n</code>&nbsp;和一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>sick</code>&nbsp;，数组按 <strong>升序</strong>&nbsp;排序。</p>

<p>有&nbsp;<code>n</code>&nbsp;位小朋友站成一排，按顺序编号为 <code>0</code>&nbsp;到 <code>n - 1</code>&nbsp;。数组&nbsp;<code>sick</code>&nbsp;包含一开始得了感冒的小朋友的位置。如果位置为&nbsp;<code>i</code>&nbsp;的小朋友得了感冒，他会传染给下标为 <code>i - 1</code>&nbsp;或者 <code>i + 1</code>&nbsp;的小朋友，<strong>前提</strong> 是被传染的小朋友存在且还没有得感冒。每一秒中， <strong>至多一位</strong>&nbsp;还没感冒的小朋友会被传染。</p>

<p>经过有限的秒数后，队列中所有小朋友都会感冒。<strong>感冒序列</strong>&nbsp;指的是 <strong>所有</strong>&nbsp;一开始没有感冒的小朋友最后得感冒的顺序序列。请你返回所有感冒序列的数目。</p>

<p>由于答案可能很大，请你将答案对&nbsp;<code>10<sup>9</sup> + 7</code>&nbsp;取余后返回。</p>

<p><b>注意</b>，感冒序列 <strong>不</strong> 包含一开始就得了感冒的小朋友的下标。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<b>输入：</b>n = 5, sick = [0,4]
<b>输出：</b>4
<b>解释：</b>一开始，下标为 1 ，2 和 3 的小朋友没有感冒。总共有 4 个可能的感冒序列：
- 一开始，下标为 1 和 3 的小朋友可以被传染，因为他们分别挨着有感冒的小朋友 0 和 4 ，令下标为 1 的小朋友先被传染。
然后，下标为 2 的小朋友挨着感冒的小朋友 1 ，下标为 3 的小朋友挨着感冒的小朋友 4 ，两位小朋友都可以被传染，令下标为 2 的小朋友被传染。
最后，下标为 3 的小朋友被传染，因为他挨着感冒的小朋友 2 和 4 ，感冒序列为 [1,2,3] 。
- 一开始，下标为 1 和 3 的小朋友可以被传染，因为他们分别挨着感冒的小朋友 0 和 4 ，令下标为 1 的小朋友先被传染。
然后，下标为 2 的小朋友挨着感冒的小朋友 1 ，下标为 3 的小朋友挨着感冒的小朋友 4 ，两位小朋友都可以被传染，令下标为 3 的小朋友被传染。
最后，下标为 2 的小朋友被传染，因为他挨着感冒的小朋友 1 和 3 ，感冒序列为  [1,3,2] 。
- 感冒序列 [3,1,2] ，被传染的顺序：[<strong><em>0</em></strong>,1,2,3,<strong><em>4</em></strong>] =&gt; [<strong><em>0</em></strong>,1,2,<strong><em>3</em></strong>,<strong><em>4</em></strong>] =&gt; [<strong><em>0</em></strong>,<strong><em>1</em></strong>,2,<em><strong>3</strong></em>,<strong><em>4</em></strong>] =&gt; [<strong><em>0</em></strong>,<strong><em>1</em></strong>,<strong><em>2</em></strong>,<strong><em>3</em></strong>,<strong><em>4</em></strong>] 。
- 感冒序列 [3,2,1] ，被传染的顺序：[<strong><em>0</em></strong>,1,2,3,<strong><em>4</em></strong>] =&gt; [<strong><em>0</em></strong>,1,2,<strong><em>3</em></strong>,<strong><em>4</em></strong>] =&gt; [<strong><em>0</em></strong>,1,<strong><em>2</em></strong>,<strong><em>3</em></strong>,<strong><em>4</em></strong>] =&gt; [<strong><em>0</em></strong>,<strong><em>1</em></strong>,<strong><em>2</em></strong>,<strong><em>3</em></strong>,<strong><em>4</em></strong>] 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<b>输入：</b>n = 4, sick = [1]
<b>输出：</b>3
<b>解释：</b>一开始，下标为 0 ，2 和 3 的小朋友没有感冒。总共有 3 个可能的感冒序列：
- 感冒序列 [0,2,3] ，被传染的顺序：[0,<strong><em>1</em></strong>,2,3] =&gt; [<strong><em>0</em></strong>,<strong><em>1</em></strong>,2,3] =&gt; [<strong><em>0</em></strong>,<strong><em>1</em></strong>,<strong><em>2</em></strong>,3] =&gt; [<strong><em>0</em></strong>,<strong><em>1</em></strong>,<strong><em>2</em></strong>,<strong><em>3</em></strong>] 。
- 感冒序列 [2,0,3] ，被传染的顺序：[0,<strong><em>1</em></strong>,2,3] =&gt; [0,<strong><em>1</em></strong>,<strong><em>2</em></strong>,3] =&gt; [<strong><em>0</em></strong>,<strong><em>1</em></strong>,<strong><em>2</em></strong>,3] =&gt; [<strong><em>0</em></strong>,<strong><em>1</em></strong>,<strong><em>2</em></strong>,<strong><em>3</em></strong>] 。
- 感冒序列 [2,3,0] ，被传染的顺序：[0,<strong><em>1</em></strong>,2,3] =&gt; [0,<strong><em>1</em></strong>,<strong><em>2</em></strong>,3] =&gt; [0,<strong><em>1</em></strong>,<strong><em>2</em></strong>,<strong><em>3</em></strong>] =&gt; [<strong><em>0</em></strong>,<strong><em>1</em></strong>,<strong><em>2</em></strong>,<strong><em>3</em></strong>] 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= sick.length &lt;= n - 1</code></li>
	<li><code>0 &lt;= sick[i] &lt;= n - 1</code></li>
	<li><code>sick</code>&nbsp;按升序排列。</li>
</ul>


## 难度

Hard

## 标签

- 数组
- 数学
- 组合数学

## 提示

1. Consider infected children as <code>0</code> and non-infected as <code>1</code>, then divide the array into segments with the same value.
2. For each segment of non-infected children whose indices are <code>[i, j]</code> and indices <code>(i - 1)</code> and <code>(j + 1)</code>, if they exist, are already infected. Then if <code>i == 0</code> or <code>j == n - 1</code>, each second there is only one kid that can be infected (which is at the other endpoint).
3. If <code>i > 0</code> and <code>j < n - 1</code>, we have two choices per second since the children at the two endpoints can both be the infect candidates. So there are <code>2<sup>j - i</sup></code> orders to infect all children in the segment.
4. Each second we can select a segment and select one endpoint from it.
5. The answer is: 
<code>S! / (len[1]! * len[2]! * ... * len[m]! * len<sub>start</sub>! * len<sub>end</sub>!) * 2<sup>k</sup></code> 
where <code>len[1], len[2], ..., len[m]</code> are the lengths of each segment of non-infected children that have an infected child at both endpoints, <code>len<sub>start</sub></code> and <code>len<sub>end</sub></code> denote the number of non-infected children with infected child at one endpoint, <code>S</code> is the total length of all segments of non-infected children, and <code>k = (len[1] - 1) + (len[2] - 1) + ... + (len[m] - 1)</code>.

## 示例

```
5
[0,4]
4
[1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfSequence(int n, vector<int>& sick) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfSequence(int n, int[] sick) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfSequence(self, n, sick):
        """
        :type n: int
        :type sick: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        
```

### C

```c
int numberOfSequence(int n, int* sick, int sickSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfSequence(int n, int[] sick) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} sick
 * @return {number}
 */
var numberOfSequence = function(n, sick) {
    
};
```

### TypeScript

```typescript
function numberOfSequence(n: number, sick: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $sick
     * @return Integer
     */
    function numberOfSequence($n, $sick) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfSequence(_ n: Int, _ sick: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfSequence(n: Int, sick: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfSequence(int n, List<int> sick) {
    
  }
}
```

### Go

```golang
func numberOfSequence(n int, sick []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} sick
# @return {Integer}
def number_of_sequence(n, sick)
    
end
```

### Scala

```scala
object Solution {
    def numberOfSequence(n: Int, sick: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_sequence(n: i32, sick: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-sequence n sick)
  (-> exact-integer? (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_sequence(N :: integer(), Sick :: [integer()]) -> integer().
number_of_sequence(N, Sick) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_sequence(n :: integer, sick :: [integer]) :: integer
  def number_of_sequence(n, sick) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfSequence(n: Int64, sick: Array<Int64>): Int64 {

    }
}
```

