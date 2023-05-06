class Sort:

    def minimum(self, arr: list[int]) -> int:
        min_val = float('inf')
        for i in range(len(arr)):
            if arr[i] < min_val:
                min_val = arr[i]

        return min_val

    def maximum(self, arr: list[int]) -> int:
        max_val = float('-inf')
        for i in range(len(arr)):
            if arr[i] > max_val:
                max_val = arr[i]

        return max_val

    def selection(self, arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            arr_min = self.minimum(arr[i::])
            if arr[i] > arr_min:
                j = arr[i::].index(arr_min)
                arr[i], arr[j] = arr[j], arr[i]

        return arr