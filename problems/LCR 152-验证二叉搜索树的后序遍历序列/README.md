# LCR 152. 验证二叉搜索树的后序遍历序列

## 题目描述

<p>请实现一个函数来判断整数数组 <code>postorder</code> 是否为二叉搜索树的后序遍历结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1706665328-rfvWhs-%E6%88%AA%E5%B1%8F2024-01-31%2009.41.48.png" style="width: 300px; height: 279px;" /></p>

<pre>
<strong>输入: </strong>postorder = [4,9,6,5,8]
<strong>输出: </strong>false 
<strong>解释：</strong>从上图可以看出这不是一颗二叉搜索树
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://pic.leetcode.cn/1694762510-vVpTic-%E5%89%91%E6%8C%8733.png" /></p>

<pre>
<strong>输入: </strong>postorder = [4,6,5,9,8]
<strong>输出: </strong>true 
<strong>解释：</strong>可构建的二叉搜索树如上图
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>数组长度 &lt;= 1000</code></li>
	<li><code>postorder</code> 中无重复数字</li>
</ul>

<p>&nbsp;</p>


## 难度

Medium

## 标签

- 栈
- 树
- 二叉搜索树
- 递归
- 数组
- 二叉树
- 单调栈

## 示例

```
[4,9,6,5,8]
[4,6,5,9,8]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool verifyTreeOrder(vector<int>& postorder) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean verifyTreeOrder(int[] postorder) {
        
    }
}
```

### Python

```python
class Solution(object):
    def verifyTreeOrder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def verifyTreeOrder(self, postorder: List[int]) -> bool:
        
```

### C

```c
bool verifyTreeOrder(int* postorder, int postorderSize) {
    
}
```

### C#

```csharp
public class Solution {
    public bool VerifyTreeOrder(int[] postorder) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} postorder
 * @return {boolean}
 */
var verifyTreeOrder = function(postorder) {
    
};
```

### TypeScript

```typescript
function verifyTreeOrder(postorder: number[]): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $postorder
     * @return Boolean
     */
    function verifyTreeOrder($postorder) {
        
    }
}
```

### Swift

```swift
class Solution {
    func verifyTreeOrder(_ postorder: [Int]) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun verifyTreeOrder(postorder: IntArray): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool verifyTreeOrder(List<int> postorder) {
    
  }
}
```

### Go

```golang
func verifyTreeOrder(postorder []int) bool {
    
}
```

### Ruby

```ruby
# @param {Integer[]} postorder
# @return {Boolean}
def verify_tree_order(postorder)
    
end
```

### Scala

```scala
object Solution {
    def verifyTreeOrder(postorder: Array[Int]): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn verify_tree_order(postorder: Vec<i32>) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (verify-tree-order postorder)
  (-> (listof exact-integer?) boolean?)
  )
```

### Erlang

```erlang
-spec verify_tree_order(Postorder :: [integer()]) -> boolean().
verify_tree_order(Postorder) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec verify_tree_order(postorder :: [integer]) :: boolean
  def verify_tree_order(postorder) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func verifyTreeOrder(postorder: Array<Int64>): Bool {

    }
}
```

