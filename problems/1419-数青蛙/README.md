# 1419. 数青蛙

## 题目描述

<p>给你一个字符串 <code>croakOfFrogs</code>，它表示不同青蛙发出的蛙鸣声（字符串 <code>"croak"</code> ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以&nbsp;<code>croakOfFrogs</code> 中会混合多个 <code>“croak”</code> <em>。</em></p>

<p>请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。</p>

<p>要想发出蛙鸣 "croak"，青蛙必须 <strong>依序</strong> 输出 <code>‘c’, ’r’, ’o’, ’a’, ’k’</code> 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。如果字符串 <code>croakOfFrogs</code> 不是由若干有效的 "croak" 字符混合而成，请返回 <code>-1</code> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>croakOfFrogs = "croakcroak"
<strong>输出：</strong>1 
<strong>解释：</strong>一只青蛙 “呱呱” 两次
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>croakOfFrogs = "crcoakroak"
<strong>输出：</strong>2 
<strong>解释：</strong>最少需要两只青蛙，“呱呱” 声用黑体标注
第一只青蛙 "<strong>cr</strong>c<strong>oak</strong>roak"
第二只青蛙 "cr<strong>c</strong>oak<strong>roak</strong>"
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>croakOfFrogs = "croakcrook"
<strong>输出：</strong>-1
<strong>解释：</strong>给出的字符串不是 "croak<strong>"</strong> 的有效组合。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= croakOfFrogs.length &lt;= 10<sup>5</sup></code></li>
	<li>字符串中的字符只有 <code>'c'</code>, <code>'r'</code>, <code>'o'</code>, <code>'a'</code> 或者 <code>'k'</code></li>
</ul>


## 难度

Medium

## 标签

- 字符串
- 计数

## 提示

1. keep the frequency of all characters from "croak" using a hashmap.
2. For each character in the given string, greedily match it to a possible "croak".

## 示例

```
"croakcroak"
"crcoakroak"
"croakcrook"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minNumberOfFrogs(string croakOfFrogs) {
        
    }
};
```

### Java

```java
class Solution {
    public int minNumberOfFrogs(String croakOfFrogs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        
```

### C

```c
int minNumberOfFrogs(char* croakOfFrogs) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinNumberOfFrogs(string croakOfFrogs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} croakOfFrogs
 * @return {number}
 */
var minNumberOfFrogs = function(croakOfFrogs) {
    
};
```

### TypeScript

```typescript
function minNumberOfFrogs(croakOfFrogs: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $croakOfFrogs
     * @return Integer
     */
    function minNumberOfFrogs($croakOfFrogs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minNumberOfFrogs(_ croakOfFrogs: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minNumberOfFrogs(croakOfFrogs: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minNumberOfFrogs(String croakOfFrogs) {
    
  }
}
```

### Go

```golang
func minNumberOfFrogs(croakOfFrogs string) int {
    
}
```

### Ruby

```ruby
# @param {String} croak_of_frogs
# @return {Integer}
def min_number_of_frogs(croak_of_frogs)
    
end
```

### Scala

```scala
object Solution {
    def minNumberOfFrogs(croakOfFrogs: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_number_of_frogs(croak_of_frogs: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-number-of-frogs croakOfFrogs)
  (-> string? exact-integer?)
  )
```

### Erlang

```erlang
-spec min_number_of_frogs(CroakOfFrogs :: unicode:unicode_binary()) -> integer().
min_number_of_frogs(CroakOfFrogs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_number_of_frogs(croak_of_frogs :: String.t) :: integer
  def min_number_of_frogs(croak_of_frogs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minNumberOfFrogs(croakOfFrogs: String): Int64 {

    }
}
```

