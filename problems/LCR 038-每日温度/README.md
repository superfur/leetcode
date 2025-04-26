# LCR 038. 每日温度

## 题目描述

<p>请根据每日 <code>气温</code> 列表 <code>temperatures</code>&nbsp;，重新生成一个列表，要求其对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用&nbsp;<code>0</code> 来代替。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>temperatures = [73,74,75,71,69,72,76,73]
<strong>输出：</strong>[1,1,4,2,1,1,0,0]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>temperatures = [30,40,50,60]
<strong>输出：</strong>[1,1,1,0]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>temperatures = [30,60,90]
<strong>输出：</strong>[1,1,0]</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;temperatures.length &lt;= 10<sup>5</sup></code></li>
	<li><code>30 &lt;=&nbsp;temperatures[i]&nbsp;&lt;= 100</code></li>
</ul>

<p>&nbsp;</p>

<p><meta charset="UTF-8" />注意：本题与主站 739&nbsp;题相同：&nbsp;<a href="https://leetcode-cn.com/problems/daily-temperatures/">https://leetcode-cn.com/problems/daily-temperatures/</a></p>


## 难度

Medium

## 标签

- 栈
- 数组
- 单调栈

## 示例

```
[73,74,75,71,69,72,76,73]
[30,40,50,60]
[30,60,90]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {

    }
};
```

### Java

```java
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {

    }
}
```

### Python

```python
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
```

### Python3

```python3
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
```

### C

```c


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* dailyTemperatures(int* temperatures, int temperaturesSize, int* returnSize){

}
```

### C#

```csharp
public class Solution {
    public int[] DailyTemperatures(int[] temperatures) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function(temperatures) {

};
```

### TypeScript

```typescript
function dailyTemperatures(temperatures: number[]): number[] {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $temperatures
     * @return Integer[]
     */
    function dailyTemperatures($temperatures) {

    }
}
```

### Swift

```swift
class Solution {
    func dailyTemperatures(_ temperatures: [Int]) -> [Int] {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun dailyTemperatures(temperatures: IntArray): IntArray {

    }
}
```

### Go

```golang
func dailyTemperatures(temperatures []int) []int {

}
```

### Ruby

```ruby
# @param {Integer[]} temperatures
# @return {Integer[]}
def daily_temperatures(temperatures)

end
```

### Scala

```scala
object Solution {
    def dailyTemperatures(temperatures: Array[Int]): Array[Int] = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {

    }
}
```

### Racket

```racket
(define/contract (daily-temperatures temperatures)
  (-> (listof exact-integer?) (listof exact-integer?))

  )
```

### Erlang

```erlang
-spec daily_temperatures(Temperatures :: [integer()]) -> [integer()].
daily_temperatures(Temperatures) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec daily_temperatures(temperatures :: [integer]) :: [integer]
  def daily_temperatures(temperatures) do

  end
end
```

