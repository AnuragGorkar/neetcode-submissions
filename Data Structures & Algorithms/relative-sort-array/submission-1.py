class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr2_order = {item: i for i, item in enumerate(arr2)}

        arr1.sort(key=lambda x: (arr2_order.get(x, len(arr2)), x))
        return arr1
        