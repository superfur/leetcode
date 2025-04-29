function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    const merged = [...nums1, ...nums2].sort((a, b) => a - b);
    const middle = Math.floor(merged.length / 2);
    if (merged.length % 2 === 1) {
        return merged[middle];
    } else {
        return (merged[middle - 1] + merged[middle]) / 2;
    }
}

export default findMedianSortedArrays;

// function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
//     let middle = 0;
//     const list = [...nums1, ...nums2].sort((a,b) => a - b);
//     if (list.length % 2 === 1) {
//         middle = list[Math.floor(list.length / 2)]
//     } else {
//         middle = (list[Math.floor(list.length / 2)-1] +  list[Math.floor(list.length / 2)]) / 2
//     }

//     return middle;
// };