# 1604. 警告一小时内使用相同员工卡大于等于三次的人

## 题目描述

<p>力扣公司的员工都使用员工卡来开办公室的门。每当一个员工使用一次他的员工卡，安保系统会记录下员工的名字和使用时间。如果一个员工在一小时时间内使用员工卡的次数大于等于三次，这个系统会自动发布一个 <strong>警告</strong>&nbsp;。</p>

<p>给你字符串数组&nbsp;<code>keyName</code>&nbsp;和&nbsp;<code>keyTime</code> ，其中&nbsp;<code>[keyName[i], keyTime[i]]</code>&nbsp;对应一个人的名字和他在&nbsp;<strong>某一天</strong> 内使用员工卡的时间。</p>

<p>使用时间的格式是 <strong>24小时制</strong>&nbsp;，形如<strong>&nbsp;"HH:MM"</strong>&nbsp;，比方说&nbsp;<code>"23:51"</code> 和&nbsp;<code>"09:49"</code>&nbsp;。</p>

<p>请你返回去重后的收到系统警告的员工名字，将它们按 <strong>字典序</strong><strong>升序&nbsp;</strong>排序后返回。</p>

<p>请注意&nbsp;<code>"10:00"</code> - <code>"11:00"</code>&nbsp;视为一个小时时间范围内，而&nbsp;<code>"22:51"</code> - <code>"23:52"</code>&nbsp;不被视为一小时时间范围内。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
<strong>输出：</strong>["daniel"]
<strong>解释：</strong>"daniel" 在一小时内使用了 3 次员工卡（"10:00"，"10:40"，"11:00"）。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
<strong>输出：</strong>["bob"]
<strong>解释：</strong>"bob" 在一小时内使用了 3 次员工卡（"21:00"，"21:20"，"21:30"）。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= keyName.length, keyTime.length &lt;= 10<sup>5</sup></code></li>
	<li><code>keyName.length == keyTime.length</code></li>
	<li><code>keyTime</code> 格式为&nbsp;<strong>"HH:MM"&nbsp;</strong>。</li>
	<li>保证&nbsp;<code>[keyName[i], keyTime[i]]</code>&nbsp;形成的二元对&nbsp;<strong>互不相同&nbsp;</strong>。</li>
	<li><code>1 &lt;= keyName[i].length &lt;= 10</code></li>
	<li><code>keyName[i]</code>&nbsp;只包含小写英文字母。</li>
</ul>


## 难度

Medium

## 标签

- 数组
- 哈希表
- 字符串
- 排序

## 提示

1. Group the times by the name of the card user, then sort each group

## 示例

```
["daniel","daniel","daniel","luis","luis","luis","luis"]
["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
["alice","alice","alice","bob","bob","bob","bob"]
["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    vector<string> alertNames(vector<string>& keyName, vector<string>& keyTime) {
        
    }
};
```

### Java

```java
class Solution {
    public List<String> alertNames(String[] keyName, String[] keyTime) {
        
    }
}
```

### Python

```python
class Solution(object):
    def alertNames(self, keyName, keyTime):
        """
        :type keyName: List[str]
        :type keyTime: List[str]
        :rtype: List[str]
        """
        
```

### Python3

```python3
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
```

### C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** alertNames(char** keyName, int keyNameSize, char** keyTime, int keyTimeSize, int* returnSize) {
    
}
```

### C#

```csharp
public class Solution {
    public IList<string> AlertNames(string[] keyName, string[] keyTime) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {string[]} keyName
 * @param {string[]} keyTime
 * @return {string[]}
 */
var alertNames = function(keyName, keyTime) {
    
};
```

### TypeScript

```typescript
function alertNames(keyName: string[], keyTime: string[]): string[] {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param String[] $keyName
     * @param String[] $keyTime
     * @return String[]
     */
    function alertNames($keyName, $keyTime) {
        
    }
}
```

### Swift

```swift
class Solution {
    func alertNames(_ keyName: [String], _ keyTime: [String]) -> [String] {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun alertNames(keyName: Array<String>, keyTime: Array<String>): List<String> {
        
    }
}
```

### Dart

```dart
class Solution {
  List<String> alertNames(List<String> keyName, List<String> keyTime) {
    
  }
}
```

### Go

```golang
func alertNames(keyName []string, keyTime []string) []string {
    
}
```

### Ruby

```ruby
# @param {String[]} key_name
# @param {String[]} key_time
# @return {String[]}
def alert_names(key_name, key_time)
    
end
```

### Scala

```scala
object Solution {
    def alertNames(keyName: Array[String], keyTime: Array[String]): List[String] = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn alert_names(key_name: Vec<String>, key_time: Vec<String>) -> Vec<String> {
        
    }
}
```

### Racket

```racket
(define/contract (alert-names keyName keyTime)
  (-> (listof string?) (listof string?) (listof string?))
  )
```

### Erlang

```erlang
-spec alert_names(KeyName :: [unicode:unicode_binary()], KeyTime :: [unicode:unicode_binary()]) -> [unicode:unicode_binary()].
alert_names(KeyName, KeyTime) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec alert_names(key_name :: [String.t], key_time :: [String.t]) :: [String.t]
  def alert_names(key_name, key_time) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func alertNames(keyName: Array<String>, keyTime: Array<String>): ArrayList<String> {

    }
}
```

