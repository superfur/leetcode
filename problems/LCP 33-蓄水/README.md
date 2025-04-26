# LCP 33. 蓄水

## 题目描述

给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 `i` 个水缸配备的水桶容量记作 `bucket[i]`。小扣有以下两种操作：
-  升级水桶：选择任意一个水桶，使其容量增加为 `bucket[i]+1`
-  蓄水：将全部水桶接满水，倒入各自对应的水缸

每个水缸对应最低蓄水量记作 `vat[i]`，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。

注意：实际蓄水量 **达到或超过** 最低蓄水量，即完成蓄水要求。

**示例 1：**
>输入：`bucket = [1,3], vat = [6,8]`
>
>输出：`4`
>
>解释：
>第 1 次操作升级 bucket[0]；
>第 2 ~ 4 次操作均选择蓄水，即可完成蓄水要求。
![vat1.gif](https://pic.leetcode-cn.com/1616122992-RkDxoL-vat1.gif)



**示例 2：**
>输入：`bucket = [9,0,1], vat = [0,2,2]`
>
>输出：`3`
>
>解释：
>第 1 次操作均选择升级 bucket[1]
>第 2~3 次操作选择蓄水，即可完成蓄水要求。

**提示：**
- `1 <= bucket.length == vat.length <= 100`
- `0 <= bucket[i], vat[i] <= 10^4`


## 难度

Easy

## 标签

- 贪心
- 数组
- 堆（优先队列）

## 示例

```
[1,3]
[6,8]
[9,0,1]
[0,2,2]
```

## 示例代码

### C++

```cpp
class Solution {
public:
    int storeWater(vector<int>& bucket, vector<int>& vat) {

    }
};
```

### Java

```java
class Solution {
    public int storeWater(int[] bucket, int[] vat) {

    }
}
```

### Python

```python
class Solution(object):
    def storeWater(self, bucket, vat):
        """
        :type bucket: List[int]
        :type vat: List[int]
        :rtype: int
        """
```

### Python3

```python3
class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
```

### C

```c


int storeWater(int* bucket, int bucketSize, int* vat, int vatSize){

}
```

### C#

```csharp
public class Solution {
    public int StoreWater(int[] bucket, int[] vat) {

    }
}
```

### JavaScript

```javascript
/**
 * @param {number[]} bucket
 * @param {number[]} vat
 * @return {number}
 */
var storeWater = function(bucket, vat) {

};
```

### TypeScript

```typescript
function storeWater(bucket: number[], vat: number[]): number {

};
```

### PHP

```php
class Solution {

    /**
     * @param Integer[] $bucket
     * @param Integer[] $vat
     * @return Integer
     */
    function storeWater($bucket, $vat) {

    }
}
```

### Swift

```swift
class Solution {
    func storeWater(_ bucket: [Int], _ vat: [Int]) -> Int {

    }
}
```

### Kotlin

```kotlin
class Solution {
    fun storeWater(bucket: IntArray, vat: IntArray): Int {

    }
}
```

### Go

```golang
func storeWater(bucket []int, vat []int) int {

}
```

### Ruby

```ruby
# @param {Integer[]} bucket
# @param {Integer[]} vat
# @return {Integer}
def store_water(bucket, vat)

end
```

### Scala

```scala
object Solution {
    def storeWater(bucket: Array[Int], vat: Array[Int]): Int = {

    }
}
```

### Rust

```rust
impl Solution {
    pub fn store_water(bucket: Vec<i32>, vat: Vec<i32>) -> i32 {

    }
}
```

### Racket

```racket
(define/contract (store-water bucket vat)
  (-> (listof exact-integer?) (listof exact-integer?) exact-integer?)

  )
```

