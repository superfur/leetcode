# 2621. 睡眠函数

## 题目描述

<p>请你编写一个异步函数，它接收一个正整数参数 <code>millis</code>&nbsp;，并休眠 <code>millis</code> 毫秒。要求此函数可以解析任何值。</p>

<p><strong>请注意</strong>，实际睡眠持续时间与&nbsp;<code>millis</code> 之间的微小偏差是可以接受的。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<pre>
<b>输入：</b>millis = 100
<b>输出：</b>100
<b>解释：</b>
在 100ms 后此异步函数执行完时返回一个 Promise 对象
let t = Date.now();
sleep(100).then(() =&gt; {
  console.log(Date.now() - t); // 100
});
</pre>

<p><b>示例 2：</b></p>

<pre>
<b>输入：</b>millis = 200
<b>输出：</b>200
<b>解释：</b>在 200ms 后函数执行完时返回一个 Promise 对象
</pre>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= millis &lt;= 1000</code></li>
</ul>


## 难度

Easy

## 提示

1. In Javascript, you can execute code after some delay with the setTimeout(fn, sleepTime) function.
2. An async function is defined as function which returns a Promise.
3. To create a Promise, you can code new Promise((resolve, reject) => {}). When you want the function to return a value, code resolve(value) inside the callback.

## 示例

```
100
200
```

## 示例代码

### JavaScript

```javascript
/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
```

### TypeScript

```typescript
async function sleep(millis: number): Promise<void> {
    
}


/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */
```

