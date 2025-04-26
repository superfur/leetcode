# 1640. 能否连接形成数组

## 题目描述

<p>给你一个整数数组 <code>arr</code> ，数组中的每个整数 <strong>互不相同</strong> 。另有一个由整数数组构成的数组 <code>pieces</code>，其中的整数也 <strong>互不相同</strong> 。请你以 <strong>任意顺序</strong> 连接 <code>pieces</code> 中的数组以形成 <code>arr</code> 。但是，<strong>不允许</strong> 对每个数组 <code>pieces[i]</code> 中的整数重新排序。</p>

<p>如果可以连接<em> </em><code>pieces</code> 中的数组形成 <code>arr</code> ，返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>arr = [15,88], pieces = [[88],[15]]
<strong>输出：</strong>true
<strong>解释：</strong>依次连接 <code>[15]</code> 和 <code>[88]</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>arr = [49,18,16], pieces = [[16,18,49]]
<strong>输出：</strong>false
<strong>解释：</strong>即便数字相符，也不能重新排列 pieces[0]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
<strong>输出：</strong>true
<strong>解释：</strong>依次连接 <code>[91]</code>、<code>[4,64]</code> 和 <code>[78]</code></pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= pieces.length &lt;= arr.length &lt;= 100</code></li>
	<li><code>sum(pieces[i].length) == arr.length</code></li>
	<li><code>1 &lt;= pieces[i].length &lt;= arr.length</code></li>
	<li><code>1 &lt;= arr[i], pieces[i][j] &lt;= 100</code></li>
	<li><code>arr</code> 中的整数 <strong>互不相同</strong></li>
	<li><code>pieces</code> 中的整数 <strong>互不相同</strong>（也就是说，如果将 <code>pieces</code> 扁平化成一维数组，数组中的所有整数互不相同）</li>
</ul>


## 难度

Easy

## 标签

- 数组
- 哈希表

## 提示

1. Note that the distinct part means that every position in the array belongs to only one piece
2. Note that you can get the piece every position belongs to naively

## 示例

```
[15,88]
[[88],[15]]
[49,18,16]
[[16,18,49]]
[91,4,64,78]
[[78],[4,64],[91]]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
```

### C

```c
bool canFormArray(int* arr, int arrSize, int** pieces, int piecesSize, int* piecesColSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanFormArray(int[] arr, int[][] pieces) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number[][]} pieces
 * @return {boolean}
 */
var canFormArray = function(arr, pieces) {
    
};
```

### TypeScript

```typescript
function canFormArray(arr: number[], pieces: number[][]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer[][] $pieces
     * @return Boolean
     */
    function canFormArray($arr, $pieces) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canFormArray(_ arr: [Int], _ pieces: [[Int]]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canFormArray(arr: IntArray, pieces: Array<IntArray>): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canFormArray(List<int> arr, List<List<int>> pieces) {
    
  }
}
```

### Go

```golang
func canFormArray(arr []int, pieces [][]int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer[][]} pieces
# @return {Boolean}
def can_form_array(arr, pieces)
    
end
```

### Scala

```scala
object Solution {
    def canFormArray(arr: Array[Int], pieces: Array[Array[Int]]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_form_array(arr: Vec<i32>, pieces: Vec<Vec<i32>>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-form-array arr pieces)
  (-> (listof exact-integer?) (listof (listof exact-integer?)) boolean?)
  )
```

### Erlang

```erlang
-spec can_form_array(Arr :: [integer()], Pieces :: [[integer()]]) -> boolean().
can_form_array(Arr, Pieces) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_form_array(arr :: [integer], pieces :: [[integer]]) :: boolean
  def can_form_array(arr, pieces) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canFormArray(arr: Array<Int64>, pieces: Array<Array<Int64>>): Bool {

    }
}
```

