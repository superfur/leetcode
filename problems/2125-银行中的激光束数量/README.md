# 2125. 银行中的激光束数量

## 题目描述

<p>银行内部的防盗安全装置已经激活。给你一个下标从 <strong>0</strong> 开始的二进制字符串数组 <code>bank</code> ，表示银行的平面图，这是一个大小为 <code>m x n</code> 的二维矩阵。 <code>bank[i]</code> 表示第 <code>i</code> 行的设备分布，由若干 <code>'0'</code> 和若干 <code>'1'</code> 组成。<code>'0'</code> 表示单元格是空的，而 <code>'1'</code> 表示单元格有一个安全设备。</p>

<p>对任意两个安全设备而言，<strong>如果</strong><strong>同时</strong> 满足下面两个条件，则二者之间存在 <strong>一个</strong> 激光束：</p>

<ul>
	<li>两个设备位于两个 <strong>不同行</strong> ：<code>r<sub>1</sub></code> 和 <code>r<sub>2</sub></code> ，其中 <code>r<sub>1</sub> &lt; r<sub>2</sub></code> 。</li>
	<li>满足&nbsp;<code>r<sub>1</sub> &lt; i &lt; r<sub>2</sub></code>&nbsp;的 <strong>所有&nbsp;</strong>行&nbsp;<code>i</code>&nbsp;，都&nbsp;<strong>没有安全设备</strong> 。</li>
</ul>

<p>激光束是独立的，也就是说，一个激光束既不会干扰另一个激光束，也不会与另一个激光束合并成一束。</p>

<p>返回银行中激光束的总数量。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/laser1.jpg" style="width: 400px; height: 368px;" /></p>

<pre>
<strong>输入：</strong>bank = ["011001","000000","010100","001000"]
<strong>输出：</strong>8
<strong>解释：</strong>在下面每组设备对之间，存在一条激光束。总共是 8 条激光束：
 * bank[0][1] -- bank[2][1]
 * bank[0][1] -- bank[2][3]
 * bank[0][2] -- bank[2][1]
 * bank[0][2] -- bank[2][3]
 * bank[0][5] -- bank[2][1]
 * bank[0][5] -- bank[2][3]
 * bank[2][1] -- bank[3][2]
 * bank[2][3] -- bank[3][2]
注意，第 0 行和第 3 行上的设备之间不存在激光束。
这是因为第 2 行存在安全设备，这不满足第 2 个条件。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/laser2.jpg" style="width: 244px; height: 325px;" /></p>

<pre>
<strong>输入：</strong>bank = ["000","111","000"]
<strong>输出：</strong>0
<strong>解释：</strong>不存在两个位于不同行的设备
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == bank.length</code></li>
	<li><code>n == bank[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>bank[i][j]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 数学
- 字符串
- 矩阵

## 提示

1. What is the commonality between security devices on the same row?
2. Each device on the same row has the same number of beams pointing towards the devices on the next row with devices.
3. If you were given an integer array where each element is the number of security devices on each row, can you solve it?
4. Convert the input to such an array, skip any row with no security device, then find the sum of the product between adjacent elements.

## 示例

```
["011001","000000","010100","001000"]
["000","111","000"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int numberOfBeams(vector<string>& bank) {
        
    }
};
```

### Java

```java
class Solution {
    public int numberOfBeams(String[] bank) {
        
    }
}
```

### Python

```python
class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
```

### C

```c
int numberOfBeams(char** bank, int bankSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int NumberOfBeams(string[] bank) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} bank
 * @return {number}
 */
var numberOfBeams = function(bank) {
    
};
```

### TypeScript

```typescript
function numberOfBeams(bank: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $bank
     * @return Integer
     */
    function numberOfBeams($bank) {
        
    }
}
```

### Swift

```swift
class Solution {
    func numberOfBeams(_ bank: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun numberOfBeams(bank: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int numberOfBeams(List<String> bank) {
    
  }
}
```

### Go

```golang
func numberOfBeams(bank []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} bank
# @return {Integer}
def number_of_beams(bank)
    
end
```

### Scala

```scala
object Solution {
    def numberOfBeams(bank: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn number_of_beams(bank: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (number-of-beams bank)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec number_of_beams(Bank :: [unicode:unicode_binary()]) -> integer().
number_of_beams(Bank) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec number_of_beams(bank :: [String.t]) :: integer
  def number_of_beams(bank) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func numberOfBeams(bank: Array<String>): Int64 {

    }
}
```

