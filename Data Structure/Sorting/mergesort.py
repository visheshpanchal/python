from typing import List


def merge_sort(arr: List, l: int, r: int):
    """
    l->left pointer
    r-> right pointer
    """
    if (l < r):
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)


def merge(arr: List, l: int, m: int, r: int):
    """
    l -> left
    m -> middle
    r -> right
    """

    # We use k for calculating arr index, i and j for beginning index of temp array, n1 and n2 are length of two array
    k = l
    i = 0
    j = 0
    n1 = m - l + 1
    n2 = r - m

    L = arr[l:m+1]
    R = arr[m+1:r+1]

    # Comparing and Merging Two Array
    while (i < n1 and j < n2):

        if (L[i] <= R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1

        k += 1

    # If Remaining part of array sorted then we need to only merge that array till end of array
    while (i < n1):
        arr[k] = L[i]
        i += 1
        k += 1

    while (j < n2):
        arr[k] = R[j]
        j += 1
        k += 1


if __name__ == "__main__":

    arr = [0]

    merge_sort(arr, 0, 0)

    print(arr)
