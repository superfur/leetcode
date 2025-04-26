# 1306. 跳跃游戏 III

## 题目描述

<p>这里有一个非负整数数组&nbsp;<code>arr</code>，你最开始位于该数组的起始下标&nbsp;<code>start</code>&nbsp;处。当你位于下标&nbsp;<code>i</code>&nbsp;处时，你可以跳到&nbsp;<code>i + arr[i]</code> 或者 <code>i - arr[i]</code>。</p>

<p>请你判断自己是否能够跳到对应元素值为 0 的 <strong>任一</strong> 下标处。</p>

<p>注意，不管是什么情况下，你都无法跳到数组之外。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [4,2,3,0,3,1,2], start = 5
<strong>输出：</strong>true
<strong>解释：</strong>
到达值为 0 的下标 3 有以下可能方案： 
下标 5 -&gt; 下标 4 -&gt; 下标 1 -&gt; 下标 3 
下标 5 -&gt; 下标 6 -&gt; 下标 4 -&gt; 下标 1 -&gt; 下标 3 
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [4,2,3,0,3,1,2], start = 0
<strong>输出：</strong>true 
<strong>解释：
</strong>到达值为 0 的下标 3 有以下可能方案： 
下标 0 -&gt; 下标 4 -&gt; 下标 1 -&gt; 下标 3
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [3,0,2,1,2], start = 2
<strong>输出：</strong>false
<strong>解释：</strong>无法到达值为 0 的下标 1 处。 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 5 * 10^4</code></li>
	<li><code>0 &lt;= arr[i] &lt;&nbsp;arr.length</code></li>
	<li><code>0 &lt;= start &lt; arr.length</code></li>
</ul>


## 难度

Medium

## 标签

- 深度优先搜索
- 广度优先搜索
- 数组

## 提示

1. Think of BFS to solve the problem.
2. When you reach a position with a value = 0 then return true.

## 示例

```
[4,2,3,0,3,1,2]
5
[4,2,3,0,3,1,2]
0
[3,0,2,1,2]
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean canReach(int[] arr, int start) {
        
    }
}
```

### Python

```python
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
```

### C

```c
bool canReach(int* arr, int arrSize, int start) {
    
}
```

### C#

```csharp
public class Solution {
    public bool CanReach(int[] arr, int start) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} arr
 * @param {number} start
 * @return {boolean}
 */
var canReach = function(arr, start) {
    
};
```

### TypeScript

```typescript
function canReach(arr: number[], start: number): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $arr
     * @param Integer $start
     * @return Boolean
     */
    function canReach($arr, $start) {
        
    }
}
```

### Swift

```swift
class Solution {
    func canReach(_ arr: [Int], _ start: Int) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun canReach(arr: IntArray, start: Int): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool canReach(List<int> arr, int start) {
    
  }
}
```

### Go

```golang
func canReach(arr []int, start int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} arr
# @param {Integer} start
# @return {Boolean}
def can_reach(arr, start)
    
end
```

### Scala

```scala
object Solution {
    def canReach(arr: Array[Int], start: Int): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn can_reach(arr: Vec<i32>, start: i32) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (can-reach arr start)
  (-> (listof exact-integer?) exact-integer? boolean?)
  )
```

### Erlang

```erlang
-spec can_reach(Arr :: [integer()], Start :: integer()) -> boolean().
can_reach(Arr, Start) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec can_reach(arr :: [integer], start :: integer) :: boolean
  def can_reach(arr, start) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func canReach(arr: Array<Int64>, start: Int64): Bool {

    }
}
```

