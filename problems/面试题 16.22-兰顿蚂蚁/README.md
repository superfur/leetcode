# 面试题 16.22. 兰顿蚂蚁

## 题目描述

<p>一只蚂蚁坐在由白色和黑色方格构成的无限网格上。开始时，网格全白，蚂蚁面向右侧。每行走一步，蚂蚁执行以下操作。</p>

<p>(1) 如果在白色方格上，则翻转方格的颜色，向右(顺时针)转 90 度，并向前移动一个单位。<br />
(2) 如果在黑色方格上，则翻转方格的颜色，向左(逆时针方向)转 90 度，并向前移动一个单位。</p>

<p>编写程序来模拟蚂蚁执行的前 K 个动作，并返回最终的网格。</p>

<p>网格由数组表示，每个元素是一个字符串，代表网格中的一行，黑色方格由&nbsp;<code>'X'</code>&nbsp;表示，白色方格由&nbsp;<code>'_'</code>&nbsp;表示，蚂蚁所在的位置由&nbsp;<code>'L'</code>, <code>'U'</code>, <code>'R'</code>, <code>'D'</code>&nbsp;表示，分别表示蚂蚁&nbsp;左、上、右、下 的朝向。只需要返回能够包含蚂蚁走过的所有方格的最小矩形。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>0
<strong>输出：</strong>["R"]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>2
<strong>输出：
</strong>[
&nbsp; "_X",
&nbsp; "LX"
]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>5
<strong>输出：
</strong>[
&nbsp; "_U",
&nbsp; "X_",
&nbsp; "XX"
]
</pre>

<p><strong>说明：</strong></p>

<ul>
	<li><code>K &lt;= 100000</code></li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 矩阵
- 模拟

## 提示

1. 棘手的是处理无限网格。你有什么选择？
2. 选项1：你真的需要一个无线的网络吗？再次审题。你知道网格的最大尺寸吗？
3. 选项 2：想想ArrayList的工作原理。它能派上用场吗？
4. 选项2：使用ArrayList是不可能的，因为那样太烦琐了。也许构建自己的列表会更容易，但要专门针对矩阵。
5. 方法2：一种方法是当蚂蚁到达边缘时，将数组的大小加倍。但是，你将如何处理蚂蚁到达负坐标的问题呢？数组不能有负的索引。
6. 选项2：注意，问题中没有规定坐标的标签必须保持不变。你能把蚂蚁和所有的单元格信息移动到正坐标吗？换句话说，如果当你需要让数组n向负方向增长时，你重新标记了所有的指标使它们仍然是正的，会发生什么?
7. 选项3：另一件需要考虑的事情是，你是否真的需要一个网格来实现它。在这个问题中你真正需要什么信息?
8. 选项3：你实际上需要的是来查看一个单元格是白色的还是黑色的某种方式（当然还有蚂蚁的位置）。你能把所有的白色方格存在一个链表中吗?
9. 选项3：你可以考虑维护一个所有白色方格的散列集合。不过，你怎么才能打印出整个网格呢?

## 示例

```
0
1
2
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> printKMoves(int K) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> printKMoves(int K) {
        
    }
}
```

### Python

```python
class Solution(object):
    def printKMoves(self, K):
        """
        :type K: int
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def printKMoves(self, K: int) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** printKMoves(int K, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> PrintKMoves(int K) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} K
 * @return {string[]}
 */
var printKMoves = function(K) {
    
};
```

### TypeScript

```typescript
function printKMoves(K: number): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $K
     * @return String[]
     */
    function printKMoves($K) {
        
    }
}
```

### Swift

```swift
class Solution {
    func printKMoves(_ K: Int) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun printKMoves(K: Int): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> printKMoves(int K) {
    
  }
}
```

### Go

```golang
func printKMoves(K int) []string {
    
}
```

### Ruby

```ruby
# @param {Integer} k
# @return {String[]}
def print_k_moves(k)
    
end
```

### Scala

```scala
object Solution {
    def printKMoves(K: Int): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn print_k_moves(k: i32) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (print-k-moves K)
  (-> exact-integer? (listof string?))
  )
```

### Erlang

```erlang
-spec print_k_moves(K :: integer()) -> [unicode:unicode_binary()].
print_k_moves(K) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec print_k_moves(k :: integer) :: [String.t]
  def print_k_moves(k) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func printKMoves(K: Int64): ArrayList<String> {

    }
}
```

