# 1598. 文件夹操作日志搜集器

## 题目描述

<p>每当用户执行变更文件夹操作时，LeetCode 文件系统都会保存一条日志记录。</p>

<p>下面给出对变更操作的说明：</p>

<ul>
	<li><code>&quot;../&quot;</code> ：移动到当前文件夹的父文件夹。如果已经在主文件夹下，则 <strong>继续停留在当前文件夹</strong> 。</li>
	<li><code>&quot;./&quot;</code> ：继续停留在当前文件夹<strong>。</strong></li>
	<li><code>&quot;x/&quot;</code> ：移动到名为 <code>x</code> 的子文件夹中。题目数据 <strong>保证总是存在文件夹 <code>x</code></strong> 。</li>
</ul>

<p>给你一个字符串列表 <code>logs</code> ，其中 <code>logs[i]</code> 是用户在 <code>i<sup>th</sup></code> 步执行的操作。</p>

<p>文件系统启动时位于主文件夹，然后执行 <code>logs</code> 中的操作。</p>

<p>执行完所有变更文件夹操作后，请你找出 <strong>返回主文件夹所需的最小步数</strong> 。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/sample_11_1957.png" style="height: 151px; width: 775px;"></p>

<pre><strong>输入：</strong>logs = [&quot;d1/&quot;,&quot;d2/&quot;,&quot;../&quot;,&quot;d21/&quot;,&quot;./&quot;]
<strong>输出：</strong>2
<strong>解释：</strong>执行 &quot;../&quot; 操作变更文件夹 2 次，即可回到主文件夹
</pre>

<p><strong>示例 2：</strong></p>

<p><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/sample_22_1957.png" style="height: 270px; width: 600px;"></p>

<pre><strong>输入：</strong>logs = [&quot;d1/&quot;,&quot;d2/&quot;,&quot;./&quot;,&quot;d3/&quot;,&quot;../&quot;,&quot;d31/&quot;]
<strong>输出：</strong>3
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>logs = [&quot;d1/&quot;,&quot;../&quot;,&quot;../&quot;,&quot;../&quot;]
<strong>输出：</strong>0
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= logs.length &lt;= 10<sup>3</sup></code></li>
	<li><code>2 &lt;= logs[i].length &lt;= 10</code></li>
	<li><code>logs[i]</code> 包含小写英文字母，数字，<code>&#39;.&#39;</code> 和 <code>&#39;/&#39;</code></li>
	<li><code>logs[i]</code> 符合语句中描述的格式</li>
	<li>文件夹名称由小写英文字母和数字组成</li>
</ul>


## 难度

Easy

## 标签

- 栈
- 数组
- 字符串

## 提示

1. Simulate the process but don’t move the pointer beyond the main folder.

## 示例

```
["d1/","d2/","../","d21/","./"]
["d1/","d2/","./","d3/","../","d31/"]
["d1/","../","../","../"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int minOperations(vector<string>& logs) {
        
    }
};
```

### Java

```java
class Solution {
    public int minOperations(String[] logs) {
        
    }
}
```

### Python

```python
class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
```

### C

```c
int minOperations(char** logs, int logsSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int MinOperations(string[] logs) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} logs
 * @return {number}
 */
var minOperations = function(logs) {
    
};
```

### TypeScript

```typescript
function minOperations(logs: string[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $logs
     * @return Integer
     */
    function minOperations($logs) {
        
    }
}
```

### Swift

```swift
class Solution {
    func minOperations(_ logs: [String]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun minOperations(logs: Array<String>): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int minOperations(List<String> logs) {
    
  }
}
```

### Go

```golang
func minOperations(logs []string) int {
    
}
```

### Ruby

```ruby
# @param {String[]} logs
# @return {Integer}
def min_operations(logs)
    
end
```

### Scala

```scala
object Solution {
    def minOperations(logs: Array[String]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn min_operations(logs: Vec<String>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (min-operations logs)
  (-> (listof string?) exact-integer?)
  )
```

### Erlang

```erlang
-spec min_operations(Logs :: [unicode:unicode_binary()]) -> integer().
min_operations(Logs) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec min_operations(logs :: [String.t]) :: integer
  def min_operations(logs) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func minOperations(logs: Array<String>): Int64 {

    }
}
```

