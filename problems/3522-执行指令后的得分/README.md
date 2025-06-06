# 3522. 执行指令后的得分

## 题目描述

<p>给你两个数组：<code>instructions</code> 和 <code>values</code>，数组的长度均为 <code>n</code>。</p>

<p>你需要根据以下规则模拟一个过程：</p>

<ul>
	<li>从下标&nbsp;<code>i = 0</code> 的第一个指令开始，初始得分为 0。</li>
	<li>如果 <code>instructions[i]</code> 是 <code>"add"</code>：
	<ul>
		<li>将 <code>values[i]</code> 加到你的得分中。</li>
		<li>移动到下一个指令 <code>(i + 1)</code>。</li>
	</ul>
	</li>
	<li>如果 <code>instructions[i]</code> 是 <code>"jump"</code>：
	<ul>
		<li>移动到下标为&nbsp;<code>(i + values[i])</code> 的指令，但不修改你的得分。</li>
	</ul>
	</li>
</ul>

<p>当以下任一情况发生时，过程会终止：</p>

<ul>
	<li>越界（即 <code>i &lt; 0</code> 或 <code>i &gt;= n</code>），或</li>
	<li>尝试再次执行已经执行过的指令。被重复访问的指令不会再次执行。</li>
</ul>

<p>返回过程结束时的得分。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">instructions = ["jump","add","add","jump","add","jump"], values = [2,1,3,1,-2,-3]</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>从下标&nbsp;0 开始模拟过程：</p>

<ul>
	<li>下标 0：指令是 <code>"jump"</code>，移动到下标&nbsp;<code>0 + 2 = 2</code>。</li>
	<li>下标 2：指令是 <code>"add"</code>，将 <code>values[2] = 3</code> 加到得分中，移动到下标&nbsp;3。得分变为 3。</li>
	<li>下标 3：指令是 <code>"jump"</code>，移动到下标&nbsp;<code>3 + 1 = 4</code>。</li>
	<li>下标 4：指令是 <code>"add"</code>，将 <code>values[4] = -2</code> 加到得分中，移动到下标&nbsp;5。得分变为 1。</li>
	<li>下标 5：指令是 <code>"jump"</code>，移动到下标&nbsp;<code>5 + (-3) = 2</code>。</li>
	<li>下标 2：已经访问过。过程结束。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">instructions = ["jump","add","add"], values = [3,1,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>从下标&nbsp;0 开始模拟过程：</p>

<ul>
	<li>下标 0：指令是 <code>"jump"</code>，移动到下标&nbsp;<code>0 + 3 = 3</code>。</li>
	<li>下标 3：越界。过程结束。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">instructions = ["jump"], values = [0]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>从下标&nbsp;0 开始模拟过程：</p>

<ul>
	<li>下标 0：指令是 <code>"jump"</code>，移动到下标&nbsp;<code>0 + 0 = 0</code>。</li>
	<li>下标 0：已经访问过。过程结束。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == instructions.length == values.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>instructions[i]</code> 只能是 <code>"add"</code> 或 <code>"jump"</code>。</li>
	<li><code>-10<sup>5</sup> &lt;= values[i] &lt;= 10<sup>5</sup></code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 模拟

## 提示

1. Simulate the process step by step, following the rules for each instruction.
2. Use a data structure to track which instructions have already been executed to detect revisits.

## 示例

```
["jump","add","add","jump","add","jump"]
[2,1,3,1,-2,-3]
["jump","add","add"]
[3,1,1]
["jump"]
[0]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    long long calculateScore(vector<string>& instructions, vector<int>& values) {
        
    }
};
```

### Java

```java
class Solution {
    public long calculateScore(String[] instructions, int[] values) {
        
    }
}
```

### Python

```python
class Solution(object):
    def calculateScore(self, instructions, values):
        """
        :type instructions: List[str]
        :type values: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        
```

### C

```c
long long calculateScore(char** instructions, int instructionsSize, int* values, int valuesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public long CalculateScore(string[] instructions, int[] values) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} instructions
 * @param {number[]} values
 * @return {number}
 */
var calculateScore = function(instructions, values) {
    
};
```

### TypeScript

```typescript
function calculateScore(instructions: string[], values: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $instructions
     * @param Integer[] $values
     * @return Integer
     */
    function calculateScore($instructions, $values) {
        
    }
}
```

### Swift

```swift
class Solution {
    func calculateScore(_ instructions: [String], _ values: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun calculateScore(instructions: Array<String>, values: IntArray): Long {
        
    }
}
```

### Dart

```dart
class Solution {
  int calculateScore(List<String> instructions, List<int> values) {
    
  }
}
```

### Go

```golang
func calculateScore(instructions []string, values []int) int64 {
    
}
```

### Ruby

```ruby
# @param {String[]} instructions
# @param {Integer[]} values
# @return {Integer}
def calculate_score(instructions, values)
    
end
```

### Scala

```scala
object Solution {
    def calculateScore(instructions: Array[String], values: Array[Int]): Long = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn calculate_score(instructions: Vec<String>, values: Vec<i32>) -> i64 {
        
    }
}
```

### Racket

```racket
(define/contract (calculate-score instructions values)
  (-> (listof string?) (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec calculate_score(Instructions :: [unicode:unicode_binary()], Values :: [integer()]) -> integer().
calculate_score(Instructions, Values) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec calculate_score(instructions :: [String.t], values :: [integer]) :: integer
  def calculate_score(instructions, values) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func calculateScore(instructions: Array<String>, values: Array<Int64>): Int64 {

    }
}
```

