class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr_length = len(arr)
        original_arr = arr
        previous_value = -1
        for i in range (arr_length-1, -1, -1):
            current_val = arr[i]
            arr[i] = previous_value
            if current_val > previous_value:
                previous_value = current_val

        return arr