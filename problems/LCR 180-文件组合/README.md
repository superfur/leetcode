# LCR 180. 文件组合

## 题目描述

<p>待传输文件被切分成多个部分，按照原排列顺序，每部分文件编号均为一个 <strong>正整数</strong>（至少含有两个文件）。传输要求为：连续文件编号总和为接收方指定数字 <code>target</code> 的所有文件。请返回所有符合该要求的文件传输组合列表。</p>

<p><strong>注意</strong>，返回时需遵循以下规则：</p>

<ul>
	<li>每种组合按照文件编号 <strong>升序</strong> 排列；</li>
	<li>不同组合按照第一个文件编号 <strong>升序</strong> 排列。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>target = 12
<strong>输出：</strong>[[3, 4, 5]]
<strong>解释：</strong>在上述示例中，存在一个连续正整数序列的和为 12，为 [3, 4, 5]。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>target = 18
<strong>输出：</strong>[[3,4,5,6],[5,6,7]]
<strong>解释：</strong>在上述示例中，存在两个连续正整数序列的和分别为 18，分别为 [3, 4, 5, 6] 和 [5, 6, 7]。
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= target &lt;= 10^5</code></li>
</ul>

<p>&nbsp;</p>


## 难度

Easy

## 标签

- 数学
- 双指针
- 枚举

## 示例

```
12
18
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<vector<int>> fileCombination(int target) {
        
    }
};
```

### Java

```java
class Solution {
    public int[][] fileCombination(int target) {
        
    }
}
```

### Python

```python
class Solution(object):
    def fileCombination(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        
```

### Python3

```python3
class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        
```

### C

```c
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** fileCombination(int target, int* returnSize, int** returnColumnSizes) {
    
}
```

### C#

```csharp
public class Solution {
    public int[][] FileCombination(int target) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} target
 * @return {number[][]}
 */
var fileCombination = function(target) {
    
};
```

### TypeScript

```typescript
function fileCombination(target: number): number[][] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $target
     * @return Integer[][]
     */
    function fileCombination($target) {
        
    }
}
```

### Swift

```swift
class Solution {
    func fileCombination(_ target: Int) -> [[Int]] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun fileCombination(target: Int): Array<IntArray> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<List<int>> fileCombination(int target) {
    
  }
}
```

### Go

```golang
func fileCombination(target int) [][]int {
    
}
```

### Ruby

```ruby
# @param {Integer} target
# @return {Integer[][]}
def file_combination(target)
    
end
```

### Scala

```scala
object Solution {
    def fileCombination(target: Int): Array[Array[Int]] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn file_combination(target: i32) -> Vec<Vec<i32>> {
        
    }
}
```

### Racket

```racket
(define/contract (file-combination target)
  (-> exact-integer? (listof (listof exact-integer?)))
  )
```

### Erlang

```erlang
-spec file_combination(Target :: integer()) -> [[integer()]].
file_combination(Target) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec file_combination(target :: integer) :: [[integer]]
  def file_combination(target) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func fileCombination(target: Int64): Array<Array<Int64>> {

    }
}
```

