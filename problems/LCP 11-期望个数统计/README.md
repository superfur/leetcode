# LCP 11. 期望个数统计

## 题目描述

<p>某互联网公司一年一度的春招开始了，一共有 <code>n</code> 名面试者入选。每名面试者都会提交一份简历，公司会根据提供的简历资料产生一个预估的能力值，数值越大代表越有可能通过面试。</p>

<p>小 A 和小 B 负责审核面试者，他们均有所有面试者的简历，并且将各自根据面试者能力值从大到小的顺序浏览。由于简历事先被打乱过，能力值相同的简历的出现顺序是从它们的全排列中<strong>等可能</strong>地取一个。现在给定 <code>n</code> 名面试者的能力值 <code>scores</code>，设 <code>X</code> 代表小 A 和小 B 的浏览顺序中出现在同一位置的简历数，求 <code>X</code> 的期望。</p>

<p>提示：离散的非负随机变量的期望计算公式为 <img alt="1" src="http://latex.codecogs.com/svg.latex?E%28X%29%3D%5Csum_%7Bk%3D1%7D%5E%7B%5Cinfty%7D%20k%20%5CPr%28X%20%3D%20k%29" />。在本题中，由于 <code>X</code> 的取值为 0 到 <code>n</code> 之间，期望计算公式可以是 <img alt="2" src="http://latex.codecogs.com/svg.latex?E%28X%29%3D%5Csum_%7Bk%3D1%7D%5E%7Bn%7D%20k%20%5CPr%28X%20%3D%20k%29" />。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>scores = [1,2,3]</code></p>

<p>输出：<code>3</code></p>

<p>解释：由于面试者能力值互不相同，小 A 和小 B 的浏览顺序一定是相同的。<code>X</code>的期望是 3 。</p>
</blockquote>

<p><strong>示例 2：</strong></p>

<blockquote>
<p>输入：<code>scores = [1,1]</code></p>

<p>输出：<code>1</code></p>

<p>解释：设两位面试者的编号为 0, 1。由于他们的能力值都是 1，小 A 和小 B 的浏览顺序都为从全排列 <code>[[0,1],[1,0]]</code> 中等可能地取一个。如果小 A 和小 B 的浏览顺序都是 <code>[0,1]</code> 或者 <code>[1,0]</code> ，那么出现在同一位置的简历数为 2 ，否则是 0 。所以 <code>X</code> 的期望是 (2+0+2+0) * 1/4 = 1</p>
</blockquote>

<p><strong>示例 3：</strong></p>

<blockquote>
<p>输入：<code>scores = [1,1,2]</code></p>

<p>输出：<code>2</code></p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= scores.length &lt;= 10^5</code></li>
	<li><code>0 &lt;= scores[i] &lt;= 10^6</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表
- 数学
- 概率与统计

## 示例

```
[1,2,3]
[1,1]
[1,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int expectNumber(vector<int>& scores) {

    }
};
```

### Java

```java
class Solution {
    public int expectNumber(int[] scores) {

    }
}
```

### Python

```python
class Solution(object):
    def expectNumber(self, scores):
        """
        :type scores: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def expectNumber(self, scores: List[int]) -> int:
```

### C

```c


int expectNumber(int* scores, int scoresSize){

}
```

### C#

```csharp
public class Solution {
    public int ExpectNumber(int[] scores) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} scores
 * @return {number}
 */
var expectNumber = function(scores) {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $scores
     * @return Integer
     */
    function expectNumber($scores) {

    }
}
```

### Swift

```swift
class Solution {
    func expectNumber(_ scores: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun expectNumber(scores: IntArray): Int {

    }
}
```

### Go

```golang
func expectNumber(scores []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} scores
# @return {Integer}
def expect_number(scores)

end
```

### Scala

```scala
object Solution {
    def expectNumber(scores: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn expect_number(scores: Vec<i32>) -> i32 {

    }
}
```

