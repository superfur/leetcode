# 1705. 吃苹果的最大数目

## 题目描述

<p>有一棵特殊的苹果树，一连 <code>n</code> 天，每天都可以长出若干个苹果。在第 <code>i</code> 天，树上会长出 <code>apples[i]</code> 个苹果，这些苹果将会在 <code>days[i]</code> 天后（也就是说，第 <code>i + days[i]</code> 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 <code>apples[i] == 0</code> 且 <code>days[i] == 0</code> 表示。</p>

<p>你打算每天 <strong>最多</strong> 吃一个苹果来保证营养均衡。注意，你可以在这 <code>n</code> 天之后继续吃苹果。</p>

<p>给你两个长度为 <code>n</code> 的整数数组 <code>days</code> 和 <code>apples</code> ，返回你可以吃掉的苹果的最大数目<em>。</em></p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>apples = [1,2,3,5,2], days = [3,2,1,4,2]
<strong>输出：</strong>7
<strong>解释：</strong>你可以吃掉 7 个苹果：
- 第一天，你吃掉第一天长出来的苹果。
- 第二天，你吃掉一个第二天长出来的苹果。
- 第三天，你吃掉一个第二天长出来的苹果。过了这一天，第三天长出来的苹果就已经腐烂了。
- 第四天到第七天，你吃的都是第四天长出来的苹果。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
<strong>输出：</strong>5
<strong>解释：</strong>你可以吃掉 5 个苹果：
- 第一天到第三天，你吃的都是第一天长出来的苹果。
- 第四天和第五天不吃苹果。
- 第六天和第七天，你吃的都是第六天长出来的苹果。
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>apples.length == n</code></li>
	<li><code>days.length == n</code></li>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= apples[i], days[i] &lt;= 2 * 10<sup>4</sup></code></li>
	<li>只有在 <code>apples[i] = 0</code> 时，<code>days[i] = 0</code> 才成立</li>
</ul>


## 难度

Medium

## 标签

- 贪心
- 数组
- 堆（优先队列）

## 提示

1. It's optimal to finish the apples that will rot first before those that will rot last
2. You need a structure to keep the apples sorted by their finish time

## 示例

```
[1,2,3,5,2]
[3,2,1,4,2]
[3,0,0,0,0,2]
[3,0,0,0,0,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int eatenApples(vector<int>& apples, vector<int>& days) {
        
    }
};
```

### Java

```java
class Solution {
    public int eatenApples(int[] apples, int[] days) {
        
    }
}
```

### Python

```python
class Solution(object):
    def eatenApples(self, apples, days):
        """
        :type apples: List[int]
        :type days: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        
```

### C

```c
int eatenApples(int* apples, int applesSize, int* days, int daysSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int EatenApples(int[] apples, int[] days) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} apples
 * @param {number[]} days
 * @return {number}
 */
var eatenApples = function(apples, days) {
    
};
```

### TypeScript

```typescript
function eatenApples(apples: number[], days: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $apples
     * @param Integer[] $days
     * @return Integer
     */
    function eatenApples($apples, $days) {
        
    }
}
```

### Swift

```swift
class Solution {
    func eatenApples(_ apples: [Int], _ days: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun eatenApples(apples: IntArray, days: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int eatenApples(List<int> apples, List<int> days) {
    
  }
}
```

### Go

```golang
func eatenApples(apples []int, days []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} apples
# @param {Integer[]} days
# @return {Integer}
def eaten_apples(apples, days)
    
end
```

### Scala

```scala
object Solution {
    def eatenApples(apples: Array[Int], days: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn eaten_apples(apples: Vec<i32>, days: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (eaten-apples apples days)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec eaten_apples(Apples :: [integer()], Days :: [integer()]) -> integer().
eaten_apples(Apples, Days) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec eaten_apples(apples :: [integer], days :: [integer]) :: integer
  def eaten_apples(apples, days) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func eatenApples(apples: Array<Int64>, days: Array<Int64>): Int64 {

    }
}
```

