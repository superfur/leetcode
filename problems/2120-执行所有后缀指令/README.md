# 2120. 执行所有后缀指令

## 题目描述

<p>现有一个 <code>n x n</code> 大小的网格，左上角单元格坐标 <code>(0, 0)</code> ，右下角单元格坐标 <code>(n - 1, n - 1)</code> 。给你整数 <code>n</code> 和一个整数数组 <code>startPos</code> ，其中 <code>startPos = [start<sub>row</sub>, start<sub>col</sub>]</code> 表示机器人最开始在坐标为 <code>(start<sub>row</sub>, start<sub>col</sub>)</code> 的单元格上。</p>

<p>另给你一个长度为 <code>m</code> 、下标从 <strong>0</strong> 开始的字符串 <code>s</code> ，其中 <code>s[i]</code> 是对机器人的第 <code>i</code> 条指令：<code>'L'</code>（向左移动），<code>'R'</code>（向右移动），<code>'U'</code>（向上移动）和 <code>'D'</code>（向下移动）。</p>

<p>机器人可以从 <code>s</code> 中的任一第 <code>i</code> 条指令开始执行。它将会逐条执行指令直到 <code>s</code> 的末尾，但在满足下述条件之一时，机器人将会停止：</p>

<ul>
	<li>下一条指令将会导致机器人移动到网格外。</li>
	<li>没有指令可以执行。</li>
</ul>

<p>返回一个长度为 <code>m</code> 的数组 <code>answer</code> ，其中 <code>answer[i]</code> 是机器人从第 <code>i</code>&nbsp;条指令 <strong>开始</strong>&nbsp;，可以执行的 <strong>指令数目</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/09/1.png" style="width: 145px; height: 142px;" /></p>

<pre>
<strong>输入：</strong>n = 3, startPos = [0,1], s = "RRDDLU"
<strong>输出：</strong>[1,5,4,3,1,0]
<strong>解释：</strong>机器人从 startPos 出发，并从第 i 条指令开始执行：
- 0: "<em><strong>R</strong></em>RDDLU" 在移动到网格外之前，只能执行一条 "R" 指令。
- 1:  "<em><strong>RDDLU</strong></em>" 可以执行全部五条指令，机器人仍在网格内，最终到达 (0, 0) 。
- 2:   "<em><strong>DDLU</strong></em>" 可以执行全部四条指令，机器人仍在网格内，最终到达 (0, 0) 。
- 3:    "<em><strong>DLU</strong></em>" 可以执行全部三条指令，机器人仍在网格内，最终到达 (0, 0) 。
- 4:     "<em><strong>L</strong></em>U" 在移动到网格外之前，只能执行一条 "L" 指令。
- 5:      "U" 如果向上移动，将会移动到网格外。
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/09/2.png" style="width: 106px; height: 103px;" /></p>

<pre>
<strong>输入：</strong>n = 2, startPos = [1,1], s = "LURD"
<strong>输出：</strong>[4,1,0,0]
<strong>解释：</strong>
- 0: "<em><strong>LURD</strong></em>"
- 1:  "<em><strong>U</strong></em>RD"
- 2:   "RD"
- 3:    "D"
</pre>

<p><strong>示例 3：</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/12/09/3.png" style="width: 67px; height: 64px;" /></p>

<pre>
<strong>输入：</strong>n = 1, startPos = [0,0], s = "LRUD"
<strong>输出：</strong>[0,0,0,0]
<strong>解释：</strong>无论机器人从哪条指令开始执行，都会移动到网格外。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == s.length</code></li>
	<li><code>1 &lt;= n, m &lt;= 500</code></li>
	<li><code>startPos.length == 2</code></li>
	<li><code>0 &lt;= start<sub>row</sub>, start<sub>col</sub> &lt; n</code></li>
	<li><code>s</code> 由 <code>'L'</code>、<code>'R'</code>、<code>'U'</code> 和 <code>'D'</code> 组成</li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 模拟

## 提示

1. The constraints are not very large. Can we simulate the execution by starting from each index of s?
2. Before any of the stopping conditions is met, stop the simulation for that index and set the answer for that index.

## 示例

```
3
[0,1]
"RRDDLU"
2
[1,1]
"LURD"
1
[0,0]
"LRUD"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> executeInstructions(int n, vector<int>& startPos, string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] executeInstructions(int n, int[] startPos, String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def executeInstructions(self, n, startPos, s):
        """
        :type n: int
        :type startPos: List[int]
        :type s: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* executeInstructions(int n, int* startPos, int startPosSize, char* s, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] ExecuteInstructions(int n, int[] startPos, string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} n
 * @param {number[]} startPos
 * @param {string} s
 * @return {number[]}
 */
var executeInstructions = function(n, startPos, s) {
    
};
```

### TypeScript

```typescript
function executeInstructions(n: number, startPos: number[], s: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $n
     * @param Integer[] $startPos
     * @param String $s
     * @return Integer[]
     */
    function executeInstructions($n, $startPos, $s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func executeInstructions(_ n: Int, _ startPos: [Int], _ s: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun executeInstructions(n: Int, startPos: IntArray, s: String): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> executeInstructions(int n, List<int> startPos, String s) {
    
  }
}
```

### Go

```golang
func executeInstructions(n int, startPos []int, s string) []int {
    
}
```

### Ruby

```ruby
# @param {Integer} n
# @param {Integer[]} start_pos
# @param {String} s
# @return {Integer[]}
def execute_instructions(n, start_pos, s)
    
end
```

### Scala

```scala
object Solution {
    def executeInstructions(n: Int, startPos: Array[Int], s: String): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn execute_instructions(n: i32, start_pos: Vec<i32>, s: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (execute-instructions n startPos s)
  (-> exact-integer? (listof exact-integer?) string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec execute_instructions(N :: integer(), StartPos :: [integer()], S :: unicode:unicode_binary()) -> [integer()].
execute_instructions(N, StartPos, S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec execute_instructions(n :: integer, start_pos :: [integer], s :: String.t) :: [integer]
  def execute_instructions(n, start_pos, s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func executeInstructions(n: Int64, startPos: Array<Int64>, s: String): Array<Int64> {

    }
}
```

