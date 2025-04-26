# 1769. 移动所有球到每个盒子所需的最小操作数

## 题目描述

<p>有 <code>n</code> 个盒子。给你一个长度为 <code>n</code> 的二进制字符串 <code>boxes</code> ，其中 <code>boxes[i]</code> 的值为 <code>'0'</code> 表示第 <code>i</code> 个盒子是 <strong>空</strong> 的，而 <code>boxes[i]</code> 的值为 <code>'1'</code> 表示盒子里有 <strong>一个</strong> 小球。</p>

<p>在一步操作中，你可以将 <strong>一个</strong> 小球从某个盒子移动到一个与之相邻的盒子中。第 <code>i</code> 个盒子和第 <code>j</code> 个盒子相邻需满足 <code>abs(i - j) == 1</code> 。注意，操作执行后，某些盒子中可能会存在不止一个小球。</p>

<p>返回一个长度为 <code>n</code> 的数组 <code>answer</code> ，其中 <code>answer[i]</code> 是将所有小球移动到第 <code>i</code> 个盒子所需的 <strong>最小</strong> 操作数。</p>

<p>每个 <code>answer[i]</code> 都需要根据盒子的 <strong>初始状态</strong> 进行计算。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>boxes = "110"
<strong>输出：</strong>[1,1,3]
<strong>解释：</strong>每个盒子对应的最小操作数如下：
1) 第 1 个盒子：将一个小球从第 2 个盒子移动到第 1 个盒子，需要 1 步操作。
2) 第 2 个盒子：将一个小球从第 1 个盒子移动到第 2 个盒子，需要 1 步操作。
3) 第 3 个盒子：将一个小球从第 1 个盒子移动到第 3 个盒子，需要 2 步操作。将一个小球从第 2 个盒子移动到第 3 个盒子，需要 1 步操作。共计 3 步操作。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>boxes = "001011"
<strong>输出：</strong>[11,8,5,4,3,4]</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == boxes.length</code></li>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>boxes[i]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 字符串
- 前缀和

## 提示

1. If you want to move a ball from box i to box j, you'll need abs(i-j) moves.
2. To move all balls to some box, you can move them one by one.
3. For each box i, iterate on each ball in a box j, and add abs(i-j) to answers[i].

## 示例

```
"110"
"001011"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<int> minOperations(string boxes) {
        
    }
};
```

### Java

```java
class Solution {
    public int[] minOperations(String boxes) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* minOperations(char* boxes, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int[] MinOperations(string boxes) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} boxes
 * @return {number[]}
 */
var minOperations = function(boxes) {
    
};
```

### TypeScript

```typescript
function minOperations(boxes: string): number[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $boxes
     * @return Integer[]
     */
    function minOperations($boxes) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ boxes: String) -> [Int] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(boxes: String): IntArray {
        
    }
}
```

### Dart

```dart
class Solution {
  List<int> minOperations(String boxes) {
    
  }
}
```

### Go

```golang
func minOperations(boxes string) []int {
    
}
```

### Ruby

```ruby
# @param {String} boxes
# @return {Integer[]}
def min_operations(boxes)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(boxes: String): Array[Int] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(boxes: String) -> Vec<i32> {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations boxes)
  (-> string? (listof exact-integer?))
  )
```

### Erlang

```erlang
-spec min_operations(Boxes :: unicode:unicode_binary()) -> [integer()].
min_operations(Boxes) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(boxes :: String.t) :: [integer]
  def min_operations(boxes) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(boxes: String): Array<Int64> {

    }
}
```

