# 165. 比较版本号

## 题目描述

<p>给你两个 <strong>版本号字符串</strong>&nbsp;<code>version1</code> 和 <code>version2</code> ，请你比较它们。版本号由被点&nbsp;<code>'.'</code> 分开的修订号组成。<strong>修订号的值</strong> 是它 <strong>转换为整数</strong> 并忽略前导零。</p>

<p>比较版本号时，请按 <strong>从左到右的顺序</strong> 依次比较它们的修订号。如果其中一个版本字符串的修订号较少，则将缺失的修订号视为 <code>0</code>。</p>

<p>返回规则如下：</p>

<ul>
	<li>如果&nbsp;<code><em>version1&nbsp;</em>&lt;&nbsp;<em>version2</em></code> 返回 <code>-1</code>，</li>
	<li>如果&nbsp;<code><em>version1&nbsp;</em>&gt;&nbsp;<em>version2</em></code>&nbsp;返回&nbsp;<code>1</code>，</li>
	<li>除此之外返回 <code>0</code>。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">version1 = "1.2", version2 = "1.10"</span></p>

<p><strong>输出：</strong><span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<p>version1 的第二个修订号为&nbsp;"2"，version2 的第二个修订号为 "10"：2 &lt; 10，所以 version1 &lt; version2。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">version1 = "1.01", version2 = "1.001"</span></p>

<p><strong>输出：</strong><span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>忽略前导零，"01" 和 "001" 都代表相同的整数 "1"。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">version1 = "1.0", version2 = "1.0.0.0"</span></p>

<p><strong>输出：</strong><span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>version1 有更少的修订号，每个缺失的修订号按 "0" 处理。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= version1.length, version2.length &lt;= 500</code></li>
	<li><code>version1</code> 和 <code>version2</code> 仅包含数字和 <code>'.'</code></li>
	<li><code>version1</code> 和 <code>version2</code> 都是 <strong>有效版本号</strong></li>
	<li><code>version1</code> 和 <code>version2</code> 的所有修订号都可以存储在 <strong>32 位整数</strong> 中</li>
</ul>


## 难度

Medium

## 标签

- 双指针
- 字符串

## 提示

1. You can use two pointers for each version string to traverse them together while comparing the corresponding segments.
2. Utilize the substring method to extract each version segment delimited by '.'. Ensure you're extracting the segments correctly by adjusting the start and end indices accordingly.

## 示例

```
"1.2"
"1.10"
"1.01"
"1.001"
"1.0"
"1.0.0.0"
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int compareVersion(string version1, string version2) {
        
    }
};
```

### Java

```java
class Solution {
    public int compareVersion(String version1, String version2) {
        
    }
}
```

### Python

```python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
```

### C

```c
int compareVersion(char* version1, char* version2) {
    
}
```

### C#

```csharp
public class Solution {
    public int CompareVersion(string version1, string version2) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string} version1
 * @param {string} version2
 * @return {number}
 */
var compareVersion = function(version1, version2) {
    
};
```

### TypeScript

```typescript
function compareVersion(version1: string, version2: string): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String $version1
     * @param String $version2
     * @return Integer
     */
    function compareVersion($version1, $version2) {
        
    }
}
```

### Swift

```swift
class Solution {
    func compareVersion(_ version1: String, _ version2: String) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun compareVersion(version1: String, version2: String): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int compareVersion(String version1, String version2) {
    
  }
}
```

### Go

```golang
func compareVersion(version1 string, version2 string) int {
    
}
```

### Ruby

```ruby
# @param {String} version1
# @param {String} version2
# @return {Integer}
def compare_version(version1, version2)
    
end
```

### Scala

```scala
object Solution {
    def compareVersion(version1: String, version2: String): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn compare_version(version1: String, version2: String) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (compare-version version1 version2)
  (-> string? string? exact-integer?)
  )
```

### Erlang

```erlang
-spec compare_version(Version1 :: unicode:unicode_binary(), Version2 :: unicode:unicode_binary()) -> integer().
compare_version(Version1, Version2) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec compare_version(version1 :: String.t, version2 :: String.t) :: integer
  def compare_version(version1, version2) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func compareVersion(version1: String, version2: String): Int64 {

    }
}
```

