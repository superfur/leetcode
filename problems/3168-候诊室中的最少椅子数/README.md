# 3168. 候诊室中的最少椅子数

## 题目描述

<p>给你一个字符串 <code>s</code>，模拟每秒钟的事件 <code>i</code>：</p>

<ul>
	<li>如果 <code>s[i] == 'E'</code>，表示有一位顾客进入候诊室并占用一把椅子。</li>
	<li>如果 <code>s[i] == 'L'</code>，表示有一位顾客离开候诊室，从而释放一把椅子。</li>
</ul>

<p>返回保证每位进入候诊室的顾客都能有椅子坐的<strong> 最少 </strong>椅子数，假设候诊室最初是 <strong>空的 </strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "EEEEEEE"</span></p>

<p><strong>输出：</strong><span class="example-io">7</span></p>

<p><strong>解释：</strong></p>

<p>每秒后都有一个顾客进入候诊室，没有人离开。因此，至少需要 7 把椅子。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "ELELEEL"</span></p>

<p><strong>输出：</strong><span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>假设候诊室里有 2 把椅子。下表显示了每秒钟等候室的状态。</p>
</div>
<table>
	<tbody>
		<tr>
			<th>秒</th>
			<th>事件</th>
			<th>候诊室的人数</th>
			<th>可用的椅子数</th>
		</tr>
		<tr>
			<td>0</td>
			<td>Enter</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>1</td>
			<td>Leave</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>Enter</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>Leave</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>4</td>
			<td>Enter</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>5</td>
			<td>Enter</td>
			<td>2</td>
			<td>0</td>
		</tr>
		<tr>
			<td>6</td>
			<td>Leave</td>
			<td>1</td>
			<td>1</td>
		</tr>
	</tbody>
</table>


<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "ELEELEELLL"</span></p>

<p><strong>输出：</strong><span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>假设候诊室里有 3 把椅子。下表显示了每秒钟等候室的状态。</p>
</div>
<table>
	<tbody>
		<tr>
			<th>秒</th>
			<th>事件</th>
			<th>候诊室的人数</th>
			<th>可用的椅子数</th>
		</tr>
		<tr>
			<td>0</td>
			<td>Enter</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>1</td>
			<td>Leave</td>
			<td>0</td>
			<td>3</td>
		</tr>
		<tr>
			<td>2</td>
			<td>Enter</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>3</td>
			<td>Enter</td>
			<td>2</td>
			<td>1</td>
		</tr>
		<tr>
			<td>4</td>
			<td>Leave</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>5</td>
			<td>Enter</td>
			<td>2</td>
			<td>1</td>
		</tr>
		<tr>
			<td>6</td>
			<td>Enter</td>
			<td>3</td>
			<td>0</td>
		</tr>
		<tr>
			<td>7</td>
			<td>Leave</td>
			<td>2</td>
			<td>1</td>
		</tr>
		<tr>
			<td>8</td>
			<td>Leave</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>9</td>
			<td>Leave</td>
			<td>0</td>
			<td>3</td>
		</tr>
	</tbody>
</table>


<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 50</code></li>
	<li><code>s</code> 仅由字母 <code>'E'</code> 和 <code>'L'</code> 组成。</li>
	<li><code>s</code> 表示一个有效的进出序列。</li>
</ul>


## 难度

Easy

## 标签

- 字符串
- 模拟

## 提示

1. Iterate from left to right over the string and keep track of the number of people in the waiting room using a variable that you will increment on every occurrence of ‘E’ and decrement on every occurrence of ‘L’.
2. The answer is the maximum number of people in the waiting room at any instance.

## 示例

```
"EEEEEEE"
"ELELEEL"
"ELEELEELLL"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minimumChairs(string s) {
        
    }
};
```

### Java

```java
class Solution {
    public int minimumChairs(String s) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minimumChairs(self, s: str) -> int:
        
```

### C

```c
int minimumChairs(char* s) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinimumChairs(string s) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} s
 * @return {number}
 */
var minimumChairs = function(s) {
    
};
```

### TypeScript

```typescript
function minimumChairs(s: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function minimumChairs($s) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minimumChairs(_ s: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minimumChairs(s: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minimumChairs(String s) {
    
  }
}
```

### Go

```golang
func minimumChairs(s string) int {
    
}
```

### Ruby

```ruby
# @param {String} s
# @return {Integer}
def minimum_chairs(s)
    
end
```

### Scala

```scala
object Solution {
    def minimumChairs(s: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn minimum_chairs(s: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (minimum-chairs s)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec minimum_chairs(S :: unicode:unicode_binary()) -> integer().
minimum_chairs(S) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec minimum_chairs(s :: String.t) :: integer
  def minimum_chairs(s) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minimumChairs(s: String): Int64 {

    }
}
```

