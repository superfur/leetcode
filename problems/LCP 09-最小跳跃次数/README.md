# LCP 09. 最小跳跃次数

## 题目描述

<p>为了给刷题的同学一些奖励，力扣团队引入了一个弹簧游戏机。游戏机由 <code>N</code> 个特殊弹簧排成一排，编号为 <code>0</code> 到 <code>N-1</code>。初始有一个小球在编号 <code>0</code> 的弹簧处。若小球在编号为 <code>i</code> 的弹簧处，通过按动弹簧，可以选择把小球向右弹射&nbsp;<code>jump[i]</code> 的距离，或者向左弹射到任意左侧弹簧的位置。也就是说，在编号为 <code>i</code> 弹簧处按动弹簧，小球可以弹向 <code>0</code> 到 <code>i-1</code> 中任意弹簧或者 <code>i+jump[i]</code> 的弹簧（若 <code>i+jump[i]&gt;=N</code> ，则表示小球弹出了机器）。小球位于编号 0 处的弹簧时不能再向左弹。</p>

<p>为了获得奖励，你需要将小球弹出机器。请求出最少需要按动多少次弹簧，可以将小球从编号 <code>0</code> 弹簧弹出整个机器，即向右越过编号 <code>N-1</code> 的弹簧。</p>

<p><strong>示例 1：</strong></p>

<blockquote>
<p>输入：<code>jump = [2, 5, 1, 1, 1, 1]</code></p>

<p>输出：<code>3</code></p>

<p>解释：小 Z 最少需要按动 3 次弹簧，小球依次到达的顺序为 0 -&gt; 2 -&gt; 1 -&gt; 6，最终小球弹出了机器。</p>
</blockquote>

<p><strong>限制：</strong></p>

<ul>
	<li><code>1 &lt;= jump.length &lt;= 10^6</code></li>
	<li><code>1 &lt;= jump[i] &lt;= 10000</code></li>
</ul>


## 难度

Hard

## 标签

- 广度优先搜索
- 线段树
- 数组
- 动态规划

## 示例

```
[2,5,1,1,1,1]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minJump(vector<int>& jump) {

    }
};
```

### Java

```java
class Solution {
    public int minJump(int[] jump) {

    }
}
```

### Python

```python
class Solution(object):
    def minJump(self, jump):
        """
        :type jump: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def minJump(self, jump: List[int]) -> int:
```

### C

```c


int minJump(int* jump, int jumpSize){

}

```

### C#

```csharp
public class Solution {
    public int MinJump(int[] jump) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} jump
 * @return {number}
 */
var minJump = function(jump) {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $jump
     * @return Integer
     */
    function minJump($jump) {

    }
}
```

### Swift

```swift
class Solution {
    func minJump(_ jump: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minJump(jump: IntArray): Int {

    }
}
```

### Go

```golang
func minJump(jump []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} jump
# @return {Integer}
def min_jump(jump)

end
```

### Scala

```scala
object Solution {
    def minJump(jump: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_jump(jump: Vec<i32>) -> i32 {

    }
}
```

