# 2960. 统计已测试设备

## 题目描述

<p>给你一个长度为 <code>n</code> 、下标从<strong> 0 </strong>开始的整数数组 <code>batteryPercentages</code> ，表示 <code>n</code> 个设备的电池百分比。</p>

<p>你的任务是按照顺序测试每个设备 <code>i</code>，执行以下测试操作：</p>

<ul>
	<li>如果 <code>batteryPercentages[i]</code> <strong>大于</strong> <code>0</code>：

	<ul>
		<li><strong>增加</strong> 已测试设备的计数。</li>
		<li>将下标在 <code>[i + 1, n - 1]</code> 的所有设备的电池百分比减少 <code>1</code>，确保它们的电池百分比<strong> 不会低于</strong> <code>0</code> ，即 <code>batteryPercentages[j] = max(0, batteryPercentages[j] - 1)</code>。</li>
		<li>移动到下一个设备。</li>
	</ul>
	</li>
	<li>否则，移动到下一个设备而不执行任何测试。</li>
</ul>

<p>返回一个整数，表示按顺序执行测试操作后 <strong>已测试设备</strong> 的数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>batteryPercentages = [1,1,2,1,3]
<strong>输出：</strong>3
<strong>解释：</strong>按顺序从设备 0 开始执行测试操作：
在设备 0 上，batteryPercentages[0] &gt; 0 ，现在有 1 个已测试设备，batteryPercentages 变为 [1,0,1,0,2] 。
在设备 1 上，batteryPercentages[1] == 0 ，移动到下一个设备而不进行测试。
在设备 2 上，batteryPercentages[2] &gt; 0 ，现在有 2 个已测试设备，batteryPercentages 变为 [1,0,1,0,1] 。
在设备 3 上，batteryPercentages[3] == 0 ，移动到下一个设备而不进行测试。
在设备 4 上，batteryPercentages[4] &gt; 0 ，现在有 3 个已测试设备，batteryPercentages 保持不变。
因此，答案是 3 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>batteryPercentages = [0,1,2]
<strong>输出：</strong>2
<strong>解释：</strong>按顺序从设备 0 开始执行测试操作：
在设备 0 上，batteryPercentages[0] == 0 ，移动到下一个设备而不进行测试。
在设备 1 上，batteryPercentages[1] &gt; 0 ，现在有 1 个已测试设备，batteryPercentages 变为 [0,1,1] 。
在设备 2 上，batteryPercentages[2] &gt; 0 ，现在有 2 个已测试设备，batteryPercentages 保持不变。
因此，答案是 2 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == batteryPercentages.length &lt;= 100 </code></li>
	<li><code>0 &lt;= batteryPercentages[i] &lt;= 100</code></li>
</ul>


## 难度

Easy

## 标签

- 数组
- 计数
- 模拟

## 提示

1. One solution is simulating the operations as explained in the problem statement, and it works in <code>O(n<sup>2</sup>)</code> time.
2. While going through the devices, you can maintain the number of previously tested devices, and the current device can be tested if <code>batteryPercentages[i]</code> is greater than the number of tested devices.

## 示例

```
[1,1,2,1,3]
[0,1,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int countTestedDevices(vector<int>& batteryPercentages) {
        
    }
};
```

### Java

```java
class Solution {
    public int countTestedDevices(int[] batteryPercentages) {
        
    }
}
```

### Python

```python
class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        
```

### Python3

```python3
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        
```

### C

```c
int countTestedDevices(int* batteryPercentages, int batteryPercentagesSize) {
    
}
```

### C#

```csharp
public class Solution {
    public int CountTestedDevices(int[] batteryPercentages) {
        
    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} batteryPercentages
 * @return {number}
 */
var countTestedDevices = function(batteryPercentages) {
    
};
```

### TypeScript

```typescript
function countTestedDevices(batteryPercentages: number[]): number {
    
};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $batteryPercentages
     * @return Integer
     */
    function countTestedDevices($batteryPercentages) {
        
    }
}
```

### Swift

```swift
class Solution {
    func countTestedDevices(_ batteryPercentages: [Int]) -> Int {
        
    }
}
```

### Kotlin

```kotlin
class Solution {
    fun countTestedDevices(batteryPercentages: IntArray): Int {
        
    }
}
```

### Dart

```dart
class Solution {
  int countTestedDevices(List<int> batteryPercentages) {
    
  }
}
```

### Go

```golang
func countTestedDevices(batteryPercentages []int) int {
    
}
```

### Ruby

```ruby
# @param {Integer[]} battery_percentages
# @return {Integer}
def count_tested_devices(battery_percentages)
    
end
```

### Scala

```scala
object Solution {
    def countTestedDevices(batteryPercentages: Array[Int]): Int = {
        
    }
}
```

### Rust

```rust
impl Solution {
    pub fn count_tested_devices(battery_percentages: Vec<i32>) -> i32 {
        
    }
}
```

### Racket

```racket
(define/contract (count-tested-devices batteryPercentages)
  (-> (listof exact-integer?) exact-integer?)
  )
```

### Erlang

```erlang
-spec count_tested_devices(BatteryPercentages :: [integer()]) -> integer().
count_tested_devices(BatteryPercentages) ->
  .
```

### Elixir

```elixir
defmodule Solution do
  @spec count_tested_devices(battery_percentages :: [integer]) :: integer
  def count_tested_devices(battery_percentages) do
    
  end
end
```

### Cangjie

```cangjie
class Solution {
    func countTestedDevices(batteryPercentages: Array<Int64>): Int64 {

    }
}
```

