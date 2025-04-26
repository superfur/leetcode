# 2611. 老鼠和奶酪

## 题目描述

<p>有两只老鼠和&nbsp;<code>n</code>&nbsp;块不同类型的奶酪，每块奶酪都只能被其中一只老鼠吃掉。</p>

<p>下标为 <code>i</code>&nbsp;处的奶酪被吃掉的得分为：</p>

<ul>
	<li>如果第一只老鼠吃掉，则得分为&nbsp;<code>reward1[i]</code>&nbsp;。</li>
	<li>如果第二只老鼠吃掉，则得分为&nbsp;<code>reward2[i]</code>&nbsp;。</li>
</ul>

<p>给你一个正整数数组&nbsp;<code>reward1</code>&nbsp;，一个正整数数组&nbsp;<code>reward2</code>&nbsp;，和一个非负整数&nbsp;<code>k</code>&nbsp;。</p>

<p>请你返回第一只老鼠恰好吃掉 <code>k</code>&nbsp;块奶酪的情况下，<strong>最大</strong>&nbsp;得分为多少。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2
<b>输出：</b>15
<b>解释：</b>这个例子中，第一只老鼠吃掉第 2&nbsp;和 3 块奶酪（下标从 0 开始），第二只老鼠吃掉第 0 和 1 块奶酪。
总得分为 4 + 4 + 3 + 4 = 15 。
15 是最高得分。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>reward1 = [1,1], reward2 = [1,1], k = 2
<b>输出：</b>2
<b>解释：</b>这个例子中，第一只老鼠吃掉第 0 和 1 块奶酪（下标从 0 开始），第二只老鼠不吃任何奶酪。
总得分为 1 + 1 = 2 。
2 是最高得分。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == reward1.length == reward2.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= reward1[i],&nbsp;reward2[i] &lt;= 1000</code></li>
	<li><code>0 &lt;= k &lt;= n</code></li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 排序
- 堆（优先队列）

## 提示

1. The intended solution uses greedy approach.
2. Imagine at first that the second mouse eats all the cheese, then we should choose k types of cheese with the maximum sum of - reward2[i] + reward1[i].

## 示例

```
[1,1,3,4]
[4,4,1,1]
2
[1,1]
[1,1]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int miceAndCheese(vector<int>& reward1, vector<int>& reward2, int k) {
        
    }
};
```

### Java

```java
class Solution {
    public int miceAndCheese(int[] reward1, int[] reward2, int k) {
        
    }
}
```

### Python

```python
class Solution(object):
    def miceAndCheese(self, reward1, reward2, k):
        """
        :type reward1: List[int]
        :type reward2: List[int]
        :type k: int
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        
```

### C

```c
int miceAndCheese(int* reward1, int reward1Size, int* reward2, int reward2Size, int k) {
    
}
```

### C#

```csharp
public class Solution {
    public int MiceAndCheese(int[] reward1, int[] reward2, int k) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} reward1
 * @param {number[]} reward2
 * @param {number} k
 * @return {number}
 */
var miceAndCheese = function(reward1, reward2, k) {
    
};
```

### TypeScript

```typescript
function miceAndCheese(reward1: number[], reward2: number[], k: number): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $reward1
     * @param Integer[] $reward2
     * @param Integer $k
     * @return Integer
     */
    function miceAndCheese($reward1, $reward2, $k) {
        
    }
}
```

### Swift

```swift
class Solution {
    func miceAndCheese(_ reward1: [Int], _ reward2: [Int], _ k: Int) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun miceAndCheese(reward1: IntArray, reward2: IntArray, k: Int): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int miceAndCheese(List<int> reward1, List<int> reward2, int k) {
    
  }
}
```

### Go

```golang
func miceAndCheese(reward1 []int, reward2 []int, k int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} reward1
# @param {Integer[]} reward2
# @param {Integer} k
# @return {Integer}
def mice_and_cheese(reward1, reward2, k)
    
end
```

### Scala

```scala
object Solution {
    def miceAndCheese(reward1: Array[Int], reward2: Array[Int], k: Int): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn mice_and_cheese(reward1: Vec<i32>, reward2: Vec<i32>, k: i32) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (mice-and-cheese reward1 reward2 k)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer? exact-integer?)
  )
```

### Erlang

```erlang
-spec mice_and_cheese(Reward1 :: [integer()], Reward2 :: [integer()], K :: integer()) -> integer().
mice_and_cheese(Reward1, Reward2, K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec mice_and_cheese(reward1 :: [integer], reward2 :: [integer], k :: integer) :: integer
  def mice_and_cheese(reward1, reward2, k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func miceAndCheese(reward1: Array<Int64>, reward2: Array<Int64>, k: Int64): Int64 {

    }
}
```

