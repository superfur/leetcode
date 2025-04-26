# 1496. 判断路径是否相交

## 题目描述

<p>给你一个字符串 <code>path</code>，其中 <code>path[i]</code> 的值可以是 <code>'N'</code>、<code>'S'</code>、<code>'E'</code> 或者 <code>'W'</code>，分别表示向北、向南、向东、向西移动一个单位。</p>

<p>你从二维平面上的原点 <code>(0, 0)</code> 处开始出发，按 <code>path</code> 所指示的路径行走。</p>

<p>如果路径在任何位置上与自身相交，也就是走到之前已经走过的位置，请返回 <code>true</code> ；否则，返回 <code>false</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/28/screen-shot-2020-06-10-at-123929-pm.png" style="height: 358px; width: 400px;" /></p>

<pre>
<strong>输入：</strong>path = "NES"
<strong>输出：</strong>false 
<strong>解释：</strong>该路径没有在任何位置相交。</pre>

<p><strong class="example">示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/28/screen-shot-2020-06-10-at-123843-pm.png" style="height: 339px; width: 400px;" /></p>

<pre>
<strong>输入：</strong>path = "NESWW"
<strong>输出：</strong>true
<strong>解释：</strong>该路径经过原点两次。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= path.length &lt;= 10<sup>4</sup></code></li>
	<li><code>path[i]</code> 为 <code>'N'</code>、<code>'S'</code>、<code>'E'</code> 或 <code>'W'</code></li>
</ul>


## 难度

Easy

## 标签

- 哈希表
- 字符串

## 提示

1. Simulate the process while keeping track of visited points.
2. Use a set to store previously visited points.

## 示例

```
"NES"
"NESWW"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    bool isPathCrossing(string path) {
        
    }
};
```

### Java

```java
class Solution {
    public boolean isPathCrossing(String path) {
        
    }
}
```

### Python

```python
class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        
```

### Python3

```python3
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
```

### C

```c
bool isPathCrossing(char* path) {
    
}
```

### C#

```csharp
public class Solution {
    public bool IsPathCrossing(string path) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} path
 * @return {boolean}
 */
var isPathCrossing = function(path) {
    
};
```

### TypeScript

```typescript
function isPathCrossing(path: string): boolean {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $path
     * @return Boolean
     */
    function isPathCrossing($path) {
        
    }
}
```

### Swift

```swift
class Solution {
    func isPathCrossing(_ path: String) -> Bool {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun isPathCrossing(path: String): Boolean {
        
    }
}
```

### Dart

```dart
class Solution {
  bool isPathCrossing(String path) {
    
  }
}
```

### Go

```golang
func isPathCrossing(path string) bool {
    
}
```

### Ruby

```ruby
# @param {String} path
# @return {Boolean}
def is_path_crossing(path)
    
end
```

### Scala

```scala
object Solution {
    def isPathCrossing(path: String): Boolean = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn is_path_crossing(path: String) -> bool {
        
    }
}
```

### Racket

```racket
(define/contract (is-path-crossing path)
  (-> string? boolean?)
  )
```

### Erlang

```erlang
-spec is_path_crossing(Path :: unicode:unicode_binary()) -> boolean().
is_path_crossing(Path) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec is_path_crossing(path :: String.t) :: boolean
  def is_path_crossing(path) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func isPathCrossing(path: String): Bool {

    }
}
```

