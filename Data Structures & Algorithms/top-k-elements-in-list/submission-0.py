class Solution:
    def topKFrequent(self, List, k):
        dictionary ={}
        for num in List:
            if (num in dictionary):
                value = dictionary[num]
                value += 1
                dictionary[num] = value
            else:
                dictionary[num] = 1
        sorted_data = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_data[:k]]