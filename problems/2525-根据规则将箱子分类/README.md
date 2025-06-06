# 2525. 根据规则将箱子分类

## 题目描述

<p>给你四个整数&nbsp;<code>length</code>&nbsp;，<code>width</code>&nbsp;，<code>height</code>&nbsp;和&nbsp;<code>mass</code>&nbsp;，分别表示一个箱子的三个维度和质量，请你返回一个表示箱子 <strong>类别</strong> 的字符串。</p>

<ul>
	<li>如果满足以下条件，那么箱子是&nbsp;<code>"Bulky"</code>&nbsp;的：

	<ul>
		<li>箱子 <strong>至少有一个</strong> 维度大于等于 <code>10<sup>4</sup></code>&nbsp;。</li>
		<li>或者箱子的 <strong>体积</strong> 大于等于&nbsp;<code>10<sup>9</sup></code>&nbsp;。</li>
	</ul>
	</li>
	<li>如果箱子的质量大于等于&nbsp;<code>100</code>&nbsp;，那么箱子是&nbsp;<code>"Heavy"</code>&nbsp;的。</li>
	<li>如果箱子同时是&nbsp;<code>"Bulky"</code> 和&nbsp;<code>"Heavy"</code>&nbsp;，那么返回类别为&nbsp;<code>"Both"</code>&nbsp;。</li>
	<li>如果箱子既不是&nbsp;<code>"Bulky"</code>&nbsp;，也不是&nbsp;<code>"Heavy"</code>&nbsp;，那么返回类别为&nbsp;<code>"Neither"</code>&nbsp;。</li>
	<li>如果箱子是&nbsp;<code>"Bulky"</code>&nbsp;但不是&nbsp;<code>"Heavy"</code>&nbsp;，那么返回类别为&nbsp;<code>"Bulky"</code>&nbsp;。</li>
	<li>如果箱子是&nbsp;<code>"Heavy"</code>&nbsp;但不是&nbsp;<code>"Bulky"</code>&nbsp;，那么返回类别为&nbsp;<code>"Heavy"</code>&nbsp;。</li>
</ul>

<p><strong>注意</strong>，箱子的体积等于箱子的长度、宽度和高度的乘积。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>length = 1000, width = 35, height = 700, mass = 300
<b>输出：</b>"Heavy"
<b>解释：</b>
箱子没有任何维度大于等于 10<sup>4 </sup>。
体积为 24500000 &lt;= 10<sup>9 </sup>。所以不能归类为 "Bulky" 。
但是质量 &gt;= 100 ，所以箱子是 "Heavy" 的。
由于箱子不是 "Bulky" 但是是 "Heavy" ，所以我们返回 "Heavy" 。</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>length = 200, width = 50, height = 800, mass = 50
<b>输出：</b>"Neither"
<b>解释：</b>
箱子没有任何维度大于等于 10<sup>4</sup>&nbsp;。
体积为 8 * 10<sup>6</sup> &lt;= 10<sup>9</sup>&nbsp;。所以不能归类为 "Bulky" 。
质量小于 100 ，所以不能归类为 "Heavy" 。
由于不属于上述两者任何一类，所以我们返回 "Neither" 。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= length, width, height &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= mass &lt;= 10<sup>3</sup></code></li>
</ul>


## 难度

Easy

## 标签

- 数学

## 提示

1. Use conditional statements to find the right category of the box.

## 示例

```
1000
35
700
300
200
50
800
50
```

## 示例代码

### C++

```cpp
class Solution {
public:
    string categorizeBox(int length, int width, int height, int mass) {
        
    }
};
```

### Java

```java
class Solution {
    public String categorizeBox(int length, int width, int height, int mass) {
        
    }
}
```

### Python

```python
class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        
```

### Python3

```python3
class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
```

### C

```c
char* categorizeBox(int length, int width, int height, int mass) {
    
}
```

### C#

```csharp
public class Solution {
    public string CategorizeBox(int length, int width, int height, int mass) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number} length
 * @param {number} width
 * @param {number} height
 * @param {number} mass
 * @return {string}
 */
var categorizeBox = function(length, width, height, mass) {
    
};
```

### TypeScript

```typescript
function categorizeBox(length: number, width: number, height: number, mass: number): string {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer $length
     * @param Integer $width
     * @param Integer $height
     * @param Integer $mass
     * @return String
     */
    function categorizeBox($length, $width, $height, $mass) {
        
    }
}
```

### Swift

```swift
class Solution {
    func categorizeBox(_ length: Int, _ width: Int, _ height: Int, _ mass: Int) -> String {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun categorizeBox(length: Int, width: Int, height: Int, mass: Int): String {
        
    }
}
```

### Dart

```dart
class Solution {
  String categorizeBox(int length, int width, int height, int mass) {
    
  }
}
```

### Go

```golang
func categorizeBox(length int, width int, height int, mass int) string {
    
}
```

### Ruby

```ruby
# @param {Integer} length
# @param {Integer} width
# @param {Integer} height
# @param {Integer} mass
# @return {String}
def categorize_box(length, width, height, mass)
    
end
```

### Scala

```scala
object Solution {
    def categorizeBox(length: Int, width: Int, height: Int, mass: Int): String = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn categorize_box(length: i32, width: i32, height: i32, mass: i32) -> String {
        
    }
}
```

### Racket

```racket
(define/contract (categorize-box length width height mass)
  (-> exact-integer? exact-integer? exact-integer? exact-integer? string?)
  )
```

### Erlang

```erlang
-spec categorize_box(Length :: integer(), Width :: integer(), Height :: integer(), Mass :: integer()) -> unicode:unicode_binary().
categorize_box(Length, Width, Height, Mass) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec categorize_box(length :: integer, width :: integer, height :: integer, mass :: integer) :: String.t
  def categorize_box(length, width, height, mass) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func categorizeBox(length: Int64, width: Int64, height: Int64, mass: Int64): String {

    }
}
```

